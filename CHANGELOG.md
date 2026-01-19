# Changelog
Histórico de alterações do Conversor MP4 para MP3

---

## [1.0.0] - 2024-12-15

### ✨ Lançamento Inicial

#### Funcionalidades Principais
- ✅ Conversão de vídeos MP4 para áudio MP3
- ✅ Sistema modular com scripts < 1000 linhas
- ✅ Configuração 100% via `config.ini`
- ✅ 3 perfis pré-definidos (baixa, média, alta) + customizável

#### Processamento de Áudio
- ✅ Normalização automática de volume
- ✅ Remoção de silêncios (início/fim)
- ✅ Remoção de segmentos específicos
- ✅ Filtros de áudio:
  - Passa-alta (remove ruído de fundo)
  - Passa-baixa (remove chiado)
  - Compressão dinâmica

#### Análise de Qualidade
- ✅ Análise antes/depois da conversão
- ✅ Estatísticas detalhadas:
  - Duração, sample rate, canais
  - Bitrate estimado
  - Taxa de compressão
  - Score de qualidade (0-100)

#### Gestão de Ficheiros
- ✅ Processamento em lote (todos os MP4s)
- ✅ Opção de sobrescrever ou criar versões
- ✅ Manutenção de nome original
- ✅ Validação de ficheiros de entrada

#### Documentação
- ✅ README.md completo
- ✅ INSTALL.md (guia de instalação)
- ✅ QUICKSTART.md (início rápido)
- ✅ config_examples.ini (7 exemplos práticos)
- ✅ README_PT.txt (resumo em português)

#### Scripts Auxiliares
- ✅ test_install.py (verificar instalação)
- ✅ run.bat (Windows)
- ✅ run.sh (Linux/Mac)

#### Logging
- ✅ Sistema de logs configurável
- ✅ Níveis: DEBUG, INFO, WARNING, ERROR, CRITICAL
- ✅ Logs com timestamp opcional
- ✅ Estatísticas de processamento

#### Módulos
```
config_loader.py     (11K) - Carrega configurações
file_manager.py      (6.8K) - Gestão de ficheiros
video_processor.py   (4.6K) - Extração de áudio
audio_converter.py   (8.6K) - Conversão e otimização
quality_analyzer.py  (9.7K) - Análise de qualidade
main.py             (10K)  - Orquestrador principal
```

#### Dependências
- moviepy >= 1.0.3
- pydub >= 0.25.1
- numpy >= 1.21.0
- FFmpeg (externo)

---

## Versões Futuras (Planejadas)

### [1.1.0] - Planejado
- [ ] Suporte para mais formatos de entrada (AVI, MKV, MOV)
- [ ] Suporte para mais formatos de saída (WAV, AAC, OGG)
- [ ] Interface gráfica (GUI) opcional
- [ ] Processamento paralelo (múltiplos vídeos simultâneos)

### [1.2.0] - Planejado
- [ ] Corte de segmentos por timestamp
- [ ] Fade in/fade out automático
- [ ] Equalização personalizada
- [ ] Detecção de idioma do áudio

### [1.3.0] - Planejado
- [ ] Conversão de listas de reprodução
- [ ] Download de vídeos de URLs
- [ ] Integração com APIs de streaming
- [ ] Metadata tags automáticas

---

## Formato das Versões

```
[MAJOR.MINOR.PATCH]

MAJOR: Mudanças incompatíveis na API
MINOR: Novas funcionalidades compatíveis
PATCH: Correções de bugs compatíveis
```

---

## Tipos de Alterações

- ✨ **Added**: Novas funcionalidades
- 🔧 **Changed**: Alterações em funcionalidades existentes
- 🗑️ **Deprecated**: Funcionalidades obsoletas (serão removidas)
- 🔥 **Removed**: Funcionalidades removidas
- 🐛 **Fixed**: Correções de bugs
- 🔒 **Security**: Correções de segurança

---

## Contribuir

Para reportar bugs ou sugerir funcionalidades:
1. Verificar logs em `logs/`
2. Documentar o problema claramente
3. Incluir versão Python e SO
4. Fornecer exemplo de reprodução
