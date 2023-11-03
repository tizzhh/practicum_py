import sqlite3

con = sqlite3.connect("db.sqlite")
cur = con.cursor()
cur.execute(
    '''
CREATE TABLE IF NOT EXISTS ice_cream(
    id INTEGER PRIMARY KEY,
    title TEXT,
    description TEXT,
    category TEXT
);
'''
)

con.commit()
con.close()
