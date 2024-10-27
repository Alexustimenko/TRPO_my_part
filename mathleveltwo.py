from imports import tk, font
from window_config import configure_window
from window_manager import switch_window
from cursor_manager import apply_cursor_to_window
from play_once import play_on_loading
from play_on_hover import attach_hover_sound
from shake_manager import shake_button
from image_loader import load_image_by_name
from winner_categories import create_ball_animation_window_for_categories

def create_count_triangles_window(root):
    from menu_window_creation import create_menu

    play_on_loading("F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\triangles.mp3")

    triangles_window = tk.Toplevel(root)
    apply_cursor_to_window(triangles_window)
    configure_window(triangles_window)

    title_font = font.Font(family="Helvetica", size=40, weight="bold")
    button_font = font.Font(family="Helvetica", size=25, weight="bold")


    title_label = tk.Label(triangles_window, text="Посчитай треугольники", font=title_font, bg="#BDFCC9")
    title_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)


    triangle1 = tk.PhotoImage(file="F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\triangle1.png")
    triangle2 = tk.PhotoImage(file="F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\triangle1.png")
    triangle3 = tk.PhotoImage(file="F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\triangle3.png")


    triangle1_label = tk.Label(triangles_window, image=triangle1, bg="#BDFCC9")
    triangle1_label.place(relx=0.25, rely=0.4, anchor=tk.CENTER)


    plus_label = tk.Label(triangles_window, text="+", font=button_font, bg="#BDFCC9")
    plus_label.place(relx=0.35, rely=0.4, anchor=tk.CENTER)


    triangle2_label = tk.Label(triangles_window, image=triangle2, bg="#BDFCC9")
    triangle2_label.place(relx=0.45, rely=0.4, anchor=tk.CENTER)


    equals_label = tk.Label(triangles_window, text="+", font=button_font, bg="#BDFCC9")
    equals_label.place(relx=0.55, rely=0.4, anchor=tk.CENTER)


    triangle3_label = tk.Label(triangles_window, image=triangle3, bg="#BDFCC9")
    triangle3_label.place(relx=0.65, rely=0.4, anchor=tk.CENTER)

    equals_label2 = tk.Label(triangles_window,text="=",font=button_font,bg="#BDFCC9")
    equals_label2.place(relx=0.75,rely=0.4,anchor=tk.CENTER)

    button_1 = tk.Button(triangles_window, text="1", font=button_font, width=10, height=2, bg="#FFC107")
    button_2 = tk.Button(triangles_window, text="2", font=button_font, width=10, height=2, bg="#FFC107")
    button_3 = tk.Button(triangles_window, text="3", font=button_font, width=10, height=2, bg="#FFC107", command=lambda: create_ball_animation_window_for_categories(root))
    button_4 = tk.Button(triangles_window, text="4", font=button_font, width=10, height=2, bg="#FFC107")


    button_1.place(relx=0.2, rely=0.7, anchor=tk.CENTER)
    button_2.place(relx=0.4, rely=0.7, anchor=tk.CENTER)
    button_3.place(relx=0.6, rely=0.7, anchor=tk.CENTER)
    button_4.place(relx=0.8, rely=0.7, anchor=tk.CENTER)


    attach_hover_sound(button_1, "F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\one.mp3")
    attach_hover_sound(button_2, "F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\two.mp3")
    attach_hover_sound(button_3, "F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\three.mp3")
    attach_hover_sound(button_4, "F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\four.mp3")


    menu_button = tk.Button(triangles_window, text="Главное меню", font=button_font, bg="#FFC107",
                            command=lambda: switch_window(triangles_window, create_menu, root))
    menu_button.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

    attach_hover_sound(menu_button, "F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\menu.mp3")


    triangles_window.triangle1 = triangle1
    triangles_window.triangle2 = triangle2
    triangles_window.triangle3 = triangle3

    apply_cursor_to_window(triangles_window)
