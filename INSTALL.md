# Guia de Instalação
## Conversor de Vídeo MP4 para Áudio MP3

Instruções passo a passo para instalar e configurar o sistema.

---

## 📋 Pré-requisitos

- **Python 3.8 ou superior**
- **FFmpeg** (necessário para processamento de áudio/vídeo)
- **pip** (gestor de pacotes Python)

---

## 🪟 Instalação no Windows

### Passo 1: Instalar Python

1. Acesse: https://www.python.org/downloads/
2. Descarregue Python 3.8+ (versão mais recente recomendada)
3. Durante a instalação:
   - ✅ Marque "Add Python to PATH"
   - ✅ Marque "Install pip"
4. Verificar instalação:
   ```cmd
   python --version
   pip --version
   ```

### Passo 2: Instalar FFmpeg

**Opção A - Via Chocolatey (recomendado):**
```cmd
choco install ffmpeg
```

**Opção B - Instalação Manual:**
1. Acesse: https://ffmpeg.org/download.html
2. Descarregue FFmpeg para Windows
3. Extraia para `C:\ffmpeg`
4. Adicione ao PATH:
   - Painel de Controlo → Sistema → Variáveis de Ambiente
   - Edite `Path` e adicione: `C:\ffmpeg\bin`
5. Verificar:
   ```cmd
   ffmpeg -version
   ```

### Passo 3: Instalar Dependências Python

```cmd
cd caminho\para\o\projeto
pip install -r requirements.txt
```

### Passo 4: Configurar e Executar

1. Coloque vídeos MP4 na pasta `entrada\`
2. Configure `config.ini` conforme necessário
3. Execute:
   ```cmd
   run.bat
   ```
   ou
   ```cmd
   python main.py
   ```

---

## 🍎 Instalação no macOS

### Passo 1: Instalar Homebrew (se ainda não tiver)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Passo 2: Instalar Python e FFmpeg

```bash
brew install python3
brew install ffmpeg
```

### Passo 3: Verificar Instalações

```bash
python3 --version
pip3 --version
ffmpeg -version
```

### Passo 4: Instalar Dependências Python

```bash
cd caminho/para/o/projeto
pip3 install -r requirements.txt
```

### Passo 5: Configurar e Executar

1. Coloque vídeos MP4 na pasta `entrada/`
2. Configure `config.ini` conforme necessário
3. Execute:
   ```bash
   ./run.sh
   ```
   ou
   ```bash
   python3 main.py
   ```

---

## 🐧 Instalação no Linux (Ubuntu/Debian)

### Passo 1: Atualizar Sistema

```bash
sudo apt update
sudo apt upgrade
```

### Passo 2: Instalar Python e FFmpeg

```bash
sudo apt install python3 python3-pip ffmpeg
```

### Passo 3: Verificar Instalações

```bash
python3 --version
pip3 --version
ffmpeg -version
```

### Passo 4: Instalar Dependências Python

```bash
cd caminho/para/o/projeto
pip3 install -r requirements.txt
```

### Passo 5: Configurar e Executar

1. Coloque vídeos MP4 na pasta `entrada/`
2. Configure `config.ini` conforme necessário
3. Execute:
   ```bash
   ./run.sh
   ```
   ou
   ```bash
   python3 main.py
   ```

---

## ✅ Verificação da Instalação

Execute este teste para verificar se tudo está funcionando:

```python
# test_install.py
import sys

def test_installation():
    errors = []
    
    # Testar Python
    print("✓ Python versão:", sys.version)
    
    # Testar moviepy
    try:
        import moviepy.editor
        print("✓ moviepy instalado")
    except ImportError:
        errors.append("❌ moviepy não encontrado")
    
    # Testar pydub
    try:
        import pydub
        print("✓ pydub instalado")
    except ImportError:
        errors.append("❌ pydub não encontrado")
    
    # Testar FFmpeg
    try:
        from moviepy.config import get_setting
        ffmpeg_path = get_setting("FFMPEG_BINARY")
        print(f"✓ FFmpeg encontrado: {ffmpeg_path}")
    except:
        errors.append("❌ FFmpeg não encontrado")
    
    if errors:
        print("\n⚠️ ERROS ENCONTRADOS:")
        for error in errors:
            print(error)
        return False
    else:
        print("\n✅ Instalação completa e funcional!")
        return True

if __name__ == "__main__":
    test_installation()
```

Executar teste:
```bash
python test_install.py
```

---

## 🔧 Problemas Comuns

### Erro: "Python não é reconhecido"
- **Solução:** Python não está no PATH. Reinstale Python e marque "Add to PATH"

### Erro: "FFmpeg não encontrado"
- **Solução:** Instale FFmpeg e adicione ao PATH do sistema

### Erro: "No module named 'moviepy'"
- **Solução:** Execute `pip install -r requirements.txt`

### Erro: "Permission denied" (Linux/Mac)
- **Solução:** 
  ```bash
  chmod +x run.sh
  ./run.sh
  ```

### Erro: "ModuleNotFoundError: No module named 'imageio_ffmpeg'"
- **Solução:** 
  ```bash
  pip install imageio-ffmpeg
  ```

---

## 📦 Estrutura Final

Após instalação, seu projeto deve ter:

```
projeto/
├── config.ini          ✅ Configuração
├── main.py             ✅ Script principal
├── config_loader.py    ✅ Módulo
├── file_manager.py     ✅ Módulo
├── video_processor.py  ✅ Módulo
├── audio_converter.py  ✅ Módulo
├── quality_analyzer.py ✅ Módulo
├── requirements.txt    ✅ Dependências
├── README.md           ✅ Documentação
├── run.bat            ✅ Windows
├── run.sh             ✅ Linux/Mac
├── entrada/           📂 Coloque MP4s aqui
├── saida/             📂 MP3s aparecem aqui
└── logs/              📂 Logs de execução
```

---

## 🎯 Pronto para Usar!

Após instalação completa:

1. ✅ Python instalado e no PATH
2. ✅ FFmpeg instalado e funcional
3. ✅ Dependências Python instaladas
4. ✅ Pastas criadas
5. ✅ config.ini configurado

**Próximo passo:** Coloque seus MP4s em `entrada/` e execute!

---

## 📞 Suporte

- Consulte `README.md` para uso detalhado
- Verifique `logs/` para diagnóstico de erros
- Teste com 1 vídeo pequeno primeiro (configure `process_all = false`)
