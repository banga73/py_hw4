import random

N = int(input ("Введите число: "))
dic_N = dict()
sum_3 = []
for i in range(N):
    dic_N[i] = random.randint(1, 10)
sum_3.append(dic_N[0] + dic_N[N - 1] + dic_N[1])
for i in range(1, N - 1):
    sum_3.append(dic_N[i - 1] + dic_N[i] +dic_N[i + 1])
sum_3.append(dic_N[0] + dic_N[N - 1] + dic_N[N - 2])
print(max(sum_3))
