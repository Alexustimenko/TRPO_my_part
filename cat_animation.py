from imports import sqlite3, Image, ImageTk, tk, io,time


def animate_cat(root):
    # Извлекаем изображение кота из базы данных .db
    conn = sqlite3.connect('game_images.db')  # Подключение к базе данных
    cursor = conn.cursor()

    # Предполагается, что изображение хранится в поле image_data
    cursor.execute("SELECT image FROM images WHERE name = 'kot'")
    image_data = cursor.fetchone()[0]  # Получаем бинарные данные изображения
    conn.close()

    # Конвертируем бинарные данные в изображение
    image_stream = io.BytesIO(image_data)
    image = Image.open(image_stream)

    # Преобразуем изображение для Tkinter
    cat_image = ImageTk.PhotoImage(image)

    # Создаем метку с изображением
    cat_label = tk.Label(root, image=cat_image, bg='#BDFCC9')
    cat_label.place(relx=0.5, rely=0, anchor=tk.N)

    # Сохраняем ссылку на изображение, чтобы предотвратить его сбор мусора
    cat_label.image = cat_image

    # Анимация падения изображения
    y_position = 0
    while y_position < 1:
        cat_label.place(relx=0.5, rely=y_position, anchor=tk.N)
        y_position += 0.01
        root.update()
        time.sleep(0.03)  # Плавность анимации
    cat_label.destroy()
