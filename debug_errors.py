# debug_errors.py

def calculate_average(numbers):
    try:
        total = 0
        for i in range(len(numbers)):
            total += numbers[i]
        return total / len(numbers)
    except ZeroDivisionError:
        # Gracefully handle the case for an empty list
        return 0  # or return None if preferred

data1 = [10, 20, 30, 40, 50]
data2 = [5, 15]
data3 = []  # This will cause an error if not handled properly

print(f"Average of data1: {calculate_average(data1)}")
print(f"Average of data2: {calculate_average(data2)}")
print(f"Average of data3: {calculate_average(data3)}")

