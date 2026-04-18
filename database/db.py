import sqlite3
import pandas as pd
from datetime import datetime
from pathlib import Path
import os

# Database path
DB_PATH = Path(__file__).parent.parent / "data" / "manga_collection.db"


def get_connection():
    """Get SQLite connection"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Initialize database with tables if they don't exist"""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Create Manga table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Manga (
            manga_id INTEGER PRIMARY KEY AUTOINCREMENT,
            manga_name VARCHAR(255) NOT NULL,
            manga_author VARCHAR(255) NOT NULL,
            manga_edition VARCHAR(255) NOT NULL,
            manga_link VARCHAR(255),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Create Tome table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Tome (
            tome_id INTEGER PRIMARY KEY AUTOINCREMENT,
            manga_id INTEGER NOT NULL,
            tome_num INTEGER NOT NULL,
            tome_prix REAL NOT NULL,
            tome_offert BOOLEAN DEFAULT 0,
            tome_date_achat DATE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (manga_id) REFERENCES Manga(manga_id) ON DELETE CASCADE
        )
    """)
    
    conn.commit()
    conn.close()


# ============= MANGA CRUD =============

def add_manga(name, author, edition, link):
    """Add new manga to database"""
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            INSERT INTO Manga (manga_name, manga_author, manga_edition, manga_link)
            VALUES (?, ?, ?, ?)
        """, (name, author, edition, link))
        
        manga_id = cursor.lastrowid
        conn.commit()
        return manga_id
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()


def get_all_manga():
    """Get all manga from database"""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Manga ORDER BY manga_name")
    rows = cursor.fetchall()
    conn.close()
    
    return [dict(row) for row in rows]


def get_manga_by_id(manga_id):
    """Get specific manga by ID"""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Manga WHERE manga_id = ?", (manga_id,))
    row = cursor.fetchone()
    conn.close()
    
    return dict(row) if row else None


def update_manga(manga_id, name, author, edition, link):
    """Update manga information"""
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            UPDATE Manga 
            SET manga_name = ?, manga_author = ?, manga_edition = ?, manga_link = ?
            WHERE manga_id = ?
        """, (name, author, edition, link, manga_id))
        
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()


def delete_manga(manga_id):
    """Delete manga and all associated tomes"""
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("DELETE FROM Tome WHERE manga_id = ?", (manga_id,))
        cursor.execute("DELETE FROM Manga WHERE manga_id = ?", (manga_id,))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()


# ============= TOME CRUD =============

def add_tome(manga_id, num, prix, offert, date_achat):
    """Add new tome to manga"""
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            INSERT INTO Tome (manga_id, tome_num, tome_prix, tome_offert, tome_date_achat)
            VALUES (?, ?, ?, ?, ?)
        """, (manga_id, num, prix, offert, date_achat))
        
        tome_id = cursor.lastrowid
        conn.commit()
        return tome_id
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()


def get_tomes_by_manga(manga_id):
    """Get all tomes for a specific manga"""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Tome WHERE manga_id = ? ORDER BY tome_num", (manga_id,))
    rows = cursor.fetchall()
    conn.close()
    
    return [dict(row) for row in rows]


def get_all_tomes():
    """Get all tomes from database"""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Tome ORDER BY tome_date_achat DESC")
    rows = cursor.fetchall()
    conn.close()
    
    return [dict(row) for row in rows]


def update_tome(tome_id, num, prix, offert, date_achat):
    """Update tome information"""
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            UPDATE Tome 
            SET tome_num = ?, tome_prix = ?, tome_offert = ?, tome_date_achat = ?
            WHERE tome_id = ?
        """, (num, prix, offert, date_achat, tome_id))
        
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()


def delete_tome(tome_id):
    """Delete a specific tome"""
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("DELETE FROM Tome WHERE tome_id = ?", (tome_id,))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()


# ============= JOINED QUERIES =============

def get_all_data_joined():
    """Get all manga with their tomes in a single DataFrame"""
    conn = get_connection()
    
    query = """
        SELECT 
            m.manga_id,
            m.manga_name,
            m.manga_author,
            m.manga_edition,
            m.manga_link,
            t.tome_id,
            t.tome_num,
            t.tome_prix,
            t.tome_offert,
            t.tome_date_achat
        FROM Manga m
        LEFT JOIN Tome t ON m.manga_id = t.manga_id
        ORDER BY m.manga_name, t.tome_num
    """
    
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    return df


def get_manga_summary():
    """Get summary statistics for visualization"""
    conn = get_connection()
    
    query = """
        SELECT 
            m.manga_id,
            m.manga_name,
            m.manga_author,
            m.manga_edition,
            COUNT(DISTINCT t.tome_id) as total_tomes,
            SUM(CASE WHEN t.tome_offert = 0 THEN 1 ELSE 0 END) as tomes_achetes,
            SUM(CASE WHEN t.tome_offert = 1 THEN 1 ELSE 0 END) as tomes_offerts,
            SUM(t.tome_prix) as valeur_totale
        FROM Manga m
        LEFT JOIN Tome t ON m.manga_id = t.manga_id
        GROUP BY m.manga_id, m.manga_name, m.manga_author, m.manga_edition
        ORDER BY m.manga_name
    """
    
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    return df


def get_metrics():
    """Get overall metrics"""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Total number of mangas
    cursor.execute("SELECT COUNT(*) as count FROM Manga")
    total_mangas = cursor.fetchone()[0]
    
    # Number of unique mangas
    cursor.execute("SELECT COUNT(DISTINCT manga_id) as count FROM Tome")
    mangas_with_tomes = cursor.fetchone()[0]
    
    # Total value
    cursor.execute("SELECT SUM(tome_prix) as total FROM Tome WHERE tome_offert = 0")
    result = cursor.fetchone()[0]
    total_value = result if result else 0
    
    # Number of purchased tomes
    cursor.execute("SELECT COUNT(*) as count FROM Tome WHERE tome_offert = 0")
    tomes_purchased = cursor.fetchone()[0]
    
    # Number of offered tomes
    cursor.execute("SELECT COUNT(*) as count FROM Tome WHERE tome_offert = 1")
    tomes_offered = cursor.fetchone()[0]
    
    conn.close()
    
    return {
        "total_mangas": total_mangas,
        "mangas_with_tomes": mangas_with_tomes,
        "total_value": total_value,
        "tomes_purchased": tomes_purchased,
        "tomes_offered": tomes_offered
    }
