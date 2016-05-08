## 1. Introduction ##

import sqlite3
conn = sqlite3.connect('factbook.db')
schema = conn.execute('pragma table_info(facts);').fetchall()
for e in schema:
    print(e)
conn.close()

## 3. Explain query plan ##

conn = sqlite3.connect("factbook.db")
query_plan_one = conn.execute('explain query plan select * from facts where area > 40000;').fetchall()
query_plan_two = conn.execute('explain query plan select area from facts where area > 40000;').fetchall()
query_plan_three = conn.execute('explain query plan select * from facts where name == "Czech Republic";').fetchall()
print(query_plan_one, query_plan_two, query_plan_three)
conn.close()

## 5. Time complexity ##

conn = sqlite3.connect("factbook.db")
query_plan_four = conn.execute('explain query plan select * from facts where id == 20;').fetchall()
print(query_plan_four)
conn.close()

## 7. Indexing ##

conn = sqlite3.connect("factbook.db")

india_index = conn.execute('select id from name_idx where name == "India";').fetchall()[0][0]
first_query_plan = conn.execute('explain query plan select id from name_idx where name == "India";').fetchall()

india_row = conn.execute('select * from facts where id == ' + str(india_index) + ';').fetchall()
second_query_plan = conn.execute('explain query plan select * from facts where id == ' + str(india_index) + ';').fetchall()

print(first_query_plan, india_index, second_query_plan, india_row)
conn.close()

## 9. All together now ##

conn = sqlite3.connect("factbook.db")

query_plan_six = conn.execute('explain query plan select * from facts where population > 10000;').fetchall()
print(query_plan_six)

conn.execute('create index if not exists pop_idx on facts(population);')

query_plan_seven = conn.execute('explain query plan select * from facts where population > 10000;').fetchall()
print(query_plan_seven)

conn.close()