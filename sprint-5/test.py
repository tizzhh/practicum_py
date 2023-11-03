import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

res = cur.execute(
    '''
SELECT video_products.name,
       product_types.name
FROM video_products,
     product_types
WHERE video_products.type_id = product_types.id AND product_types.name = 'Фильм';
'''
)
for res in res:
    print(res)
con.close()
