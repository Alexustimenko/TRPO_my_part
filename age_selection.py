from imports import tk, font
from window_config import configure_window
from window_manager import switch_window
from play_once import play_on_loading
from play_on_hover import attach_hover_sound

def create_age_window(root):
    from menu_window_creation import create_menu
    from player_selection import create_players_window

    age_window = tk.Toplevel(root)  # Создание нового окна
    play_on_loading("F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\howoldareyou.mp3")
    configure_window(age_window)  # Настройка окна

    age_font = font.Font(family='Helvetica', size=40, weight='bold')
    button_font = font.Font(family="Helvetica", size=25, weight="bold")

    # Заголовок
    age_label = tk.Label(age_window, text="Сколько тебе лет?", font=age_font, bg="#BDFCC9")
    age_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    # Кнопка "3-5 лет"
    left_button = tk.Button(age_window, text="3-5 лет", font=button_font, bg="#FFC107", width=15, height=3,
                            command=lambda: switch_window(age_window,create_players_window,root))
    left_button.place(relx=0.25, rely=0.5, anchor='center')

    # Кнопка "6-8 лет"
    right_button = tk.Button(age_window, text="6-8 лет", font=button_font, bg="#FFC107", width=15, height=3)
    right_button.place(relx=0.75, rely=0.5, anchor='center')

    # Кнопка "Главное меню"
    main_menu_button = tk.Button(age_window, text="Главное меню", font=button_font, bg="#FFC107", width=20, height=3,
                                 command=lambda: switch_window(age_window, create_menu, root))
    main_menu_button.place(relx=0.5, rely=0.85, anchor='center')

    attach_hover_sound(main_menu_button,"F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\menu.mp3")


