def shake_button(button):
    # Проверяем, были ли уже сохранены исходные размеры кнопки
    if not hasattr(button, 'original_width'):
        button.original_width = button.winfo_width()
        button.original_height = button.winfo_height()

    original_width = button.original_width
    original_height = button.original_height
    scale_factor = 1.2
    shake_duration = 200
    shake_count = 5

    # Локальная переменная для отслеживания состояния тряски
    if not hasattr(shake_button, 'is_shaking'):
        shake_button.is_shaking = False

    def shake(remaining_count):
        if remaining_count > 0:
            if remaining_count % 2 == 0:
                # Увеличиваем кнопку
                button.config(width=int(original_width * scale_factor), height=int(original_height * scale_factor))
            else:
                # Возвращаем к исходному размеру
                button.config(width=original_width, height=original_height)

            # Запланировать следующий шаг тряски
            button.after(shake_duration // shake_count, shake, remaining_count - 1)
        else:
            # После завершения тряски, гарантируем, что размер вернется к оригинальному
            button.config(width=original_width, height=original_height)
            shake_button.is_shaking = False  # Сбрасываем состояние

    if not shake_button.is_shaking:  # Проверка, не происходит ли уже тряска
        shake_button.is_shaking = True  # Устанавливаем состояние тряски
        shake(shake_count)  # Начинаем тряску с полного количества
