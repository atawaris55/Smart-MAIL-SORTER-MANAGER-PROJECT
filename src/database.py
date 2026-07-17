import sqlite3
import pandas as pd
import os

DATABASE_DIR = "database"
DATABASE_PATH = "database/email.db"
CSV_PATH = "data/emails.csv"


# Create database folder if not exists
os.makedirs(DATABASE_DIR, exist_ok=True)


def create_database():

    conn = sqlite3.connect(DATABASE_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emails(
        id INTEGER PRIMARY KEY,
        sender TEXT,
        subject TEXT,
        body TEXT,
        date TEXT
    )
    """)

    conn.commit()
    conn.close()

    print("Database created successfully")


def insert_email():

    conn = sqlite3.connect(DATABASE_PATH)

    # Check existing data
    count = conn.execute(
        "SELECT COUNT(*) FROM emails"
    ).fetchone()[0]

    if count == 0:
        df = pd.read_csv(CSV_PATH)

        df.to_sql(
            "emails",
            conn,
            if_exists="append",
            index=False
        )

        print("Emails inserted successfully")

    else:
        print("Emails already exist")

    conn.close()


def show_emails():

    conn = sqlite3.connect(DATABASE_PATH)

    df = pd.read_sql(
        "SELECT * FROM emails",
        conn
    )

    conn.close()

    return df


if __name__ == "__main__":

    create_database()
    insert_email()

    print(show_emails())