def insert_zero_before_series(arr):
    if not arr:
        return arr  # Если массив пустой, возвращаем его.

    result = []
    i = 0
    while i < len(arr):
        result.append(arr[i])

        # Если серия начинается (текущий элемент равен следующему и это начало серии).
        if i < len(arr) - 1 and arr[i] == arr[i + 1] and (i == 0 or arr[i] != arr[i - 1]):
            result.append(0)  # Вставляем 0 перед серией.

        i += 1

    return result


# Пример использования:
arr = [1, 10, 10, 2, 5, 5, 5, 5, 10]
new_arr = insert_zero_before_series(arr)
print(new_arr)  # Ожидаемый вывод: [1, 0, 10, 10, 2, 0, 5, 5, 5, 5, 10]
