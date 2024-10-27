from imports import tk, font
from window_config import configure_window
from window_manager import switch_window
from cursor_manager import apply_cursor_to_window
from play_on_click import play_sound_on_click
from play_once import play_on_loading
from play_on_hover import attach_hover_sound
from image_loader import load_image_by_name
from shake_manager import shake_button
from winner_categories import create_ball_animation_window_for_categories

def create_continue_phrase_window(root):
    from menu_window_creation import create_menu


    play_on_loading("F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\nashatanya.mp3")

    phrase_window = tk.Toplevel(root)
    apply_cursor_to_window(phrase_window)
    configure_window(phrase_window)

    title_font = font.Font(family="Helvetica", size=30, weight="bold")
    button_font = font.Font(family="Helvetica", size=25, weight="bold")


    title_label = tk.Label(phrase_window, text="Продолжи фразу: Наша Таня громко плачет, уронила в речку...", font=title_font, bg="#BDFCC9")
    title_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)


    option_image1 = tk.PhotoImage(file="F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\zhiraf.png")
    option_image2 = tk.PhotoImage(file="F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\elochka.png")
    option_image3 = tk.PhotoImage(file="F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\myachikv3.png")
    option_image4 = tk.PhotoImage(file="F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\chainik.png")
    dinamik_image = tk.PhotoImage(file="F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\dinamikspeaking.png")


    option_button1 = tk.Button(phrase_window, image=option_image1, bg="#FFC107", command=lambda:shake_button(option_button1))
    option_button2 = tk.Button(phrase_window, image=option_image2, bg="#FFC107", command=lambda:shake_button(option_button2))
    option_button3 = tk.Button(phrase_window, image=option_image3, bg="#FFC107", command=lambda: create_ball_animation_window_for_categories(root))
    option_button4 = tk.Button(phrase_window, image=option_image4, bg="#FFC107", command=lambda:shake_button(option_button4))


    option_button1.place(relx=0.2, rely=0.4, anchor=tk.CENTER)
    option_button2.place(relx=0.4, rely=0.4, anchor=tk.CENTER)
    option_button3.place(relx=0.6, rely=0.4, anchor=tk.CENTER)
    option_button4.place(relx=0.8, rely=0.4, anchor=tk.CENTER)


    sound_button1 = tk.Button(phrase_window, image=dinamik_image, bg="#FFC107", command=lambda: play_sound_on_click("F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\zhiraf.mp3"))
    sound_button2 = tk.Button(phrase_window,image=dinamik_image, bg="#FFC107", command=lambda: play_sound_on_click("F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\elochka.mp3"))
    sound_button3 = tk.Button(phrase_window,image=dinamik_image, bg="#FFC107", command=lambda: play_sound_on_click("F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\myachik.mp3"))
    sound_button4 = tk.Button(phrase_window,image=dinamik_image, bg="#FFC107", command=lambda: play_sound_on_click("F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\chainik.mp3"))


    sound_button1.place(relx=0.2, rely=0.65, anchor=tk.CENTER)
    sound_button2.place(relx=0.4, rely=0.65, anchor=tk.CENTER)
    sound_button3.place(relx=0.6, rely=0.65, anchor=tk.CENTER)
    sound_button4.place(relx=0.8, rely=0.65, anchor=tk.CENTER)


    menu_button = tk.Button(phrase_window, text="Главное меню", font=button_font, bg="#FFC107",
                            command=lambda: switch_window(phrase_window, create_menu, root))
    menu_button.place(relx=0.5, rely=0.85, anchor=tk.CENTER)


    attach_hover_sound(menu_button, "F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\menumale.mp3")


    phrase_window.option_image1 = option_image1
    phrase_window.option_image2 = option_image2
    phrase_window.option_image3 = option_image3
    phrase_window.option_image4 = option_image4
    phrase_window.dinamik_image = dinamik_image

    apply_cursor_to_window(phrase_window)
