N = int(input())

numbers = []
for i in range(N):
    num = int(input())
    numbers.append(num)

reversed_numbers = numbers[::-1]

for num in reversed_numbers:
    print(num)