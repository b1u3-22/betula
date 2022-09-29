from datetime import datetime
import sqlite3 as sqlite

def start_database():
    connection = sqlite.connect("data.db")
    connection.execute("CREATE TABLE IF NOT EXISTS general_info(id INTEGER PRIMARY KEY, property TEXT NOT NULL, value TEXT NOT NULL)")
    connection.execute("CREATE TABLE IF NOT EXISTS pictures(id INTEGER PRIMARY KEY, link TEXT NOT NULL, location TEXT NOT NULL, description TEXT)")
    connection.execute("CREATE TABLE IF NOT EXISTS financials_general(id INTEGER PRIMARY KEY, property TEXT NOT NULL, value TEXT NOT NULL)")
    connection.execute("CREATE TABLE IF NOT EXISTS debts(id INTEGER PRIMARY KEY, total_debt INTEGER NOT NULL, remaining_debt INTEGER NULL, remaining_debt_per_flat INTEGER NOT NULL, repayment_per_flat INTEGER NOT NULL)")
    connection.execute("CREATE TABLE IF NOT EXISTS posts(id INTEGER PRIMARY KEY, timestamp TIMESTAMP, title TEXT NOT NULL, text TEXT NOT NULL)")
    connection.execute("CREATE TABLE IF NOT EXISTS finus(id INTEGER PRIMARY KEY, link TEXT NOT NULL, location TEXT NOT NULL, timestamp TIMESTAMP)")
    connection.commit()
    connection.close()

def get_general_info():
    connection = sqlite.connect("data.db")
    result = connection.execute("SELECT * FROM general_info").fetchall()
    financials_general = {}

    for i in range(len(result)):
        financials_general[result[i][1]] = result[i][2]

    connection.close()
    return financials_general

def insert_into_general_info(property, value):
    connection = sqlite.connect("data.db")
    connection.execute("INSERT INTO general_info VALUES(NULL, ?, ?)", (property, value))
    connection.commit()
    connection.close()

#====================================================================================================================================

def get_general_financials():
    connection = sqlite.connect("data.db")
    result = connection.execute("SELECT * FROM financials_general").fetchall()
    general_info = {}

    for i in range(len(result)):
        general_info[result[i][1]] = result[i][2]

    connection.close()
    return general_info

def insert_into_general_financials(property, value):
    connection = sqlite.connect("data.db")
    connection.execute("INSERT INTO financials_general VALUES(NULL, ?, ?)", (property, value))
    connection.commit()
    connection.close()

#====================================================================================================================================

def get_all_pictures():
    connection = sqlite.connect("data.db")
    result = connection.execute("SELECT * FROM pictures").fetchall()
    pictures = {}

    for i in range(len(result)):
        pictures[result[i][0]] = {'link': result[i][1], 'location': result[i][2], 'description': result[i][3]}

    connection.close()
    return pictures

def get_picture_by_id(id):
    connection = sqlite.connect("data.db")
    result = connection.execute("SELECT * FROM pictures WHERE id = ?", (id, )).fetchall()[0]
    picture = {'id': result[0], 'link': result[1], 'location': result[2], 'description': result[3]}
    connection.close()
    return picture

def get_picture_by_link(link):
    connection = sqlite.connect("data.db")
    result = connection.execute("SELECT * FROM pictures WHERE link = ?", (link, )).fetchall()[0]
    picture = {'id': result[0], 'link': result[1], 'location': result[2], 'description': result[3]}
    connection.close()
    return picture

def insert_into_pictures(link, location, description):
    connection = sqlite.connect("data.db")
    connection.execute("INSERT INTO pictures VALUES(NULL, ?, ?, ?)", (link, location, description))
    connection.commit()
    connection.close()

#====================================================================================================================================

def get_all_debts():
    connection = sqlite.connect("data.db")
    result = connection.execute("SELECT * FROM debts").fetchall()
    debts = {}

    for i in range(len(result)):
        debts[result[i][0]] = {'total_debt': result[i][1], 'remaining_debt': result[i][2], 'remaining_debt_per_flat': result[i][3], 'repainment_per_flat': result[i][3]}

    connection.close()
    return debts

def insert_into_debts(total_debt, remaining_debt, remaining_debt_per_flat, repayment_per_flat):
    connection = sqlite.connect("data.db")
    connection.execute("INSERT INTO debts VALUES(NULL, ?, ?, ?, ?)", (total_debt, remaining_debt, remaining_debt_per_flat, repayment_per_flat))
    connection.commit()
    connection.close()

#====================================================================================================================================

def get_all_posts():
    connection = sqlite.connect("data.db")
    result = connection.execute("SELECT * FROM debts").fetchall()
    posts = {}

    for i in range(len(result)):
        posts[result[i][0]] = {'timestamp': result[i][1], 'title': result[i][2], 'text': result[i][3]}

    connection.close()
    return posts

def get_post_by_id(id):
    connection = sqlite.connect("data.db")
    result = connection.execute("SELECT * FROM posts WHERE id = ?", (id, )).fetchall()[0]
    post = {'id': result[0], 'timestamp': result[1], 'title': result[2], 'text': result[3]}
    connection.close()
    return post

def insert_into_posts(title, text):
    connection = sqlite.connect("data.db")
    connection.execute("INSERT INTO debts VALUES(NULL, ?, ?, ?)", (datetime.now(), title, text))
    connection.commit()
    connection.close()

#====================================================================================================================================

def get_all_finus():
    connection = sqlite.connect("data.db")
    result = connection.execute("SELECT * FROM finus").fetchall()
    finus = {}

    for i in range(len(result)):
        finus[result[i][0]] = {'link': result[i][1], 'location': result[i][2], 'timestamp': result[i][3]}

    connection.close()
    return finus

def get_latest_finu():
    connection = sqlite.connect("data.db")
    result = connection.execute("SELECT * FROM table ORDER BY id DESC LIMIT 1").fetchall()[0]
    finu = {'id': result[0], 'link': result[1], 'location': result[2], 'timestamp': result[3]}
    connection.close()
    return finu

def insert_into_finus(link, location):
    connection = sqlite.connect("data.db")
    connection.execute("INSERT INTO finus VALUES(NULL, ?, ?, ?)", (link, location, datetime.now()))
    connection.commit()
    connection.close()

#====================================================================================================================================