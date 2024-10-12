import schedule
import time

def job():
    # Your scraping and database insertion logic here
    print("Running daily scrape...")

# Schedule the job every day at a specific time
schedule.every().day.at("10:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
