# Generated by Django 4.2 on 2023-10-30 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL("""
            INSERT INTO music_artist (name)
            VALUES ('Soda Stereo');
                          
            INSERT INTO music_artist (name)
            VALUES ('The Police');            

            insert INTO music_album (name, release, artist_id)
            values ('Soda Stereo', 1984, (select id from music_artist where name = 'Soda Stereo'));

            insert INTO music_album (name, release, artist_id)
            values ('Nada Personal', 1984, (select id from music_artist where name = 'Soda Stereo'));

            insert INTO music_album (name, release, artist_id)
            values ('Signos', 1986, (select id from music_artist where name = 'Soda Stereo'));

            insert INTO music_album (name, release, artist_id)
            values ('Ruido Blanco', 1987, (select id from music_artist where name = 'Soda Stereo'));

            insert INTO music_album (name, release, artist_id)
            values ("Outlandos d'Amour", 1978, (select id from music_artist where name = 'The Police'));
                          
            insert INTO music_album (name, release, artist_id)
            values ('Reggatta de Blanc ', 1979, (select id from music_artist where name = 'The Police'));

            insert INTO music_album (name, release, artist_id)
            values ('Zenyatta Mondatta ', 1980, (select id from music_artist where name = 'The Police'));

            insert INTO music_album (name, release, artist_id)
            values ('Ghost in the Machine', 1981, (select id from music_artist where name = 'The Police'));

            insert INTO music_album (name, release, artist_id)
            values ('Synchronicity', 1983, (select id from music_artist where name = 'The Police'));
        """)
    ]