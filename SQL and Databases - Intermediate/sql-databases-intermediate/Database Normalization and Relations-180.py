## 4. Querying a normalized database ##

query = 'select ceremonies.year, nominations.movie from nominations inner join ceremonies on nominations.ceremony_id == ceremonies.id where nominations.nominee == "Natalie Portman";'
portman_movies = conn.execute(query).fetchall()
print(portman_movies)
conn.close();

## 6. Join table ##

five_join_table = conn.execute('select * from movies_actors limit 5;').fetchall()
five_actors = conn.execute('select * from actors limit 5;').fetchall()
five_movies = conn.execute('select * from movies limit 5;').fetchall()
print(five_join_table, five_actors, five_movies)
conn.close();

## 7. Querying a many-to-many relation ##

query = 'select actors.actor, movies.movie from movies inner join movies_actors on movies.id == movies_actors.movie_id inner join actors on movies_actors.actor_id == actors.id where movies.movie == "The King\'s Speech"'
kings_actors = conn.execute(query).fetchall()
print(kings_actors)
conn.close()

## 8. Practice: querying a many-to-many relation ##

query = 'select movies.movie, actors.actor from actors inner join movies_actors on actors.id == movies_actors.actor_id inner join movies on movies_actors.movie_id == movies.id where actors.actor == "Natalie Portman"'
portman_joins = conn.execute(query).fetchall()
print(portman_joins)
conn.close()