# TailNode Assignment

This repository contains a Python project for completing the TailNode assignment, which consists of two parts: fetching users and their corresponding posts data from an API and storing it in a database (Part A), and scraping book data from a website and storing it in a database (Part B).

## Part A: Fetching Users and Posts Data

### Objective
The objective of Part A is to use the provided API to fetch users' data and their corresponding posts data, and store it in a database.

### Implementation
- The project uses the `dummyapi.io` API to fetch users' data and posts data.
- It utilizes SQLite as the database to store the fetched data.
- Python scripts `fetch_users.py` and `fetch_users_posts.py` are implemented to fetch users' data and posts data respectively, and store it in the database.

### Running the Project
To run Part A of the project, follow these steps:
1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Create an account on the `dummyapi.io` website and obtain an app ID.
4. Update the `config.py` file with your app ID.
5. Run the `fetch_users.py` script to fetch users' data and store it in the database:
6. Run the `fetch_users_posts.py` script to fetch users' posts data and store it in the database:


## Part B: Scraping Book Data

### Objective
The objective of Part B is to scrape book data from the `http://books.toscrape.com` website and store it in a database.

### Implementation
- The project utilizes web scraping techniques to extract book data from the provided website.
- It uses BeautifulSoup and requests libraries in Python for web scraping.
- The scraped data is stored in an SQLite database.

### Running the Project
To run Part B of the project, follow these steps:
1. Run the `scrape_books.py` script to scrape book data and store it in the database:

