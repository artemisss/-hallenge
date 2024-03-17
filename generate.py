import re
import time
from concurrent.futures import ProcessPoolExecutor


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


def print_cond(cond):
    if cond:
        print(f"Type: {cond.type}, Field: {cond.field}, Condition: {cond.condition}, Value: {cond.value}")


def process_batch(batch, executor):
    results = executor.map(parse, batch)  # Обработка батча
    for cond in results:
        print_cond(cond)


if __name__ == "__main__":
    start_time = time.time()
    batch_size = 20000

    with ProcessPoolExecutor() as executor:
        with open('conditions.txt', 'r') as file:
            lines = file.readlines()
            # Обработка батчами
            for i in range(0, len(lines), batch_size):
                batch = lines[i:i + batch_size]
                process_batch(batch, executor)

    end_time = time.time()
    print(f"Общее время выполнения: {end_time - start_time:.6f} секунд")
