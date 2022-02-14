import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('postgresql://postgres:postgre@localhost:5432/postgres')
connection = engine.connect()

# connection.execute("""DELETE FROM artist""")

# connection.execute("""
#     INSERT INTO artist
#     VALUES(1, 'Bill Murrey');
#     INSERT INTO artist
#     VALUES(2, 'Joe Crossby');
#     INSERT INTO artist
#     VALUES(3, 'Monica Belucci');
#     INSERT INTO artist
#     VALUES(4, 'Eddie Murphy');
#     INSERT INTO artist
#     VALUES(5, 'Oleg Bulygin');
#     INSERT INTO artist
#     VALUES(6, 'Constantine Ponamorev');
#     INSERT INTO artist
#     VALUES(7, 'Mega Artist');
#     INSERT INTO artist
#     VALUES(8, 'Whoare You');
#     """)

sel = connection.execute("""
    SELECT * FROM artist;
    """).fetchall()

pprint(sel)