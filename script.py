import os
import os.path
import shutil

def get_directory_size(path):
    """
    Рекурсивно вычисляет размер директории.
    """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            try:
                total_size += os.path.getsize(filepath)
            except FileNotFoundError:
                # Пропускаем файлы, которых не существует
                pass
    return total_size

def format_size(size):
    """
    Форматирует размер в килобайтах.
    """
    return f"{size / 1024:.2f} KB"

def print_directory_sizes(path='.'):
    """
    Выводит размер каждой директории и файла в указанной директории (по умолчанию - текущая).
    """
    sizes = []
    for entry in os.listdir(path):
        entry_path = os.path.join(path, entry)
        if os.path.isdir(entry_path):
            size = get_directory_size(entry_path)
            sizes.append((size, entry, 'dir'))
        elif os.path.isfile(entry_path):
            size = os.path.getsize(entry_path)
            sizes.append((size, entry, 'file'))

    # Сортировка по уменьшению размера
    sizes.sort(reverse=True)

    for size, name, type in sizes:
        print(f"{format_size(size):>10} - {type}: {name}")

# Вызов функции для отображения размеров в текущей директории
print_directory_sizes()
