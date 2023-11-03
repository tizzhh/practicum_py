import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

results = cur.execute('''
SELECT SUM(price)
FROM ice_cream
WHERE is_published = 1
  AND is_on_main = 1;
''')


for result in results:
    print(result)

con.close()