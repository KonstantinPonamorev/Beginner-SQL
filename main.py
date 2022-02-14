import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('postgresql://postgres:postgre@localhost:5432/postgres')
connection = engine.connect()

# connection.execute("""DELETE FROM artist""")

connection.execute("""
    INSERT INTO artist
    VALUES(1, 'Bill Murrey');
    INSERT INTO artist
    VALUES(2, 'Joe Crossby');
    INSERT INTO artist
    VALUES(3, 'Monica Belucci');
    INSERT INTO artist
    VALUES(4, 'Eddie Murphy');
    INSERT INTO artist
    VALUES(5, 'Oleg Bulygin');
    INSERT INTO artist
    VALUES(6, 'Constantine Ponamorev');
    INSERT INTO artist
    VALUES(7, 'Mega Artist');
    INSERT INTO artist
    VALUES(8, 'Whoare You');
    """)
connection.execute("""
    INSERT INTO genre (id, genre_name)
    VALUES(1, 'HipHop');
    INSERT INTO genre
    VALUES(2, 'Pop');
    INSERT INTO genre
    VALUES(3, 'Country');
    INSERT INTO genre
    VALUES(4, 'Jazz');
    INSERT INTO genre
    VALUES(5, 'Blues');
    """)
connection.execute("""
    INSERT INTO artist_genre
    VALUES(1, 1);
    INSERT INTO artist_genre
    VALUES(1, 2);
    INSERT INTO artist_genre
    VALUES(1, 4);
    INSERT INTO artist_genre
    VALUES(2, 1);
    INSERT INTO artist_genre
    VALUES(3, 3);
    INSERT INTO artist_genre
    VALUES(3, 5);
    INSERT INTO artist_genre
    VALUES(4, 4);
    INSERT INTO artist_genre
    VALUES(4, 5);
    INSERT INTO artist_genre
    VALUES(5, 1);
    INSERT INTO artist_genre
    VALUES(5, 2);
    INSERT INTO artist_genre
    VALUES(5, 3);
    INSERT INTO artist_genre
    VALUES(5, 4);
    INSERT INTO artist_genre
    VALUES(5, 5);
    INSERT INTO artist_genre
    VALUES(6, 1);
    INSERT INTO artist_genre
    VALUES(6, 2);
    INSERT INTO artist_genre
    VALUES(6, 3);
    INSERT INTO artist_genre
    VALUES(6, 4);
    INSERT INTO artist_genre
    VALUES(6, 5);
    INSERT INTO artist_genre
    VALUES(7, 1);
    INSERT INTO artist_genre
    VALUES(7, 2);
    INSERT INTO artist_genre
    VALUES(7, 3);
    INSERT INTO artist_genre
    VALUES(8, 4);
    INSERT INTO artist_genre
    VALUES(8, 5);
    """)

connection.execute("""
    INSERT INTO album
    VALUES(1, 'If you ask me', 2018);
    INSERT INTO album
    VALUES(2, 'Broforce', 2017);
    INSERT INTO album
    VALUES(3, 'Who is', 2018);
    INSERT INTO album
    VALUES(4, 'Hope', 2022);
    INSERT INTO album
    VALUES(5, 'The best student', 2018);
    INSERT INTO album
    VALUES(6, 'Christian or Chris', 2010);
    INSERT INTO album
    VALUES(7, 'Scales', 2015);
    INSERT INTO album
    VALUES(8, 'My answer will be...', 2018);
    INSERT INTO album
    VALUES(9, 'Last Dance', 2018);
    INSERT INTO album
    VALUES(10, 'Last Dance', 2018);
    """)




# sel = connection.execute("""
#     SELECT * FROM artist;
#     """).fetchall()
#
# pprint(sel)