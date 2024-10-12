import sqlite3

# Connect to SQLite (or create the database if it doesn't exist)
conn = sqlite3.connect('phd_vacancies.db')

# Create a cursor object
cursor = conn.cursor()

# Create the table if it doesn't already exist
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

# Commit the changes and close the connection
conn.commit()
conn.close()
