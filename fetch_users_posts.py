import requests
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('users_posts.db')
cursor = conn.cursor()

# Create users table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id TEXT PRIMARY KEY,
                    title TEXT,
                    firstName TEXT,
                    lastName TEXT,
                    picture TEXT    
                )''')

# Create posts table
cursor.execute('''CREATE TABLE IF NOT EXISTS posts (
                    id TEXT PRIMARY KEY,
                    image TEXT,
                    likes TEXT,
                    tags TEXT,
                    content TEXT, 
                    publishDate TEXT
                )''')

conn.commit()

# API endpoint for fetching users data
users_api_url = "https://dummyapi.io/data/v1/user"
headers = {'app-id': '65f1ce472d8e5b321653472b'}  

# Make GET request to fetch users data
response = requests.get(users_api_url, headers=headers)
users_data = response.json()['data']

# Insert users data into the users table
for user in users_data:
    user_id = user.get('id')
    title = user.get('title')
    first_name = user.get('firstName')
    last_name = user.get('lastName')
    picture = user.get('picture')

    # Check if any required field is missing
    if user_id and first_name and last_name and picture and title:
        cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)", (user_id, title, first_name, last_name, picture))
    else:
        print("User data is incomplete:", user)

conn.commit()

# Function to fetch and store posts data for each user
def fetch_and_store_posts(user_id):
    posts_api_url = f"https://dummyapi.io/data/v1/user/{user_id}/post"
    response = requests.get(posts_api_url, headers=headers)
    posts_data = response.json()['data']
    
    # Insert posts data into the posts table
    for post in posts_data:
        tags = ",".join(post['tags'])
        cursor.execute("INSERT INTO posts VALUES (?, ?, ?, ?, ?, ?)", (post['id'], post['image'], post['likes'], tags, post['text'], post['publishDate']))
    
    conn.commit()

# Fetch list of user IDs from the users table
cursor.execute("SELECT id FROM users")
user_ids = cursor.fetchall()

# Fetch and store posts data for each user
for user_id in user_ids:
    fetch_and_store_posts(user_id[0])  
 
conn.close()