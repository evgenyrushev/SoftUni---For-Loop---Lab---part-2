import sys

number_lines = int(input())
max_number = -sys.maxsize
min_number = sys.maxsize

for num in range (number_lines):
    current_num = int(input())

    if current_num > max_number:
        max_number = current_num

    if current_num < min_number:
        min_number = current_num

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")