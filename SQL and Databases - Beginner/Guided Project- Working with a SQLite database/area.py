import pandas as pd
import sqlite3

conn = sqlite3.connect('factbook.db')
sum_land = pd.read_sql_query('select sum(area_land) from facts', conn)['sum(area_land)'][0]
print(sum_land)
sum_water = pd.read_sql_query('select sum(area_water) from facts', conn)['sum(area_water)'][0]
print(sum_water)
print(sum_land / sum_water)
conn.close()
