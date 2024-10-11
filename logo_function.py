from imports import tk,font
from window_config import configure_window
from cat_animation import animate_cat
from menu_switcher import transition_to_menu
from play_once import play_on_loading
def create_logo(root):
    configure_window(root)
    custom_font = font.Font(family='Brush Script MT',size=140,weight='bold')
    play_on_loading("F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\hello.mp3")
    label = tk.Label(root,text="Alex's PlayLab",font=custom_font,bg="#BDFCC9")
    label.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

    animate_cat(root)
    transition_to_menu(root)

