def vacancy_exists(link):
    conn = sqlite3.connect('phd_vacancies.db')
    cursor = conn.cursor()

    cursor.execute('SELECT 1 FROM vacancies WHERE link = ?', (link,))
    exists = cursor.fetchone() is not None

    conn.close()
    return exists

# Example usage
link = "https://www.example.com/phd-vacancy-123"
if not vacancy_exists(link):
    # Insert if it doesn't exist
    insert_vacancy(
        title="New PhD Position",
        university="Example University",
        link=link,
        date_posted="2024-10-11",
        description="Another exciting PhD opportunity."
    )
