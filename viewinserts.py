import sqlite3
import json

# Load User Profiles
def load_profiles():
    with open('profiles.json', 'r') as file:
        profiles = json.load(file)
    return profiles["profiles"]

# Load University List
def load_universities():
    with open('universities.json', 'r') as file:
        universities = json.load(file)
    return universities["universities"]

# View all records from each user's database
def view_all_databases():
    profiles = load_profiles()
    universities = load_universities()

    for profile in profiles:
        db_name = f"{profile['name'].lower().replace(' ', '_')}_vacancies.db"
        print(f"\nViewing records for {profile['name']} in database: {db_name}")
        
        try:
            # Connect to the SQLite database for this user
            conn = sqlite3.connect(db_name)

            # Create a cursor object
            cursor = conn.cursor()

            # Select all records from the vacancies table
            cursor.execute('SELECT * FROM vacancies')
            rows = cursor.fetchall()

            # Close the connection
            conn.close()

            # Display the results
            if rows:
                for row in rows:
                    print(f"University: {row[2]}, Title: {row[1]}, Link: {row[3]}, Date Posted: {row[4]}, Scraped Date: {row[5]}, Description: {row[6]}")
            else:
                print("No records found.")

        except sqlite3.Error as e:
            print(f"Error accessing database {db_name}: {e}")

    # Pause before closing
    input("Press Enter to close...")

# Run the function
if __name__ == "__main__":
    view_all_databases()
