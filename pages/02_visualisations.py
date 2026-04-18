import streamlit as st
import pandas as pd
from database.db import get_all_data_joined, get_metrics
from utils.filters import apply_filters, get_unique_editions, get_unique_authors
from utils.charts import chart_top_authors, chart_top_mangas, chart_edition_distribution, chart_monthly_evolution
from utils.data_helpers import format_price

st.set_page_config(page_title="Visualisations", layout="wide")
st.title("📊 Visualisations & Graphiques")

# Get data
df = get_all_data_joined()
metrics = get_metrics()

# Filter section
st.subheader("🔍 Filtres")

col1, col2, col3, col4 = st.columns(4)

with col1:
    editions = ["Tous"] + get_unique_editions(df)
    selected_edition = st.selectbox("Édition", editions, key="filter_edition")

with col2:
    authors = ["Tous"] + get_unique_authors(df)
    selected_author = st.selectbox("Auteur", authors, key="filter_author")

with col3:
    date_from = st.date_input("Date de", key="filter_date_from")

with col4:
    date_to = st.date_input("Date à", key="filter_date_to")

# Apply filters
filters = {
    "edition": selected_edition,
    "author": selected_author,
    "date_from": date_from,
    "date_to": date_to
}

df_filtered = apply_filters(df, filters)

# Display metrics
st.subheader("📈 Métriques")

metric_col1, metric_col2, metric_col3, metric_col4, metric_col5 = st.columns(5)

with metric_col1:
    st.metric("Nombre total de mangas", metrics["total_mangas"])

with metric_col2:
    st.metric("Nombre de mangas différents", metrics["mangas_with_tomes"])

with metric_col3:
    st.metric("Valeur totale", format_price(metrics["total_value"]))

with metric_col4:
    st.metric("Nombre de tomes achetés", metrics["tomes_purchased"])

with metric_col5:
    st.metric("Nombre de tomes offerts", metrics["tomes_offered"])

# Display charts
st.subheader("📉 Graphiques")

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(chart_top_authors(df_filtered), use_container_width=True)

with col2:
    st.plotly_chart(chart_top_mangas(df_filtered), use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    st.plotly_chart(chart_edition_distribution(df_filtered), use_container_width=True)

with col4:
    st.plotly_chart(chart_monthly_evolution(df_filtered), use_container_width=True)
