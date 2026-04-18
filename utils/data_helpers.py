from datetime import datetime
import pandas as pd


def validate_manga(name, author, edition, link):
    """Validate manga input"""
    errors = []
    
    if not name or not name.strip():
        errors.append("Le nom du manga est obligatoire")
    if not author or not author.strip():
        errors.append("L'auteur est obligatoire")
    if not edition or not edition.strip():
        errors.append("L'édition est obligatoire")
    
    return errors


def validate_tome(manga_id, num, prix, date_achat):
    """Validate tome input"""
    errors = []
    
    if not manga_id:
        errors.append("Veuillez sélectionner un manga")
    
    try:
        num_int = int(num)
        if num_int < 1:
            errors.append("Le numéro du tome doit être positif")
    except (ValueError, TypeError):
        errors.append("Le numéro du tome doit être un nombre")
    
    try:
        prix_float = float(prix)
        if prix_float < 0:
            errors.append("Le prix ne peut pas être négatif")
    except (ValueError, TypeError):
        errors.append("Le prix doit être un nombre")
    
    if not date_achat:
        errors.append("La date d'achat est obligatoire")
    
    return errors


def format_price(price):
    """Format price as currency"""
    if price is None:
        return "0,00 €"
    return f"{price:.2f} €".replace('.', ',')


def format_date(date):
    """Format date to French format"""
    if date is None:
        return "-"
    if isinstance(date, str):
        return date
    return date.strftime("%d/%m/%Y")


def calculate_metrics(df_tomes):
    """Calculate metrics from tomes dataframe"""
    if df_tomes.empty:
        return {
            "total_price": 0,
            "purchased_count": 0,
            "offered_count": 0
        }
    
    total_price = df_tomes[df_tomes["tome_offert"] == False]["tome_prix"].sum()
    purchased_count = len(df_tomes[df_tomes["tome_offert"] == False])
    offered_count = len(df_tomes[df_tomes["tome_offert"] == True])
    
    return {
        "total_price": total_price,
        "purchased_count": purchased_count,
        "offered_count": offered_count
    }


def date_to_year_month(date_str):
    """Convert date string to year-month for grouping"""
    try:
        date_obj = pd.to_datetime(date_str)
        return date_obj.strftime("%Y-%m")
    except:
        return None
