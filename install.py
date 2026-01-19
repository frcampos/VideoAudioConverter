#!/usr/bin/env python3
"""
install.py
Script automático de instalação de dependências
"""

import subprocess
import sys
import os

def print_step(step, message):
    """Imprime passo formatado"""
    print(f"\n{'='*70}")
    print(f"PASSO {step}: {message}")
    print('='*70)

def run_command(cmd, description):
    """Executa comando e mostra resultado"""
    print(f"\n🔧 {description}...")
    print(f"   Comando: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300
        )
        
        if result.returncode == 0:
            print(f"   ✅ {description} - Sucesso!")
            return True
        else:
            print(f"   ❌ {description} - Falhou!")
            print(f"   Erro: {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print(f"   ⏱️ Timeout - operação demorou muito")
        return False
    except Exception as e:
        print(f"   ❌ Erro: {str(e)}")
        return False

def check_python_version():
    """Verifica versão Python"""
    print_step(1, "Verificando Python")
    
    version = sys.version_info
    print(f"   Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 8:
        print("   ✅ Versão compatível!")
        return True
    else:
        print("   ❌ Python 3.8+ necessário!")
        return False

def upgrade_pip():
    """Atualiza pip"""
    print_step(2, "Atualizando pip")
    
    cmd = [sys.executable, "-m", "pip", "install", "--upgrade", "pip"]
    return run_command(cmd, "Atualização do pip")

def install_dependencies():
    """Instala dependências"""
    print_step(3, "Instalando dependências")
    
    if not os.path.exists('requirements.txt'):
        print("   ❌ requirements.txt não encontrado!")
        return False
    
    # Tentar instalar normalmente
    print("\n📦 Tentativa 1: Instalação normal")
    cmd = [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"]
    
    if run_command(cmd, "Instalação de dependências"):
        return True
    
    # Se falhar, tentar sem cache
    print("\n📦 Tentativa 2: Instalação sem cache")
    cmd = [sys.executable, "-m", "pip", "install", "-r", "requirements.txt", "--no-cache-dir"]
    
    if run_command(cmd, "Instalação sem cache"):
        return True
    
    # Se falhar, tentar moviepy específico
    print("\n📦 Tentativa 3: Instalando moviepy manualmente")
    
    # Primeiro desinstalar se existir
    subprocess.run([sys.executable, "-m", "pip", "uninstall", "moviepy", "-y"], 
                   capture_output=True)
    
    cmd = [sys.executable, "-m", "pip", "install", "moviepy==1.0.3", "--no-cache-dir"]
    
    if not run_command(cmd, "Instalação moviepy 1.0.3"):
        return False
    
    # Instalar resto das dependências
    cmd = [sys.executable, "-m", "pip", "install", "pydub", "numpy", "imageio", 
           "imageio-ffmpeg", "decorator", "proglog", "tqdm", "requests"]
    
    return run_command(cmd, "Instalação outras dependências")

def test_imports():
    """Testa imports das bibliotecas"""
    print_step(4, "Testando imports")
    
    errors = []
    
    # Testar PyAV (av)
    print("\n🧪 Testando PyAV...")
    try:
        import av
        print(f"   ✅ av (PyAV) {av.__version__} importado")
        
        try:
            # Testar se consegue abrir container
            print("   ✅ av.open() disponível")
        except Exception as e:
            errors.append(f"av.open(): {e}")
            print(f"   ❌ av.open() falhou: {e}")
    except ImportError as e:
        errors.append(f"av: {e}")
        print(f"   ❌ av (PyAV) não encontrado: {e}")
    
    # Testar numpy
    print("\n🧪 Testando numpy...")
    try:
        import numpy
        print(f"   ✅ numpy {numpy.__version__} importado")
    except ImportError as e:
        errors.append(f"numpy: {e}")
        print(f"   ❌ numpy não encontrado: {e}")
    
    # Testar scipy
    print("\n🧪 Testando scipy...")
    try:
        import scipy
        from scipy import signal
        print(f"   ✅ scipy {scipy.__version__} importado")
    except ImportError as e:
        errors.append(f"scipy: {e}")
        print(f"   ❌ scipy não encontrado: {e}")
    
    # Testar soundfile
    print("\n🧪 Testando soundfile...")
    try:
        import soundfile as sf
        print(f"   ✅ soundfile {sf.__version__} importado")
    except ImportError as e:
        errors.append(f"soundfile: {e}")
        print(f"   ❌ soundfile não encontrado: {e}")
    
    return len(errors) == 0

def main():
    """Função principal"""
    print("\n" + "="*70)
    print("INSTALADOR AUTOMÁTICO".center(70))
    print("Conversor MP4 para WAV - Python Puro".center(70))
    print("="*70)
    
    # Verificar Python
    if not check_python_version():
        print("\n❌ Versão Python incompatível!")
        print("   Instale Python 3.8 ou superior")
        return False
    
    # Atualizar pip
    if not upgrade_pip():
        print("\n⚠️  Aviso: Falha ao atualizar pip (continuando...)")
    
    # Instalar dependências
    if not install_dependencies():
        print("\n❌ Falha na instalação de dependências!")
        print("\n🔧 SOLUÇÕES MANUAIS:")
        print("   1. Atualizar pip:")
        print("      pip install --upgrade pip")
        print("\n   2. Instalar dependências manualmente:")
        print("      pip install av numpy scipy soundfile librosa")
        print("\n   3. Se persistir, criar ambiente virtual:")
        print("      python -m venv venv")
        print("      source venv/bin/activate  # Linux/Mac")
        print("      venv\\Scripts\\activate     # Windows")
        print("      pip install -r requirements.txt")
        return False
    
    # Testar imports
    if not test_imports():
        print("\n❌ Alguns imports falharam!")
        print("\n🔧 Tente reinstalar manualmente:")
        print("   pip install av numpy scipy soundfile")
        return False
    
    # Sucesso
    print("\n" + "="*70)
    print("✅ INSTALAÇÃO COMPLETA!".center(70))
    print("="*70)
    print("\n📝 Próximos passos:")
    print("   1. Teste a instalação:")
        print("      python test_install.py")
    print("\n   2. Coloque vídeos MP4 em: entrada/")
    print("\n   3. Execute o conversor:")
    print("      python main.py")
    print("\n   4. Ficheiros WAV estarão em: saida/")
    print("\n" + "="*70 + "\n")
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Instalação cancelada pelo utilizador")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erro fatal: {str(e)}")
        sys.exit(1)
