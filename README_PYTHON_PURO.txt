================================================================================
           ✅ VERSÃO PYTHON PURO - SEM FFmpeg EXTERNO
        Conversor MP4 para WAV - Apenas pip install
================================================================================

🎯 O QUE MUDOU?
================================================================================

Esta versão foi COMPLETAMENTE REFEITA para usar APENAS bibliotecas Python,
SEM NECESSIDADE de instalar FFmpeg externamente!

ANTES (versão anterior):
   ❌ Precisava: brew install ffmpeg (macOS)
   ❌ Usava: moviepy + pydub (dependem de FFmpeg externo)
   ❌ Gerava: MP3 (comprimido)

AGORA (esta versão):
   ✅ Precisa: Apenas pip install (Python puro!)
   ✅ Usa: PyAV + scipy + numpy + soundfile
   ✅ Gera: WAV (16-bit PCM, sem compressão)


🔧 BIBLIOTECAS USADAS:
================================================================================

av (PyAV)         → Extração de áudio (FFmpeg bundled no pip)
numpy             → Processamento numérico
scipy             → Filtros de sinal (passa-alta, passa-baixa, resample)
soundfile         → Gravação de ficheiros WAV
librosa           → Análise de áudio (opcional)

IMPORTANTE: PyAV tem FFmpeg compilado DENTRO do pacote pip!
            Não precisa instalar FFmpeg separadamente!


📦 INSTALAÇÃO SIMPLIFICADA:
================================================================================

PASSO 1 - Instalar dependências (APENAS isto):
----------------------------------------------
pip install -r requirements.txt

Ou manualmente:
pip install av numpy scipy soundfile librosa


PASSO 2 - Testar:
-----------------
python test_install.py

Deve ver: "✅ INSTALAÇÃO PERFEITA!"


PASSO 3 - Usar:
---------------
python main.py

Pronto! Sem brew install, sem FFmpeg externo!


🎵 FORMATO DE SAÍDA: WAV
================================================================================

POR QUE WAV EM VEZ DE MP3?
--------------------------
MP3 requer codec proprietário (LAME) que não existe em Python puro.
WAV é formato não comprimido, nativo, sem patentes.

VANTAGENS DO WAV:
-----------------
✅ Qualidade 100% lossless (sem perda)
✅ Compatível com tudo (players, editores, DAWs)
✅ Python puro (sem dependências externas)
✅ Processamento mais rápido

DESVANTAGENS DO WAV:
--------------------
❌ Ficheiros maiores (~10MB por minuto em stereo 44.1kHz)

TAMANHOS APROXIMADOS:
--------------------
| Perfil | Canais | Sample Rate | Tamanho/Minuto | Tamanho/Hora |
|--------|--------|-------------|----------------|--------------|
| baixa  | mono   | 22050Hz     | ~2.5 MB        | ~150 MB      |
| media  | stereo | 44100Hz     | ~10 MB         | ~600 MB      |
| alta   | stereo | 48000Hz     | ~11 MB         | ~660 MB      |


⚙️ CONFIGURAÇÃO:
================================================================================

O config.ini foi ajustado:

[PROFILE]
# Não há mais 'bitrate' (WAV não usa compressão)
active_profile = media

[PROFILE_CUSTOM]
channels = stereo       # mono ou stereo
sample_rate = 44100     # 22050, 44100, 48000

Perfis disponíveis:
- baixa:  Mono, 22050Hz   (~150MB/hora)
- media:  Stereo, 44100Hz (~600MB/hora)  ← RECOMENDADO
- alta:   Stereo, 48000Hz (~660MB/hora)


🔄 FUNCIONALIDADES MANTIDAS:
================================================================================

TUDO funciona igual:
✅ Normalização de volume
✅ Remoção de silêncios
✅ Remoção de segmentos
✅ Filtros (passa-alta, passa-baixa, compressão)
✅ Conversão mono/stereo
✅ Resample de sample rate
✅ Análise de qualidade
✅ Processamento em lote
✅ Logs detalhados


💡 COMPARAÇÃO COM VERSÃO ANTERIOR:
================================================================================

VERSÃO MP3 (moviepy/pydub):
   Instalação: brew install ffmpeg + pip install moviepy pydub
   Saída:      MP3 (comprimido, ~5MB/hora com 128kbps)
   Qualidade:  Com perda (lossy)
   Velocidade: Mais lenta (encoding MP3)

VERSÃO WAV (PyAV/scipy):
   Instalação: pip install av numpy scipy soundfile
   Saída:      WAV (sem compressão, ~600MB/hora stereo 44.1kHz)
   Qualidade:  Sem perda (lossless)
   Velocidade: Mais rápida (sem encoding)


🚀 INÍCIO RÁPIDO:
================================================================================

1. Instalar:
   pip install av numpy scipy soundfile

2. Testar:
   python test_install.py

3. Colocar MP4s em: entrada/

4. Executar:
   python main.py

5. Pegar WAVs em: saida/


❓ FAQ:
================================================================================

P: Posso converter WAV para MP3 depois?
R: Sim! Use ferramentas online ou: pip install pydub + FFmpeg

P: Os ficheiros WAV são muito grandes!
R: Use perfil 'baixa' (mono 22050Hz) ou converta para MP3 depois

P: Preciso de instalar algo além do pip?
R: NÃO! Apenas: pip install -r requirements.txt

P: Funciona no Windows/Mac/Linux?
R: SIM! Python puro funciona em todos

P: PyAV não usa FFmpeg?
R: Usa, mas FFmpeg vem BUNDLED no pip. Não precisa brew/apt install!


🆘 RESOLUÇÃO DE PROBLEMAS:
================================================================================

Erro: "No module named 'av'"
   pip install av

Erro: "No module named 'scipy'"
   pip install scipy

Erro: "No module named 'soundfile'"
   pip install soundfile

Erro ao carregar vídeo:
   Verifique se MP4 tem áudio (alguns não têm!)

Ficheiros muito grandes:
   Use perfil 'baixa' em config.ini


✅ CONFIRMAÇÃO:
================================================================================

Para confirmar que está tudo correto:

1. Executar: python test_install.py
2. Deve ver: "✅ FFmpeg NÃO É NECESSÁRIO (Python puro!)"
3. Todos os testes devem passar
4. Executar: python main.py
5. Ver WAVs criados em saida/


================================================================================
         PRONTO PARA USAR - 100% PYTHON - SEM INSTALAÇÕES EXTERNAS!
================================================================================
