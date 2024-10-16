from imports import tk
from window_config import configure_window
from cursor_manager import apply_cursor_to_window
from play_once import play_on_loading
from image_loader import load_image_by_name
def play_encouraging_sound():
    play_on_loading("F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\sounds\\umnichka.mp3")

def animate_ball_image(ball_canvas, ball_image_id, on_animation_end):
    step = 5
    middle_y = ball_canvas.winfo_height() // 2

    def move_image():
        x0, y0 = ball_canvas.coords(ball_image_id)
        if y0 > middle_y:
            ball_canvas.move(ball_image_id, 0, -step)
            ball_canvas.after(150, move_image)
        else:
            on_animation_end()
    move_image()

def create_ball_animation_window(root, on_finish_window):
    animation_window = tk.Toplevel(root)
    apply_cursor_to_window(animation_window)
    configure_window(animation_window)

    play_encouraging_sound()

    ball_canvas = tk.Canvas(animation_window, bg='#BDFCC9')
    ball_canvas.pack(fill=tk.BOTH, expand=True)

    ball_image = load_image_by_name('balls')

    def initialize_ball_image():

        ball_canvas_width = ball_canvas.winfo_width()
        ball_canvas_height = ball_canvas.winfo_height()

        ball_image_id = ball_canvas.create_image(
            ball_canvas_width // 2, 650,
            image=ball_image, anchor=tk.CENTER
        )

        animate_ball_image(ball_canvas, ball_image_id, lambda: on_finish_window(root))


        animation_window.ball_image = ball_image


    ball_canvas.after(100, initialize_ball_image)

