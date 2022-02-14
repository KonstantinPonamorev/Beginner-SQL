import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('postgresql://postgres:postgre@localhost:5432/postgres')
connection = engine.connect()

select_album_2018 = connection.execute("""
    SELECT title, release_date FROM album
    WHERE release_date = 2018;
    """).fetchall()

select_longest_track = connection.execute("""
    SELECT track_name, duration_sec FROM track
    ORDER BY duration_sec DESC;
    """).fetchone()

select_tracks_longer_210 = connection.execute("""
    SELECT track_name FROM track
    WHERE duration_sec >= 210;
    """).fetchall()

select_compilations_2018_2020 = connection.execute("""
    SELECT compilation_name FROM compilation
    WHERE release_date BETWEEN 2018 and 2020;
    """).fetchall()

select_onewordname_artists = connection.execute("""
    SELECT name FROM artist
    WHERE name NOT LIKE '%% %%';
    """).fetchall()

select_word_tracks = connection.execute("""
    SELECT track_name FROM track
    WHERE track_name iLIKE '%%my%%';
    """).fetchall()

# pprint(select_album_2018)
# pprint(select_longest_track)
# pprint(select_tracks_longer_210)
# pprint(select_compilations_2018_2020)
# pprint(select_onewordname_artists)
# pprint(select_word_tracks)