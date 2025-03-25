import psycopg2
from psycopg2 import sql
from datetime import datetime

def create_connection():
    conn = psycopg2.connect(
        dbname='postgres', 
        user='postgres', 
        password='1234', 
        host='localhost', 
        port='5432'
    )
    return conn

def initialize_db(conn):
    with conn.cursor() as cursor:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS items (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL,
                employee_name TEXT NOT NULL,
                client_name TEXT,
                purchase_date TIMESTAMP,
                date_added TIMESTAMP NOT NULL,
                city TEXT NOT NULL
            )
        ''')
    conn.commit()

def add_item(conn, name, quantity, price, employee_name, city):
    """Adding new """
    with conn.cursor() as cursor:
        date_added = datetime.now()
        cursor.execute('''
            INSERT INTO items (name, quantity, price, employee_name, date_added, city)
            VALUES (%s, %s, %s, %s, %s, %s)
        ''', (name, quantity, price, employee_name, date_added, city))
    conn.commit()

def get_items(conn):
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM items')
        return cursor.fetchall()

def update_item_quantity(conn, item_id, quantity):
    """Uodating"""
    with conn.cursor() as cursor:
        cursor.execute('''
            UPDATE items
            SET quantity = quantity - %s
            WHERE id = %s
        ''', (quantity, item_id))
    conn.commit()

def get_item_by_id(conn, item_id):
    """getting item ID"""
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM items WHERE id = %s', (item_id,))
        return cursor.fetchone()

def buy_item(conn, item_id, quantity, client_name):
    """function for bying some stuff"""
    item = get_item_by_id(conn, item_id)
    if item:
        current_quantity = item[2]  # quantity is the third column (index 2)
        if current_quantity >= quantity:
            purchase_date = datetime.now()
            with conn.cursor() as cursor:
                cursor.execute('''
                    UPDATE items
                    SET quantity = quantity - %s,
                        client_name = %s,
                        purchase_date = %s
                    WHERE id = %s
                ''', (quantity, client_name, purchase_date, item_id))
            conn.commit()
            print(f"Purchased {quantity} of item ID {item_id}.")
        else:
            print("Not enough stock available.")
    else:
        print("Item not found.")
