import os
import sqlite3
from datetime import datetime

def insert_vacancy(title, university, link, date_posted, description, application_deadline, db_name):
    # Make sure to use the 'databases' folder
    db_path = os.path.join('databases', db_name)

    # Create the folder if it doesn't exist
    os.makedirs('databases', exist_ok=True)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS vacancies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        university TEXT,
        link TEXT UNIQUE,
        date_posted TEXT,
        scraped_date TEXT,
        description TEXT
    )
    ''')

    try:
        cursor.execute('''
        INSERT INTO vacancies (title, university, link, date_posted, scraped_date, description)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (title, university, link, date_posted, datetime.now().strftime("%Y-%m-%d"), f"{description}. Deadline: {application_deadline}"))

        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Vacancy already exists in the database: {db_name}")

    conn.close()
