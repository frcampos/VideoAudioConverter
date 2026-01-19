#!/bin/bash
# Script de execução para Linux/Mac
# Conversor de Vídeo MP4 para Áudio MP3

echo "========================================"
echo "Conversor MP4 para MP3"
echo "========================================"
echo ""

# Verificar se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "ERRO: Python3 não encontrado!"
    echo "Instale Python 3.8+ de: https://www.python.org"
    exit 1
fi

# Verificar se config.ini existe
if [ ! -f "config.ini" ]; then
    echo "ERRO: config.ini não encontrado!"
    echo "Crie o arquivo config.ini antes de executar."
    exit 1
fi

# Criar pastas se não existirem
mkdir -p entrada
mkdir -p saida
mkdir -p logs

# Verificar se há vídeos na pasta entrada
if ! ls entrada/*.mp4 1> /dev/null 2>&1; then
    echo "AVISO: Nenhum vídeo MP4 encontrado em 'entrada/'"
    echo "Coloque seus vídeos MP4 na pasta 'entrada/' antes de continuar."
    echo ""
    read -p "Pressione Enter para continuar..."
fi

echo "Iniciando conversão..."
echo ""

# Executar script principal
python3 main.py

echo ""
echo "========================================"
echo "Conversão concluída!"
echo "Os arquivos MP3 estão em: saida/"
echo "========================================"
echo ""
