import requests
from bs4 import BeautifulSoup
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('users_posts.db')
cursor = conn.cursor()

# Create books table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        name TEXT PRIMARY KEY,
        price REAL,
        availability TEXT,
        rating TEXT
    )
''')

conn.commit()

# Function to scrape books data from a given page URL
def scrape_books_data(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    books = soup.find_all('article', class_='product_pod')
    
    for book in books:
        name = book.find('h3').find('a')['title']
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability').text.strip()
        rating = book.find('p', class_='star-rating')['class'][1]
        
        # Check if the book already exists in the database
        cursor.execute("SELECT * FROM books WHERE name=?", (name,))
        existing_book = cursor.fetchone()
        
        if existing_book:
            # Update the existing record
            cursor.execute("UPDATE books SET price=?, availability=?, rating=? WHERE name=?", (price, availability, rating, name))
        else:
            # Insert a new record
            cursor.execute("INSERT INTO books VALUES (?, ?, ?, ?)", (name, price, availability, rating))
    
    conn.commit()

for page_num in range(1, 51):
    page_url = f"http://books.toscrape.com/catalogue/page-{page_num}.html"
    scrape_books_data(page_url)

conn.close()