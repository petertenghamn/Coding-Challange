from flask import Flask

import psycopg2 #pip install psycopg2
import psycopg2.extras

app = Flask(__name__)

DB_HOST = "localhost"
DB_NAME = ""
DB_USER = "postgres"
DB_PASS = ""

#conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

@app.route('/')
def home():
    testText = ('Home test check!')
    print(testText)
    return testText

if __name__ == "__main__":
    app.run()