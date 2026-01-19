"""
quality_analyzer.py
Análise de qualidade de áudio antes e depois da conversão
"""

import logging
import os
from pydub import AudioSegment


class QualityAnalyzer:
    """Analisa qualidade de áudio"""
    
    def __init__(self, config):
        self.config = config
        self.enabled = config.get_quality_analysis_enabled()
        self.detailed = config.get_detailed_stats()
    
    def analyze_conversion(self, original_path, converted_path, video_duration):
        """
        Analisa qualidade antes e depois da conversão
        
        Args:
            original_path (str): Caminho do áudio original (WAV temporário)
            converted_path (str): Caminho do áudio convertido (MP3)
            video_duration (float): Duração do vídeo original em segundos
            
        Returns:
            dict: Análise comparativa
        """
        if not self.enabled:
            return None
        
        try:
            logging.info("Analisando qualidade do áudio...")
            
            # Estatísticas do áudio original (WAV)
            original_stats = self._get_audio_stats(original_path)
            
            # Estatísticas do áudio convertido (MP3)
            converted_stats = self._get_audio_stats(converted_path)
            
            # Análise comparativa
            analysis = {
                'original': original_stats,
                'converted': converted_stats,
                'video_duration': video_duration,
                'compression': self._calculate_compression(original_stats, converted_stats),
                'quality_score': self._calculate_quality_score(converted_stats)
            }
            
            # Log da análise
            self._log_analysis(analysis)
            
            return analysis
            
        except Exception as e:
            logging.error(f"Erro na análise de qualidade: {str(e)}")
            return None
    
    def _get_audio_stats(self, audio_path):
        """
        Obtém estatísticas detalhadas do áudio
        
        Args:
            audio_path (str): Caminho do áudio
            
        Returns:
            dict: Estatísticas
        """
        audio = AudioSegment.from_file(audio_path)
        file_stats = os.stat(audio_path)
        
        stats = {
            'duration': len(audio) / 1000.0,
            'sample_rate': audio.frame_rate,
            'channels': audio.channels,
            'sample_width': audio.sample_width * 8,  # bits
            'dBFS': round(audio.dBFS, 2),
            'max_dBFS': round(audio.max_dBFS, 2),
            'size_bytes': file_stats.st_size,
            'size_mb': round(file_stats.st_size / (1024 * 1024), 2),
            'bitrate_kbps': self._estimate_bitrate(file_stats.st_size, len(audio) / 1000.0)
        }
        
        return stats
    
    def _estimate_bitrate(self, size_bytes, duration_seconds):
        """
        Estima bitrate do áudio
        
        Args:
            size_bytes (int): Tamanho em bytes
            duration_seconds (float): Duração em segundos
            
        Returns:
            int: Bitrate estimado em kbps
        """
        if duration_seconds == 0:
            return 0
        
        bitrate_bps = (size_bytes * 8) / duration_seconds
        bitrate_kbps = int(bitrate_bps / 1000)
        
        return bitrate_kbps
    
    def _calculate_compression(self, original, converted):
        """
        Calcula taxa de compressão
        
        Args:
            original (dict): Estatísticas do original
            converted (dict): Estatísticas do convertido
            
        Returns:
            dict: Dados de compressão
        """
        size_reduction = original['size_bytes'] - converted['size_bytes']
        reduction_percent = (size_reduction / original['size_bytes']) * 100
        
        return {
            'original_size_mb': original['size_mb'],
            'converted_size_mb': converted['size_mb'],
            'reduction_mb': round(size_reduction / (1024 * 1024), 2),
            'reduction_percent': round(reduction_percent, 1)
        }
    
    def _calculate_quality_score(self, stats):
        """
        Calcula score de qualidade (0-100)
        
        Args:
            stats (dict): Estatísticas do áudio
            
        Returns:
            dict: Score e categoria
        """
        score = 0
        
        # Sample rate (max 30 pontos)
        if stats['sample_rate'] >= 48000:
            score += 30
        elif stats['sample_rate'] >= 44100:
            score += 25
        elif stats['sample_rate'] >= 32000:
            score += 20
        else:
            score += 10
        
        # Bitrate (max 40 pontos)
        if stats['bitrate_kbps'] >= 320:
            score += 40
        elif stats['bitrate_kbps'] >= 256:
            score += 35
        elif stats['bitrate_kbps'] >= 192:
            score += 30
        elif stats['bitrate_kbps'] >= 128:
            score += 25
        elif stats['bitrate_kbps'] >= 96:
            score += 20
        else:
            score += 10
        
        # Canais (max 15 pontos)
        if stats['channels'] == 2:
            score += 15
        else:
            score += 10
        
        # Sample width (max 15 pontos)
        if stats['sample_width'] >= 24:
            score += 15
        elif stats['sample_width'] >= 16:
            score += 12
        else:
            score += 8
        
        # Categoria de qualidade
        if score >= 90:
            category = "Excelente"
        elif score >= 75:
            category = "Muito Boa"
        elif score >= 60:
            category = "Boa"
        elif score >= 45:
            category = "Aceitável"
        else:
            category = "Baixa"
        
        return {
            'score': score,
            'category': category
        }
    
    def _log_analysis(self, analysis):
        """
        Log detalhado da análise
        
        Args:
            analysis (dict): Dados da análise
        """
        if not self.detailed:
            # Log resumido
            comp = analysis['compression']
            quality = analysis['quality_score']
            logging.info(f"Compressão: {comp['reduction_percent']:.1f}% "
                        f"({comp['original_size_mb']}MB → {comp['converted_size_mb']}MB)")
            logging.info(f"Qualidade: {quality['category']} (score: {quality['score']}/100)")
            return
        
        # Log detalhado
        original = analysis['original']
        converted = analysis['converted']
        comp = analysis['compression']
        quality = analysis['quality_score']
        
        logging.info("\n" + "="*70)
        logging.info("ANÁLISE DE QUALIDADE".center(70))
        logging.info("="*70)
        
        logging.info(f"\n📹 VÍDEO ORIGINAL:")
        logging.info(f"   Duração: {self._format_duration(analysis['video_duration'])}")
        
        logging.info(f"\n🎵 ÁUDIO EXTRAÍDO (WAV):")
        logging.info(f"   Duração:     {self._format_duration(original['duration'])}")
        logging.info(f"   Sample Rate: {original['sample_rate']} Hz")
        logging.info(f"   Canais:      {original['channels']} ({'Stereo' if original['channels'] == 2 else 'Mono'})")
        logging.info(f"   Sample Width: {original['sample_width']} bits")
        logging.info(f"   Bitrate:     ~{original['bitrate_kbps']} kbps")
        logging.info(f"   dBFS:        {original['dBFS']} (max: {original['max_dBFS']})")
        logging.info(f"   Tamanho:     {original['size_mb']} MB")
        
        logging.info(f"\n🎧 ÁUDIO CONVERTIDO (MP3):")
        logging.info(f"   Duração:     {self._format_duration(converted['duration'])}")
        logging.info(f"   Sample Rate: {converted['sample_rate']} Hz")
        logging.info(f"   Canais:      {converted['channels']} ({'Stereo' if converted['channels'] == 2 else 'Mono'})")
        logging.info(f"   Sample Width: {converted['sample_width']} bits")
        logging.info(f"   Bitrate:     ~{converted['bitrate_kbps']} kbps")
        logging.info(f"   dBFS:        {converted['dBFS']} (max: {converted['max_dBFS']})")
        logging.info(f"   Tamanho:     {converted['size_mb']} MB")
        
        logging.info(f"\n📊 COMPRESSÃO:")
        logging.info(f"   Tamanho original:  {comp['original_size_mb']} MB")
        logging.info(f"   Tamanho final:     {comp['converted_size_mb']} MB")
        logging.info(f"   Redução:           {comp['reduction_mb']} MB ({comp['reduction_percent']:.1f}%)")
        
        logging.info(f"\n⭐ QUALIDADE FINAL:")
        logging.info(f"   Score:      {quality['score']}/100")
        logging.info(f"   Categoria:  {quality['category']}")
        
        logging.info("\n" + "="*70)
    
    def _format_duration(self, seconds):
        """Formata duração"""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        
        if hours > 0:
            return f"{hours:02d}:{minutes:02d}:{secs:02d}"
        else:
            return f"{minutes:02d}:{secs:02d}"
    
    def print_summary(self, analysis):
        """
        Imprime resumo visual da análise
        
        Args:
            analysis (dict): Dados da análise
        """
        if not analysis:
            return
        
        comp = analysis['compression']
        quality = analysis['quality_score']
        
        print("\n" + "="*70)
        print("RESULTADO DA CONVERSÃO".center(70))
        print("="*70)
        print(f"\n📦 Compressão: {comp['original_size_mb']}MB → {comp['converted_size_mb']}MB "
              f"({comp['reduction_percent']:.1f}% redução)")
        print(f"⭐ Qualidade:  {quality['category']} ({quality['score']}/100)")
        print("\n" + "="*70)
