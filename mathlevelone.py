from imports import tk, font
from window_config import configure_window
from window_manager import switch_window
from cursor_manager import apply_cursor_to_window
from play_once import play_on_loading
from play_on_hover import attach_hover_sound
from shake_manager import shake_button
from image_loader import load_image_by_name

def create_count_cubes_window(root):
    from menu_window_creation import create_menu

    play_on_loading("F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\count_cubes.mp3")

    cubes_window = tk.Toplevel(root)
    apply_cursor_to_window(cubes_window)
    configure_window(cubes_window)

    title_font = font.Font(family="Helvetica", size=40, weight="bold")
    button_font = font.Font(family="Helvetica", size=25, weight="bold")


    title_label = tk.Label(cubes_window, text="Сколько кубиков на рисунке?", font=title_font, bg="#BDFCC9")
    title_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)


    cubes_image = tk.PhotoImage(file="F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\cubikmathv2.png")
    cubes_label = tk.Label(cubes_window, image=cubes_image, width=250, height=200, bg="#BDFCC9")
    cubes_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)


    button_1 = tk.Button(cubes_window, text="1", font=button_font, width=10, height=2, bg="#FFC107")
    button_2 = tk.Button(cubes_window, text="2", font=button_font, width=10, height=2, bg="#FFC107")
    button_3 = tk.Button(cubes_window, text="3", font=button_font, width=10, height=2, bg="#FFC107", command=lambda: shake_button(button_3))
    button_4 = tk.Button(cubes_window, text="4", font=button_font, width=10, height=2, bg="#FFC107")


    button_1.place(relx=0.2, rely=0.7, anchor=tk.CENTER)
    button_2.place(relx=0.4, rely=0.7, anchor=tk.CENTER)
    button_3.place(relx=0.6, rely=0.7, anchor=tk.CENTER)
    button_4.place(relx=0.8, rely=0.7, anchor=tk.CENTER)


    # attach_hover_sound(button_1, "F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\option1.mp3")
    # attach_hover_sound(button_2, "F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\option2.mp3")
    # attach_hover_sound(button_3, "F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\option3.mp3")
    # attach_hover_sound(button_4, "F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\option4.mp3")


    menu_button = tk.Button(cubes_window, text="Главное меню", font=button_font, bg="#FFC107", command=lambda: switch_window(cubes_window, create_menu, root))
    menu_button.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

    attach_hover_sound(menu_button, "F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\menu.mp3")


    cubes_window.cubes_image = cubes_image

    apply_cursor_to_window(cubes_window)
