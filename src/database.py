import sqlite3
import pandas as pd

database_path="database/email.db"
csv_path=csv_path = "data/emails.csv"
def create_database():
    conn=sqlite3.connect(database_path)
    cursor=conn.cursor()
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
    print("Database created succesfully")
def insert_email():
    df=pd.read_csv(csv_path)
    conn=sqlite3.connect(database_path)
    df.to_sql(
        "emails",
        conn,
        if_exists='append',
        index=False
    )
    conn.close()
    print("Email inserted succesfully")
def show_emails():
    conn=sqlite3.connect(database_path)
    data=pd.read_sql(
        'SELECT * FROM emails',
        conn
    )
    conn.close()
    print(data)
def show_emails():
    conn = sqlite3.connect(database_path)

    df = pd.read_sql("SELECT * FROM emails", conn)

    conn.close()

    print(df)
if __name__=='__main__':
    create_database()
    insert_email()
    show_emails()




