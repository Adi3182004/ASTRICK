import csv
import sqlite3
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Connect to SQLite database
con = sqlite3.connect("astrick.db")
cursor = con.cursor()

# Create the sys_command table if it doesn't exist
cursor.execute("CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))")
cursor.execute("INSERT INTO sys_command VALUES (null, 'one note', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.exe')")
cursor.execute("INSERT INTO sys_command VALUES (null, 'whatsapp', 'C:\\Users\\adity\\Desktop\\whatsapp.lnk')")
cursor.execute("INSERT INTO sys_command VALUES (null, 'Whatsapp', 'C:\\Users\\adity\\Desktop\\whatsapp.lnk')")
cursor.execute("INSERT INTO sys_command VALUES (null, 'whatsApp', 'C:\\Users\\adity\\Desktop\\whatsapp.lnk')")
cursor.execute("INSERT INTO sys_command VALUES (null, 'whutsapp', 'C:\\Users\\adity\\Desktop\\whatsapp.lnk')")
cursor.execute("INSERT INTO sys_command VALUES (null, 'instagram', 'C:\\Users\\adity\\Desktop\\Instagram.lnk')")
con.commit()

# Create the web_command table if it doesn't exist
cursor.execute("CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))")
cursor.execute("INSERT INTO web_command VALUES (null, 'youtube', 'https://www.youtube.com/')")
cursor.execute("INSERT INTO web_command VALUES (null, 'Youtube', 'https://www.youtube.com/')")
cursor.execute("INSERT INTO web_command VALUES (null, 'youTube', 'https://www.youtube.com/')")
cursor.execute("INSERT INTO web_command VALUES (null, 'YouTube', 'https://www.youtube.com/')")
cursor.execute("INSERT INTO web_command VALUES (null, 'yt', 'https://www.youtube.com/')")
cursor.execute("INSERT INTO web_command VALUES (null, 'YT', 'https://www.youtube.com/')")
cursor.execute("INSERT INTO web_command VALUES (null, 'Yt', 'https://www.youtube.com/')")
con.commit()

# Function to find the closest match using fuzzywuzzy
def fuzzy_search(table_name, column_name, search_query):
    cursor.execute(f"SELECT {column_name} FROM {table_name}")
    all_values = [row[0] for row in cursor.fetchall()]
    
    best_match = process.extractOne(search_query, all_values)
    
    if best_match:
        print(f"Best match for '{search_query}': {best_match[0]} with a score of {best_match[1]}")
        return best_match[0]
    else:
        print(f"No match found for '{search_query}'")
        return None


# Create the contacts table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
                    id integer primary key, 
                    name VARCHAR(200), 
                    mobile_no VARCHAR(255), 
                    email VARCHAR(255) NULL)''')

# Specify the column indices you want to import from the CSV file (e.g., first name, middle name, last name, and mobile_no)
desired_columns_indices = [0, 1, 2, 18]  # First, Middle, Last name, and Mobile Number

# Read contact data from 'contacts.csv' and insert it into the database
with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        # Combine First, Middle, and Last Name into a full name
        full_name = f"{row[0]} {row[1]} {row[2]}".strip()  # Concatenate and strip leading/trailing spaces
        mobile_no = row[18]  # The mobile number field
        
        # Insert only full_name and mobile_no into the contacts table
        cursor.execute('''INSERT INTO contacts (id, name, mobile_no) VALUES (null, ?, ?);''', (full_name, mobile_no))

# Commit changes to the database
con.commit()

# Close the database connection
con.close()
