from imports import Image,ImageDraw,ImageTk,sqlite3,io

def create_round_image(name,db_path="game_images.db",size=(128,128)):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT image FROM images WHERE name = ?",(name,))
    result = cursor.fetchone()

    conn.close()

    if result is None:
        raise ValueError(f"Изображение с именем '{name}' не найдено в базе данных.")
    img_blob = result[0]
    image = Image.open(io.BytesIO(img_blob)).resize(size,Image.Resampling.LANCZOS).convert("RGBA")

    mask = Image.new("L",size,0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0,0,size[0],size[1]),fill=255)

    rounded_image = Image.new("RGBA",size)
    rounded_image.paste(image,(0,0),mask)

    return ImageTk.PhotoImage(rounded_image)