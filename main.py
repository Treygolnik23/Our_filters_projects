import pathlib
from PIL import Image
from Filters import InverseFilter, MirrorFilter, BrighteningFilter, DimmingFilter, ResizeFilter
import os


def main():
    filters_names = [
        "Инверсия",
        "Отзеркаливание",
        "Повышение яркости",
        "Понижение яркости",
        "Изменение разрешения",
    ]

    filters = [
        InverseFilter(),
        MirrorFilter(),
        BrighteningFilter(),
        DimmingFilter(),
        ResizeFilter(),
    ]

    # Интерфейс
    is_finished = False  # переменная для окончания программы

    print("Добро пожаловать в консольный фоторедактор.")

    while not is_finished:
        file_path = input("Введите путь к изображению: ")

        # Проверка на существование изображения
        while not os.path.exists(file_path) or not file_path.endswith(('.png', '.jpg', '.jpeg')):
            file_path = input("Файл не найден или не является изображением. Попробуйте ещё раз: ")
        img = Image.open(file_path).convert('RGB')
        # Выбор фильтров
        print("Выберите один из фильтров: ")
        for i in range(len(filters_names)):
            print(f"{i + 1} - {filters_names[i]}")
        print(f"{len(filters_names) + 1} - Выход")

        choice = input("Выберите один из вариантов: ")

        # Проверка выбора
        while not choice.isdigit() or not (0 < int(choice) <= len(filters_names)):
            if choice == "6":
                is_finished = True
                break
            choice = input("Некорректный ввод, попробуйте еще раз: ")

        if is_finished:  # Проверяет, нужно ли выйти
            break

        # Применяет фильтр
        filt = filters[int(choice) - 1]
        img = filt.apply_to_image(img)

        # Имя файла
        save_file = input("Назовите файл (только имя): ")
        while True:
            if not "\\" in save_file: # Проверка на наличия только имени
                break
            save_file = input("Некорректный ввод, напишите только имя: ")

        # Проверка пути
        save_path = input("\nВыберите путь сохранения изображения: ")
        while not os.path.exists(save_path):
            save_path = input("Путь не найден. Попробуйте ещё раз: ")

        # Сохраняем
        img.save(pathlib.Path(f"{save_path}\{save_file}.jpg"))

        answer = input("Использовать фильтр еще раз? (да/нет): ").lower()

        # Выход
        while answer != "да" and answer != "нет":
            answer = input("Некорректный ввод. Попробуйте ещё раз: ").lower()
        is_finished = answer == "нет"
    print("\nВы вышли из программы.")

if __name__ == "__main__":
    main()