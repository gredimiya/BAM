import streamlit as st
import pandas as pd
from database.db import get_all_data_joined
from utils.filters import apply_filters, get_unique_editions, get_unique_authors
from utils.data_helpers import format_price, format_date

st.set_page_config(page_title="Table", layout="wide")
st.title("📋 Tableau des données")

# Get data
df = get_all_data_joined()

if df.empty:
    st.info("Aucune donnée disponible. Veuillez ajouter des mangas et des tomes.")
else:
    # Filter section
    st.subheader("🔍 Filtres")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        editions = ["Tous"] + get_unique_editions(df)
        selected_edition = st.selectbox("Édition", editions, key="table_filter_edition")
    
    with col2:
        authors = ["Tous"] + get_unique_authors(df)
        selected_author = st.selectbox("Auteur", authors, key="table_filter_author")
    
    with col3:
        purchase_status = ["Tous", "Achetés", "Offerts"]
        selected_status = st.selectbox("Statut", purchase_status, key="table_filter_status")
    
    with col4:
        search = st.text_input("Rechercher par nom", key="table_search")
    
    # Apply filters
    filters = {
        "edition": selected_edition,
        "author": selected_author,
        "purchase_status": selected_status
    }
    
    df_filtered = apply_filters(df, filters)
    
    # Search by name
    if search:
        df_filtered = df_filtered[
            df_filtered["manga_name"].str.contains(search, case=False, na=False) |
            df_filtered["manga_author"].str.contains(search, case=False, na=False)
        ]
    
    # Format and display
    df_display = df_filtered.copy()
    
    # Format columns for display
    if not df_display.empty:
        df_display["tome_prix"] = df_display["tome_prix"].apply(format_price)
        df_display["tome_date_achat"] = df_display["tome_date_achat"].apply(format_date)
        df_display["tome_offert"] = df_display["tome_offert"].apply(lambda x: "🎁 Offert" if x else "✅ Acheté")
        
        # Rename columns in French
        df_display = df_display.rename(columns={
            "manga_id": "ID",
            "manga_name": "Nom",
            "manga_author": "Auteur",
            "manga_edition": "Édition",
            "manga_link": "Lien MAL",
            "tome_num": "Tome n°",
            "tome_prix": "Prix",
            "tome_offert": "Statut",
            "tome_date_achat": "Date d'achat"
        })
        
        # Select columns to display
        display_columns = ["ID", "Nom", "Auteur", "Édition", "Lien MAL", "Tome n°", "Prix", "Statut", "Date d'achat"]
        df_display = df_display[display_columns]
        
        st.subheader(f"📊 {len(df_filtered)} résultats")
        
        # Display table
        st.dataframe(df_display, use_container_width=True, hide_index=True)
        
        # Export CSV
        csv = df_display.to_csv(index=False)
        st.download_button(
            label="📥 Télécharger en CSV",
            data=csv,
            file_name="manga_collection.csv",
            mime="text/csv"
        )
    else:
        st.warning("Aucun résultat ne correspond à vos filtres.")
