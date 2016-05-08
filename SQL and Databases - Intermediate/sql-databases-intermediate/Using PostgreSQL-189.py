## 3. Psycopg2 ##

import psycopg2
conn = psycopg2.connect('dbname=dq user=dq')
cur = conn.cursor()
print(cur)
conn.close()

## 4. Creating a table ##

import psycopg2
conn = psycopg2.connect('dbname=dq user=dq')
cur = conn.cursor()
cur.execute('create table notes(id integer primary key, body text, title text);')
conn.close()

## 5. SQL Transactions ##

import psycopg2
conn = psycopg2.connect('dbname=dq user=dq')
cur = conn.cursor()
cur.execute('create table notes(iq integer primary key, body text, title text);')
conn.commit()
conn.close()

## 6. Autocommitting ##

import psycopg2
conn = psycopg2.connect('dbname=dq user=dq')
conn.autocommit = True
cur = conn.cursor()
cur.execute('create table facts(id integer primary key, country text, value integer);')
conn.close()

## 7. Executing queries ##

import psycopg2
conn = psycopg2.connect('dbname=dq user=dq')
conn.autocommit = True
cur = conn.cursor()
cur.execute("insert into notes values (1, 'Do more missions on Dataquest.', 'Dataquest reminder');")
cur.execute('select * from notes;')
rows = cur.fetchall()
print(rows)
conn.close()

## 8. Creating a database ##

import psycopg2
conn = psycopg2.connect('dbname=dq user=dq')
conn.autocommit = True
cur = conn.cursor()
cur.execute('create database income owner dq')
conn.close()

## 9. Deleting a database ##

import psycopg2
conn = psycopg2.connect('dbname=dq user=dq')
conn.autocommit = True
cur = conn.cursor()
cur.execute('drop database income')
conn.close()