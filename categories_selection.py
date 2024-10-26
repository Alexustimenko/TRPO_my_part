from imports import tk, font
from window_config import configure_window
from window_manager import switch_window
from cursor_manager import apply_cursor_to_window
def create_category_window(root):
    from menu_window_creation import create_menu
    from around_world_level_one import create_who_is_bigger
    from attention_level_one import create_find_extra_image_window
    from vnimanie_level_one import create_vnimanie_one
    from mathlevelone import create_count_cubes_window
    from speaking_level_one import create_listen_and_choose_window
    category_window = tk.Toplevel(root)
    apply_cursor_to_window(category_window)
    configure_window(category_window)

    title_font = font.Font(family="Helvetica",size=40,weight="bold")
    button_font = font.Font(family="Helvetica",size=25,weight="bold")

    title_label = tk.Label(category_window,text="Выбери категорию",font=title_font,bg="#BDFCC9")
    title_label.place(relx=0.5,rely=0.2,anchor=tk.CENTER)

    cat1_button = tk.Button(category_window,text="Математика",font=button_font,bg="#FFC107",width=20,height=3,
                            command=lambda: switch_window(category_window,create_count_cubes_window,root))
    cat1_button.place(relx=0.2,rely=0.5,anchor='center')

    cat2_button = tk.Button(category_window,text="Логика",font=button_font,bg="#FFC107",width=20,height=3,
                            command=lambda: switch_window(category_window,create_find_extra_image_window,root))
    cat2_button.place(relx=0.4,rely=0.5,anchor='center')

    cat3_button = tk.Button(category_window,text="Внимание",font=button_font,bg="#FFC107",width=20,height=3,
                            command=lambda: switch_window(category_window,create_vnimanie_one,root))
    cat3_button.place(relx=0.6,rely=0.5,anchor='center')

    cat4_button = tk.Button(category_window,text="Развитие речи",font=button_font,bg="#FFC107",width=20,height=3,
                            command=lambda:switch_window(category_window,create_listen_and_choose_window,root))
    cat4_button.place(relx=0.8,rely=0.5,anchor='center')

    cat5_button = tk.Button(category_window,text="Окружающий мир",font=button_font,bg="#FFC107",width=20,height=3,
                            command=lambda: switch_window(category_window,create_who_is_bigger,root))
    cat5_button.place(relx=0.5,rely=0.7,anchor='center')

    menu_button = tk.Button(category_window,text="Главное меню",font=button_font,bg="#FFC107",width=20,height=3,
                            command=lambda: switch_window(category_window,create_menu,root))
    menu_button.place(relx=0.5,rely=0.85,anchor='center')

    apply_cursor_to_window(category_window)