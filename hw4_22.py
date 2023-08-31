import random

N = int(input ("Введите число: "))
M = int(input ("Введите число: "))
list_N = []
list_M = []
for i in range(N):
    list_N.append(random.randint(0, 100))
for i in range(M):
    list_M.append(random.randint(0, 100))
print(list_N)
print(list_M)
print(sorted(set(list_N).intersection(set(list_M))))