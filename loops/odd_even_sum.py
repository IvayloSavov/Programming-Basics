n = int(input())

even_sum = 0
odd_sum = 0

for position in range(n):
    number = int(input())
    if position % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

if even_sum == odd_sum:
    print(f"Yes")
    print(f'Sum = {even_sum}')
else:
    print(f'No')
    print(f'Diff = {abs(even_sum-odd_sum)}')