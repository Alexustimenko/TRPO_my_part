from imports import tk, font
from window_config import configure_window
from window_manager import switch_window
from cursor_manager import apply_cursor_to_window
from play_on_click import play_sound_on_click
from play_once import play_on_loading
from play_on_hover import attach_hover_sound
from image_loader import load_image_by_name
from shake_manager import shake_button
from winner_animation import create_ball_animation_window
from speaking_leveL_two import create_continue_phrase_window

def create_listen_and_choose_window(root):
    from menu_window_creation import create_menu

    # Воспроизведение звука при загрузке окна
    play_on_loading("F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\listen_and_choose.mp3")

    listen_window = tk.Toplevel(root)
    apply_cursor_to_window(listen_window)
    configure_window(listen_window)

    title_font = font.Font(family="Helvetica", size=40, weight="bold")
    button_font = font.Font(family="Helvetica", size=25, weight="bold")


    title_label = tk.Label(listen_window, text="Послушай внимательно слова и скажи, какое длиннее", font=title_font, bg="#BDFCC9")
    title_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)


    word_image1 = tk.PhotoImage(file="F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\lisa2.png")
    word_image2 = tk.PhotoImage(file="F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\zayac.png")
    dinamik_image = tk.PhotoImage(file="F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\dinamikspeaking.png")


    word_button1 = tk.Button(listen_window, image=word_image1, bg="#FFC107", command=lambda:shake_button(word_button1))
    word_button2 = tk.Button(listen_window, image=word_image2, bg="#FFC107", command=lambda:create_ball_animation_window(root,create_continue_phrase_window))
    word_button1.place(relx=0.35, rely=0.5, anchor=tk.CENTER)
    word_button2.place(relx=0.65, rely=0.5, anchor=tk.CENTER)


    sound_button1 = tk.Button(listen_window,image=dinamik_image,bg="#FFC107", command=lambda: play_sound_on_click("F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\hvost.mp3"))
    sound_button2 = tk.Button(listen_window,image=dinamik_image, bg="#FFC107", command=lambda: play_sound_on_click("F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\hvostik.mp3"))
    sound_button1.place(relx=0.35, rely=0.7, anchor=tk.CENTER)
    sound_button2.place(relx=0.65, rely=0.7, anchor=tk.CENTER)


    menu_button = tk.Button(listen_window, text="Главное меню", font=button_font, bg="#FFC107",
                            command=lambda: switch_window(listen_window, create_menu, root))
    menu_button.place(relx=0.5, rely=0.85, anchor=tk.CENTER)


    attach_hover_sound(menu_button, "F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\menu.mp3")


    listen_window.word_image1 = word_image1
    listen_window.word_image2 = word_image2
    listen_window.dinamik_image=dinamik_image

    apply_cursor_to_window(listen_window)
