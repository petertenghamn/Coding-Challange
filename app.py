from flask import Flask, jsonify, request

import re
import json
import psycopg2 #pip install psycopg2
import psycopg2.extras

app = Flask(__name__)

DB_HOST = "localhost"
DB_NAME = "seen_db"
DB_USER = "postgres"
DB_PASS = "1234"
DB_PORT = "5555"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)

# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def validEmail(email):
    if (re.fullmatch(regex, email)):
        return True
    else:
        return False

def isAnInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

@app.route('/')
def home():
    return "Routes available = [GET](/customers, /landingpages) [POST](checked using Postman)"

@app.route('/customers')
def customers():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM customers;")
    output = json.dumps(cur.fetchall())
    conn.commit()
    cur.close()
    return output

@app.route('/customers/add', methods=['POST'])
def addCustomer():
    #verify that all fields exist
    _json = request.json
    _email = _json['email']
    _phone = _json['phone']
    #visits is automatically set to 0 for a new customer

    if _email and _phone:
        #if one is of the wrong type, return error
        if (validEmail(_email)):
            cur = conn.cursor()
            cur.execute("INSERT INTO customers (email_address, phone_number, viewed_personal) VALUES ('"+_email+"', '"+_phone+"', 0);")
            conn.commit()
            cur.close()
            return "Customer added successfully!"
        else:
            resp = jsonify({'message' : 'Bad Request - invalid email format'})
            resp.status_code = 400
            return resp
    else:
        resp = jsonify({'message' : 'Bad Request - invalid data'})
        resp.status_code = 400
        return resp

@app.route('/customers/update', methods=['POST'])
def updateCustomer():
    #verify that all fields exist
    _json = request.json
    _email = _json['email']
    _phone = _json['phone']
    _pagevisits = _json['pagevisits']

    if _email and _phone and _pagevisits:
        #check to see if the fields are of the correct type
        if (validEmail(_email)):
            if (isAnInt(_pagevisits)):
                #check that the user exists in the DB
                cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
                cur.execute("SELECT * FROM customers WHERE email_address=%s;", (_email,))
                row = cur.fetchone()
                email = row['email_address']

                if row:
                    if (email==_email):
                        #attempt to write over the existing one
                        cur = conn.cursor()
                        cur.execute("UPDATE customers SET phone_number='"+_phone+"', viewed_personal="+_pagevisits+" WHERE email_address='"+_email+"';")
                        conn.commit()
                        cur.close()
                        return "Customer updated!"
                    else:
                        resp = jsonify({'message' : 'Bad Request - invalid email'})
                        resp.status_code = 400
                        return resp
            else:
                resp = jsonify({'message' : 'Bad Request - invalid format of page visits value'})
                resp.status_code = 400
                return resp
        else:
            resp = jsonify({'message' : 'Bad Request - invalid email format'})
            resp.status_code = 400
            return resp
    else:
        resp = jsonify({'message' : 'Bad Request - invalid data'})
        resp.status_code = 400
        return resp

@app.route('/landingpages')
def landingpages():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM landing_pages;")
    output = json.dumps(cur.fetchall())
    conn.commit()
    cur.close()
    return output

#similar methods to the customer should be added for POST
#would add functions to just allow incrementing the video views/page visits by 1, rather then requesting a full update

if __name__ == "__main__":
    app.run()