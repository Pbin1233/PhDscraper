import json
import sqlite3
from scrapers.lund_university import scrape_lund_university
from scrapers.eth_zurich import scrape_eth_zurich
from scrapers.kth import scrape_kth
from scrapers.uppsala_university import scrape_uppsala
from scrapers.dtu import scrape_dtu

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

# Execute the scraper for all profiles and universities
def main():
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
