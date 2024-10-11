from image_switcher import switch_image

def image_switcher(button,image1,image2):
    button.image_name = switch_image(
        button,
        button.image_name,
        image1,
        image2,
        db_path="game_images.db"
    )