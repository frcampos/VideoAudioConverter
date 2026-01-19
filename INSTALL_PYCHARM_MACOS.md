# 🐍 Instalação no PyCharm + macOS

Guia completo para configurar o Conversor MP4 para MP3 no PyCharm com ambiente virtual.

---

## 📋 Pré-requisitos

- macOS 10.14 ou superior
- PyCharm (Community ou Professional)
- Homebrew (gestor de pacotes macOS)

---

## 🚀 Instalação Completa (Passo a Passo)

### PASSO 1: Instalar Homebrew (se ainda não tiver)

Abra o **Terminal** (fora do PyCharm):

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Aguarde a instalação (~5 minutos).

---

### PASSO 2: Instalar FFmpeg (Obrigatório!)

No **Terminal**:

```bash
brew install ffmpeg
```

Verificar instalação:
```bash
ffmpeg -version
```

Deve mostrar algo como:
```
ffmpeg version 6.0
```

**⚠️ IMPORTANTE:** FFmpeg deve estar instalado ANTES de instalar as bibliotecas Python!

---

### PASSO 3: Abrir Projeto no PyCharm

1. Abra **PyCharm**
2. **File → Open**
3. Selecione a pasta `video_to_mp3_converter`
4. Aguarde PyCharm indexar o projeto

---

### PASSO 4: Configurar Ambiente Virtual no PyCharm

#### Opção A - Criar Novo Ambiente Virtual (Recomendado)

1. **PyCharm → Settings** (ou `Cmd + ,`)
2. **Project: video_to_mp3_converter → Python Interpreter**
3. Clicar no ⚙️ → **Add Interpreter**
4. Selecionar **Virtualenv Environment**
5. Escolher **New environment**
6. Base interpreter: Python 3.8+ (usar `/usr/local/bin/python3` ou `/usr/bin/python3`)
7. Location: deixar padrão (`./venv`)
8. Marcar: ✅ **Inherit global site-packages** (opcional)
9. Clicar **OK**

PyCharm criará o ambiente virtual automaticamente.

#### Opção B - Usar Ambiente Virtual Existente

Se já tem `.venv` na pasta:

1. **PyCharm → Settings** (ou `Cmd + ,`)
2. **Project → Python Interpreter**
3. Clicar no ⚙️ → **Add Interpreter**
4. Selecionar **Virtualenv Environment**
5. **Existing environment**
6. Interpreter: `/Users/fernandocampos/PycharmProjects/PConverterVideoAudio/.venv/bin/python`
7. Clicar **OK**

---

### PASSO 5: Abrir Terminal do PyCharm

No PyCharm:
1. **View → Tool Windows → Terminal** (ou `Alt + F12`)
2. O terminal abre já com o ambiente virtual ativado
3. Deve ver `(.venv)` no início da linha

**Exemplo:**
```
(.venv) fernandocampos@MacBook-Pro PConverterVideoAudio %
```

---

### PASSO 6: Instalar Dependências no PyCharm Terminal

No **Terminal do PyCharm** (com venv ativado):

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Se der erro "ModuleNotFoundError: No module named 'moviepy.editor'":**

```bash
# Desinstalar versão problemática
pip uninstall moviepy -y

# Instalar versão específica
pip install moviepy==1.0.3 --no-cache-dir

# Instalar outras dependências
pip install pydub numpy imageio imageio-ffmpeg decorator proglog tqdm
```

---

### PASSO 7: Testar Instalação

No **Terminal do PyCharm**:

```bash
python test_install.py
```

Deve ver:
```
✅ INSTALAÇÃO PERFEITA!
✅ Python 3.x.x
✅ moviepy 1.0.3 instalado
✅ pydub instalado
✅ FFmpeg encontrado: /opt/homebrew/bin/ffmpeg
```

---

### PASSO 8: Configurar Projeto

Editar `config.ini` no PyCharm:

```ini
[PATHS]
input_folder = ./entrada
output_folder = ./saida

[PROFILE]
active_profile = media  # baixa|media|alta

[PROCESSING]
process_all = true
```

---

### PASSO 9: Preparar Vídeos

Copiar vídeos MP4 para pasta `entrada/`:

**Opção 1 - No Finder:**
- Arrastar MP4s para pasta `entrada/` do projeto

**Opção 2 - Terminal do PyCharm:**
```bash
cp ~/Movies/meu_video.mp4 entrada/
```

---

### PASSO 10: Executar no PyCharm

#### Método 1 - Terminal do PyCharm (Recomendado)

```bash
python main.py
```

#### Método 2 - Run Configuration

1. Botão direito em `main.py`
2. **Run 'main'**

Ou:
1. **Run → Edit Configurations**
2. **+ → Python**
3. Name: `Conversor MP4 para MP3`
4. Script path: `/caminho/completo/main.py`
5. Working directory: pasta do projeto
6. Python interpreter: selecionar venv
7. **OK**
8. Clicar no ▶️ verde

---

### PASSO 11: Verificar Resultados

MP3s estarão em `saida/`:

