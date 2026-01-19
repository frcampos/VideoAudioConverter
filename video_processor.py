"""
video_processor.py
Extrai áudio de vídeos MP4 usando moviepy
"""

import logging
from moviepy.editor import VideoFileClip
import os


class VideoProcessor:
    """Extrai áudio de ficheiros MP4"""
    
    def __init__(self, config):
        self.config = config
    
    def extract_audio(self, video_path, temp_audio_path):
        """
        Extrai áudio do vídeo MP4
        
        Args:
            video_path (str): Caminho do vídeo MP4
            temp_audio_path (str): Caminho temporário para salvar áudio bruto
            
        Returns:
            tuple: (sucesso, duração, mensagem)
        """
        video_clip = None
        
        try:
            logging.info(f"Extraindo áudio de: {os.path.basename(video_path)}")
            
            # Carregar vídeo
            video_clip = VideoFileClip(video_path)
            
            # Verificar se vídeo tem áudio
            if video_clip.audio is None:
                logging.error(f"Vídeo não contém áudio: {video_path}")
                return False, 0, "Vídeo sem áudio"
            
            # Obter duração
            duration = video_clip.duration
            logging.info(f"Duração do vídeo: {duration:.2f}s ({self._format_duration(duration)})")
            
            # Extrair áudio
            audio_clip = video_clip.audio
            
            # Salvar áudio temporário (WAV para preservar qualidade)
            audio_clip.write_audiofile(
                temp_audio_path,
                codec='pcm_s16le',  # WAV sem compressão
                fps=44100,
                nbytes=2,
                verbose=False,
                logger=None
            )
            
            logging.info(f"Áudio extraído com sucesso: {os.path.basename(temp_audio_path)}")
            
            return True, duration, "Áudio extraído"
            
        except Exception as e:
            logging.error(f"Erro ao extrair áudio de {video_path}: {str(e)}")
            return False, 0, str(e)
        
        finally:
            # Fechar recursos
            if video_clip:
                video_clip.close()
    
    def get_video_info(self, video_path):
        """
        Obtém informações do vídeo
        
        Args:
            video_path (str): Caminho do vídeo
            
        Returns:
            dict: Informações do vídeo
        """
        video_clip = None
        
        try:
            video_clip = VideoFileClip(video_path)
            
            info = {
                'duration': video_clip.duration,
                'duration_formatted': self._format_duration(video_clip.duration),
                'fps': video_clip.fps,
                'size': video_clip.size,
                'has_audio': video_clip.audio is not None
            }
            
            if video_clip.audio:
                info['audio_fps'] = video_clip.audio.fps
                info['audio_channels'] = video_clip.audio.nchannels
            
            return info
            
        except Exception as e:
            logging.error(f"Erro ao obter informações do vídeo {video_path}: {str(e)}")
            return None
        
        finally:
            if video_clip:
                video_clip.close()
    
    def _format_duration(self, seconds):
        """
        Formata duração em formato legível
        
        Args:
            seconds (float): Duração em segundos
            
        Returns:
            str: Duração formatada (HH:MM:SS)
        """
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        
        if hours > 0:
            return f"{hours:02d}:{minutes:02d}:{secs:02d}"
        else:
            return f"{minutes:02d}:{secs:02d}"
    
    def validate_video(self, video_path):
        """
        Valida se vídeo é válido e contém áudio
        
        Args:
            video_path (str): Caminho do vídeo
            
        Returns:
            tuple: (válido, mensagem)
        """
        video_clip = None
        
        try:
            video_clip = VideoFileClip(video_path)
            
            if video_clip.audio is None:
                return False, "Vídeo não contém áudio"
            
            if video_clip.duration <= 0:
                return False, "Vídeo com duração inválida"
            
            return True, "Vídeo válido"
            
        except Exception as e:
            return False, f"Erro ao validar vídeo: {str(e)}"
        
        finally:
            if video_clip:
                video_clip.close()
