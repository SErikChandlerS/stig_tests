import os
import zipfile
import argparse

def create_zip_archive(name):
    files = []
    
    # Поиск файлов с заданным именем
    for file in os.listdir('./tests_collection_2'):
        print(file)
        if name in file and os.path.isfile(file):
            files.append(file)
    
    if len(files) == 0:
        print(f"Файлы с названием {name} не найдены.")
        return
    
    # Создание ZIP-архива
    with zipfile.ZipFile(f"{name}_archive.zip", 'w') as zipf:
        for file in files:
            zipf.write(file)
    
    print(f"Архив '{name}_archive.zip' успешно создан.")
    zipf.close()

# Парсинг аргумента командной строки 'name'
parser = argparse.ArgumentParser(description='Создание ZIP-архива для файлов с заданным именем.')
parser.add_argument('name', type=str)

args = parser.parse_args()

# Вызов функции создания архива с переданным именем
create_zip_archive(args.name)
