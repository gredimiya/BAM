# Structure du Projet

## Vue d'Ensemble

```
BAM/
│
├── 📄 Fichiers Essentiels Racine
│   ├── README.md                 # Vue d'ensemble du projet
│   ├── QUICKSTART.md             # Démarrage rapide
│   ├── app.py                    # Point d'entrée Streamlit
│   ├── install.sh                # Script d'installation
│   ├── run.sh                    # Script de lancement
│   ├── requirements.txt           # Dépendances (production)
│   ├── requirements-dev.txt       # Dépendances (développement)
│   ├── .gitignore                # Fichiers ignorés par Git
│   └── LICENSE                   # Licence MIT
│
├── 📁 config/                    # Fichiers de configuration
│   └── .env.example              # Exemple de variables d'environnement
│
├── 📁 assets/                    # Design et wireframes
│   ├── BAM - MLD.png             # Diagramme base de données
│   ├── BAM - Wireframe.pdf       # Wireframes
│   └── BAM - Wireframe.pptx      # Présentation designs
│
├── 📁 pages/                     # Pages Streamlit (multi-page app)
│   ├── __init__.py
│   ├── 01_add_manga.py           # Gestion des mangas et tomes
│   ├── 02_visualisations.py      # Graphiques et visualisations
│   └── 03_table_view.py          # Tableau et export de données
│
├── 📁 database/                  # Couche d'accès aux données
│   ├── __init__.py
│   └── db.py                     # Opérations CRUD et requêtes SQL
│
├── 📁 utils/                     # Fonctions utilitaires
│   ├── __init__.py
│   ├── charts.py                 # Graphiques Plotly
│   ├── data_helpers.py           # Validation et formatage
│   └── filters.py                # Logique de filtrage
│
├── 📁 data/                      # Dossier de données
│   └── manga_collection.db       # Base de données SQLite (créée automatiquement)
│
├── 📁 docs/                      # Documentation complète
│   ├── README.md                 # Index de la documentation
│   ├── INDEX.md                  # Navigation complète
│   ├── INSTALLATION.md           # Instructions d'installation
│   ├── USAGE.md                  # Guide d'utilisation
│   ├── TROUBLESHOOTING.md        # Résolution des problèmes
│   ├── ARCHITECTURE.md           # Architecture technique
│   ├── DEVELOPMENT.md            # Guide de développement
│   ├── API.md                    # Référence API
│   ├── PROJECT_STRUCTURE.md      # Ce fichier
│   └── SECURITY.md               # Politique de sécurité
│
├── 📁 .git/                      # Répertoire Git (local)
│
└── 📁 venv/                      # Environnement virtuel Python (créé localement)
```

## Détail des Répertoires

### Racine - Fichiers Essentiels

| Fichier | Description |
|---------|-------------|
| `README.md` | Vue d'ensemble du projet et lien vers QUICKSTART |
| `QUICKSTART.md` | Guide de démarrage rapide (30 secondes) |
| `app.py` | Point d'entrée principal de Streamlit |
| `install.sh` | Script d'installation automatique |
| `run.sh` | Script de lancement de l'application |
| `requirements.txt` | Dépendances Python (production) |
| `requirements-dev.txt` | Dépendances supplémentaires (développement) |
| `LICENSE` | Licence MIT |
| `.gitignore` | Fichiers/dossiers ignorés par Git |

### `config/` - Configuration

| Fichier | Description |
|---------|-------------|
| `.env.example` | Exemple de variables d'environnement |

### `assets/` - Design et Wireframes

| Fichier | Description |
|---------|-------------|
| `BAM - MLD.png` | Diagramme du modèle de données |
| `BAM - Wireframe.pdf` | Wireframes (format PDF) |
| `BAM - Wireframe.pptx` | Présentation designs (PowerPoint) |

### `pages/` - Pages Streamlit

| Fichier | Description | Fonctionnalités |
|---------|-------------|-----------------|
| `01_add_manga.py` | Gestion des mangas | Ajouter, éditer, supprimer mangas et tomes |
| `02_visualisations.py` | Visualisations | Graphiques, métriques, filtres |
| `03_table_view.py` | Tableau et export | Vue tableau complète, export CSV |

