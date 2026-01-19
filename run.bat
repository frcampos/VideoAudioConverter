@echo off
REM Script de execução para Windows
REM Conversor de Vídeo MP4 para Áudio MP3

echo ========================================
echo Conversor MP4 para MP3
echo ========================================
echo.

REM Verificar se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERRO: Python nao encontrado!
    echo Instale Python 3.8+ de: https://www.python.org
    pause
    exit /b 1
)

REM Verificar se config.ini existe
if not exist "config.ini" (
    echo ERRO: config.ini nao encontrado!
    echo Crie o arquivo config.ini antes de executar.
    pause
    exit /b 1
)

REM Criar pastas se não existirem
if not exist "entrada" mkdir entrada
if not exist "saida" mkdir saida
if not exist "logs" mkdir logs

REM Verificar se há vídeos na pasta entrada
dir /b entrada\*.mp4 >nul 2>&1
if errorlevel 1 (
    echo AVISO: Nenhum video MP4 encontrado em 'entrada\'
    echo Coloque seus videos MP4 na pasta 'entrada\' antes de continuar.
    echo.
    pause
)

echo Iniciando conversao...
echo.

REM Executar script principal
python main.py

echo.
echo ========================================
echo Conversao concluida!
echo Os arquivos MP3 estao em: saida\
echo ========================================
echo.

pause
