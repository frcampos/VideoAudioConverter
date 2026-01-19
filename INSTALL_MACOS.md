# 🍎 Instalação Completa no macOS

Guia passo a passo para instalar o Conversor MP4 para MP3 no macOS.

---

## 📋 Requisitos

- macOS 10.14 ou superior
- Terminal (aplicação nativa do macOS)
- Conexão à internet

---

## 🚀 Instalação Completa (10 minutos)

### Passo 1: Instalar Homebrew (se ainda não tiver)

Abra o **Terminal** e execute:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Aguarde a instalação (pode demorar alguns minutos).

---

### Passo 2: Instalar Python 3

```bash
brew install python3
```

Verificar instalação:
```bash
python3 --version
# Deve mostrar: Python 3.x.x
```

---

### Passo 3: Instalar FFmpeg

```bash
brew install ffmpeg
```

Verificar instalação:
```bash
ffmpeg -version
# Deve mostrar informações do FFmpeg
```

---

### Passo 4: Descarregar e Extrair o Projeto

**Opção A - Se tem o ZIP:**
1. Descarregue `video_to_mp3_converter.zip`
2. Dê duplo clique para extrair
3. Mova a pasta para um local conveniente (ex: Documents)

**Opção B - Terminal:**
```bash
cd ~/Documents
unzip video_to_mp3_converter.zip
cd video_to_mp3_converter
```

---

### Passo 5: Instalar Dependências Python

No Terminal, dentro da pasta do projeto:

**Método Automático (Recomendado):**
```bash
python3 install.py
```

**Método Manual:**
```bash
# Atualizar pip
python3 -m pip install --upgrade pip

# Instalar dependências
python3 -m pip install -r requirements.txt
```

**Se der erro com moviepy, use este método:**
```bash
# Desinstalar moviepy existente
pip3 uninstall moviepy -y

# Instalar versão específica
pip3 install moviepy==1.0.3 --no-cache-dir

# Instalar outras dependências
pip3 install pydub numpy imageio imageio-ffmpeg decorator proglog tqdm requests
```

---

### Passo 6: Testar Instalação

```bash
python3 test_install.py
```

Deve ver:
```
✅ INSTALAÇÃO PERFEITA!
```

---

### Passo 7: Preparar Vídeos

```bash
# Copiar vídeos MP4 para pasta entrada
cp ~/Movies/meu_video.mp4 entrada/

# Verificar
ls entrada/
```

---

### Passo 8: Executar Conversor

```bash
# Dar permissão ao script
chmod +x run.sh

# Executar
./run.sh
```

**Ou diretamente:**
```bash
python3 main.py
```

---

### Passo 9: Recolher MP3s

```bash
# Ver ficheiros convertidos
ls -lh saida/

# Abrir pasta no Finder
open saida/
```

---

## ⚙️ Configuração Rápida

Editar configurações:
```bash
nano config.ini
# ou
open -a TextEdit config.ini
```

Principais configurações:
```ini
[PROFILE]
active_profile = media  # baixa|media|alta

[NORMALIZATION]
enabled = true
target_level = -12.0
```

---

## 🧪 Verificação Completa

Execute estes comandos para verificar tudo:

```bash
# 1. Python
python3 --version
which python3

# 2. pip
pip3 --version

# 3. FFmpeg
ffmpeg -version
which ffmpeg

# 4. Dependências Python
pip3 list | grep moviepy
pip3 list | grep pydub

# 5. Teste completo
python3 test_install.py
```

---

## 🔧 Troubleshooting

### ❌ "command not found: brew"
Instale Homebrew (Passo 1)

### ❌ "command not found: python3"
```bash
brew install python3
```

### ❌ "ModuleNotFoundError: No module named 'moviepy'"
```bash
python3 install.py
# ou
pip3 install moviepy==1.0.3 --no-cache-dir
```

### ❌ "FFmpeg não encontrado"
```bash
brew install ffmpeg
```

### ❌ "Permission denied"
```bash
chmod +x run.sh
./run.sh
```

---

## 💡 Dicas macOS

### Usar Ambiente Virtual (Recomendado)

```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar
source venv/bin/activate

# Agora instalar
pip install -r requirements.txt

# Quando terminar
deactivate
```

### Abrir Terminal na Pasta

1. Finder → Pasta do projeto
2. Botão direito na pasta → "Novo Terminal no Diretório"

### Criar Atalho no Dock

```bash
# Criar script de atalho
echo '#!/bin/bash
cd ~/Documents/video_to_mp3_converter
python3 main.py' > ~/Desktop/converter.command

# Dar permissão
chmod +x ~/Desktop/converter.command
```

Agora pode arrastar `converter.command` para o Dock!

---

## 📁 Estrutura Recomendada

```
~/Documents/video_to_mp3_converter/
├── config.ini
├── main.py
├── entrada/          ← Colocar MP4s aqui
├── saida/           ← MP3s aparecem aqui
└── logs/            ← Ver erros aqui
```

---

## 🎯 Exemplo Completo

```bash
# 1. Navegar para pasta
cd ~/Documents/video_to_mp3_converter

# 2. Copiar vídeo
cp ~/Movies/aula.mp4 entrada/

# 3. Executar
python3 main.py

# 4. Abrir pasta saída
open saida/

# 5. Verificar logs (se houve erros)
cat logs/*.log
```

---

## 📚 Próximos Passos

- 📖 Leia `README_PT.txt` para mais detalhes
- 🚀 Veja `QUICKSTART.md` para uso rápido
- 📝 Consulte `config_examples.ini` para exemplos
- 🔧 Em caso de erro: `TROUBLESHOOTING.md`

---

## ✅ Checklist Final

- [ ] Homebrew instalado
- [ ] Python 3.8+ instalado
- [ ] FFmpeg instalado
- [ ] Dependências Python instaladas
- [ ] `python3 test_install.py` passou
- [ ] Vídeo MP4 em `entrada/`
- [ ] `python3 main.py` executou
- [ ] MP3 criado em `saida/`

---

**Tudo pronto? Boa conversão! 🎵**
