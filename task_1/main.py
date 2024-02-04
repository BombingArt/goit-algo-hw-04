file_path = './task_1/hw_example_01.txt'

def total_salary(path: str) -> tuple[int]:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            raw_data = file.readlines()

        salary_list = []
        for line in raw_data:
            line = line.strip()
            _, salary = line.split(',')
            salary_list.append(int(salary))
        
        total = sum(salary_list)
        average = int(total / len(salary_list))

        return total, average
    
    except FileNotFoundError as e:
        print(f"Помилка {e}. Файл не знайдено")
        return 0, 0
    except ValueError:
        print(f"Помилка {e}. Перевірте формат даних.")
        return 0, 0
    
total, average = total_salary(file_path)
print(f"Загальна сума заробітної плати: {total}. Середня сума заробітної плати: {average}")
