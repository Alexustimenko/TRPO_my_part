from imports import tk, font
from window_config import configure_window
from window_manager import switch_window
from cursor_manager import apply_cursor_to_window
from play_once import play_on_loading
from play_on_hover import attach_hover_sound
from shake_manager import shake_button
from image_loader import load_image_by_name
from logicleveltwo import create_find_mother_window
from winner_animation import create_ball_animation_window

def create_find_extra_image_window(root):
    from menu_window_creation import create_menu

    #Звук при загрузке окна
    play_on_loading("F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\chto_lishnee.mp3")

    # Создание окна
    extra_image_window = tk.Toplevel(root)
    apply_cursor_to_window(extra_image_window)
    configure_window(extra_image_window)

    # Настройки шрифтов
    title_font = font.Font(family="Helvetica", size=40, weight="bold")
    button_font = font.Font(family="Helvetica", size=25, weight="bold")

    # Заголовок
    title_label = tk.Label(extra_image_window, text="Что лишнее", font=title_font, bg="#BDFCC9")
    title_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    # Загрузка изображений для кнопок
    picture_1 = tk.PhotoImage(file="F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\myachikv3.png")
    picture_2 = tk.PhotoImage(file="F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\pir.png")
    picture_3 = tk.PhotoImage(file="F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\kaktusv2.png")
    picture_4 = tk.PhotoImage(file="F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\cubikiv2.png")

    # Кнопки с картинками
    button_1 = tk.Button(extra_image_window, image=picture_1, width=200, height=200, bg="#FFC107",
                         command=lambda: shake_button(button_1))
    button_1.place(relx=0.2, rely=0.6, anchor=tk.CENTER)

    button_2 = tk.Button(extra_image_window, image=picture_2, width=200, height=200, bg="#FFC107",
                         command=lambda: shake_button(button_2))
    button_2.place(relx=0.4, rely=0.6, anchor=tk.CENTER)

    button_3 = tk.Button(extra_image_window, image=picture_3, width=200, height=200, bg="#FFC107",
                         command=lambda: create_ball_animation_window(root,create_find_mother_window))
    button_3.place(relx=0.6, rely=0.6, anchor=tk.CENTER)

    button_4 = tk.Button(extra_image_window, image=picture_4, width=200, height=200, bg="#FFC107",
                         command=lambda: shake_button(button_4))
    button_4.place(relx=0.8, rely=0.6, anchor=tk.CENTER)

    # Добавление звуков при наведении на кнопки
    attach_hover_sound(button_1, "F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\myachik.mp3")
    attach_hover_sound(button_2, "F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\piramidka.mp3")
    attach_hover_sound(button_3, "F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\kaktus.mp3")
    attach_hover_sound(button_4, "F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\cubiki.mp3")

    # Кнопка "Главное меню"
    menu_button = tk.Button(extra_image_window, text="Главное меню", font=button_font, bg="#FFC107",
                            command=lambda: switch_window(extra_image_window, create_menu, root))
    menu_button.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

    # Звук при наведении на кнопку "Главное меню"
    attach_hover_sound(menu_button, "F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\menumale.mp3")

    # Сохранение ссылок на изображения, чтобы они отображались
    extra_image_window.picture_1 = picture_1
    extra_image_window.picture_2 = picture_2
    extra_image_window.picture_3 = picture_3
    extra_image_window.picture_4 = picture_4

    # Применение курсора
    apply_cursor_to_window(extra_image_window)
