"""
config_loader.py
Carrega e valida configurações do arquivo config.ini
"""

import configparser
import os
import logging
from pathlib import Path


class ConfigLoader:
    """Carrega e valida configurações do config.ini"""
    
    def __init__(self, config_path='config.ini'):
        self.config_path = config_path
        self.config = configparser.ConfigParser()
        self._load_config()
        self._validate_config()
        
    def _load_config(self):
        """Carrega arquivo config.ini"""
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Arquivo config.ini não encontrado: {self.config_path}")
        
        self.config.read(self.config_path, encoding='utf-8')
        logging.info(f"Configuração carregada: {self.config_path}")
    
    def _validate_config(self):
        """Valida seções obrigatórias"""
        required_sections = ['PATHS', 'PROCESSING', 'PROFILE']
        for section in required_sections:
            if not self.config.has_section(section):
                raise ValueError(f"Seção obrigatória não encontrada: [{section}]")
    
    # =========================================================================
    # PATHS
    # =========================================================================
    def get_input_folder(self):
        """Retorna pasta de entrada"""
        return self.config.get('PATHS', 'input_folder', fallback='./entrada')
    
    def get_output_folder(self):
        """Retorna pasta de saída"""
        return self.config.get('PATHS', 'output_folder', fallback='./saida')
    
    def get_log_folder(self):
        """Retorna pasta de logs"""
        return self.config.get('PATHS', 'log_folder', fallback='./logs')
    
    # =========================================================================
    # PROCESSING
    # =========================================================================
    def get_process_all(self):
        """Processar todos os vídeos?"""
        return self.config.getboolean('PROCESSING', 'process_all', fallback=True)
    
    def get_overwrite(self):
        """Sobrescrever ficheiros existentes?"""
        return self.config.getboolean('PROCESSING', 'overwrite', fallback=False)
    
    def get_keep_original_name(self):
        """Manter nome original do ficheiro?"""
        return self.config.getboolean('PROCESSING', 'keep_original_name', fallback=True)
    
    # =========================================================================
    # PROFILE
    # =========================================================================
    def get_active_profile(self):
        """Retorna perfil ativo: baixa, media, alta, custom"""
        return self.config.get('PROFILE', 'active_profile', fallback='media').lower()
    
    def get_profile_settings(self):
        """Retorna configurações do perfil ativo"""
        profile = self.get_active_profile()
        
        profiles = {
            'baixa': {
                'channels': 'mono',
                'bitrate': '64k',
                'sample_rate': 22050
            },
            'media': {
                'channels': 'stereo',
                'bitrate': '128k',
                'sample_rate': 44100
            },
            'alta': {
                'channels': 'stereo',
                'bitrate': '320k',
                'sample_rate': 48000
            },
            'custom': {
                'channels': self.config.get('PROFILE_CUSTOM', 'channels', fallback='stereo'),
                'bitrate': self.config.get('PROFILE_CUSTOM', 'bitrate', fallback='128k'),
                'sample_rate': self.config.getint('PROFILE_CUSTOM', 'sample_rate', fallback=44100)
            }
        }
        
        if profile not in profiles:
            logging.warning(f"Perfil '{profile}' inválido. Usando 'media'")
            profile = 'media'
        
        return profiles[profile]
    
    # =========================================================================
    # NORMALIZATION
    # =========================================================================
    def get_normalization_enabled(self):
        """Normalização de volume ativada?"""
        return self.config.getboolean('NORMALIZATION', 'enabled', fallback=True)
    
    def get_normalization_target(self):
        """Nível alvo de normalização em dBFS"""
        return self.config.getfloat('NORMALIZATION', 'target_level', fallback=-12.0)
    
    # =========================================================================
    # SILENCE_REMOVAL
    # =========================================================================
    def get_silence_removal_enabled(self):
        """Remoção de silêncios ativada?"""
        return self.config.getboolean('SILENCE_REMOVAL', 'enabled', fallback=True)
    
    def get_silence_threshold(self):
        """Limiar de silêncio em dBFS"""
        return self.config.getfloat('SILENCE_REMOVAL', 'silence_threshold', fallback=-40)
    
    def get_silence_min_duration(self):
        """Duração mínima de silêncio em segundos"""
        return self.config.getfloat('SILENCE_REMOVAL', 'min_silence_duration', fallback=1.0)
    
    # =========================================================================
    # SEGMENT_REMOVAL
    # =========================================================================
    def get_segment_removal_enabled(self):
        """Remoção de segmentos ativada?"""
        return self.config.getboolean('SEGMENT_REMOVAL', 'enabled', fallback=False)
    
    def get_remove_start(self):
        """Segundos a remover do início"""
        return self.config.getfloat('SEGMENT_REMOVAL', 'remove_start', fallback=0)
    
    def get_remove_end(self):
        """Segundos a remover do fim"""
        return self.config.getfloat('SEGMENT_REMOVAL', 'remove_end', fallback=0)
    
    # =========================================================================
    # FILTERS
    # =========================================================================
    def get_highpass_filter_enabled(self):
        """Filtro passa-alta ativado?"""
        return self.config.getboolean('FILTERS', 'highpass_filter', fallback=False)
    
    def get_highpass_freq(self):
        """Frequência do filtro passa-alta"""
        return self.config.getint('FILTERS', 'highpass_freq', fallback=80)
    
    def get_lowpass_filter_enabled(self):
        """Filtro passa-baixa ativado?"""
        return self.config.getboolean('FILTERS', 'lowpass_filter', fallback=False)
    
    def get_lowpass_freq(self):
        """Frequência do filtro passa-baixa"""
        return self.config.getint('FILTERS', 'lowpass_freq', fallback=8000)
    
    def get_compression_enabled(self):
        """Compressão dinâmica ativada?"""
        return self.config.getboolean('FILTERS', 'compression', fallback=False)
    
    def get_compression_threshold(self):
        """Limiar de compressão em dBFS"""
        return self.config.getfloat('FILTERS', 'compression_threshold', fallback=-20)
    
    def get_compression_ratio(self):
        """Rácio de compressão"""
        return self.config.getfloat('FILTERS', 'compression_ratio', fallback=4)
    
    # =========================================================================
    # QUALITY_ANALYSIS
    # =========================================================================
    def get_quality_analysis_enabled(self):
        """Análise de qualidade ativada?"""
        return self.config.getboolean('QUALITY_ANALYSIS', 'enabled', fallback=True)
    
    def get_detailed_stats(self):
        """Mostrar estatísticas detalhadas?"""
        return self.config.getboolean('QUALITY_ANALYSIS', 'detailed_stats', fallback=True)
    
    # =========================================================================
    # LOGGING
    # =========================================================================
    def get_log_level(self):
        """Nível de log: DEBUG, INFO, WARNING, ERROR"""
        return self.config.get('LOGGING', 'log_level', fallback='INFO').upper()
    
    def get_log_file(self):
        """Nome do arquivo de log"""
        return self.config.get('LOGGING', 'log_file', fallback='video_to_audio.log')
    
    def get_log_with_timestamp(self):
        """Incluir timestamp no nome do log?"""
        return self.config.getboolean('LOGGING', 'log_with_timestamp', fallback=True)
    
    # =========================================================================
    # UTILITÁRIOS
    # =========================================================================
    def print_summary(self):
        """Imprime resumo das configurações"""
        profile = self.get_profile_settings()
        
        print("\n" + "="*70)
        print("CONFIGURAÇÕES ATIVAS".center(70))
        print("="*70)
        print(f"\n📂 PASTAS:")
        print(f"   Entrada:  {self.get_input_folder()}")
        print(f"   Saída:    {self.get_output_folder()}")
        print(f"   Logs:     {self.get_log_folder()}")
        
        print(f"\n🎵 PERFIL DE CONVERSÃO: {self.get_active_profile().upper()}")
        print(f"   Canais:        {profile['channels']}")
        print(f"   Bitrate:       {profile['bitrate']}")
        print(f"   Sample Rate:   {profile['sample_rate']} Hz")
        
        print(f"\n🔊 NORMALIZAÇÃO: {'✓ Ativada' if self.get_normalization_enabled() else '✗ Desativada'}")
        if self.get_normalization_enabled():
            print(f"   Nível alvo:    {self.get_normalization_target()} dBFS")
        
        print(f"\n🔇 REMOÇÃO DE SILÊNCIOS: {'✓ Ativada' if self.get_silence_removal_enabled() else '✗ Desativada'}")
        if self.get_silence_removal_enabled():
            print(f"   Limiar:        {self.get_silence_threshold()} dBFS")
            print(f"   Duração mín:   {self.get_silence_min_duration()}s")
        
        print(f"\n✂️  REMOÇÃO DE SEGMENTOS: {'✓ Ativada' if self.get_segment_removal_enabled() else '✗ Desativada'}")
        if self.get_segment_removal_enabled():
            print(f"   Início:        {self.get_remove_start()}s")
            print(f"   Fim:           {self.get_remove_end()}s")
        
        filters_active = []
        if self.get_highpass_filter_enabled():
            filters_active.append(f"Passa-alta ({self.get_highpass_freq()}Hz)")
        if self.get_lowpass_filter_enabled():
            filters_active.append(f"Passa-baixa ({self.get_lowpass_freq()}Hz)")
        if self.get_compression_enabled():
            filters_active.append(f"Compressão ({self.get_compression_ratio()}:1)")
        
        print(f"\n🎚️  FILTROS: {', '.join(filters_active) if filters_active else '✗ Nenhum'}")
        
        print(f"\n📊 ANÁLISE DE QUALIDADE: {'✓ Ativada' if self.get_quality_analysis_enabled() else '✗ Desativada'}")
        print(f"\n⚙️  PROCESSAMENTO:")
        print(f"   Processar todos: {'✓ Sim' if self.get_process_all() else '✗ Não (apenas primeiro)'}")
        print(f"   Sobrescrever:    {'✓ Sim' if self.get_overwrite() else '✗ Não (criar versões)'}")
        
        print("\n" + "="*70 + "\n")
