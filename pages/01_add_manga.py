import streamlit as st
import pandas as pd
from database.db import (
    add_manga, get_all_manga, update_manga, delete_manga,
    add_tome, get_tomes_by_manga, delete_tome, update_tome,
    get_manga_summary
)
from utils.data_helpers import validate_manga, validate_tome, format_price, format_date
from datetime import datetime

st.set_page_config(page_title="Ajouter", layout="wide")
st.title("📝 Ajouter des éléments")

# Tabs for Add Manga / Add Tome / Manage
tab1, tab2, tab3 = st.tabs(["Ajouter Manga", "Ajouter Tome", "Gérer"])

# ===== TAB 1: ADD MANGA =====
with tab1:
    st.subheader("Ajouter un nouveau Manga")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        manga_name = st.text_input("Nom du Manga", key="add_manga_name")
    with col2:
        manga_author = st.text_input("Auteur", key="add_manga_author")
    with col3:
        manga_edition = st.text_input("Édition", key="add_manga_edition")
    with col4:
        manga_link = st.text_input("Lien MAL", key="add_manga_link")
    
    if st.button("➕ Ajouter Manga", key="btn_add_manga"):
        errors = validate_manga(manga_name, manga_author, manga_edition, manga_link)
        
        if errors:
            for error in errors:
                st.error(error)
        else:
            try:
                manga_id = add_manga(manga_name, manga_author, manga_edition, manga_link)
                st.success(f"✅ Manga ajouté avec succès ! (ID: {manga_id})")
                st.rerun()
            except Exception as e:
                st.error(f"❌ Erreur : {str(e)}")

# ===== TAB 2: ADD TOME =====
with tab2:
    st.subheader("Ajouter un Tome à un Manga")
    
    # Get all manga
    all_mangas = get_all_manga()
    
    if not all_mangas:
        st.warning("Aucun manga disponible. Veuillez d'abord ajouter un manga.")
    else:
        manga_options = {m["manga_name"]: m["manga_id"] for m in all_mangas}
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            selected_manga = st.selectbox("Sélectionner un Manga", manga_options.keys(), key="tome_manga")
        
        manga_id = manga_options[selected_manga]
        
        with col2:
            tome_num = st.number_input("Numéro du Tome", min_value=1, value=1, key="tome_num")
        
        with col3:
            tome_prix = st.number_input("Prix", min_value=0.0, value=7.0, step=0.1, key="tome_prix")
        
        with col4:
            tome_date = st.date_input("Date d'achat", value=datetime.now(), key="tome_date")
        
        tome_offert = st.checkbox("Tome offert", value=False, key="tome_offert")
        
        if st.button("➕ Ajouter Tome", key="btn_add_tome"):
            errors = validate_tome(manga_id, tome_num, tome_prix, tome_date)
            
            if errors:
                for error in errors:
                    st.error(error)
            else:
                try:
                    tome_id = add_tome(manga_id, int(tome_num), float(tome_prix), tome_offert, tome_date)
                    st.success(f"✅ Tome ajouté avec succès !")
                    st.rerun()
                except Exception as e:
                    st.error(f"❌ Erreur : {str(e)}")

