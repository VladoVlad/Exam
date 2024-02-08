import time
import re

def is_valid_input(input_str):
    return all(re.match(r'^-?\d*\.?\d*$', x) for x in input_str.split(','))

def validate_input(new_value):
    if new_value == "":
        return True
    try:
        parts = new_value.split(",")
        for part in parts:
            part = part.strip()
            if part and not re.match(r'^-?\d*\.?\d*$', part):
                return False
        return True
    except Exception:
        return False

def sort_sequence(sequence, sorting_order):
    try:
        if not validate_input(sequence):
            raise ValueError("Invalid input format")
        sequence_parts = sequence.split(",")
        sorted_sequence = []
        for part in sequence_parts:
            part = part.strip()
            if part:
                if '.' in part:
                    sorted_sequence.append(float(part))
                else:
                    sorted_sequence.append(int(part))
        start_time = time.time()
        if sorting_order == "ascending":
            sorted_sequence.sort()
        elif sorting_order == "descending":
            sorted_sequence.sort(reverse=True)
        end_time = time.time()
        sorted_result = ", ".join(map(str, sorted_sequence))
        time_taken = end_time - start_time  # время в секундах
        return sorted_result, time_taken
    except ValueError as e:
        return "Error: " + str(e), 0
    except Exception as e:
        return "An error occurred", 0

def main():
    sequence = input("Введите цифры через запятую: ")
    sorting_order = input("Выберите порядок сортировки (ascending/descending): ")
    sorted_result, time_taken = sort_sequence(sequence, sorting_order)
    print("Отсортированная последовательность:", sorted_result)
    print("Время сортировки:", "{:.6f}".format(time_taken), "секунд")
    print("Введенные цифры:", sequence)

if __name__ == "__main__":
    main()
