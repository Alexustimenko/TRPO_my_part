from imports import tk,font
from window_config import configure_window
from window_manager import switch_window
from cursor_manager import apply_cursor_to_window
from play_once import play_on_loading
from play_on_hover import attach_hover_sound
from image_loader import load_image_by_name
from shake_manager import shake_button
from  winner_animation import create_ball_animation_window
from around_the_world_level_two import  create_dog_house_window
def create_who_is_bigger(root):
    from menu_window_creation import create_menu

    play_on_loading("F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\whohavier.mp3")

    bigger_window = tk.Toplevel(root)
    apply_cursor_to_window(bigger_window)
    configure_window(bigger_window)

    title_font = font.Font(family="Helvetica",size=40,weight="bold")
    button_font = font.Font(family="Helvetica", size=25, weight="bold")

    title_label = tk.Label(bigger_window,text='Кто тяжелее?',font=title_font,bg="#BDFCC9")
    title_label.place(relx=0.5,rely=0.1,anchor=tk.CENTER)

    cow_image = load_image_by_name('korova')
    kotik_image = load_image_by_name('kot_around_the_world1')

    cow_button = tk.Button(bigger_window, image=cow_image, width=400, height=400,bg="#FFC107",command=lambda: create_ball_animation_window(root,create_dog_house_window))
    cow_button.place(relx=0.3, rely=0.5, anchor='center')

    kotik_button = tk.Button(bigger_window, image=kotik_image, width=400, height=400,bg="#FFC107",command=lambda: shake_button(kotik_button))
    kotik_button.place(relx=0.7, rely=0.5, anchor='center')

    attach_hover_sound(cow_button,"F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\korova.mp3")
    attach_hover_sound(kotik_button,"F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\kot.mp3")
    menu_button = tk.Button(bigger_window, text="Главное меню", font=button_font, bg="#FFC107", width=20, height=3,
                            command=lambda: switch_window(bigger_window, create_menu, root))
    menu_button.place(relx=0.5, rely=0.85, anchor='center')

    attach_hover_sound(menu_button,"F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\menu.mp3")

    bigger_window.cow_image = cow_image
    bigger_window.kotik_image = kotik_image

    apply_cursor_to_window(bigger_window)