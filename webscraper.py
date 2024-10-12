import requests
from insertentry import insert_vacancy
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime

# Step 1: Set up a database function
def insert_vacancy(title, university, link, date_posted, description, application_deadline):
    conn = sqlite3.connect('phd_vacancies.db')
    cursor = conn.cursor()

    try:
        cursor.execute('''
        INSERT INTO vacancies (title, university, link, date_posted, scraped_date, description)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (title, university, link, date_posted, datetime.now().strftime("%Y-%m-%d"), f"{description}. Deadline: {application_deadline}"))

        conn.commit()
    except sqlite3.IntegrityError:
        print("Vacancy already exists in the database.")

    conn.close()

# Step 2: Scraper function for Lund University
def scrape_lund_vacancies():
    url = "https://www.lunduniversity.lu.se/vacancies"
    response = requests.get(url)

    # Check if request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve page. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all job listings based on the structure you provided
    job_listings = soup.find_all('tr', class_='vacancies-list__job')

    for job in job_listings:
        try:
            title = job['data-job-title']
            department = job['data-job-department']
            link = job.find('a')['href']
            date_posted = job['data-job-published']
            application_deadline = job['data-job-ends']
            description = job.find('p', class_='vacancies-list__job--dept').text.strip()

            # Insert vacancy into the database
            insert_vacancy(title, "Lund University", link, date_posted, description, application_deadline)
            print(f"Added: {title}")
        except Exception as e:
            print(f"Error scraping a job entry: {e}")

# Step 3: Execute the scraper
scrape_lund_vacancies()
