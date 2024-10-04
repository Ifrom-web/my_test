#!/bin/bash

# Функция для получения размера файла или директории
get_size() {
    local path="$1"
    local size=$(du -sh "$path" | cut -f1)
    echo "$size $path"
}

# Главная функция
main() {
    local files=()
    local dirs=()

    # Получение списка файлов и директорий
    for item in *; do
        if [ -f "$item" ]; then
            files+=("$item")
        elif [ -d "$item" ]; then
            dirs+=("$item")
        fi
    done

    # Вывод информации о размере файлов
    echo "Файлы:"
    for file in "${files[@]}"; do
        get_size "$file"
    done | sort -nr

    # Вывод информации о размере директорий
    echo "Директории:"
    for dir in "${dirs[@]}"; do
        get_size "$dir"
    done | sort -nr
}

main
