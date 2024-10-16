from imports import tk,font
from window_config import configure_window
from window_manager import switch_window
from cursor_manager import apply_cursor_to_window
from play_once import play_on_loading
from play_on_hover import attach_hover_sound
from winner_categories import create_ball_animation_window_for_categories
from shake_manager import shake_button
from image_loader import load_image_by_name

def create_dog_house_window(root):
    from menu_window_creation import create_menu

    play_on_loading("F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\choose_house.mp3")

    dog_window = tk.Toplevel(root)
    apply_cursor_to_window(dog_window)
    configure_window(dog_window)

    title_font = font.Font(family="Helvetica",size=40,weight="bold")
    button_font = font.Font(family="Helvetica", size=25, weight="bold")

    title_label=tk.Label(dog_window,text="Выбери домик для собачки",font=title_font,bg="#BDFCC9")
    title_label.place(relx=0.5,rely=0.1,anchor=tk.CENTER)

    dog_image = load_image_by_name('dog')
    dog_label= tk.Label(dog_window,image=dog_image,bg="#BDFCC9")
    dog_label.place(relx=0.5,rely=0.3,anchor=tk.CENTER)

    nest_picture=load_image_by_name('gnezdo')
    nora_picture = load_image_by_name('nora')
    budka_picture = load_image_by_name('budka')
    skvorechnik_picture = load_image_by_name('skvorechnik')

    nest_button = tk.Button(dog_window,image=nest_picture,width=200,height=200,bg="#FFC107",command=lambda:shake_button(nest_button))
    nest_button.place(relx=0.2,rely=0.6,anchor=tk.CENTER)

    nora_button = tk.Button(dog_window, image=nora_picture, width=200, height=200,bg="#FFC107",command=lambda:shake_button(nora_button))
    nora_button.place(relx=0.4, rely=0.6, anchor=tk.CENTER)

    budka_button = tk.Button(dog_window, image=budka_picture, width=200, height=200,bg="#FFC107",
                             command=lambda: create_ball_animation_window_for_categories(root))
    budka_button.place(relx=0.6, rely=0.6, anchor=tk.CENTER)

    skvorechnik_button = tk.Button(dog_window, image=skvorechnik_picture, width=200, height=200,bg="#FFC107",command=lambda:shake_button(skvorechnik_button))
    skvorechnik_button.place(relx=0.8, rely=0.6, anchor=tk.CENTER)

    attach_hover_sound(nest_button,"F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\gnezdo.mp3")
    attach_hover_sound(nora_button, "F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\nora.mp3")
    attach_hover_sound(budka_button, "F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\budka.mp3")
    attach_hover_sound(skvorechnik_button, "F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\skvorechnik.mp3")

    menu_button = tk.Button(dog_window,text="Главное меню",font=button_font,bg="#FFC107",
                            command=lambda: switch_window(dog_window,create_menu,root))
    menu_button.place(relx=0.5,rely=0.85,anchor=tk.CENTER)

    attach_hover_sound(menu_button,"F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\menu.mp3")

    dog_window.dog_image=dog_image
    dog_window.nest_picture=nest_picture
    dog_window.nora_picture=nora_picture
    dog_window.budka_picture=budka_picture
    dog_window.skvorechnik_picture=skvorechnik_picture

    apply_cursor_to_window(dog_window)


