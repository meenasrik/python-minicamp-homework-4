from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/movie', methods = ['POST'])
def movie():
    try:
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        print('Connected to database')

        #get values from the form where movie info was entered
        #store in local variables
        Name = request.form['name']
        Language = request.form['language']
        Country = request.form['country']
        print(Name + ",", Language + ",", Country)

        cursor.execute('INSERT INTO info VALUES (?,?,?)', (Name, Language, Country))
        print('Tried inserting record')

        connection.commit()
        msg = 'Successfully inserted record'
        print(msg)

    except:
        connection.rollback()
        msg = 'Error while inserting record'

    finally:
        connection.close()
        return msg

@app.route('/movies')
#retun json for all movies in the database

def movies():
    try:
        connection = sqlite3.connect('database.db')
        cur = connection.cursor()
        print('Connected to database successfully')

        cur.execute('SELECT * FROM info')
        result = cur.fetchall()
        print('Searched the database records')
        print(result)

    except:
        connection.rollback()

    finally:
        connection.close()
        return jsonify(result)

@app.route('/search', methods = {'GET'})
def search():
    try:
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        Name = (request.args['name']).lower()
        print(Name)

        cursor.execute('SELECT * FROM info WHERE LOWER(name)=?', (Name,))
        srch_result = cursor.fetchall()
        print(srch_result)

    except:
        connection.rollback()

    finally:
        connection.close()
        return jsonify(srch_result)
