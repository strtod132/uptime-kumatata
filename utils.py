import bcrypt
import sqlite3

import random
import string

random_string = string.ascii_letters+string.digits

def crypt(string):
    bytes = string.encode('utf-8') 
    salt = bcrypt.gensalt(10)
    hash = bcrypt.hashpw(bytes, salt)
    return hash.decode('utf-8')

def get_db(path):
    con = sqlite3.connect(path)
    return con

def sqli_fetch(db, cursor, request):
    cursor.execute("SELECT * FROM example")
    return cursor.fetchall()

def sqli_commit(db, cursor, request):
    cursor.execute(request)
    db.commit()

def sqli_close(con):
    con.close()

def get_random_string(length):
    result_str = ''.join(random.choice(random_string) for i in range(length))
    return result_str