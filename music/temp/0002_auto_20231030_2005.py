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

            insert INTO music_album (name, release, image_url, artist_id)
            values ('Soda Stereo', 1984, 
                          'https://rovimusic.rovicorp.com/image.jpg?c=oTnTYy3Ag9pqtuakmZWcr5hUoDg0hsvx4F4sL4oO-nA=&f=6', 
                          (select id from music_artist where name = 'Soda Stereo'));

            insert INTO music_album (name, release, image_url, artist_id)
            values ('Nada Personal', 1984, 
                          'https://rovimusic.rovicorp.com/image.jpg?c=Ts-P9CaR0PxpLKVRqnTOLd_M69_UI9rrJSVvWL2-yAg=&f=5', 
                          (select id from music_artist where name = 'Soda Stereo'));

            insert INTO music_album (name, release, image_url, artist_id)
            values ('Signos', 1986, 
                          'https://rovimusic.rovicorp.com/image.jpg?c=n-MQmuZMpp__n6e6s6VeHphUoDg0hsvx4F4sL4oO-nA=&f=5', 
                          (select id from music_artist where name = 'Soda Stereo'));

            insert INTO music_album (name, release, image_url, artist_id)
            values ('Doble Vida', 1988, 
                          'https://cdn-s3.allmusic.com/release-covers/500/0001/066/0001066345.jpg', 
                          (select id from music_artist where name = 'Soda Stereo'));

            insert INTO music_album (name, release, image_url, artist_id)
            values ("Outlandos d'Amour", 1978, 
                          'https://rovimusic.rovicorp.com/image.jpg?c=a2HKH2QHmQRjdZLExFGPQ9_M69_UI9rrJSVvWL2-yAg=&f=5', 
                          (select id from music_artist where name = 'The Police'));
                          
            insert INTO music_album (name, release, image_url, artist_id)
            values ('Reggatta de Blanc ', 1979, 
                          'https://rovimusic.rovicorp.com/image.jpg?c=nEIqZKEmuwm4bsw8c7TfygSijaXJlYnq0St31qpAJWo=&f=5', 
                          (select id from music_artist where name = 'The Police'));

            insert INTO music_album (name, release, image_url, artist_id)
            values ('Zenyatta Mondatta ', 1980, 
                          'https://rovimusic.rovicorp.com/image.jpg?c=BTPrfKn-2ibhdEvNXgW7PoAf7E_1E-2MlBBPmPAXRBU=&f=5', 
                          (select id from music_artist where name = 'The Police'));

            insert INTO music_album (name, release, image_url, artist_id)
            values ('Ghost in the Machine', 1981, 
                          'https://rovimusic.rovicorp.com/image.jpg?c=-9twTs7DSYpmeLBDBy8oBSpQg_7iAU1wjqLgK_xGXts=&f=6', 
                          (select id from music_artist where name = 'The Police'));

            insert INTO music_album (name, release, image_url, artist_id)
            values ('Synchronicity', 1983, 
                          'https://rovimusic.rovicorp.com/image.jpg?c=vpZCOXKLYWwxMcYl0wXGzwSijaXJlYnq0St31qpAJWo=&f=5', 
                          (select id from music_artist where name = 'The Police'));
        """)
    ]
