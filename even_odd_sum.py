n = int(input())

even_sum = 0
odd_sum = 0

for i in range(1, n + 1):
    element = int(input())

    if i % 2 == 0:
        even_sum += element
    else:
        odd_sum += element

if even_sum == odd_sum:
    print(f"Yes\n Sum = {even_sum}")
else:
    print(f"No\n Diff = {abs(even_sum - odd_sum)}")