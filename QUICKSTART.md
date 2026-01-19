# 🚀 Início Rápido
## Conversor MP4 para MP3 em 5 Minutos

---

## ⚡ Início Ultra-Rápido (3 Passos)

### 1️⃣ Instalar
```bash
pip install -r requirements.txt
```

### 2️⃣ Configurar
Coloque vídeos MP4 em `entrada/`

### 3️⃣ Executar
```bash
python main.py
```

**Pronto!** MP3s estarão em `saida/`

---

## 📋 Checklist Pré-Execução

- [ ] Python 3.8+ instalado
- [ ] FFmpeg instalado
- [ ] `pip install -r requirements.txt` executado
- [ ] Pelo menos 1 vídeo MP4 em `entrada/`
- [ ] `config.ini` existe no diretório

---

## 🎯 Perfis Rápidos

Edite `config.ini` → seção `[PROFILE]`:

```ini
[PROFILE]
active_profile = media  # Escolha: baixa, media, alta
```

| Perfil | Para | Tamanho/Hora | Comando Rápido |
|--------|------|--------------|----------------|
| **baixa** | Podcasts, voz | ~28 MB | `active_profile = baixa` |
| **media** | Uso geral | ~56 MB | `active_profile = media` |
| **alta** | Música | ~140 MB | `active_profile = alta` |

---

## 💡 Casos de Uso Comuns

### 🎙️ Podcast
```ini
[PROFILE]
active_profile = baixa

[NORMALIZATION]
enabled = true
target_level = -16.0
```

### 🎵 Música
```ini
[PROFILE]
active_profile = alta

[NORMALIZATION]
enabled = false
```

### 🎓 Aula Online
```ini
[PROFILE]
active_profile = media

[SILENCE_REMOVAL]
enabled = true
```

---

## ⚙️ Configurações Essenciais

### Processar Todos os Vídeos?
```ini
[PROCESSING]
process_all = true   # true = todos, false = só primeiro (teste)
```

### Normalizar Volume?
```ini
[NORMALIZATION]
enabled = true       # true = volume uniforme
target_level = -12.0 # Volume alvo
```

### Remover Silêncios?
```ini
[SILENCE_REMOVAL]
enabled = true       # true = remove pausas
```

---

## 🔧 Troubleshooting Rápido

### ❌ "FFmpeg não encontrado"
**Windows:**
```cmd
choco install ffmpeg
```
**Mac:**
```bash
brew install ffmpeg
```
**Linux:**
```bash
sudo apt install ffmpeg
```

### ❌ "No module named 'moviepy'"
```bash
pip install -r requirements.txt
```

### ❌ "Nenhum vídeo encontrado"
Coloque arquivos `.mp4` em `entrada/`

### ❌ "Permission denied" (Linux/Mac)
```bash
chmod +x run.sh
```

---

## 📊 Teste Rápido

### Testar Instalação:
```bash
python test_install.py
```

### Processar 1 Vídeo (Teste):
1. Coloque 1 MP4 em `entrada/`
2. Configure:
   ```ini
   [PROCESSING]
   process_all = false
   ```
3. Execute: `python main.py`

---

## 📁 Estrutura Mínima

```
projeto/
├── config.ini       ← Configurar aqui
├── main.py          ← Executar este
├── entrada/         ← Colocar MP4s aqui
└── saida/           ← MP3s aparecem aqui
```

---

## 🎓 Exemplo Completo

**Situação:** Converter aula de 1 hora para MP3 otimizado

1. **Colocar vídeo:**
   ```
   entrada/aula_matematica.mp4
   ```

2. **Configurar** `config.ini`:
   ```ini
   [PROFILE]
   active_profile = media
   
   [NORMALIZATION]
   enabled = true
   target_level = -14.0
   
   [SILENCE_REMOVAL]
   enabled = true
   
   [SEGMENT_REMOVAL]
   enabled = true
   remove_start = 5.0   # Remove intro
   remove_end = 10.0    # Remove outro
   ```

3. **Executar:**
   ```bash
   python main.py
   ```

4. **Resultado:**
   ```
   saida/aula_matematica.mp3
   ```
   - Tamanho: ~56 MB
   - Qualidade: Boa (128kbps, 44100Hz)
   - Otimizações: Volume normalizado, silêncios removidos

---

## 🎯 Dicas Finais

✅ **Comece com perfil `media`** - balanceado para a maioria dos casos

✅ **Teste com 1 vídeo primeiro** - use `process_all = false`

✅ **Consulte logs** em `logs/` se algo der errado

✅ **Experimente perfis** - cada caso é único

✅ **Leia `config_examples.ini`** - exemplos práticos prontos

---

## 📚 Próximos Passos

Funcionou? Explore mais:

- 📖 `README.md` - Documentação completa
- 🛠️ `INSTALL.md` - Instalação detalhada
- 📝 `config_examples.ini` - Exemplos de configuração
- 🧪 `test_install.py` - Testar sistema

---

## 🚀 Comandos Úteis

```bash
# Executar (Windows)
python main.py
# ou
run.bat

# Executar (Linux/Mac)
python3 main.py
# ou
./run.sh

# Testar instalação
python test_install.py

# Ver ajuda
python main.py --help
```

---

**Dúvidas?** Consulte `README.md` ou verifique `logs/`
