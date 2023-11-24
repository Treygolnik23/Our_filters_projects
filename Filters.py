from PIL import Image, ImageOps


# Бесконечный цикл
def cycle(number: int):
    while not number.isdigit() or int(number) == 0:
        number = input("Некорректный ввод, попробуйте еще раз: ")
    return number


class Filter:
    """
    Родительский класс для создания фильтров
    """

    def apply_to_pixel(self, r, g, b):
        raise NotImplementedError

    def apply_to_image(self, image):
        for i in range(image.width):
            for j in range(image.height):
                r, g, b = image.getpixel((i, j))
                new_pixel = self.apply_to_pixel(r, g, b)
                image.putpixel((i, j), new_pixel)
        return image


class InverseFilter(Filter):
    """
    Фильтр инверсии
    """

    def apply_to_pixel(self, r, g, b):
        new_r = 255 - r
        new_g = 255 - g
        new_b = 255 - b
        return new_r, new_g, new_b


class MirrorFilter:
    """
    Фильтр отзеркаливания
    """

    def apply_to_image(self, image):
        new_image = ImageOps.mirror(image)
        return new_image


class BrighteningFilter(Filter):
    """
    Фильтр осветления
    """

    def apply_to_pixel(self, r, g, b):
        new_r = min(255, r + 100)
        new_g = min(255, g + 100)
        new_b = min(255, b + 100)
        return new_r, new_g, new_b


class DimmingFilter(Filter):
    """
    Фильтр затемнения
    """

    def apply_to_pixel(self, r, g, b):
        new_r = max(0, r - 100)
        new_g = max(0, g - 100)
        new_b = max(0, b - 100)
        return new_r, new_g, new_b


class ResizeFilter:
    """
    Фильтр изменения размера
    """

    def apply_to_image(self, image: Image.Image):
        height, wight = image.size

        # Спрашиваем новые значения
        print(f"Текущее разрешение картинки - Высота: {height}, Ширина: {wight}")
        new_height = input("""Выберите новое разрешение:
Высота: """)
        new_height = cycle(new_height)  # Высота, проверка написания ввода
        print()
        new_wight = input("Ширина: ")
        new_wight = cycle(new_wight)  # Ширина, проверка написания ввода

        # Изменяем
        new_image = image.resize((int(new_height), int(new_wight)))
        return new_image


class BlackWhiteFilter(Filter):
    """
    Фильтр, который делает изображение чёрно-белым.
    """

    def apply_to_pixel(self, r: int, g: int, b: int) -> tuple[int, int, int]:
        # преобразуем r
        if 0 <= r <= 127:
            new_r = 0
        else:
            new_r = 255

        # преобразуем g
        if 0 <= g <= 127:
            new_g = 0
        else:
            new_g = 255

        # преобразуем b
        if 0 <= b <= 127:
            new_b = 0
        else:
            new_b = 255

        return new_r, new_g, new_b