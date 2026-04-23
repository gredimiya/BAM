# Référence API / Base de Données

## Vue d'ensemble

Ce document décrit les fonctions disponibles dans le module `database/db.py` et comment les utiliser.

## Fonctions CRUD - Manga

### `add_manga(name, author, edition, link)`

Ajoute un nouveau manga à la base de données.

**Paramètres:**
- `name` (str): Nom du manga
- `author` (str): Auteur du manga
- `edition` (str): Édition/Éditeur
- `link` (str): Lien MAL (optionnel)

**Retour:** `int` - ID du manga créé

**Exemple:**
```python
from database.db import add_manga

manga_id = add_manga("Naruto", "Kishimoto", "Glénat", "https://myanimelist.net/...")
print(f"Manga créé avec l'ID: {manga_id}")
```

---

### `get_all_manga()`

Récupère tous les mangas de la base de données.

**Paramètres:** Aucun

**Retour:** `list[dict]` - Liste des mangas

**Exemple:**
```python
from database.db import get_all_manga

mangas = get_all_manga()
for manga in mangas:
    print(f"{manga['manga_name']} par {manga['manga_author']}")
```

---

### `get_manga_by_id(manga_id)`

Récupère un manga spécifique par son ID.

**Paramètres:**
- `manga_id` (int): ID du manga

**Retour:** `dict` ou `None` si non trouvé

**Exemple:**
```python
from database.db import get_manga_by_id

manga = get_manga_by_id(1)
if manga:
    print(f"Nom: {manga['manga_name']}")
```

---

### `update_manga(manga_id, name, author, edition, link)`

Met à jour les informations d'un manga.

**Paramètres:**
- `manga_id` (int): ID du manga à modifier
- `name` (str): Nouveau nom
- `author` (str): Nouvel auteur
- `edition` (str): Nouvelle édition
- `link` (str): Nouveau lien

**Retour:** Aucun

**Exemple:**
```python
from database.db import update_manga

update_manga(1, "Naruto (édition complète)", "Masashi Kishimoto", "Glénat", "")
```

---

### `delete_manga(manga_id)`

Supprime un manga et tous ses tomes associés.

**Paramètres:**
- `manga_id` (int): ID du manga à supprimer

**Retour:** Aucun

**⚠️ Important:** Cette action supprime aussi tous les tomes du manga

**Exemple:**
```python
from database.db import delete_manga

delete_manga(1)  # Supprime le manga et ses tomes
```

---

## Fonctions CRUD - Tome

### `add_tome(manga_id, num, prix, offert, date_achat)`

Ajoute un nouveau tome à un manga.

**Paramètres:**
- `manga_id` (int): ID du manga auquel ajouter le tome
- `num` (int): Numéro du tome
- `prix` (float): Prix en euros
- `offert` (bool): True si le tome est offert, False sinon
- `date_achat` (date): Date d'achat

**Retour:** `int` - ID du tome créé

**Exemple:**
```python
from database.db import add_tome
from datetime import date

tome_id = add_tome(1, 1, 7.99, False, date(2024, 1, 15))
```

---

### `get_tomes_by_manga(manga_id)`

Récupère tous les tomes d'un manga spécifique.

**Paramètres:**
- `manga_id` (int): ID du manga

**Retour:** `list[dict]` - Liste des tomes

**Exemple:**
```python
from database.db import get_tomes_by_manga

tomes = get_tomes_by_manga(1)
for tome in tomes:
    print(f"Tome {tome['tome_num']}: {tome['tome_prix']}€")
```

---

### `get_all_tomes()`

Récupère tous les tomes de la base de données.

**Paramètres:** Aucun

**Retour:** `list[dict]` - Liste de tous les tomes

**Exemple:**
```python
from database.db import get_all_tomes

tomes = get_all_tomes()
print(f"Total de tomes: {len(tomes)}")
```

---

### `update_tome(tome_id, num, prix, offert, date_achat)`

Met à jour un tome.

**Paramètres:**
- `tome_id` (int): ID du tome
- `num` (int): Nouveau numéro
- `prix` (float): Nouveau prix
- `offert` (bool): Nouveau statut
- `date_achat` (date): Nouvelle date

