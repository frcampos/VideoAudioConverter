================================================================================
                    ❌ ERRO: ModuleNotFoundError: No module named 'moviepy.editor'
================================================================================

Este é o erro mais comum! Aqui está como resolver:

================================================================================
                    ✅ SOLUÇÃO RÁPIDA (FUNCIONA 95% das vezes)
================================================================================

PASSO 1 - EXECUTAR INSTALADOR AUTOMÁTICO:
------------------------------------------
No terminal, dentro da pasta do projeto:

macOS/Linux:
    python3 install.py

Windows:
    python install.py


PASSO 2 - SE NÃO FUNCIONAR, FAZER MANUALMENTE:
-----------------------------------------------

macOS/Linux:
    # Desinstalar moviepy
    pip3 uninstall moviepy -y
    
    # Instalar versão específica
    pip3 install moviepy==1.0.3 --no-cache-dir
    
    # Instalar outras dependências
    pip3 install pydub numpy imageio imageio-ffmpeg decorator proglog tqdm requests
    
    # Testar
    python3 test_install.py

Windows:
    # Desinstalar moviepy
    pip uninstall moviepy -y
    
    # Instalar versão específica
    pip install moviepy==1.0.3 --no-cache-dir
    
    # Instalar outras dependências
    pip install pydub numpy imageio imageio-ffmpeg decorator proglog tqdm requests
    
    # Testar
    python test_install.py


PASSO 3 - VERIFICAR SE FUNCIONOU:
----------------------------------
macOS/Linux:
    python3 test_install.py

Windows:
    python test_install.py

Deve ver: "✅ INSTALAÇÃO PERFEITA!"


================================================================================
                    🔍 PORQUÊ ESTE ERRO?
================================================================================

O moviepy tem problemas de compatibilidade com versões mais recentes.
A versão 1.0.3 é a mais estável e compatível.

Problemas comuns:
1. Versão errada do moviepy instalada
2. Cache do pip com versão corrompida
3. Ambiente virtual não ativado
4. Conflito com outras versões Python


================================================================================
                    💡 SE AINDA NÃO FUNCIONAR
================================================================================

OPÇÃO 1 - USAR AMBIENTE VIRTUAL:
---------------------------------
macOS/Linux:
    # Criar ambiente virtual
    python3 -m venv venv
    
    # Ativar
    source venv/bin/activate
    
    # Instalar
    pip install moviepy==1.0.3 --no-cache-dir
    pip install pydub numpy imageio imageio-ffmpeg
    
    # Executar projeto
    python main.py

Windows:
    # Criar ambiente virtual
    python -m venv venv
    
    # Ativar
    venv\Scripts\activate
    
    # Instalar
    pip install moviepy==1.0.3 --no-cache-dir
    pip install pydub numpy imageio imageio-ffmpeg
    
    # Executar projeto
    python main.py


OPÇÃO 2 - LIMPAR CACHE E REINSTALAR:
-------------------------------------
macOS/Linux:
    # Limpar cache
    pip3 cache purge
    
    # Desinstalar tudo
    pip3 uninstall moviepy pydub numpy -y
    
    # Reinstalar do zero
    pip3 install -r requirements.txt --no-cache-dir

Windows:
    # Limpar cache
    pip cache purge
    
    # Desinstalar tudo
    pip uninstall moviepy pydub numpy -y
    
    # Reinstalar do zero
    pip install -r requirements.txt --no-cache-dir


OPÇÃO 3 - VERIFICAR PYTHON USADO:
----------------------------------
Você pode ter múltiplas versões Python instaladas!

macOS/Linux:
    # Ver qual Python está usando
    which python3
    
    # Ver versão
    python3 --version
    
    # Instalar no Python correto
    /caminho/completo/para/python3 -m pip install moviepy==1.0.3

Windows:
    # Ver qual Python está usando
    where python
    
    # Ver versão
    python --version


================================================================================
                    🧪 TESTE RÁPIDO
================================================================================

Para testar se moviepy está instalado:

macOS/Linux:
    python3 -c "from moviepy.editor import VideoFileClip; print('✅ OK')"

Windows:
    python -c "from moviepy.editor import VideoFileClip; print('✅ OK')"

Se ver "✅ OK" → Instalação correta!
Se der erro → Ainda não está instalado


================================================================================
                    📞 CHECKLIST COMPLETO
================================================================================

□ Python 3.8+ instalado?
    Verificar: python3 --version (ou python --version)

□ pip atualizado?
    Executar: pip install --upgrade pip

□ FFmpeg instalado?
    Verificar: ffmpeg -version

□ moviepy versão 1.0.3?
    Verificar: pip show moviepy

□ Ambiente virtual ativado (se usar)?
    Ver prompt do terminal (deve ter "(venv)" no início)

□ requirements.txt existe?
    Ver: ls requirements.txt

□ Executou install.py?
    Executar: python3 install.py


================================================================================
                    🎯 COMANDOS FINAIS (COPIAR E COLAR)
================================================================================

Para macOS (no Terminal, dentro da pasta do projeto):
    pip3 uninstall moviepy -y && \
    pip3 install moviepy==1.0.3 --no-cache-dir && \
    pip3 install pydub numpy imageio imageio-ffmpeg && \
    python3 test_install.py

Para Windows (no CMD, dentro da pasta do projeto):
    pip uninstall moviepy -y
    pip install moviepy==1.0.3 --no-cache-dir
    pip install pydub numpy imageio imageio-ffmpeg
    python test_install.py


================================================================================
                    📚 DOCUMENTAÇÃO ADICIONAL
================================================================================

Consulte também:
- TROUBLESHOOTING.md → Todos os erros possíveis
- INSTALL_MACOS.md → Instalação completa macOS
- INSTALL.md → Instalação completa Windows/Linux
- test_install.py → Script de teste automático
- install.py → Instalador automático


================================================================================
                    🆘 AINDA COM PROBLEMAS?
================================================================================

1. Execute: python3 install.py (ou python install.py)
   → Instalador automático resolve a maioria dos problemas

2. Veja os logs detalhados:
   cat logs/*.log (macOS/Linux)
   type logs\*.log (Windows)

3. Envie estas informações:
   - Sistema operativo e versão
   - Resultado de: python --version
   - Resultado de: pip show moviepy
   - Resultado de: python test_install.py
   - Conteúdo dos logs (se existirem)


================================================================================

✅ Na maioria dos casos, executar "python3 install.py" resolve tudo!

================================================================================
