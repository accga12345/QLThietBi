import mysql.connector

def connect_db():
    conn= mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database= 'tech_inventory_db'
    )
    return conn

