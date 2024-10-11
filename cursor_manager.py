# cursor_manager.py
from imports import os
from cursor_loader import load_image_by_name
current_cursor_image = None

def set_cursor_by_name(root, name):
    global current_cursor_image

    cursor_image = load_image_by_name(name)

    if cursor_image:
        current_cursor_image = cursor_image
        root.config(cursor="@" + cursor_image)
    else:
        print(f"Не удалось загрузить курсор с именем '{name}'")

def apply_cursor_to_window(window):
    global current_cursor_image

    if current_cursor_image:
        window.config(cursor="@" + current_cursor_image)
    else:
        print("Курсор не установлен. Используется стандартный.")