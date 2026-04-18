import streamlit as st
from database.db import init_db

# Configure Streamlit
st.set_page_config(
    page_title="BAM - Bilan d'Achat de Manga",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize database
init_db()

# Title and description
st.title("📚 BAM - Bilan d'Achat de Manga")
st.markdown("""
Bienvenue dans votre gestionnaire personnel de collection de mangas !

Utilisez les pages de navigation pour :
- **📝 Ajouter des éléments** : Ajouter de nouveaux mangas et tomes, ou gérer votre collection
- **📊 Visualisations & Graphiques** : Explorer vos données avec des graphiques et des filtres
- **📋 Tableau des données** : Consulter le tableau complet et exporter les données
""")

# Sidebar
with st.sidebar:
    st.header("À propos")
    st.write("""
    **BAM** est une application web construite avec Streamlit pour gérer 
    votre collection de mangas.
    
    **Fonctionnalités:**
    - ✅ Ajouter, éditer et supprimer des mangas
    - ✅ Gérer les tomes par manga
    - ✅ Visualiser les statistiques et graphiques
    - ✅ Filtrer et rechercher les données
    - ✅ Exporter la collection en CSV
    """)
