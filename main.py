"""
main.py
Conversor de Vídeo MP4 para Áudio MP3
Orquestrador principal do sistema
"""

import logging
import os
import sys
from datetime import datetime
from pathlib import Path

# Importar módulos
from config_loader import ConfigLoader
from file_manager import FileManager
from video_processor import VideoProcessor
from audio_converter import AudioConverter
from quality_analyzer import QualityAnalyzer


class VideoToAudioConverter:
    """Conversor principal de vídeo para áudio"""
    
    def __init__(self, config_path='config.ini'):
        """
        Inicializa conversor
        
        Args:
            config_path (str): Caminho do arquivo de configuração
        """
        self.config_path = config_path
        self.config = None
        self.file_manager = None
        self.video_processor = None
        self.audio_converter = None
        self.quality_analyzer = None
        
        # Estatísticas
        self.stats = {
            'total': 0,
            'success': 0,
            'failed': 0,
            'start_time': None,
            'end_time': None
        }
    
    def initialize(self):
        """Inicializa componentes do sistema"""
        try:
            print("\n" + "="*70)
            print("CONVERSOR DE VÍDEO MP4 PARA ÁUDIO MP3".center(70))
            print("="*70 + "\n")
            
            # Carregar configuração
            print("📋 Carregando configurações...")
            self.config = ConfigLoader(self.config_path)
            
            # Configurar logging
            self._setup_logging()
            
            # Mostrar resumo de configurações
            self.config.print_summary()
            
            # Inicializar módulos
            print("🔧 Inicializando módulos...")
            self.file_manager = FileManager(self.config)
            self.video_processor = VideoProcessor(self.config)
            self.audio_converter = AudioConverter(self.config)
            self.quality_analyzer = QualityAnalyzer(self.config)
            
            # Configurar pastas
            self.file_manager.setup_folders()
            
            logging.info("Sistema inicializado com sucesso")
            print("✅ Sistema pronto!\n")
            
            return True
            
        except Exception as e:
            print(f"\n❌ Erro na inicialização: {str(e)}")
            logging.error(f"Erro na inicialização: {str(e)}")
            return False
    
    def _setup_logging(self):
        """Configura sistema de logging"""
        log_level = getattr(logging, self.config.get_log_level())
        log_folder = self.config.get_log_folder()
        log_file = self.config.get_log_file()
        
        # Criar pasta de logs
        Path(log_folder).mkdir(parents=True, exist_ok=True)
        
        # Nome do arquivo de log com timestamp?
        if self.config.get_log_with_timestamp():
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            log_name = f"{Path(log_file).stem}_{timestamp}{Path(log_file).suffix}"
        else:
            log_name = log_file
        
        log_path = os.path.join(log_folder, log_name)
        
        # Configurar logging
        logging.basicConfig(
            level=log_level,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_path, encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
        
        logging.info("="*70)
        logging.info(f"Sessão iniciada: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        logging.info("="*70)
    
    def process_videos(self):
        """Processa todos os vídeos da pasta de entrada"""
        print("🔍 Procurando vídeos MP4...\n")
        
        # Obter lista de vídeos
        video_files = self.file_manager.get_video_files()
        
        if not video_files:
            print("❌ Nenhum vídeo MP4 encontrado na pasta de entrada!")
            logging.warning("Nenhum vídeo encontrado para processar")
            return False
        
        print(f"📹 Encontrados {len(video_files)} vídeo(s)\n")
        
        # Processar apenas o primeiro ou todos?
        if not self.config.get_process_all():
            video_files = video_files[:1]
            print("⚠️  Modo teste: processando apenas o primeiro vídeo\n")
        
        # Estatísticas
        self.stats['total'] = len(video_files)
        self.stats['start_time'] = datetime.now()
        
        # Processar cada vídeo
        for idx, video_path in enumerate(video_files, 1):
            print("="*70)
            print(f"Processando {idx}/{len(video_files)}: {os.path.basename(video_path)}")
            print("="*70 + "\n")
            
            success = self._process_single_video(video_path)
            
            if success:
                self.stats['success'] += 1
            else:
                self.stats['failed'] += 1
            
            print()
        
        # Estatísticas finais
        self.stats['end_time'] = datetime.now()
        self._print_final_stats()
        
        return True
    
    def _process_single_video(self, video_path):
        """
        Processa um único vídeo
        
        Args:
            video_path (str): Caminho do vídeo
            
        Returns:
            bool: True se processado com sucesso
        """
        temp_audio_path = None
        
        try:
            # Validar ficheiro
            if not self.file_manager.validate_input_file(video_path):
                return False
            
            # Gerar nome de saída
            output_path = self.file_manager.generate_output_filename(video_path)
            print(f"📤 Saída: {os.path.basename(output_path)}\n")
            
            # Caminho temporário para áudio WAV
            temp_audio_path = os.path.join(
                self.file_manager.output_folder,
                '_temp_audio.wav'
            )
            
            # ETAPA 1: Extrair áudio do vídeo
            print("🎬 [1/3] Extraindo áudio do vídeo...")
            success, duration, message = self.video_processor.extract_audio(
                video_path,
                temp_audio_path
            )
            
            if not success:
                print(f"❌ Falha na extração: {message}")
                return False
            
            print(f"✅ Áudio extraído ({duration:.1f}s)\n")
            
            # ETAPA 2: Converter e otimizar áudio
            print("🎵 [2/3] Convertendo e otimizando áudio...")
            success, message = self.audio_converter.convert_audio(
                temp_audio_path,
                output_path
            )
            
            if not success:
                print(f"❌ Falha na conversão: {message}")
                return False
            
            print(f"✅ Conversão concluída\n")
            
            # ETAPA 3: Análise de qualidade
            print("📊 [3/3] Analisando qualidade...")
            analysis = self.quality_analyzer.analyze_conversion(
                temp_audio_path,
                output_path,
                duration
            )
            
            if analysis:
                self.quality_analyzer.print_summary(analysis)
            
            print("\n✅ Vídeo processado com sucesso!")
            logging.info(f"Vídeo processado: {os.path.basename(video_path)}")
            
            return True
            
        except Exception as e:
            print(f"\n❌ Erro no processamento: {str(e)}")
            logging.error(f"Erro ao processar {video_path}: {str(e)}")
            return False
        
        finally:
            # Remover arquivo temporário
            if temp_audio_path and os.path.exists(temp_audio_path):
                try:
                    os.remove(temp_audio_path)
                    logging.debug("Arquivo temporário removido")
                except:
                    pass
    
    def _print_final_stats(self):
        """Imprime estatísticas finais"""
        duration = (self.stats['end_time'] - self.stats['start_time']).total_seconds()
        
        print("\n" + "="*70)
        print("PROCESSAMENTO CONCLUÍDO".center(70))
        print("="*70)
        print(f"\n📊 Total de vídeos:       {self.stats['total']}")
        print(f"✅ Convertidos:           {self.stats['success']}")
        print(f"❌ Falhas:                {self.stats['failed']}")
        
        if self.stats['total'] > 0:
            success_rate = (self.stats['success'] / self.stats['total']) * 100
            print(f"📈 Taxa de sucesso:       {success_rate:.1f}%")
        
        print(f"⏱️  Tempo total:           {duration:.1f}s")
        
        if self.stats['success'] > 0:
            avg_time = duration / self.stats['success']
            print(f"⌛ Tempo médio/vídeo:     {avg_time:.1f}s")
        
        print("\n" + "="*70)
        
        logging.info("="*70)
        logging.info(f"Processamento concluído: {self.stats['success']}/{self.stats['total']} sucesso")
        logging.info("="*70)


def main():
    """Função principal"""
    try:
        # Verificar se config.ini existe
        if not os.path.exists('config.ini'):
            print("\n❌ Erro: Arquivo config.ini não encontrado!")
            print("   Crie o arquivo config.ini na mesma pasta do script.")
            sys.exit(1)
        
        # Criar e inicializar conversor
        converter = VideoToAudioConverter('config.ini')
        
        if not converter.initialize():
            sys.exit(1)
        
        # Processar vídeos
        converter.process_videos()
        
        print("\n👋 Até breve!\n")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Processamento interrompido pelo utilizador")
        logging.warning("Processamento interrompido")
        sys.exit(0)
    
    except Exception as e:
        print(f"\n❌ Erro fatal: {str(e)}")
        logging.critical(f"Erro fatal: {str(e)}")
        sys.exit(1)


if __name__ == '__main__':
    main()
