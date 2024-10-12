import sqlite3
def insert_image(name, image_path):
    cursor.execute('SELECT id FROM images WHERE name = ?', (name,))
    result = cursor.fetchone()
    if result is None:
        with open(image_path,'rb') as file:
            img_blob = file.read()
        cursor.execute('INSERT INTO images (name, image) VALUES (?, ?)', (name,img_blob))
        conn.commit()
        print(f"Изображение '{name}' добавлено.")
    else:
        print(f"Изображение '{name}' уже существует в базе данных.")
conn = sqlite3.connect('game_images.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    image BLOB NOT NULL
)
""")
insert_image('lvenok','E:\\!MyPython\\Razvivushka\\images\\lvenok.png')
insert_image('rybka','E:\\!MyPython\\Razvivushka\\images\\rybka.png')
insert_image('mishka','E:\\!MyPython\\Razvivushka\\images\\mishka.png')
insert_image('kot','E:\\!MyPython\\Razvivushka\\images\\kot.png')
insert_image('dinamik','F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\dinamik.png')
insert_image('dinamik1','F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\dinamik1.png')
insert_image('ezik','F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\ezik.png')
insert_image('fish_cur','F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\result_rybka_cursor.cur')
insert_image('ezik_cur','F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\result_ezik_cursor_1.cur')
insert_image('bear_cur','F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\result_bear_cursor_1.cur')
insert_image('cursor_fish','F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\free-icon-goldfish-6789575-_1_.cur')
insert_image('fish111','F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\fish111.cur')
insert_image('ez111','F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\ez.cur')
insert_image('korova','F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\korova.png')
insert_image('kot_around_the_world1','F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\kotikv7.png')
conn.close()