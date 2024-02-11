file_path = './task_2/hw_example.txt'

def get_cats_info(path: str) -> list[dict]:
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, cat_name, cat_age = line.strip().split(',')
                cats_info.append({
                    'id': cat_id,
                    'name': cat_name,
                    'age': cat_age
                })
    except FileNotFoundError as e:
        print(f'Помилка {e}. Файл не знайдено.')

    except ValueError as e:
        print(f'Помилка {e}. Перевірте формат даних')

    return cats_info

print(get_cats_info(file_path))
