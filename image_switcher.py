from image_utils import create_round_image

def switch_image(button,current_image,image1,image2,db_path="game_images.db"):
    next_image = image2 if current_image == image1 else image1
    new_image = create_round_image(next_image,db_path=db_path)

    button.config(image=new_image)
    button.image = new_image

    return next_image