from utils import crypt,sqli_close,sqli_commit,sqli_fetch,get_db,get_random_string
import datetime

def add_tcp(ip_address,port,name, db_path="uptime-kuma/db/kuma.db"):
    db = get_db(db_path)
    sqli_commit(db, db.cursor(), f"INSERT INTO monitor (name, active, user_id, interval, url, type, weight, hostname, port, created_date, keyword,maxretries) VALUES ('{name}', 1, 1, 60, 'https://', 'port', '2000', '{ip_address}', '{port}', '{datetime.datetime.now()}', NULL, 0)")
    sqli_close(db)

def add_http(url,name, db_path="uptime-kuma/db/kuma.db"):
    db = get_db(db_path)
    sqli_commit(db, db.cursor(), f"INSERT INTO monitor (name, active, user_id, interval, url, type, weight, hostname, port, created_date, keyword,maxretries) VALUES ('{name}', 1, 1, 60, '{url}','http','2000', NULL, NULL, '{datetime.datetime.now()}', NULL, 0)")
    sqli_close(db)