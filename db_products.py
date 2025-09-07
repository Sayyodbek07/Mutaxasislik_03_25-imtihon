import psycopg2
from parsing import *

connect = psycopg2.connect(
    host="localhost",
    user="postgres",
    database="news",
    password="123456"
)

cursor = connect.cursor()

def product_create():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS news_daryo (
            id SERIAL PRIMARY KEY,
            news_text VARCHAR(255),
            image VARCHAR(255)
        );
    """)

    connect.commit()
    print("Table yaraldi")
product_create()

def insert_news_info():
    cursor.execute("""
            INSERT INTO news_daryo (news_text, image)
            VALUES (%s, %s)
        """, (news_text, image))
    connect.commit()
    print("Ma'lumotlar saqlandi")

insert_news_info()

def get_info():
    cursor.execute("""
        SELECT *
        FROM news_daryo
    """)
    products = cursor.fetchall()
    print(products)
    return products

get_info()
connect.commit()