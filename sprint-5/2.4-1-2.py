import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

results = cur.execute(
    '''
SELECT ice_cream.title as ice_cream,
       categories.slug as category,
       wrappers.title as wrapper,
       MIN(ice_cream.price),
       AVG(ice_cream.price)
FROM ice_cream
JOIN categories ON ice_cream.category_id = categories.id
JOIN wrappers ON ice_cream.wrapper_id = wrappers.id
GROUP BY category
'''
)

for result in results:
    print(result)

con.close()
