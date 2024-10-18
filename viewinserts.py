import sqlite3
import json
import os

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
        db_path = os.path.join('databases', db_name)  # Update to include subfolder

        print(f"\n{'='*80}")
        print(f"Viewing records for {profile['name']} in database: {db_name}")
        print(f"{'='*80}\n")
        
        try:
            # Connect to the SQLite database for this user
            conn = sqlite3.connect(db_path)

            # Create a cursor object
            cursor = conn.cursor()

            # Select all records from the vacancies table
            cursor.execute('SELECT * FROM vacancies')
            rows = cursor.fetchall()

            # Close the connection
            conn.close()

            # Display the results with column headers and formatted output
            if rows:
                print(f"{'University':<20} | {'Title':<30} | {'Link':<50} | {'Date Posted':<15} | {'Scraped Date':<15}")
                print(f"{'-'*140}")
                for row in rows:
                    print(f"{row[2]:<20} | {row[1]:<30} | {row[3]:<50} | {row[4]:<15} | {row[5]:<15}")
            else:
                print("No records found.")

        except sqlite3.Error as e:
            print(f"Error accessing database {db_name}: {e}")

    # Pause before closing
    input("\nPress Enter to close...")

# Run the function
if __name__ == "__main__":
    view_all_databases()
