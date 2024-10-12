def shake_button(button):
    original_x = button.winfo_x()
    shake_distance = 10
    shake_duration = 200
    shake_count = 10

    def shake():
        nonlocal shake_count
        if shake_count > 0:

            if shake_count % 2 == 0:
                button.place(x=original_x - shake_distance)
            else:
                button.place(x=original_x + shake_distance)

            shake_count -=1
            button.after(shake_duration // 10,shake)
    shake()