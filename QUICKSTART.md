# 🚀 Quick Start - Démarrage Rapide

## Installation et Lancement Rapide

### Prérequis

- **Linux/Mac** : Bash shell
- **Python 3.8+** : Vérifiez avec `python3 --version`
- **Git** : Pour cloner le repository

### Installation en 1 ligne

```bash
git clone https://github.com/yourusername/BAM.git && cd BAM && chmod +x install.sh run.sh && ./install.sh
```

### Ou étape par étape

1. **Cloner le repository**
```bash
git clone https://github.com/yourusername/BAM.git
cd BAM
```

2. **Rendre les scripts exécutables**
```bash
chmod +x install.sh run.sh
```

3. **Installer l'application**
```bash
./install.sh
```

Cela va :
- ✅ Vérifier que Python 3 est installé
- ✅ Créer un environnement virtuel
- ✅ Installer toutes les dépendances
- ✅ Créer le dossier de données

4. **Lancer l'application**
```bash
./run.sh
```

L'application s'ouvre automatiquement à : **http://localhost:8501**

## Utilisation

Une fois lancée, vous pouvez :
- 📝 Ajouter des mangas et tomes
- 📊 Visualiser des graphiques
- 📋 Exporter vos données en CSV

## Arrêter l'application

Appuyez sur **Ctrl+C** dans le terminal

## Besoin d'Aide ?

### L'installation échoue

```bash
# Vérifier Python
python3 --version

# Vérifier pip
python3 -m pip --version

# Relancer manuellement
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Réinitialiser la base de données

```bash
rm data/manga_collection.db
./run.sh  # La base sera recréée automatiquement
```

### Sur Windows ?

Utilisez la version WSL (Windows Subsystem for Linux) ou Git Bash, puis suivez les instructions Linux.

## Prochaines Étapes

- Consultez [docs/INSTALLATION.md](docs/INSTALLATION.md) pour plus de détails
- Consultez [docs/USAGE.md](docs/USAGE.md) pour le guide d'utilisation
- Consultez [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) en cas de problème

---

**C'est tout ! 🎉 Profitez de BAM!**
