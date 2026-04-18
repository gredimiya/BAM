# BAM - Bilan d'Achat de Manga

Une web app Streamlit pour gérer votre collection personnelle de mangas.

## 🚀 Démarrage rapide

### Installation

1. **Cloner le repository** (déjà fait)

2. **Créer un environnement Python virtuel** (optionnel mais recommandé)
```bash
python3 -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

### Lancer l'application

```bash
streamlit run app.py
```

L'application s'ouvrira dans votre navigateur à l'adresse `http://localhost:8501`

## 📋 Fonctionnalités

### 📝 Page 1 : Ajouter des éléments
- **Ajouter un Manga** : Formulaire pour ajouter un nouveau manga avec nom, auteur, édition et lien MAL
- **Ajouter un Tome** : Formulaire pour ajouter des tomes à un manga existant
- **Gérer** : 
  - Voir tous les mangas avec leurs statistiques
  - Éditer les informations d'un manga
  - Supprimer un manga et tous ses tomes
  - Voir, éditer et supprimer les tomes individuellement

### 📊 Page 2 : Visualisations & Graphiques
- **Filtres** : Filtrez par édition, auteur, ou plage de dates
- **Métriques** : Affichage de 5 KPIs :
  - Nombre total de mangas
  - Nombre de mangas différents
  - Valeur totale de la collection
  - Nombre de tomes achetés
  - Nombre de tomes offerts
- **Graphiques** :
  - Top 5 des auteurs
  - Top 5 des mangas
  - Répartition par édition (pie chart)
  - Évolution des achats par mois (line chart)

### 📋 Page 3 : Tableau des données
- Tableau complet avec toutes les colonnes
- Filtres par édition, auteur, statut (acheté/offert)
- Recherche par nom de manga ou auteur
- Export en CSV

## 📊 Structure de la base de données

### Table Manga
- `manga_id` (int, PK, auto-increment)
- `manga_name` (varchar)
- `manga_author` (varchar)
- `manga_edition` (varchar)
- `manga_link` (varchar)
- `created_at` (timestamp)

### Table Tome
- `tome_id` (int, PK, auto-increment)
- `manga_id` (int, FK)
- `tome_num` (int)
- `tome_prix` (float)
- `tome_offert` (boolean)
- `tome_date_achat` (date)
- `created_at` (timestamp)

## 📁 Structure du projet

```
BAM/
├── app.py                          # Point d'entrée principal
├── requirements.txt                # Dépendances Python
├── data/
│   └── manga_collection.db        # Base de données SQLite (créée automatiquement)
├── database/
│   ├── __init__.py
│   └── db.py                      # Fonctions CRUD et requêtes BD
├── utils/
│   ├── __init__.py
│   ├── data_helpers.py            # Validation et calcul de métriques
│   ├── filters.py                 # Logique de filtrage et regroupement
│   └── charts.py                  # Génération des graphiques Plotly
└── pages/
    ├── __init__.py
    ├── 01_add_manga.py            # Page d'ajout et gestion
    ├── 02_visualisations.py       # Page graphiques et filtres
    └── 03_table_view.py           # Page tableau interactif
```

## 🛠️ Technologies utilisées

- **Streamlit** : Framework web Python
- **SQLite** : Base de données locale
- **Pandas** : Manipulation de données
- **Plotly** : Graphiques interactifs

## 📝 Exemple d'utilisation

1. Ouvrir l'application
2. Accéder à la page "📝 Ajouter des éléments"
3. Cliquer sur l'onglet "Ajouter Manga" et créer un nouveau manga
4. Cliquer sur l'onglet "Ajouter Tome" et ajouter des tomes à votre manga
5. Consulter la page "📊 Visualisations & Graphiques" pour voir les statistiques
6. Utiliser la page "📋 Tableau des données" pour explorer et exporter vos données

## 🔍 Filtres disponibles

- **Par édition** : Filtrez les mangas par éditeur
- **Par auteur** : Filtrez les mangas par auteur
- **Par date** : Filtrez les achats par plage de dates
- **Par statut** : Voir les tomes achetés ou offerts

## 📥 Export

Vous pouvez exporter vos données en CSV depuis la page "📋 Tableau des données" en cliquant sur le bouton "📥 Télécharger en CSV".

## ⚙️ Configuration

Aucune configuration supplémentaire n'est requise. La base de données SQLite est créée automatiquement au premier lancement.

## 📄 Licence

Ce projet est fourni à titre d'exemple.
