def switch_window(current_window, new_window_func,root, *args, return_to_menu=True):
    current_window.withdraw()  # Скрываем текущее окно
    new_window_func(root,*args)     # Вызываем новую функцию окна с аргументами
    if return_to_menu:
        root.deiconify()  # Показываем главное меню
