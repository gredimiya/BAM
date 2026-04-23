# Guide de Développement

## 🚀 Configuration de l'Environnement de Développement

### Prérequis

- Python 3.12+
- pip ou conda
- Git
- Un éditeur de code (VS Code, PyCharm, etc.)

### Installation

1. **Cloner le repository**
```bash
git clone https://github.com/yourusername/BAM.git
cd BAM
```

2. **Créer un environnement virtuel**
```bash
python3 -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Installer les dépendances de développement (optionnel)**
```bash
pip install pylint black pytest pytest-cov
```

## 📁 Structure des Fichiers

### Points d'Entrée
- `app.py` : Page d'accueil et point d'entrée principal

### Pages Streamlit
```
pages/
├── 01_add_manga.py      # Formulaires et gestion
├── 02_visualisations.py # Graphiques et statistiques
└── 03_table_view.py     # Vue tableau
```

### Modules de Code
```
database/
└── db.py               # Toutes les requêtes SQL (DAO pattern)

utils/
├── charts.py          # Fonctions Plotly pour graphiques
├── data_helpers.py    # Validation et formatage
└── filters.py         # Logique de filtrage
```

## 🔧 Tâches de Développement Courantes

### Ajouter une Nouvelle Fonctionnalité

1. **Créer la fonction dans le module approprié**

Exemple: Ajouter un graphique d'auteur par édition

```python
# Dans utils/charts.py
def chart_author_by_edition(df):
    """Create chart of authors per edition"""
    if df.empty:
        return go.Figure().add_annotation(text="Pas de données")
    
    # Votre logique ici
    return fig
```

2. **Ajouter une requête BD si nécessaire**

```python
# Dans database/db.py
def get_data_for_chart():
    """Get data formatted for chart"""
    conn = get_connection()
    query = "SELECT ... FROM ..."
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df
```

3. **Importer et utiliser dans une page**

```python
# Dans pages/02_visualisations.py
from utils.charts import chart_author_by_edition

# Dans la section graphiques
st.plotly_chart(chart_author_by_edition(df_filtered))
```

### Modifier le Schéma de la Base de Données

⚠️ **Attention** : Modifiez seulement si nécessaire

1. **Mettre à jour la fonction `init_db()`** dans `database/db.py`
2. **Créer une fonction de migration** pour les données existantes
3. **Supprimer la base ancienne** : `rm data/manga_collection.db`
4. **Relancer l'application** pour créer la nouvelle base

### Ajouter une Nouvelle Page

1. **Créer un fichier** `pages/04_ma_nouvelle_page.py`
2. **Importer Streamlit** : `import streamlit as st`
3. **Configurer la page** : `st.set_page_config(...)`
4. **Ajouter le contenu**

Exemple:
```python
import streamlit as st

st.set_page_config(page_title="Ma Page", layout="wide")
st.title("🎯 Ma Nouvelle Page")

# Contenu ici
```

## 🧪 Tests

### Tester Manuellement

1. **Lancer l'application**
```bash
streamlit run app.py
```

2. **Tester chaque fonctionnalité**
   - Ajouter des mangas
   - Ajouter des tomes
   - Éditer/supprimer
   - Filtrer
   - Visualiser les graphiques

### Tests Automatisés (Futur)

```python
# exemple test simple
import pytest
from database.db import add_manga

def test_add_manga():
    manga_id = add_manga("Naruto", "Kishimoto", "Glénat", "")
    assert manga_id > 0
```

## 📋 Conventions de Code

### Style Python (PEP 8)

```python
# Noms clairs et explicites
def get_total_manga_value():
    """Get total value of all mangas"""
    pass

# Longueur max des lignes: 100 caractères
# Utilisez des espaces pour indenter (4 espaces)
# Une ligne vide entre les fonctions
```

### Nomenclature

- Variables: `snake_case` (ex: `total_value`)
- Fonctions: `snake_case` (ex: `get_manga_by_id()`)
- Classes: `PascalCase` (ex: `MangaService`)
- Constantes: `UPPER_SNAKE_CASE` (ex: `DB_PATH`)

### Docstrings

```python
def calculate_total_price(manga_id):
    """
    Calculate the total price for a manga.
    
    Args:
        manga_id (int): The ID of the manga
        
    Returns:
        float: Total price in euros
    """
    # Implementation
    pass
```

## 🔍 Déboguer

### Avec print() (simple)
```python
print(f"DEBUG: manga_id = {manga_id}")
```

### Avec Streamlit
```python
st.write("DEBUG:", df.head())
st.write("Erreur:", str(e))
```

### Avec le debugger Python
```python
import pdb
pdb.set_trace()  # Le code s'arrête ici
```

## 📦 Dépendances

Voir `requirements.txt` pour la liste complète.

Principales:
- `streamlit` : Framework UI
- `pandas` : Data processing
- `plotly` : Graphiques interactifs
- `sqlite3` : Base de données (inclus Python)

### Ajouter une Dépendance

```bash
pip install nom_du_package
pip freeze > requirements.txt
```

## 🚀 Workflow Git

### Avant de Coder

1. **Créer une branche**
```bash
git checkout -b feature/ma-feature
```

2. **Vérifier le statut**
```bash
git status
```

### Après les Modifications

1. **Vérifier les changements**
```bash
git diff
```

2. **Ajouter et commiter**
```bash
git add .
git commit -m "Description brève du changement"
```

3. **Pusher**
```bash
git push origin feature/ma-feature
```

4. **Créer une Pull Request** sur GitHub

## 📚 Ressources Utiles

- [Documentation Streamlit](https://docs.streamlit.io/)
- [Documentation Plotly](https://plotly.com/python/)
- [Documentation Pandas](https://pandas.pydata.org/)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)

## 🤝 Avant de Soumettre une PR

- [ ] Code testé manuellement
- [ ] Pas d'erreurs ou warnings
- [ ] Documentation mise à jour
- [ ] Commit messages clairs
- [ ] Aucun code de déboggage laissé
- [ ] Respect des conventions de style

