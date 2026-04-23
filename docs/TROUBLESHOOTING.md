# Dépannage (Troubleshooting)

## Problèmes Courants et Solutions

### 🚨 L'application ne démarre pas

#### Erreur: `No module named 'streamlit'`

**Cause** : Les dépendances ne sont pas installées

**Solution** :
```bash
pip install -r requirements.txt
```

#### Erreur: `ModuleNotFoundError: No module named 'database'`

**Cause** : Vous n'êtes pas dans le bon répertoire

**Solution** :
```bash
cd /path/to/BAM
streamlit run app.py
```

### 📊 Les graphiques ne s'affichent pas

#### Les graphiques sont vides

**Causes possibles** :
1. Pas de données dans la base de données
2. Les filtres excluent toutes les données
3. Les dates sont mal formatées

**Solutions** :
1. Vérifiez que vous avez ajouté au moins un manga et un tome
2. Remettez les filtres à zéro (ne sélectionnez rien)
3. Vérifiez les dates en cliquant sur le tableau de données

### ❌ Je ne peux pas modifier un tome

#### Erreur: `st.session_state.edit_tome_XX cannot be modified`

**Cause** : Conflit de clé Streamlit

**Solution** : Rechargez la page (F5)

#### Le formulaire d'édition ne s'affiche pas

**Cause** : La session n'a pas été mise à jour

**Solution** : 
1. Rechargez la page
2. Cliquez à nouveau sur le bouton éditer

### 💾 Problèmes de Base de Données

#### Erreur: `database is locked`

**Cause** : La base de données est accédée par plusieurs processus

**Solution** :
1. Fermer l'application Streamlit
2. Attendre quelques secondes
3. Relancer l'application
```bash
streamlit run app.py
```

#### Les données semblent avoir disparu

**Cause** : La base de données s'est corrompue

**Solution** :
```bash
# Sauvegarder l'ancienne base
mv data/manga_collection.db data/manga_collection.db.backup

# Relancer l'app (créera une nouvelle base)
streamlit run app.py
```

### 🔄 Problèmes de Performance

#### L'application est lente

**Causes possibles** :
1. Trop de données
2. Filtrages complexes
3. Problèmes de ressources système

**Solutions** :
1. Vérifiez vos filtres
2. Fermez les autres applications
3. Vérifiez que vous avez assez de RAM libre

### 🖥️ Problèmes d'Affichage

#### Les textes sont coupés ou mal alignés

**Solution** :
- Agrandissez votre navigateur
- Utilisez le zoom du navigateur (Ctrl +/-)

#### Les dates ne s'affichent pas correctement

**Cause** : Format de date différent

**Solution** :
- Utilisez le format DD/MM/YYYY
- Consultez le tableau des données pour voir le format attendu

### 🔌 Problèmes de Connexion

#### "Connection refused" ou "Address already in use"

**Cause** : Le port 8501 est déjà utilisé

**Solution** :
```bash
# Lancer sur un autre port
streamlit run app.py --server.port 8502
```

### 📝 Erreurs de Validation

#### "Ce champ est obligatoire"

**Cause** : Un champ requis n'a pas été rempli

**Solution** :
- Remplissez tous les champs marqués comme obligatoires
- Pour ajouter un manga : Nom, Auteur et Édition sont obligatoires
- Pour ajouter un tome : Toutes les informations sont obligatoires

#### Le prix doit être positif

**Cause** : Vous avez entré un nombre négatif

**Solution** :
- Entrez un prix positif (ex: 7.99)

### 🔍 Autres Problèmes

#### Comment puis-je nettoyer les données de test ?

**Solution** :
```bash
# Supprimer la base de données
rm data/manga_collection.db

# Relancer (créera une nouvelle base vide)
streamlit run app.py
```

#### Comment puis-je exporter mes données ?

**Solution** :
1. Allez sur la page "Tableau des données"
2. Cliquez sur "Télécharger en CSV"
3. Un fichier CSV sera téléchargé

### 📞 Besoin d'Aide Supplémentaire ?

Si vous ne trouvez pas la solution :

1. Vérifiez la documentation dans `/docs`
2. Consultez la page [USAGE.md](USAGE.md)
3. Créez une issue sur GitHub avec :
   - La description du problème
   - Les messages d'erreur
   - Comment reproduire le problème
   - Votre environnement (OS, Python, version Streamlit)

