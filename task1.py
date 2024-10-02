def total_salary(path: str) -> tuple:
    try:
        total = 0
        average = 0
        count = 0

        with open(path, 'r', encoding='utf-8') as file:
              for line in file:
                    try:
                        salary = int(line.strip().split(",")[1])
                        total += salary
                        count += 1
                    except (IndexError, ValueError):
                        print(f"Warning: Incorrect data format in line: {line.strip()}")

        if count > 0:
            average = total // count         

    except FileNotFoundError:
        print("Warning: file not found!")
    except Exception as e:
        print(f"Something else went wrong: {e}")

    return total, average
    

total, average = total_salary("path/to/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")