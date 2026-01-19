"""
file_manager.py
Gestão de ficheiros e pastas
"""

import os
import logging
from pathlib import Path
from datetime import datetime


class FileManager:
    """Gestão de ficheiros e pastas"""
    
    def __init__(self, config):
        self.config = config
        self.input_folder = config.get_input_folder()
        self.output_folder = config.get_output_folder()
        self.log_folder = config.get_log_folder()
        
    def setup_folders(self):
        """Cria pastas necessárias se não existirem"""
        folders = [self.input_folder, self.output_folder, self.log_folder]
        
        for folder in folders:
            Path(folder).mkdir(parents=True, exist_ok=True)
            logging.debug(f"Pasta verificada/criada: {folder}")
        
        logging.info(f"Pastas configuradas: entrada={self.input_folder}, saída={self.output_folder}")
    
    def get_video_files(self):
        """
        Retorna lista de ficheiros MP4 na pasta de entrada
        
        Returns:
            list: Lista de caminhos completos dos ficheiros MP4
        """
        video_files = []
        
        if not os.path.exists(self.input_folder):
            logging.error(f"Pasta de entrada não existe: {self.input_folder}")
            return video_files
        
        for filename in os.listdir(self.input_folder):
            if filename.lower().endswith('.mp4'):
                filepath = os.path.join(self.input_folder, filename)
                video_files.append(filepath)
                logging.debug(f"Vídeo encontrado: {filename}")
        
        if not video_files:
            logging.warning(f"Nenhum ficheiro MP4 encontrado em: {self.input_folder}")
        else:
            logging.info(f"Total de vídeos encontrados: {len(video_files)}")
        
        return sorted(video_files)
    
    def generate_output_filename(self, input_path):
        """
        Gera nome do ficheiro de saída baseado nas configurações
        
        Args:
            input_path (str): Caminho do ficheiro de entrada
            
        Returns:
            str: Caminho completo do ficheiro de saída
        """
        # Obter nome base do ficheiro (sem extensão)
        base_name = Path(input_path).stem
        
        # Manter nome original ou adicionar sufixo?
        if self.config.get_keep_original_name():
            output_name = f"{base_name}.mp3"
        else:
            output_name = f"{base_name}_converted.mp3"
        
        output_path = os.path.join(self.output_folder, output_name)
        
        # Se não sobrescrever e ficheiro já existe, criar versão numerada
        if not self.config.get_overwrite() and os.path.exists(output_path):
            counter = 1
            while True:
                if self.config.get_keep_original_name():
                    output_name = f"{base_name}_{counter:03d}.mp3"
                else:
                    output_name = f"{base_name}_converted_{counter:03d}.mp3"
                
                output_path = os.path.join(self.output_folder, output_name)
                
                if not os.path.exists(output_path):
                    break
                counter += 1
            
            logging.info(f"Ficheiro já existe. Criando versão: {output_name}")
        
        return output_path
    
    def get_file_size(self, filepath):
        """
        Retorna tamanho do ficheiro em MB
        
        Args:
            filepath (str): Caminho do ficheiro
            
        Returns:
            float: Tamanho em MB
        """
        try:
            size_bytes = os.path.getsize(filepath)
            size_mb = size_bytes / (1024 * 1024)
            return round(size_mb, 2)
        except Exception as e:
            logging.error(f"Erro ao obter tamanho do ficheiro {filepath}: {e}")
            return 0
    
    def get_file_info(self, filepath):
        """
        Retorna informações detalhadas do ficheiro
        
        Args:
            filepath (str): Caminho do ficheiro
            
        Returns:
            dict: Informações do ficheiro
        """
        try:
            stats = os.stat(filepath)
            return {
                'name': os.path.basename(filepath),
                'path': filepath,
                'size_mb': round(stats.st_size / (1024 * 1024), 2),
                'size_bytes': stats.st_size,
                'modified': datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
            }
        except Exception as e:
            logging.error(f"Erro ao obter informações do ficheiro {filepath}: {e}")
            return None
    
    def delete_file(self, filepath):
        """
        Remove ficheiro
        
        Args:
            filepath (str): Caminho do ficheiro
            
        Returns:
            bool: True se removido com sucesso
        """
        try:
            if os.path.exists(filepath):
                os.remove(filepath)
                logging.info(f"Ficheiro removido: {filepath}")
                return True
            return False
        except Exception as e:
            logging.error(f"Erro ao remover ficheiro {filepath}: {e}")
            return False
    
    def validate_input_file(self, filepath):
        """
        Valida se ficheiro de entrada é válido
        
        Args:
            filepath (str): Caminho do ficheiro
            
        Returns:
            bool: True se válido
        """
        # Verifica se ficheiro existe
        if not os.path.exists(filepath):
            logging.error(f"Ficheiro não encontrado: {filepath}")
            return False
        
        # Verifica se é MP4
        if not filepath.lower().endswith('.mp4'):
            logging.error(f"Ficheiro não é MP4: {filepath}")
            return False
        
        # Verifica se não está vazio
        if os.path.getsize(filepath) == 0:
            logging.error(f"Ficheiro vazio: {filepath}")
            return False
        
        return True
    
    def get_processing_summary(self, total, success, failed):
        """
        Retorna resumo do processamento
        
        Args:
            total (int): Total de ficheiros
            success (int): Ficheiros com sucesso
            failed (int): Ficheiros com falha
            
        Returns:
            str: Resumo formatado
        """
        success_rate = (success / total * 100) if total > 0 else 0
        
        summary = f"\n{'='*70}\n"
        summary += "RESUMO DO PROCESSAMENTO".center(70) + "\n"
        summary += f"{'='*70}\n\n"
        summary += f"📊 Total de ficheiros:     {total}\n"
        summary += f"✅ Convertidos com sucesso: {success}\n"
        summary += f"❌ Falhas:                  {failed}\n"
        summary += f"📈 Taxa de sucesso:         {success_rate:.1f}%\n"
        summary += f"\n{'='*70}\n"
        
        return summary
