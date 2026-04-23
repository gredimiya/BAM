#!/bin/bash

# Script d'installation de BAM (Bilan d'Achat de Manga)
# Ce script installe toutes les dépendances et configure l'application

set -e

echo "================================================"
echo "📚 Installation de BAM - Bilan d'Achat de Manga"
echo "================================================"
echo ""

# Vérifier si Python est installé
echo "Vérification de Python..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 n'est pas installé!"
    echo "Veuillez installer Python 3.8 ou supérieur"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo "✅ Python $PYTHON_VERSION détecté"
echo ""

# Créer l'environnement virtuel
echo "Création de l'environnement virtuel..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Environnement virtuel créé"
else
    echo "✅ Environnement virtuel existant"
fi
echo ""

# Activer l'environnement virtuel
echo "Activation de l'environnement virtuel..."
source venv/bin/activate
echo "✅ Environnement activé"
echo ""

# Mettre à jour pip
echo "Mise à jour de pip..."
pip install --upgrade pip > /dev/null 2>&1
echo "✅ pip à jour"
echo ""

# Installer les dépendances
echo "Installation des dépendances Python..."
if [ -f "requirements.txt" ]; then
    pip install -q -r requirements.txt
    echo "✅ Dépendances installées"
else
    echo "❌ Fichier requirements.txt non trouvé!"
    exit 1
fi
echo ""

# Créer le répertoire data s'il n'existe pas
if [ ! -d "data" ]; then
    mkdir -p data
    echo "✅ Dossier data créé"
fi
echo ""

echo "================================================"
echo "✅ Installation terminée!"
echo "================================================"
echo ""
echo "Pour lancer l'application, exécutez:"
echo "  ./run.sh"
echo ""