**Retour:** Aucun

**Exemple:**
```python
from database.db import update_tome
from datetime import date

update_tome(1, 1, 8.99, False, date(2024, 2, 20))
```

---

### `delete_tome(tome_id)`

Supprime un tome.

**Paramètres:**
- `tome_id` (int): ID du tome à supprimer

**Retour:** Aucun

**Exemple:**
```python
from database.db import delete_tome

delete_tome(5)
```

---

## Requêtes Jointes

### `get_all_data_joined()`

Récupère tous les mangas avec leurs tomes dans un DataFrame Pandas.

**Retour:** `pd.DataFrame` avec les colonnes:
- `manga_id`, `manga_name`, `manga_author`, `manga_edition`, `manga_link`
- `tome_id`, `tome_num`, `tome_prix`, `tome_offert`, `tome_date_achat`

**Exemple:**
```python
from database.db import get_all_data_joined

df = get_all_data_joined()
print(df.head())
```

---

### `get_manga_summary()`

Récupère un résumé avec statistiques pour chaque manga.

**Retour:** `pd.DataFrame` avec les colonnes:
- `manga_id`, `manga_name`, `manga_author`, `manga_edition`
- `total_tomes`, `tomes_achetes`, `tomes_offerts`, `valeur_totale`

**Exemple:**
```python
from database.db import get_manga_summary

summary = get_manga_summary()
for _, manga in summary.iterrows():
    print(f"{manga['manga_name']}: {manga['total_tomes']} tomes - {manga['valeur_totale']}€")
```

---

### `get_metrics()`

Récupère les métriques globales de la collection.

**Retour:** `dict` avec les clés:
- `total_mangas` (int): Nombre total de mangas
- `mangas_with_tomes` (int): Nombre de mangas avec au moins 1 tome
- `total_value` (float): Valeur totale achetée
- `tomes_purchased` (int): Nombre de tomes achetés
- `tomes_offered` (int): Nombre de tomes offerts

**Exemple:**
```python
from database.db import get_metrics

metrics = get_metrics()
print(f"Valeur totale: {metrics['total_value']}€")
print(f"Tomes achetés: {metrics['tomes_purchased']}")
```

---

## Gestion de la Connexion

### `get_connection()`

Obtient une connexion SQLite.

**Retour:** `sqlite3.Connection`

**Exemple:**
```python
from database.db import get_connection

conn = get_connection()
cursor = conn.cursor()
# Votre code SQL
conn.close()
```

---

### `init_db()`

Initialise la base de données (crée les tables si elles n'existent pas).

**Paramètres:** Aucun

**Retour:** Aucun

**Exemple:**
```python
from database.db import init_db

init_db()  # Appelé automatiquement au démarrage
```

---

## Utilisation dans Streamlit

Les fonctions de la base de données sont utilisées dans les pages Streamlit.

**Exemple complet:**
```python
import streamlit as st
from database.db import add_manga, get_all_manga

st.title("Ajouter un Manga")

name = st.text_input("Nom")
author = st.text_input("Auteur")
edition = st.text_input("Édition")

if st.button("Ajouter"):
    manga_id = add_manga(name, author, edition, "")
    st.success(f"Manga ajouté! ID: {manga_id}")
    
# Afficher la liste
mangas = get_all_manga()
for manga in mangas:
    st.write(f"- {manga['manga_name']}")
```

---

## Notes et Bonnes Pratiques

1. **Validez les données** avant d'appeler les fonctions de BD
2. **Utilisez des transactions** pour les opérations critiques
3. **Fermez toujours les connexions** après usage
4. **Gérez les exceptions** quand vous insérez/modifiez des données
5. **Utilisez les DataFrames Pandas** pour les analyses

---

## Voir Aussi

- [ARCHITECTURE.md](ARCHITECTURE.md) - Vue d'ensemble technique
- [USAGE.md](USAGE.md) - Guide d'utilisation
- [DEVELOPMENT.md](DEVELOPMENT.md) - Guide de développement

