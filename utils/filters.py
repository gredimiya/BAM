import pandas as pd
from datetime import datetime


def apply_filters(df, filters):
    """Apply filters to dataframe"""
    if df.empty:
        return df
    
    filtered_df = df.copy()
    
    # Filter by edition
    if filters.get("edition") and filters["edition"] != "Tous":
        filtered_df = filtered_df[filtered_df["manga_edition"] == filters["edition"]]
    
    # Filter by author
    if filters.get("author") and filters["author"] != "Tous":
        filtered_df = filtered_df[filtered_df["manga_author"] == filters["author"]]
    
    # Filter by date range
    if filters.get("date_from"):
        filtered_df = filtered_df[pd.to_datetime(filtered_df["tome_date_achat"]) >= pd.to_datetime(filters["date_from"])]
    
    if filters.get("date_to"):
        filtered_df = filtered_df[pd.to_datetime(filtered_df["tome_date_achat"]) <= pd.to_datetime(filters["date_to"])]
    
    # Filter by purchase status
    if filters.get("purchase_status") == "Achetés":
        filtered_df = filtered_df[filtered_df["tome_offert"] == False]
    elif filters.get("purchase_status") == "Offerts":
        filtered_df = filtered_df[filtered_df["tome_offert"] == True]
    
    return filtered_df


def get_unique_editions(df):
    """Get unique editions from dataframe"""
    if df.empty:
        return []
    editions = sorted(df["manga_edition"].dropna().unique().tolist())
    return editions


def get_unique_authors(df):
    """Get unique authors from dataframe"""
    if df.empty:
        return []
    authors = sorted(df["manga_author"].dropna().unique().tolist())
    return authors


def get_top_authors(df, n=5):
    """Get top N authors by number of tomes"""
    if df.empty:
        return pd.DataFrame()
    
    grouped = df.groupby("manga_author").size().reset_index(name="count")
    grouped = grouped.sort_values("count", ascending=False).head(n)
    return grouped


def get_top_mangas(df, n=5):
    """Get top N mangas by number of tomes"""
    if df.empty:
        return pd.DataFrame()
    
    grouped = df.groupby("manga_name").size().reset_index(name="count")
    grouped = grouped.sort_values("count", ascending=False).head(n)
    return grouped


def get_edition_distribution(df):
    """Get distribution by edition"""
    if df.empty:
        return pd.DataFrame()
    
    grouped = df[df["tome_num"].notna()].groupby("manga_edition").size().reset_index(name="count")
    return grouped


def get_monthly_evolution(df):
    """Get monthly evolution of purchases"""
    if df.empty or "tome_date_achat" not in df.columns:
        return pd.DataFrame()
    
    df_copy = df[df["tome_offert"] == False].copy()
    if df_copy.empty:
        return pd.DataFrame()
    
    df_copy["year_month"] = pd.to_datetime(df_copy["tome_date_achat"]).dt.strftime("%Y-%m")
    grouped = df_copy.groupby("year_month").size().reset_index(name="count")
    grouped = grouped.sort_values("year_month")
    
    return grouped
