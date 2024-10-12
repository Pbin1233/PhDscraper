import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('phd_vacancies.db')

# Create a cursor object
cursor = conn.cursor()

# Select all records from the vacancies table
cursor.execute('SELECT * FROM vacancies')
rows = cursor.fetchall()

# Close the connection
conn.close()

# Display the results
for row in rows:
    print(row)

# Pause before closing
input("Press Enter to close...")
