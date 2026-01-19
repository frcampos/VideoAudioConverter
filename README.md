# Conversor de Vídeo MP4 para Áudio MP3

Sistema robusto e configurável para converter vídeos MP4 em áudios MP3 com otimização de qualidade.

## 📋 Características

- ✅ Conversão MP4 → MP3 com perfis configuráveis
- 🎵 3 perfis pré-definidos (baixa, média, alta) + perfil customizado
- 🔊 Normalização automática de volume
- 🔇 Remoção de silêncios (início/fim)
- ✂️  Remoção de segmentos específicos
- 🎚️  Filtros de áudio (passa-alta, passa-baixa, compressão)
- 📊 Análise de qualidade antes/depois
- 📝 Sistema de logging configurável
- 🔧 100% configurável via `config.ini`

## 🚀 Instalação

### 1. Requisitos

- Python 3.8 ou superior
- FFmpeg (necessário para moviepy/pydub)

#### Instalar FFmpeg:

**Windows:**
```bash
# Via Chocolatey
choco install ffmpeg

# Ou descarregar de: https://ffmpeg.org/download.html
```

**macOS:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install ffmpeg
```

### 2. Instalar Dependências Python

```bash
pip install -r requirements.txt
```

## 📂 Estrutura do Projeto

```
projeto/
├── config.ini              # Configuração principal
├── main.py                 # Script principal
├── config_loader.py        # Carrega configurações
├── file_manager.py         # Gestão de ficheiros
├── video_processor.py      # Extração de áudio
├── audio_converter.py      # Conversão e otimização
├── quality_analyzer.py     # Análise de qualidade
├── requirements.txt        # Dependências
├── entrada/               # Coloque os MP4 aqui
├── saida/                 # MP3s convertidos aparecem aqui
└── logs/                  # Logs de processamento
```

## ⚙️ Configuração

Edite o `config.ini` para configurar o comportamento do sistema.

### Perfis de Conversão

```ini
[PROFILE]
active_profile = media  # baixa, media, alta, custom
```

**Perfis Pré-definidos:**

| Perfil | Canais | Bitrate | Sample Rate | Uso Recomendado |
|--------|--------|---------|-------------|-----------------|
| baixa  | Mono   | 64kbps  | 22050Hz     | Podcasts, voz   |
| media  | Stereo | 128kbps | 44100Hz     | Uso geral       |
| alta   | Stereo | 320kbps | 48000Hz     | Música          |
| custom | Config | Config  | Config      | Personalizado   |

### Normalização de Volume

```ini
[NORMALIZATION]
enabled = true
target_level = -12.0  # -3.0 (alto) a -20.0 (baixo)
```

### Remoção de Silêncios

```ini
[SILENCE_REMOVAL]
enabled = true
silence_threshold = -40     # Limiar de deteção
min_silence_duration = 1.0  # Duração mínima (segundos)
```

### Filtros de Áudio

```ini
[FILTERS]
highpass_filter = true      # Remove ruído de fundo
highpass_freq = 80          # Frequência de corte

lowpass_filter = false      # Remove chiado
lowpass_freq = 8000

compression = false         # Compressão dinâmica
compression_threshold = -20
compression_ratio = 4
```

## 🎯 Uso

### Básico

1. Coloque seus vídeos MP4 na pasta `entrada/`
2. Configure o `config.ini` conforme necessário
3. Execute:

```bash
python main.py
```

4. Os MP3s aparecem na pasta `saida/`

### Modo Teste

Para testar com apenas 1 vídeo:

```ini
[PROCESSING]
process_all = false  # Processa apenas o primeiro MP4
```

### Exemplos de Uso

**Podcast (voz, tamanho mínimo):**
```ini
[PROFILE]
active_profile = baixa

[NORMALIZATION]
enabled = true
target_level = -16.0
```

**Música (qualidade máxima):**
```ini
[PROFILE]
active_profile = alta

[NORMALIZATION]
enabled = false

[FILTERS]
compression = true
```

**Personalizado:**
```ini
[PROFILE]
active_profile = custom

[PROFILE_CUSTOM]
channels = mono
bitrate = 96k
sample_rate = 32000
```

## 📊 Análise de Qualidade

O sistema analisa automaticamente:

- ✅ Duração do áudio
- ✅ Sample rate e canais
- ✅ Bitrate estimado
- ✅ Tamanho do ficheiro
- ✅ Taxa de compressão
- ✅ Score de qualidade (0-100)

Exemplo de output:
```
RESULTADO DA CONVERSÃO
======================================================================
📦 Compressão: 45.2MB → 8.5MB (81.2% redução)
⭐ Qualidade:  Muito Boa (78/100)
======================================================================
```

## 📝 Logs

Logs são salvos em `logs/` com nível configurável:

```ini
[LOGGING]
log_level = INFO  # DEBUG, INFO, WARNING, ERROR
log_with_timestamp = true
```

## 🔧 Troubleshooting

### Erro: FFmpeg não encontrado
```
Instale o FFmpeg (ver seção Instalação)
```

### Áudio sem som
```
Verifique se o vídeo MP4 tem áudio
Use outro vídeo para testar
```

### Qualidade baixa
```
Aumente o bitrate em [PROFILE_CUSTOM]
Use active_profile = alta
```

### Ficheiro muito grande
```
Use active_profile = baixa
Reduza bitrate e sample_rate
```

## 📦 Tamanhos Aproximados

Para 1 hora de áudio:

| Perfil | Tamanho Aproximado |
|--------|-------------------|
| baixa  | ~28 MB            |
| media  | ~56 MB            |
| alta   | ~140 MB           |

## 🎓 Dicas

1. **Podcasts/Voz:** Use perfil `baixa` com normalização alta (-16 dBFS)
2. **Música:** Use perfil `alta` sem normalização
3. **Vídeo-aulas:** Use perfil `media` com compressão
4. **Webinars:** Use perfil `media` com remoção de silêncios

## 📄 Licença

Projeto de uso livre para fins pessoais e educacionais.

## 🤝 Suporte

Para questões ou sugestões, consulte os logs em `logs/` para diagnóstico.
