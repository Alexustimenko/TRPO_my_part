from imports import tk,font
from window_config import configure_window
from image_loader import load_image_by_name
from window_manager import switch_window
from cursor_manager import set_cursor_by_name,apply_cursor_to_window
from play_once import play_on_loading
from play_on_hover import attach_hover_sound

def create_players_window(root):
    from menu_window_creation import create_menu
    from categories_selection import create_category_window
    play_on_loading("F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\za_kogo.mp3")
    player_window = tk.Toplevel(root)
    configure_window(player_window)

    title_font = font.Font(family="Helvetica", size=40,weight="bold")
    button_font = font.Font(family="Helvetica",size=25,weight="bold")

    ezik=load_image_by_name("ezik")
    mishka=load_image_by_name("mishka")
    rybka = load_image_by_name("rybka")

    player_window.ezik_image = ezik
    player_window.mishka_image = mishka
    player_window.rybka_image = rybka

    title_label=tk.Label(player_window,text="За кого ты хочешь играть?",font=title_font,bg="#BDFCC9")
    title_label.place(relx=0.5,rely=0.2,anchor=tk.CENTER)

    left_button=tk.Button(player_window,image=ezik,bg="#FFC107",width=150,height=150,
                          command=lambda: [set_cursor_by_name(root, "ez111"),
                                           switch_window(player_window, create_category_window, root)])
    left_button.place(relx=0.25,rely=0.5,anchor='center')

    center_button = tk.Button(player_window,image=mishka,bg="#FFC107",width=150,height=150,
                              command=lambda: [set_cursor_by_name(root, "bear_cur"),
                                               switch_window(player_window, create_category_window, root)])
    center_button.place(relx=0.5,rely=0.5,anchor='center')

    right_button = tk.Button(player_window, image=rybka, bg="#FFC107", width=150, height=150,
                             command=lambda: [set_cursor_by_name(root, "fish111"),
                                              switch_window(player_window, create_category_window, root)])
    right_button.place(relx=0.75, rely=0.5, anchor='center')

    menu_button = tk.Button(player_window,text="Главное меню",font=button_font,bg="#FFC107",width=20,height=3,
                            command=lambda :switch_window(player_window,create_menu,root))
    menu_button.place(relx=0.5,rely=0.85,anchor='center')

    attach_hover_sound(menu_button,"F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\menu.mp3")
    attach_hover_sound(right_button,"F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\rybka.mp3")
    attach_hover_sound(center_button,"F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\misha.mp3")
    attach_hover_sound(left_button,"F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\ezik.mp3")


