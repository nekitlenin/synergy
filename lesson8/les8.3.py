m = int(input())
n = int(input())

weights = []
for _ in range(n):
    weights.append(int(input()))

weights.sort()

left = 0
right = n - 1
boats_count = 0

while left <= right:
    if left < right and weights[left] + weights[right] <= m:
        left += 1
        right -= 1
    else:
        right -= 1
    
    boats_count += 1

print(boats_count)