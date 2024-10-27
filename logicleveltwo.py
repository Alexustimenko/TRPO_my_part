from imports import tk, font
from window_config import configure_window
from window_manager import switch_window
from cursor_manager import apply_cursor_to_window
from play_once import play_on_loading
from play_on_hover import attach_hover_sound
from shake_manager import shake_button
from image_loader import load_image_by_name
from winner_categories import create_ball_animation_window_for_categories

def create_find_mother_window(root):
    from menu_window_creation import create_menu

    play_on_loading("F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\naidimamu.mp3")

    mother_window = tk.Toplevel(root)
    apply_cursor_to_window(mother_window)
    configure_window(mother_window)

    title_font = font.Font(family="Helvetica", size=40, weight="bold")
    button_font = font.Font(family="Helvetica", size=25, weight="bold")

    title_label = tk.Label(mother_window, text="Найди маму для малыша", font=title_font, bg="#BDFCC9")
    title_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    baby_image = tk.PhotoImage(file="F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\ciplenok.png")
    baby_label = tk.Label(mother_window, image=baby_image, bg="#BDFCC9")
    baby_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    korova_picture = tk.PhotoImage(file="F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\korovalogic.png")
    kot_picture = tk.PhotoImage(file="F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\kotiklogic.png")
    slon_picture = tk.PhotoImage(file="F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\slonv2.png")
    kurica_picture = tk.PhotoImage(file="F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\kuricav7.png")

    lion_button = tk.Button(mother_window, image=korova_picture, width=200, height=200, bg="#FFC107", command=lambda: shake_button(lion_button))
    lion_button.place(relx=0.2, rely=0.6, anchor=tk.CENTER)

    elephant_button = tk.Button(mother_window, image=kot_picture, width=200, height=200, bg="#FFC107", command=lambda: shake_button(elephant_button))
    elephant_button.place(relx=0.4, rely=0.6, anchor=tk.CENTER)

    bird_button = tk.Button(mother_window, image=slon_picture, width=200, height=200, bg="#FFC107", command=lambda: shake_button(bird_button))
    bird_button.place(relx=0.6, rely=0.6, anchor=tk.CENTER)

    cat_button = tk.Button(mother_window, image=kurica_picture, width=200, height=200, bg="#FFC107", command=lambda: create_ball_animation_window_for_categories(root))
    cat_button.place(relx=0.8, rely=0.6, anchor=tk.CENTER)

    attach_hover_sound(lion_button, "F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\korovamale.mp3")
    attach_hover_sound(elephant_button, "F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\kotmale.mp3")
    attach_hover_sound(bird_button, "F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\slonmale.mp3")
    attach_hover_sound(cat_button, "F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\kuricamale.mp3")

    menu_button = tk.Button(mother_window, text="Главное меню", font=button_font, bg="#FFC107", command=lambda: switch_window(mother_window, create_menu, root))
    menu_button.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

    attach_hover_sound(menu_button, "F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\menumale.mp3")

    mother_window.baby_image = baby_image
    mother_window.korova_picture = korova_picture
    mother_window.kot_picture = kot_picture
    mother_window.slon_picture = slon_picture
    mother_window.kurica_picture = kurica_picture

    apply_cursor_to_window(mother_window)
