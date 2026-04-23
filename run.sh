#!/bin/bash

# Script de lancement de BAM (Bilan d'Achat de Manga)
# Lance l'application Streamlit

set -e

# Vérifier si l'environnement virtuel existe
if [ ! -d "venv" ]; then
    echo "❌ Environnement virtuel non trouvé!"
    echo ""
    echo "Veuillez d'abord exécuter: ./install.sh"
    exit 1
fi

# Activer l'environnement virtuel
source venv/bin/activate

echo "================================================"
echo "📚 Lancement de BAM - Bilan d'Achat de Manga"
echo "================================================"
echo ""
echo "L'application s'ouvre à: http://localhost:8501"
echo ""
echo "Appuyez sur Ctrl+C pour arrêter l'application"
echo ""

# Lancer Streamlit
streamlit run app.py
