import sqlite3
from datetime import datetime

def insert_vacancy(title, university, link, date_posted, description):
    conn = sqlite3.connect('phd_vacancies.db')
    cursor = conn.cursor()

    # Insert a new record into the vacancies table
    try:
        cursor.execute('''
        INSERT INTO vacancies (title, university, link, date_posted, scraped_date, description)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (title, university, link, date_posted, datetime.now().strftime("%Y-%m-%d"), description))

        conn.commit()
        print("Vacancy added successfully.")
    except sqlite3.IntegrityError:
        # This will handle duplicate links (since the link field is UNIQUE)
        print("Vacancy already exists in the database.")

    conn.close()

# Example usage
insert_vacancy(
    title="PhD Position in Urban Design",
    university="Politecnico di Milano",
    link="https://www.example.com/phd-vacancy-123",
    date_posted="2024-10-10",
    description="A PhD position focusing on human-centered urban design."
)
