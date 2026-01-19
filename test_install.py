"""
test_install.py
Verifica se todas as dependências estão instaladas corretamente
"""

import sys
import os

def test_installation():
    """Testa instalação completa do sistema"""
    
    print("\n" + "="*70)
    print("TESTE DE INSTALAÇÃO - Conversor MP4 para MP3".center(70))
    print("="*70 + "\n")
    
    errors = []
    warnings = []
    
    # Testar versão Python
    print("📍 Testando Python...")
    py_version = sys.version_info
    if py_version.major >= 3 and py_version.minor >= 8:
        print(f"   ✅ Python {py_version.major}.{py_version.minor}.{py_version.micro}")
    else:
        errors.append("❌ Python 3.8+ necessário")
        print(f"   ❌ Python {py_version.major}.{py_version.minor} (necessário 3.8+)")
    
    # Testar moviepy
    print("\n📍 Testando moviepy...")
    try:
        import moviepy
        import moviepy.editor
        print(f"   ✅ moviepy {moviepy.__version__} instalado")
    except ImportError as e:
        errors.append("❌ moviepy não instalado")
        print(f"   ❌ moviepy não encontrado: {e}")
    
    # Testar pydub
    print("\n📍 Testando pydub...")
    try:
        import pydub
        from pydub import AudioSegment
        print("   ✅ pydub instalado")
    except ImportError as e:
        errors.append("❌ pydub não instalado")
        print(f"   ❌ pydub não encontrado: {e}")
    
    # Testar numpy
    print("\n📍 Testando numpy...")
    try:
        import numpy
        print(f"   ✅ numpy {numpy.__version__} instalado")
    except ImportError as e:
        errors.append("❌ numpy não instalado")
        print(f"   ❌ numpy não encontrado: {e}")
    
    # Testar FFmpeg
    print("\n📍 Testando FFmpeg...")
    try:
        from moviepy.config import get_setting
        ffmpeg_binary = get_setting("FFMPEG_BINARY")
        print(f"   ✅ FFmpeg encontrado: {ffmpeg_binary}")
        
        # Testar se FFmpeg funciona
        import subprocess
        result = subprocess.run(
            [ffmpeg_binary, '-version'],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            version_line = result.stdout.split('\n')[0]
            print(f"   ✅ FFmpeg funcional: {version_line}")
        else:
            warnings.append("⚠️  FFmpeg encontrado mas pode não funcionar corretamente")
            print("   ⚠️  FFmpeg encontrado mas retornou erro")
    except Exception as e:
        errors.append("❌ FFmpeg não encontrado ou não funcional")
        print(f"   ❌ FFmpeg não encontrado: {e}")
    
    # Testar arquivos do projeto
    print("\n📍 Testando arquivos do projeto...")
    required_files = [
        'main.py',
        'config_loader.py',
        'file_manager.py',
        'video_processor.py',
        'audio_converter.py',
        'quality_analyzer.py',
        'config.ini'
    ]
    
    for filename in required_files:
        if os.path.exists(filename):
            print(f"   ✅ {filename}")
        else:
            warnings.append(f"⚠️  {filename} não encontrado")
            print(f"   ⚠️  {filename} não encontrado")
    
    # Testar pastas
    print("\n📍 Testando estrutura de pastas...")
    folders = ['entrada', 'saida', 'logs']
    for folder in folders:
        if os.path.exists(folder):
            print(f"   ✅ {folder}/")
        else:
            warnings.append(f"⚠️  Pasta {folder}/ não existe (será criada automaticamente)")
            print(f"   ⚠️  {folder}/ não existe (será criada no primeiro uso)")
    
    # Resultado final
    print("\n" + "="*70)
    print("RESULTADO DO TESTE".center(70))
    print("="*70 + "\n")
    
    if not errors and not warnings:
        print("✅ INSTALAÇÃO PERFEITA!")
        print("   Todas as dependências estão instaladas e funcionais.")
        print("   O sistema está pronto para uso!")
        print("\n📝 Próximos passos:")
        print("   1. Coloque vídeos MP4 na pasta 'entrada/'")
        print("   2. Configure 'config.ini' conforme necessário")
        print("   3. Execute: python main.py")
        return True
    
    elif errors:
        print("❌ ERROS CRÍTICOS ENCONTRADOS:")
        for error in errors:
            print(f"   {error}")
        print("\n🔧 Soluções:")
        print("   1. Execute: pip install -r requirements.txt")
        print("   2. Instale FFmpeg: https://ffmpeg.org/download.html")
        print("   3. Consulte INSTALL.md para instruções detalhadas")
        return False
    
    elif warnings:
        print("⚠️  AVISOS (não impedem funcionamento):")
        for warning in warnings:
            print(f"   {warning}")
        print("\n✅ Sistema funcional, mas verifique os avisos acima.")
        return True
    
    print("\n" + "="*70 + "\n")


if __name__ == "__main__":
    try:
        success = test_installation()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ Erro durante teste: {str(e)}")
        sys.exit(1)
