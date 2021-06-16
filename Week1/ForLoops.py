first_numbers = list(range(0, 6))  # Creates a range iterator from [0, 6)
second_numbers = list(range(6, 12))  # Creates a range iterator from [6, 12)

add_nums = []

for l, m in zip(first_numbers, second_numbers):
    add_nums.append(l + m)

print(first_numbers)
print(second_numbers)
print(add_nums)
