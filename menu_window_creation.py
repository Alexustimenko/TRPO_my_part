from imports import font,Tk,Button,Canvas
from window_config import configure_window
from image_utils import create_round_image
from music_button_image_switcher import image_switcher
from window_manager import switch_window
from age_selection import create_age_window
from play_on_hover import attach_hover_sound
def create_menu(root):
    for widget in root.winfo_children():
        widget.destroy()
    configure_window(root)
    button_font = font.Font(family="Helvetica",size=25,weight="bold")
    play_button = Button(root, text="Играть", font=button_font, bg="#FFC107",
                         command=lambda: switch_window(root, create_age_window, root), width=30, height=4)
    play_button.place(relx=0.5, rely=0.4, anchor='center')

    exit_button = Button(root,text="Выход", font=button_font,bg="#FFC107",command=root.quit,width=30,height=4)
    exit_button.place(relx=0.5,rely=0.7,anchor='center')

    attach_hover_sound(play_button,"F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\play.mp3")
    attach_hover_sound(exit_button,"F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\exit.mp3")

    music_image = create_round_image('dinamik1')
    second_music = create_round_image('dinamik')

    settings_button = Button(root,image=music_image,bg="#BDFCC9",width=128,height=128)
    settings_button.image_name = 'dinamik1'
    settings_button.image = music_image
    settings_button.config(command=lambda:image_switcher(settings_button,'dinamik1','dinamik'))
    settings_button.place(relx=0.95,rely=0.05,anchor='ne')



