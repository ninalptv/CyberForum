n1 = int(input('Введите одно число N1: '))
n2 = int(input('Введите одно число N2: '))
quantity = 0
for num in range(n1, n2 + 1):
    num = str(num)
    n = len(num)
    if n == 1:
        quantity += 1
    if n == 2:
        if num[0] < num[1]:
            quantity += 1
    for i in range(2, n):
        if i % 2 == 0:
            if num[i] < num[i - 1] > num[i - 2]:
                if i == n - 1:
                    quantity += 1
                continue
        else:
            if num[i - 2] > num[i - 1] < num[i]:
                if i == n - 1:
                    quantity += 1
                continue
print(f"Количество пилообразных чисел в промежутке N1 и N2: {quantity}")


