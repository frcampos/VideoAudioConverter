"""
audio_converter.py
Conversão e otimização de áudio com pydub
"""

import logging
from pydub import AudioSegment
from pydub.effects import normalize, compress_dynamic_range
from pydub.silence import detect_leading_silence
import os


class AudioConverter:
    """Converte e otimiza áudio com perfis configuráveis"""
    
    def __init__(self, config):
        self.config = config
        self.profile = config.get_profile_settings()
    
    def convert_audio(self, input_audio_path, output_audio_path):
        """
        Converte áudio aplicando todas as otimizações configuradas
        
        Args:
            input_audio_path (str): Caminho do áudio de entrada (WAV)
            output_audio_path (str): Caminho do áudio de saída (MP3)
            
        Returns:
            tuple: (sucesso, mensagem)
        """
        try:
            logging.info(f"Carregando áudio: {os.path.basename(input_audio_path)}")
            
            # Carregar áudio
            audio = AudioSegment.from_wav(input_audio_path)
            original_duration = len(audio) / 1000.0
            
            logging.info(f"Áudio original: {original_duration:.2f}s, "
                        f"{audio.frame_rate}Hz, {audio.channels} canal(is)")
            
            # Aplicar processamentos
            audio = self._apply_segment_removal(audio)
            audio = self._apply_silence_removal(audio)
            audio = self._apply_filters(audio)
            audio = self._apply_normalization(audio)
            audio = self._apply_profile_settings(audio)
            
            # Exportar MP3
            logging.info(f"Exportando MP3: {os.path.basename(output_audio_path)}")
            self._export_mp3(audio, output_audio_path)
            
            final_duration = len(audio) / 1000.0
            logging.info(f"Conversão concluída. Duração final: {final_duration:.2f}s")
            
            return True, "Conversão concluída"
            
        except Exception as e:
            logging.error(f"Erro na conversão: {str(e)}")
            return False, str(e)
    
    def _apply_segment_removal(self, audio):
        """Remove segmentos do início e fim"""
        if not self.config.get_segment_removal_enabled():
            return audio
        
        remove_start = self.config.get_remove_start()
        remove_end = self.config.get_remove_end()
        
        if remove_start > 0 or remove_end > 0:
            duration_ms = len(audio)
            start_ms = int(remove_start * 1000)
            end_ms = int(remove_end * 1000)
            
            # Validar limites
            if start_ms >= duration_ms:
                logging.warning("Remoção do início maior que duração total. Pulando.")
                return audio
            
            if end_ms >= duration_ms - start_ms:
                logging.warning("Remoção total maior que duração. Ajustando.")
                end_ms = 0
            
            # Aplicar corte
            audio = audio[start_ms : duration_ms - end_ms]
            logging.info(f"Segmentos removidos: início={remove_start}s, fim={remove_end}s")
        
        return audio
    
    def _apply_silence_removal(self, audio):
        """Remove silêncios do início e fim"""
        if not self.config.get_silence_removal_enabled():
            return audio
        
        threshold = self.config.get_silence_threshold()
        min_duration = int(self.config.get_silence_min_duration() * 1000)  # ms
        
        # Detectar silêncio no início
        start_trim = detect_leading_silence(audio, silence_threshold=threshold, chunk_size=10)
        
        # Detectar silêncio no fim (reverter áudio)
        end_trim = detect_leading_silence(audio.reverse(), silence_threshold=threshold, chunk_size=10)
        
        # Aplicar apenas se maior que duração mínima
        if start_trim > min_duration:
            audio = audio[start_trim:]
            logging.info(f"Silêncio removido do início: {start_trim/1000:.2f}s")
        
        if end_trim > min_duration:
            audio = audio[:-end_trim]
            logging.info(f"Silêncio removido do fim: {end_trim/1000:.2f}s")
        
        return audio
    
    def _apply_filters(self, audio):
        """Aplica filtros de áudio (passa-alta, passa-baixa, compressão)"""
        
        # Filtro passa-alta (remove frequências baixas/ruído)
        if self.config.get_highpass_filter_enabled():
            freq = self.config.get_highpass_freq()
            audio = audio.high_pass_filter(freq)
            logging.info(f"Filtro passa-alta aplicado: {freq}Hz")
        
        # Filtro passa-baixa (remove frequências altas/chiado)
        if self.config.get_lowpass_filter_enabled():
            freq = self.config.get_lowpass_freq()
            audio = audio.low_pass_filter(freq)
            logging.info(f"Filtro passa-baixa aplicado: {freq}Hz")
        
        # Compressão dinâmica
        if self.config.get_compression_enabled():
            threshold = self.config.get_compression_threshold()
            ratio = self.config.get_compression_ratio()
            audio = compress_dynamic_range(audio, threshold=threshold, ratio=ratio)
            logging.info(f"Compressão aplicada: threshold={threshold}dBFS, ratio={ratio}:1")
        
        return audio
    
    def _apply_normalization(self, audio):
        """Normaliza volume do áudio"""
        if not self.config.get_normalization_enabled():
            return audio
        
        target_level = self.config.get_normalization_target()
        
        # Normalizar para nível padrão
        audio = normalize(audio, headroom=0.1)
        
        # Ajustar para nível alvo
        current_dBFS = audio.dBFS
        gain_needed = target_level - current_dBFS
        audio = audio + gain_needed
        
        logging.info(f"Volume normalizado: {current_dBFS:.1f} → {target_level:.1f} dBFS")
        
        return audio
    
    def _apply_profile_settings(self, audio):
        """Aplica configurações do perfil (canais, sample rate)"""
        
        # Converter para mono ou stereo
        channels = self.profile['channels']
        if channels == 'mono' and audio.channels > 1:
            audio = audio.set_channels(1)
            logging.info("Convertido para mono")
        elif channels == 'stereo' and audio.channels == 1:
            audio = audio.set_channels(2)
            logging.info("Convertido para stereo")
        
        # Ajustar sample rate
        target_rate = self.profile['sample_rate']
        if audio.frame_rate != target_rate:
            audio = audio.set_frame_rate(target_rate)
            logging.info(f"Sample rate ajustado: {audio.frame_rate}Hz → {target_rate}Hz")
        
        return audio
    
    def _export_mp3(self, audio, output_path):
        """
        Exporta áudio para MP3
        
        Args:
            audio (AudioSegment): Áudio processado
            output_path (str): Caminho de saída
        """
        bitrate = self.profile['bitrate']
        
        # Exportar com configurações do perfil
        audio.export(
            output_path,
            format='mp3',
            bitrate=bitrate,
            parameters=["-q:a", "0"]  # Melhor qualidade de encoding
        )
        
        logging.info(f"MP3 exportado: bitrate={bitrate}, {audio.channels} canal(is)")
    
    def get_audio_stats(self, audio_path):
        """
        Obtém estatísticas do áudio
        
        Args:
            audio_path (str): Caminho do áudio
            
        Returns:
            dict: Estatísticas do áudio
        """
        try:
            audio = AudioSegment.from_file(audio_path)
            
            stats = {
                'duration': len(audio) / 1000.0,
                'duration_formatted': self._format_duration(len(audio) / 1000.0),
                'sample_rate': audio.frame_rate,
                'channels': audio.channels,
                'sample_width': audio.sample_width * 8,  # bits
                'dBFS': round(audio.dBFS, 2),
                'max_dBFS': round(audio.max_dBFS, 2),
                'size_mb': round(os.path.getsize(audio_path) / (1024 * 1024), 2)
            }
            
            return stats
            
        except Exception as e:
            logging.error(f"Erro ao obter estatísticas: {str(e)}")
            return None
    
    def _format_duration(self, seconds):
        """Formata duração"""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        
        if hours > 0:
            return f"{hours:02d}:{minutes:02d}:{secs:02d}"
        else:
            return f"{minutes:02d}:{secs:02d}"
