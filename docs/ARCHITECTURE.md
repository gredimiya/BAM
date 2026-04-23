# Architecture de BAM

## Vue d'ensemble

BAM est une application web monolithique construite avec Streamlit et SQLite. L'architecture est simple et modulaire avec une séparation claire des responsabilités.

## Structure du Projet

```
BAM/
├── app.py                      # Point d'entrée principal
├── database/
│   ├── __init__.py
│   └── db.py                   # Couche accès aux données (DAO)
├── pages/
│   ├── __init__.py
│   ├── 01_add_manga.py         # Page gestion des mangas
│   ├── 02_visualisations.py    # Page graphiques et visualisations
│   └── 03_table_view.py        # Page tableau et export
├── utils/
│   ├── __init__.py
│   ├── charts.py               # Fonctions de création de graphiques
│   ├── data_helpers.py         # Fonctions utilitaires de données
│   └── filters.py              # Logique de filtrage
├── data/                       # Dossier données
│   └── manga_collection.db     # Base de données SQLite
└── docs/                       # Documentation
```

## Couches Architecturales

### 1. Couche Présentation (Streamlit)
- `app.py` : Page d'accueil
- `pages/` : Pages de l'application
- Gère l'interface utilisateur et la navigation

### 2. Couche Métier
- `utils/charts.py` : Logique de visualisation
- `utils/filters.py` : Logique de filtrage
- `utils/data_helpers.py` : Fonctions utilitaires

### 3. Couche Données
- `database/db.py` : CRUD operations et requêtes SQL
- Gère la communication avec SQLite

## Modèle de Données

### Table: Manga
```sql
CREATE TABLE Manga (
    manga_id INTEGER PRIMARY KEY AUTOINCREMENT,
    manga_name VARCHAR(255) NOT NULL,
    manga_author VARCHAR(255) NOT NULL,
    manga_edition VARCHAR(255) NOT NULL,
    manga_link VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
```

### Table: Tome
```sql
CREATE TABLE Tome (
    tome_id INTEGER PRIMARY KEY AUTOINCREMENT,
    manga_id INTEGER NOT NULL,
    tome_num INTEGER NOT NULL,
    tome_prix REAL NOT NULL,
    tome_offert BOOLEAN DEFAULT 0,
    tome_date_achat DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (manga_id) REFERENCES Manga(manga_id) ON DELETE CASCADE
)
```

## Flux de Données

1. **Ajout de données** :
   - Utilisateur soumet un formulaire Streamlit
   - Validation dans `utils/data_helpers.py`
   - Insertion via `database/db.py`
   - Rerun de l'app pour afficher les changements

2. **Affichage des données** :
   - Récupération via `database/db.py`
   - Filtrage via `utils/filters.py`
   - Affichage/visualisation via `utils/charts.py`

## Technologies

- **Framework UI** : Streamlit
- **Base de données** : SQLite
- **Visualisations** : Plotly
- **Data processing** : Pandas
- **Langage** : Python 3.12

## Avantages de cette Architecture

✅ Simple et facile à maintenir
✅ Pas de serveur complexe requis
✅ Déploiement facile
✅ Séparation des responsabilités

## Limitations et Futures Améliorations

- SQLite est limité pour les applications multi-utilisateur
- Pas de système d'authentification actuellement
- Les filtres réappellent le serveur à chaque changement (pas optimal)

Futures améliorations possibles :
- Migration vers PostgreSQL
- Système de cache
- Authentification utilisateur
- API REST
