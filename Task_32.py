# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат диапазону 5 - 15
# (т.е. не меньше заданного минимума и не больше заданного максимума)

qnt, mini, maxi, li_in, li_out = int(input('Nums qnt: ')), int(input('Min num: ')), int(input('Max num: ')), [], []

for i in range(0, qnt):
    li_in.append(int(input('Input a num: ')))


for i in range(len(li_in)):
    if mini <= li_in[i] <= maxi:
        li_out.append(i)

print(li_out)