### `database/` - Couche Données

| Fichier | Description |
|---------|-------------|
| `db.py` | Opérations CRUD, requêtes SQL, métriques |

### `utils/` - Utilitaires

| Fichier | Description |
|---------|-------------|
| `charts.py` | 5 graphiques Plotly |
| `data_helpers.py` | Validation et formatage |
| `filters.py` | Logique de filtrage |

### `docs/` - Documentation Complète

| Fichier | Audience | Contenu |
|---------|----------|---------|
| `README.md` | Tous | Index et points d'entrée |
| `INDEX.md` | Tous | Navigation complète |
| `INSTALLATION.md` | Tous | Installation détaillée |
| `USAGE.md` | Utilisateurs | Guide d'utilisation |
| `TROUBLESHOOTING.md` | Tous | Résolution des problèmes |
| `ARCHITECTURE.md` | Développeurs | Architecture technique |
| `DEVELOPMENT.md` | Développeurs | Guide de développement |
| `API.md` | Développeurs | Référence API |
| `SECURITY.md` | Tous | Politique de sécurité |
| `PROJECT_STRUCTURE.md` | Développeurs | Ce fichier |

## Arborescence Simplifiée

```
BAM/
├── 🚀 Point d'Entrée Rapide
│   ├── README.md          # Lire d'abord
│   ├── QUICKSTART.md      # Installer et lancer en 30 sec
│   ├── install.sh         # Exécuter: ./install.sh
│   └── run.sh             # Exécuter: ./run.sh
│
├── ⚙️ Configuration
│   └── config/.env.example
│
├── 💾 Application
│   ├── app.py
│   ├── pages/
│   ├── database/
│   ├── utils/
│   └── data/
│
├── 📚 Documentation
│   └── docs/
│       ├── README.md      # Lire pour plus de détails
│       └── [autres fichiers]
│
└── 🎨 Assets
    └── assets/
        └── [designs, wireframes]
```

## Points d'Entrée

### Pour les Utilisateurs
1. **Lire** : [README.md](../README.md)
2. **Installer** : [QUICKSTART.md](QUICKSTART.md) → `./install.sh`
3. **Lancer** : `./run.sh`
4. **Guide complet** : [USAGE.md](USAGE.md)
5. **Problèmes** : [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

### Pour les Développeurs
1. **Lire** : [README.md](../README.md) et [QUICKSTART.md](../QUICKSTART.md)
2. **Setup** : [INSTALLATION.md](INSTALLATION.md) ou `./install.sh`
3. **Architecture** : [ARCHITECTURE.md](ARCHITECTURE.md)
4. **Développement** : [DEVELOPMENT.md](DEVELOPMENT.md)
5. **API** : [API.md](API.md)

## Conventions de Nommage

### Fichiers
- **Python** : minuscules avec underscores (`data_helpers.py`)
- **Pages Streamlit** : numérotées (`01_add_manga.py`)
- **Documentation** : majuscules (`README.md`, `QUICKSTART.md`)
- **Configuration** : points (`.env.example`)

### Dossiers
- **Minuscules** : `pages/`, `database/`, `utils/`, `docs/`, `config/`, `assets/`
- **Pas d'underscores** généralement

## Tailles Typiques

| Fichier | Lignes | Notes |
|---------|--------|-------|
| `app.py` | ~40 | Très court, accueil |
| `db.py` | ~300 | Tous les CRUD + requêtes |
| `charts.py` | ~200 | 5 graphiques Plotly |
| `01_add_manga.py` | ~200 | Formulaires et gestion |
| `02_visualisations.py` | ~80 | UI + appels charts |
| `03_table_view.py` | ~60 | Tableau et export |

## Scripts de Développement

```bash
./install.sh              # Installation complète
./run.sh                  # Lancer l'app
rm data/manga_collection.db   # Réinitialiser la BD
```

---

**Plus de détails** : [ARCHITECTURE.md](ARCHITECTURE.md)
