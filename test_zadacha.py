import re
import time


class Cond:
    def __init__(self, type_, field, condition, value):
        self.type = type_
        self.field = field
        self.condition = condition
        self.value = value


def parse(cond_str):
    pattern = re.compile(r'^([@#])([^:]+)(?::(>=|<=|!=|>|<|=)?(.+))?$')
    match = pattern.match(cond_str)

    if not match:
        return None

    type_, field, condition, value = match.groups()
    condition = condition if condition else "="

    if value is not None:
        try:
            value = int(value)
        except ValueError:
            pass

    return Cond(type_, field, condition, value)


# Засекаем время в начале выполнения скрипта
start_time = time.time()

# Чтение строк условий из файла и их обработка
with open('conditions.txt', 'r') as file:
    for line in file:
        cond_str = line.strip()
        if cond_str:  # Проверяем, не пустая ли строка
            cond = parse(cond_str)
            if cond:
                print(f"Type: {cond.type}, Field: {cond.field}, Condition: {cond.condition}, Value: {cond.value}")

# Засекаем время в конце выполнения скрипта
end_time = time.time()

# Расчет и вывод общего времени выполнения скрипта
total_duration = end_time - start_time
print(f"Общее время выполнения: {total_duration:.6f} секунд")
