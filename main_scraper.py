import json
import sqlite3
import os
from scrapers.lund_university import scrape_lund_university
from scrapers.eth_zurich import scrape_eth_zurich
from scrapers.kth import scrape_kth
from scrapers.uppsala_university import scrape_uppsala
from scrapers.dtu import scrape_dtu

# Ensure the /databases subfolder exists
def ensure_db_folder_exists():
    if not os.path.exists('databases'):
        os.makedirs('databases')

# Initialize the central database in the /databases folder
def init_db():
    ensure_db_folder_exists()
    db_path = os.path.join('databases', 'scraped_data.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        profile_name TEXT,
        university_name TEXT,
        data TEXT,
        date_scraped TEXT
    )
    ''')
    
    conn.commit()
    conn.close()

# Load University URLs from JSON
def load_universities():
    with open('universities.json', 'r') as file:
        universities = json.load(file)
    return universities["universities"]

# Load User Profiles from JSON
def load_profiles():
    with open('profiles.json', 'r') as file:
        profiles = json.load(file)
    return profiles["profiles"]

# Mapping of university scrapers
SCRAPER_FUNCTIONS = {
    "Lund University": scrape_lund_university,
    "ETH Zurich": scrape_eth_zurich,
    "KTH Royal Institute of Technology": scrape_kth,
    "Uppsala University": scrape_uppsala,
    "Technical University of Denmark (DTU)": scrape_dtu,
}

def main():
    init_db()  # Initialize the database
    
    profiles = load_profiles()
    universities = load_universities()

    for profile in profiles:
        for university in universities:
            if university["name"] in profile["universities"]:
                scraper_function = SCRAPER_FUNCTIONS.get(university["name"])
                if scraper_function:
                    scraper_function(profile, university)
                else:
                    print(f"No scraper available for {university['name']}")

if __name__ == "__main__":
    main()
