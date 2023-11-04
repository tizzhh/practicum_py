import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

results = cur.execute('''
SELECT ice_cream.title AS ice_title,
       wrappers.title AS wrap_title
FROM ice_cream
JOIN wrappers ON ice_cream.wrapper_id = wrappers.id
WHERE wrap_title LIKE '%праздн%';
''')

for result in results:
    print(result)

con.close()