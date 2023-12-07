import sqlite3 
conn = sqlite3.connect('imagesdatabase.db') 
c = conn.cursor()

def table_exists(table_name): 
    c.execute('''SELECT count(name) FROM sqlite_master WHERE TYPE = 'table' AND name = '{}' '''.format(table_name)) 
    if c.fetchone()[0] == 1: 
        return True 
    return False

def insert_movie(movie_id, name, release_year, genre, rating): 
    c.execute(''' INSERT INTO movies (movie_id, name, release_year, genre, rating) VALUES(?, ?, ?, ?, ?) ''', (movie_id, name, release_year, genre, rating)) 
    conn.commit()

def get_movies(): 
    c.execute('''SELECT * FROM movies''') 
    data = [] 
    for row in c.fetchall(): 
        data.append(row) 
    return data

if not table_exists('movies'): 
    c.execute(''' 
        CREATE TABLE `images` (
                        `id` int(9) unsigned NOT NULL AUTO_INCREMENT,
                        `image_id` int(11) NOT NULL,
                        `author` varchar(255) NOT NULL,
                        `width` int(9) unsigned NOT NULL,
                        `height` int(11) NOT NULL,
                        `folder_slug` int(11) NOT NULL,
                        `created_on` timestamp NOT NULL DEFAULT current_timestamp(),
                        PRIMARY KEY (`id`)
                        ) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci; 
                            ''')

insert_movie(1, 'Titanic', 1997, 'Drama', 7.8) 


print(get_movies())