from imports import sqlite3,Image,ImageTk,io

def load_image_by_name(name):
    # Подключаемся к базе данных
    conn = sqlite3.connect('game_images.db')
    cursor = conn.cursor()

    # Выполняем запрос для получения изображения по имени
    cursor.execute('SELECT image FROM images WHERE name = ?', (name,))
    result = cursor.fetchone()

    if result is not None:
        # Преобразуем BLOB данные в изображение
        img_data = result[0]
        image = Image.open(io.BytesIO(img_data))
        return ImageTk.PhotoImage(image)
    else:
        print(f"Изображение с именем '{name}' не найдено в базе данных.")
        return None

    # Закрываем соединение
    conn.close()