# Guide d'Utilisation de BAM

## 📖 Table des Matières

1. [Démarrage](#démarrage)
2. [Ajouter des Mangas](#ajouter-des-mangas)
3. [Ajouter des Tomes](#ajouter-des-tomes)
4. [Gérer les Mangas](#gérer-les-mangas)
5. [Visualiser les Graphiques](#visualiser-les-graphiques)
6. [Consulter le Tableau](#consulter-le-tableau)

## Démarrage

### 1. Lancer l'application

```bash
cd /path/to/BAM
source venv/bin/activate  # Activer l'environnement virtuel
streamlit run app.py
```

L'application s'ouvrira dans votre navigateur à `http://localhost:8501`

### 2. Interface Principale

La barre latérale gauche contient la navigation avec 3 pages :
- 📝 **Ajouter des éléments** : Gestion des mangas et tomes
- 📊 **Visualisations & Graphiques** : Statistiques et graphiques
- 📋 **Tableau des données** : Vue tableau et export

## Ajouter des Mangas

### Onglet "Ajouter Manga"

1. Remplissez les champs :
   - **Nom du Manga** : Le titre du manga
   - **Auteur** : Le créateur du manga
   - **Édition** : L'éditeur (ex: Glénat, Akaoni, etc.)
   - **Lien MAL** : Lien vers MyAnimeList (optionnel)

2. Cliquez sur **➕ Ajouter Manga**

3. Un message de confirmation apparaîtra

⚠️ **Important** : Les trois premiers champs sont obligatoires

## Ajouter des Tomes

### Onglet "Ajouter Tome"

1. Sélectionnez un manga existant dans la liste déroulante
2. Remplissez les champs :
   - **Numéro du Tome** : 1, 2, 3, etc.
   - **Prix** : Le prix d'achat en euros
   - **Date d'achat** : Quand vous avez acheté le tome
   - **Tome offert** : Cochez si le tome a été offert

3. Cliquez sur **➕ Ajouter Tome**

⚠️ **Important** : Vous devez d'abord créer un manga avant d'ajouter des tomes

## Gérer les Mangas

### Onglet "Gérer"

Cet onglet affiche tous les mangas avec leurs statistiques :

```
Nom du Manga
Auteur: XXX | Édition: YYY
📚 5 tome(s) - 💰 35.00€ - ✅ 4 achetés - 🎁 1 offert
```

### Actions Disponibles

#### Éditer un Manga
1. Cliquez sur **✏️ Éditer**
2. Modifiez les informations
3. Cliquez sur **💾 Sauvegarder**

#### Supprimer un Manga
1. Cliquez sur **🗑️ Supprimer**
2. Confirmez la suppression

⚠️ **Attention** : Supprimer un manga supprime aussi tous ses tomes

#### Voir les Tomes
1. Cliquez sur **Voir les X tome(s)**
2. La liste des tomes apparaît

### Gérer les Tomes

Chaque tome affiche :
```
Tome 1
7.99€ - 2024-01-15 ✅
```

#### Éditer un Tome
1. Cliquez sur **✏️**
2. Modifiez :
   - Numéro
   - Prix
   - Date d'achat
   - Statut (offert/acheté)
3. Cliquez sur **💾**

#### Supprimer un Tome
1. Cliquez sur **🗑️**
2. Le tome est supprimé immédiatement

## Visualiser les Graphiques

### Page "Visualisations & Graphiques"

#### Filtres

Utilisez les filtres pour affiner les données affichées :

1. **Édition** : Sélectionnez une ou plusieurs éditions
2. **Auteur** : Sélectionnez un ou plusieurs auteurs
3. **Date de** : Date de début
4. **Date à** : Date de fin

💡 **Astuce** : Laisser les filtres vides affiche toutes les données

#### Métriques

Cinq KPIs s'affichent :
- **Nombre total de mangas** : Tous les mangas ajoutés
- **Nombre de mangas différents** : Mangas avec au moins un tome
- **Valeur totale** : Prix total achetés (sans les offerts)
- **Nombre de tomes achetés** : Tomes achetés
- **Nombre de tomes offerts** : Tomes reçus en cadeau

#### Graphiques Disponibles

1. **Top des auteurs** : Les 5 auteurs avec le plus de tomes
2. **Top des mangas** : Les 5 mangas avec le plus de tomes
3. **Répartition par édition** : Graphique circulaire des éditeurs
4. **Évolution des achats par mois** : Nombre de tomes achetés chaque mois
5. **Évolution des dépenses par mois** : Prix total dépensé chaque mois

💡 Les graphiques se mettent à jour automatiquement selon les filtres

## Consulter le Tableau

### Page "Tableau des données"

Affiche toutes les données dans un tableau éditable avec les colonnes :
- Manga ID
- Nom
- Auteur
- Édition
- Lien
- Tome ID
- Numéro
- Prix
- Offert
- Date d'achat

### Exporter les Données

Cliquez sur **Télécharger en CSV** pour exporter vos données en fichier CSV.

## 💡 Conseils d'Utilisation

1. **Soyez cohérent** : Utilisez les mêmes noms d'éditeurs et d'auteurs
2. **Dates** : Remplissez les dates correctement pour les statistiques mensuelles
3. **Sauvegardes** : Exportez régulièrement vos données en CSV
4. **Filtres** : Utilisez les filtres pour analyser des sous-ensembles de votre collection

## 🆘 Besoin d'Aide ?

- Consultez le fichier [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- Vérifiez que l'application est bien lancée avec `streamlit run app.py`
- Vérifiez que tous les dépendances sont installées : `pip install -r requirements.txt`
