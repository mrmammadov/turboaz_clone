import psycopg2
import json

try:
    conn = psycopg2.connect("dbname='django_blog' user='qulumammadli' host='localhost' password=''")
except:
    print("I am unable to connect to the database")


cursor = conn.cursor()

q_read = """
SELECT * FROM cars_carmodel;
"""

with open('/Users/qulumammadli/Documents/Personal/Coding/django_projects/turboaz/car_data.json', 'r') as read_json:
    data = json.load(read_json)

for car in data:
    # s = f'''"{car['name']}", "{car['price']}", "{car["city"]}", "{car['brand']}", "{car['category']}", "{car['color']}", "{car['engine']}", "{car['year']}"'''
    # print(s)
    q_insert = f"""
    INSERT INTO cars_carmodel (name, price, city, brand, category, color, engine, year)
    VALUES('{car['name']}', '{car['price']}', '{car['city']}', '{car['brand']}', '{car['category']}', '{car['color']}', '{car['engine']}', '{car['year']}');
    """

    # print(q_insert)

    cursor.execute(q_insert)
    conn.commit()

cursor.execute(q_read)
record = cursor.fetchall()
print(record)

if conn:
    cursor.close()
    conn.close()
