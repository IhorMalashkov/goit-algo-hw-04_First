from pathlib import Path

file_name = Path('.')

def total_salary(path):
    try:
        total = 0
        workers = 0
        
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    name, salary = line.split(',')
                    total += float(salary)
                    workers += 1
        
                    if workers == 0:
                        return (0, 0)
            
        average = total / workers
        return (total, average)
        
    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
        return (0, 0)
    except ValueError:
        print("Помилка: Файл містить некоректні дані.")
        return (0, 0)
    except Exception as e:
        print(f"Сталася непередбачена помилка: {e}")
        return (0, 0)

total, average = total_salary("path/to/salary_file.txt")
print(f"Загальна сума заробітної плати: {round(total, 2)}, Середня заробітна плата: {round(average, 2)}")