import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


def chart_top_authors(df, n=5):
    """Create bar chart for top authors"""
    if df.empty:
        return go.Figure().add_annotation(
            text="Pas de données",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False
        )
    
    grouped = df.groupby("manga_author").size().reset_index(name="count")
    grouped = grouped.sort_values("count", ascending=False).head(n)
    
    fig = px.bar(
        grouped,
        x="manga_author",
        y="count",
        labels={"manga_author": "Auteur", "count": "Nombre de tomes"},
        title="Top des auteurs",
        color="count",
        color_continuous_scale="Blues"
    )
    
    fig.update_layout(
        hovermode="x unified",
        showlegend=False,
        height=400
    )
    
    return fig


def chart_top_mangas(df, n=5):
    """Create bar chart for top mangas"""
    if df.empty:
        return go.Figure().add_annotation(
            text="Pas de données",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False
        )
    
    # Only count rows where tome_num exists (actual tomes)
    df_with_tomes = df[df["tome_num"].notna()]
    grouped = df_with_tomes.groupby("manga_name").size().reset_index(name="count")
    grouped = grouped.sort_values("count", ascending=False).head(n)
    
    fig = px.bar(
        grouped,
        x="manga_name",
        y="count",
        labels={"manga_name": "Manga", "count": "Nombre de tomes"},
        title="Top des mangas",
        color="count",
        color_continuous_scale="Greens"
    )
    
    fig.update_layout(
        hovermode="x unified",
        showlegend=False,
        height=400
    )
    
    return fig


def chart_edition_distribution(df):
    """Create pie chart for edition distribution"""
    if df.empty:
        return go.Figure().add_annotation(
            text="Pas de données",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False
        )
    
    df_with_tomes = df[df["tome_num"].notna()]
    grouped = df_with_tomes.groupby("manga_edition").size().reset_index(name="count")
    
    fig = px.pie(
        grouped,
        names="manga_edition",
        values="count",
        title="Répartition par édition",
        color_discrete_sequence=px.colors.sequential.Blues
    )
    
    fig.update_layout(height=400)
    
    return fig


def chart_monthly_evolution(df):
    """Create line chart for monthly purchase evolution"""
    if df.empty:
        return go.Figure().add_annotation(
            text="Pas de données",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False
        )
    
    # Only count purchased items (not offered)
    df_purchased = df[df["tome_offert"] == False].copy()
    
    if df_purchased.empty:
        return go.Figure().add_annotation(
            text="Pas de données",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False
        )
    
    df_purchased["year_month"] = pd.to_datetime(df_purchased["tome_date_achat"]).dt.strftime("%Y-%m")
    grouped = df_purchased.groupby("year_month").size().reset_index(name="count")
    grouped = grouped.sort_values("year_month")
    
    fig = px.line(
        grouped,
        x="year_month",
        y="count",
        markers=True,
        labels={"year_month": "Mois", "count": "Nombre de tomes"},
        title="Évolution des achats par mois"
    )
    
    fig.update_layout(
        hovermode="x unified",
        height=400
    )
    
    return fig
