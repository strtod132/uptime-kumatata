from utils import crypt,sqli_close,sqli_commit,sqli_fetch,get_db,get_random_string

def create_user(username, db_path="uptime-kuma/db/kuma.db"):
    password = get_random_string(10)
    db = get_db(db_path)
    print(password)
    sqli_commit(db, db.cursor(), f"INSERT INTO user (username, password, active, timezone) VALUES ('{username}', '{crypt(password)}', 1, NULL)")
    sqli_close(db)