from flask import Flask

import psycopg2 #pip install psycopg2
import psycopg2.extras

app = Flask(__name__)

DB_HOST = "localhost"
DB_NAME = "seen_db"
DB_USER = "postgres"
DB_PASS = "1234"
DB_PORT = "5555"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)

@app.route('/')
def home():
    return "Routes available = [GET](/customers, /landingpages) [POST]() "

@app.route('/customers')
def customers():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM customers;")
    output = str(cur.fetchall())
    conn.commit()
    cur.close()
    return output

@app.route('/landingpages')
def landingpages():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM landing_pages;")
    output = str(cur.fetchall())
    conn.commit()
    cur.close()
    return output

if __name__ == "__main__":
    app.run()