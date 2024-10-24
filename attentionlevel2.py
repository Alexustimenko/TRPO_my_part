from imports import tk, font
from window_config import configure_window
from window_manager import switch_window
from cursor_manager import apply_cursor_to_window
from play_once import play_on_loading
from play_on_hover import attach_hover_sound
from shake_manager import shake_button
from image_loader import load_image_by_name
import time
from winner_categories import create_ball_animation_window_for_categories

def create_remember_picture_window(root):
    from menu_window_creation import create_menu

    play_on_loading("F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\remember_picture.mp3")

    picture_window = tk.Toplevel(root)
    apply_cursor_to_window(picture_window)
    configure_window(picture_window)

    title_font = font.Font(family="Helvetica", size=40, weight="bold")
    button_font = font.Font(family="Helvetica", size=25, weight="bold")

    title_label = tk.Label(picture_window, text="Запомни картинку и найди ее", font=title_font, bg="#BDFCC9")
    title_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    picture_image = tk.PhotoImage(file="F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\babochka.png")
    picture_label = tk.Label(picture_window, image=picture_image, bg="#BDFCC9")
    picture_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)


    picture_window.after(5000, picture_label.place_forget)


    option1_image = tk.PhotoImage(file="F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\babochkav2.png")
    option2_image = tk.PhotoImage(file="F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\babochkav33.png")
    option3_image = tk.PhotoImage(file="F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\babochka.png")
    option4_image = tk.PhotoImage(file="F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\babochkav4.png")


    option1_button = tk.Button(picture_window, image=option1_image, width=200, height=200, bg="#FFC107", command=lambda: shake_button(option1_button))
    option2_button = tk.Button(picture_window, image=option2_image, width=200, height=200, bg="#FFC107", command=lambda: shake_button(option2_button))
    option3_button = tk.Button(picture_window, image=option3_image, width=200, height=200, bg="#FFC107", command=lambda: create_ball_animation_window_for_categories(root))
    option4_button = tk.Button(picture_window, image=option4_image, width=200, height=200, bg="#FFC107", command=lambda: shake_button(option4_button))


    def show_buttons():
        option1_button.place(relx=0.2, rely=0.6, anchor=tk.CENTER)
        option2_button.place(relx=0.4, rely=0.6, anchor=tk.CENTER)
        option3_button.place(relx=0.6, rely=0.6, anchor=tk.CENTER)
        option4_button.place(relx=0.8, rely=0.6, anchor=tk.CENTER)

    picture_window.after(5000, show_buttons)


    # attach_hover_sound(option1_button, "F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\option1.mp3")
    # attach_hover_sound(option2_button, "F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\option2.mp3")
    # attach_hover_sound(option3_button, "F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\option3.mp3")
    # attach_hover_sound(option4_button, "F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\option4.mp3")

    menu_button = tk.Button(picture_window, text="Главное меню", font=button_font, bg="#FFC107", command=lambda: switch_window(picture_window, create_menu, root))
    menu_button.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

    attach_hover_sound(menu_button, "F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\menu.mp3")

    picture_window.picture_image = picture_image
    picture_window.option1_image = option1_image
    picture_window.option2_image = option2_image
    picture_window.option3_image = option3_image
    picture_window.option4_image = option4_image

    apply_cursor_to_window(picture_window)