# ===== TAB 3: MANAGE =====
with tab3:
    st.subheader("Gérer les Mangas")
    
    # Get manga summary
    manga_summary = get_manga_summary()
    
    if manga_summary.empty:
        st.info("Aucun manga dans la base de données.")
    else:
        # Display manga list with actions
        for idx, row in manga_summary.iterrows():
            with st.container(border=True):
                col1, col2, col3 = st.columns([3, 1, 1])
                
                with col1:
                    st.markdown(f"### {row['manga_name']}")
                    st.write(f"**Auteur:** {row['manga_author']} | **Édition:** {row['manga_edition']}")
                    st.write(f"📚 {int(row['total_tomes'])} tome(s) - 💰 {format_price(row['valeur_totale'])} - ✅ {int(row['tomes_achetes'])} achetés - 🎁 {int(row['tomes_offerts'])} offerts")
                
                with col2:
                    if st.button("✏️ Éditer", key=f"edit_manga_{row['manga_id']}"):
                        st.session_state[f"edit_manga_{row['manga_id']}"] = True
                
                with col3:
                    if st.button("🗑️ Supprimer", key=f"delete_manga_{row['manga_id']}"):
                        if st.button("Confirmer suppression", key=f"confirm_delete_{row['manga_id']}"):
                            try:
                                delete_manga(row['manga_id'])
                                st.success("✅ Manga supprimé avec succès !")
                                st.rerun()
                            except Exception as e:
                                st.error(f"❌ Erreur : {str(e)}")
                
                # Edit form
                if st.session_state.get(f"edit_manga_{row['manga_id']}", False):
                    with st.form(f"edit_form_{row['manga_id']}"):
                        st.write("**Modifier ce manga:**")
                        
                        new_name = st.text_input("Nom", value=row['manga_name'], key=f"edit_name_{row['manga_id']}")
                        new_author = st.text_input("Auteur", value=row['manga_author'], key=f"edit_author_{row['manga_id']}")
                        new_edition = st.text_input("Édition", value=row['manga_edition'], key=f"edit_edition_{row['manga_id']}")
                        new_link = st.text_input("Lien MAL", value="", key=f"edit_link_{row['manga_id']}")
                        
                        if st.form_submit_button("💾 Sauvegarder"):
                            errors = validate_manga(new_name, new_author, new_edition, new_link)
                            if errors:
                                for error in errors:
                                    st.error(error)
                            else:
                                try:
                                    update_manga(row['manga_id'], new_name, new_author, new_edition, new_link)
                                    st.success("✅ Manga modifié avec succès !")
                                    st.session_state[f"edit_manga_{row['manga_id']}"] = False
                                    st.rerun()
                                except Exception as e:
                                    st.error(f"❌ Erreur : {str(e)}")
                
                # Show tomes
                with st.expander(f"Voir les {int(row['total_tomes'])} tome(s)"):
                    tomes = get_tomes_by_manga(row['manga_id'])
                    
                    if tomes:
                        for tome in tomes:
                            tome_col1, tome_col2, tome_col3, tome_col4 = st.columns([1, 2, 1, 1])
                            
                            with tome_col1:
                                st.write(f"**Tome {tome['tome_num']}**")
                            
                            with tome_col2:
                                st.write(f"{format_price(tome['tome_prix'])} - {tome['tome_date_achat']} {'🎁' if tome['tome_offert'] else '✅'}")
                            
                            with tome_col3:
                                if st.button("✏️", key=f"edit_tome_{tome['tome_id']}"):
                                    st.session_state[f"edit_tome_{tome['tome_id']}"] = True
                            
                            with tome_col4:
                                if st.button("🗑️", key=f"delete_tome_{tome['tome_id']}"):
                                    try:
                                        delete_tome(tome['tome_id'])
                                        st.success("✅ Tome supprimé")
                                        st.rerun()
                                    except Exception as e:
                                        st.error(f"❌ Erreur : {str(e)}")
                            
                            # Edit tome form
                            if st.session_state.get(f"edit_tome_{tome['tome_id']}", False):
                                with st.form(f"edit_tome_form_{tome['tome_id']}"):
                                    new_tome_num = st.number_input("Numéro", value=tome['tome_num'], key=f"et_num_{tome['tome_id']}")
                                    new_tome_prix = st.number_input("Prix", value=tome['tome_prix'], step=0.1, key=f"et_prix_{tome['tome_id']}")
                                    new_tome_offert = st.checkbox("Offert", value=tome['tome_offert'], key=f"et_offert_{tome['tome_id']}")
                                    new_tome_date = st.date_input("Date", value=pd.to_datetime(tome['tome_date_achat']).date(), key=f"et_date_{tome['tome_id']}")
                                    
                                    if st.form_submit_button("💾"):
                                        try:
                                            update_tome(tome['tome_id'], new_tome_num, new_tome_prix, new_tome_offert, new_tome_date)
                                            st.success("✅ Tome modifié !")
                                            st.session_state[f"edit_tome_{tome['tome_id']}"] = False
                                            st.rerun()
                                        except Exception as e:
                                            st.error(f"❌ Erreur : {str(e)}")
                    else:
                        st.write("Aucun tome pour ce manga")
