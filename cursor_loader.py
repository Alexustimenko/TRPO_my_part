from imports import sqlite3, io

def load_image_by_name(name):
    # Подключаемся к базе данных
    conn = sqlite3.connect('game_images.db')
    cursor = conn.cursor()

    try:
        # Выполняем запрос для получения курсора по имени
        cursor.execute('SELECT image FROM images WHERE name = ?', (name,))
        result = cursor.fetchone()

        if result is not None:
            # Преобразуем BLOB данные в файл курсора
            cur_data = result[0]
            cursor_path = f"{name}.cur"  # Название временного файла

            # Сохраняем файл .cur на диск
            with open(cursor_path, "wb") as cur_file:
                cur_file.write(cur_data)

            # Возвращаем путь к файлу .cur
            return cursor_path
        else:
            print(f"Курсор с именем '{name}' не найден в базе данных.")
            return None
    finally:
        # Закрываем соединение
        conn.close()
