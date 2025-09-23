n1 = int(input())
list1 = [int(input()) for _ in range(n1)]

n2 = int(input())
list2 = [int(input()) for _ in range(n2)]

set1 = set(list1)
set2 = set(list2)
common_numbers = set1 & set2

print(len(common_numbers))