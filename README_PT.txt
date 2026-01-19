================================================================================
        CONVERSOR DE VÍDEO MP4 PARA ÁUDIO MP3
        Sistema Completo e Configurável
================================================================================

📁 ESTRUTURA DO PROJETO:
------------------------
video_to_mp3_converter/
├── 📄 config.ini              → Configuração principal
├── 🐍 main.py                 → Script principal (EXECUTAR ESTE)
├── 🐍 config_loader.py        → Módulo: carrega configurações
├── 🐍 file_manager.py         → Módulo: gestão de ficheiros
├── 🐍 video_processor.py      → Módulo: extração de áudio
├── 🐍 audio_converter.py      → Módulo: conversão e otimização
├── 🐍 quality_analyzer.py     → Módulo: análise de qualidade
├── 📋 requirements.txt        → Dependências Python
├── 📖 README.md               → Documentação completa (LEIA PRIMEIRO)
├── 📖 INSTALL.md              → Guia de instalação detalhado
├── 🚀 QUICKSTART.md           → Início rápido (5 minutos)
├── 🧪 test_install.py         → Testar instalação
├── 🪟 run.bat                 → Executar no Windows
├── 🐧 run.sh                  → Executar no Linux/Mac
├── 📝 config_examples.ini     → Exemplos de configuração
├── 📂 entrada/                → COLOCAR VÍDEOS MP4 AQUI
├── 📂 saida/                  → MP3s CONVERTIDOS APARECEM AQUI
└── 📂 logs/                   → Logs de processamento


🚀 INÍCIO RÁPIDO (3 PASSOS):
----------------------------

1️⃣ INSTALAR DEPENDÊNCIAS:
   
   Windows:
   > pip install -r requirements.txt
   
   Linux/Mac:
   $ pip3 install -r requirements.txt


2️⃣ COLOCAR VÍDEOS:
   
   Copie seus vídeos MP4 para a pasta: entrada/


3️⃣ EXECUTAR:
   
   Windows:
   > python main.py
   ou clique em: run.bat
   
   Linux/Mac:
   $ python3 main.py
   ou execute: ./run.sh


✅ PRONTO! Os MP3s estarão em: saida/


📋 PRÉ-REQUISITOS:
------------------
✓ Python 3.8+ instalado
✓ FFmpeg instalado (necessário!)
✓ Dependências Python instaladas

Para instalar FFmpeg:
- Windows: choco install ffmpeg
- Mac: brew install ffmpeg  
- Linux: sudo apt install ffmpeg


⚙️ CONFIGURAÇÃO RÁPIDA:
-----------------------
Edite config.ini para personalizar:

[PROFILE]
active_profile = media    # Escolha: baixa, media, alta, custom

PERFIS DISPONÍVEIS:
- baixa:  Podcasts, voz (64kbps, mono, ~28MB/hora)
- media:  Uso geral (128kbps, stereo, ~56MB/hora)  ← RECOMENDADO
- alta:   Música (320kbps, stereo, ~140MB/hora)
- custom: Configure você mesmo


🎯 FUNCIONALIDADES:
-------------------
✅ Conversão MP4 → MP3 otimizada
✅ 3 perfis pré-definidos + customizável
✅ Normalização automática de volume
✅ Remoção de silêncios (início/fim)
✅ Remoção de segmentos configurável
✅ Filtros de áudio (passa-alta, passa-baixa, compressão)
✅ Análise de qualidade antes/depois
✅ Processamento em lote (todos os MP4s)
✅ Logs detalhados
✅ 100% configurável via config.ini


📊 CASOS DE USO:
----------------

🎙️ PODCASTS:
   active_profile = baixa
   Resultado: ~28MB/hora, ótimo para voz

🎵 MÚSICA:
   active_profile = alta
   Resultado: ~140MB/hora, qualidade máxima

🎓 AULAS ONLINE:
   active_profile = media
   Resultado: ~56MB/hora, balanceado


🧪 TESTAR INSTALAÇÃO:
---------------------
python test_install.py

Este script verifica se:
✓ Python está instalado
✓ FFmpeg está funcional
✓ Dependências instaladas
✓ Arquivos do projeto presentes


📖 DOCUMENTAÇÃO:
----------------
1. QUICKSTART.md   → Início rápido (5 minutos)
2. INSTALL.md      → Instalação detalhada passo a passo
3. README.md       → Documentação completa
4. config_examples.ini → Exemplos práticos de configuração


🔧 RESOLUÇÃO DE PROBLEMAS:
--------------------------

❌ "FFmpeg não encontrado"
   Solução: Instale FFmpeg (ver PRÉ-REQUISITOS acima)

❌ "No module named 'moviepy'"
   Solução: pip install -r requirements.txt

❌ "Nenhum vídeo encontrado"
   Solução: Coloque arquivos .mp4 na pasta entrada/

❌ "Permission denied" (Linux/Mac)
   Solução: chmod +x run.sh


💡 DICAS:
---------
• Comece testando com 1 vídeo pequeno
  (configure: process_all = false no config.ini)

• Use perfil 'media' para a maioria dos casos

• Consulte logs/ se algo der errado

• Veja config_examples.ini para exemplos prontos


📞 ESTRUTURA DOS MÓDULOS:
-------------------------
main.py              → Orquestra todo o processo
config_loader.py     → Carrega config.ini
file_manager.py      → Gestão de ficheiros/pastas
video_processor.py   → Extrai áudio do MP4 (moviepy)
audio_converter.py   → Converte/otimiza áudio (pydub)
quality_analyzer.py  → Analisa qualidade antes/depois


📈 ARQUITETURA:
--------------
Todos os scripts têm < 1000 linhas (modular e limpo)
Configuração 100% via config.ini (sem código)
Logs detalhados em logs/
Sistema robusto com tratamento de erros


================================================================================
                    PRONTO PARA COMEÇAR!
================================================================================

1. Leia QUICKSTART.md (5 minutos)
2. Instale dependências: pip install -r requirements.txt
3. Coloque MP4s em: entrada/
4. Execute: python main.py
5. Pegue MP3s em: saida/

Boa conversão! 🎵