**Ver no PyCharm:**
- Painel esquerdo → `saida/` → ver MP3s criados

**Abrir no Finder:**
```bash
open saida/
```

---

## 🔧 Troubleshooting PyCharm

### ❌ "No module named 'moviepy.editor'"

**Causa:** moviepy não instalado no venv do PyCharm

**Solução:**
```bash
# No Terminal do PyCharm (com venv ativado)
pip install moviepy==1.0.3 --no-cache-dir
python test_install.py
```

---

### ❌ "FFmpeg não encontrado"

**Causa:** FFmpeg não instalado ou não no PATH

**Solução:**
```bash
# Instalar FFmpeg
brew install ffmpeg

# Verificar
which ffmpeg
ffmpeg -version
```

Se PyCharm não encontra, adicionar ao PATH no terminal:
```bash
export PATH="/opt/homebrew/bin:$PATH"
```

Ou permanentemente em `~/.zshrc`:
```bash
echo 'export PATH="/opt/homebrew/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

---

### ❌ Terminal do PyCharm não ativa venv

**Solução:**
1. **PyCharm → Settings**
2. **Tools → Terminal**
3. Marcar: ✅ **Activate virtualenv**
4. Fechar e reabrir Terminal do PyCharm

---

### ❌ "Permission denied" ao executar

**Solução:**
```bash
chmod +x main.py
python main.py
```

---

### ❌ Importações sublinhadas em vermelho no PyCharm

**Causa:** PyCharm não reconhece o venv

**Solução:**
1. **File → Invalidate Caches**
2. Selecionar: **Invalidate and Restart**

Ou:
1. **Settings → Project → Python Interpreter**
2. Reconfigurar venv

---

## 💡 Dicas PyCharm

### Executar Direto no Editor

1. Abrir `main.py`
2. Clicar direito no código
3. **Run 'main'**

### Ver Logs em Tempo Real

1. Executar `main.py`
2. Aba **Run** mostra output em tempo real
3. Ver logs detalhados em `logs/`

### Debugar

1. Colocar breakpoint (clicar à esquerda da linha)
2. Botão direito em `main.py` → **Debug 'main'**
3. Inspecionar variáveis, step-by-step

### Atalhos Úteis

- `Ctrl + Enter`: Executar linha no Terminal
- `Shift + F10`: Run
- `Shift + F9`: Debug
- `Alt + F12`: Terminal
- `Cmd + ,`: Settings

---

## 📊 Verificação Completa

Execute estes comandos no **Terminal do PyCharm**:

```bash
# 1. Verificar venv ativado
which python
# Deve mostrar: .../venv/bin/python

# 2. Verificar FFmpeg
ffmpeg -version

# 3. Verificar instalação Python
python test_install.py

# 4. Listar pacotes instalados
pip list | grep -E "moviepy|pydub|numpy"

# 5. Testar conversão
python main.py
```

---

## 🎯 Estrutura no PyCharm

```
video_to_mp3_converter/
├── .venv/               # Ambiente virtual (PyCharm cria)
├── config.ini          # Editar configurações aqui
├── main.py             # Executar este
├── entrada/            # Colocar MP4s aqui
├── saida/              # MP3s aparecem aqui
├── logs/               # Ver erros aqui
├── requirements.txt    # Dependências
└── modules...          # Scripts auxiliares
```

---

## 📝 Workflow Típico no PyCharm

1. ✅ Abrir PyCharm
2. ✅ Verificar venv selecionado (canto inferior direito)
3. ✅ Colocar MP4s em `entrada/`
4. ✅ Editar `config.ini` se necessário
5. ✅ Terminal do PyCharm: `python main.py`
6. ✅ Verificar MP3s em `saida/`
7. ✅ Ver logs em `logs/` se houver erros

---

## ✅ Checklist Final

- [ ] Homebrew instalado
- [ ] FFmpeg instalado (`brew install ffmpeg`)
- [ ] PyCharm aberto com projeto
- [ ] Ambiente virtual configurado (venv)
- [ ] Terminal do PyCharm ativa venv automaticamente
- [ ] `pip install -r requirements.txt` executado
- [ ] `python test_install.py` passou
- [ ] MP4s em `entrada/`
- [ ] `python main.py` executou com sucesso
- [ ] MP3s criados em `saida/`

---

## 🆘 Suporte

**Ver logs detalhados:**
```bash
cat logs/video_to_audio*.log
```

**Reinstalar tudo:**
```bash
# Apagar venv
rm -rf .venv

# Recriar no PyCharm
# Settings → Project → Python Interpreter → Add → New Virtualenv

# Reinstalar
pip install -r requirements.txt
```

---

## 🎓 Recursos

- [Documentação moviepy](https://zulko.github.io/moviepy/)
- [Documentação pydub](https://github.com/jiaaro/pydub)
- [FFmpeg Download](https://ffmpeg.org/download.html)
- [PyCharm Docs](https://www.jetbrains.com/help/pycharm/)

---

**Tudo pronto! Boa conversão no PyCharm! 🎵**
