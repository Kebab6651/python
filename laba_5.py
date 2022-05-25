""" Смирнов Вадим ИСТбд-11 Вариант - 12
Формируется матрица F следующим образом:
скопировать в нее А и  если в Е количество чисел, больших К в четных столбцах больше,
чем сумма чисел в нечетных строках, то поменять местами С и Е симметрично, иначе В и С поменять местами несимметрично.
При этом матрица А не меняется. После чего если определитель матрицы А больше суммы диагональных элементов матрицы F,
то вычисляется выражение: A^-1*AT – K * F^-1, иначе вычисляется выражение (A^-1+G-F^-1)*K,
где G-нижняя треугольная матрица, полученная из А.
Выводятся по мере формирования А, F и все матричные операции последовательно.
"""

import numpy as np
import time
N = int(input("Введите количество строк (столбцов) квадратной матрицы в интервале от 4 до 100: "))
while N < 4 or 100 < N:
    N = int(input("Введите количество строк (столбцов) квадратной матрицы в интервале от 4 до 100: "))

k = int(input("Введите число К: "))
start = time.time()
A = np.random.randint(-10, 10, (N, N)) #заполняем матрицу А случайными числами
print("Матрица А")
print(A)
F = A.copy()           #копируем элементы матрицы А в матрицу F
print("Матрица F")
print(F)
n = N // 2             #размер подматрицы E
E = np.zeros((n, n))   #заполняем подматрицу E нулями
print("Матрица C")
print(E)

for i in range(n):     #заполняем подматрицу E элементами из матрицы F
    for j in range(n):
        E[i][j] = F[i][n + (N % 2) + j]
print("Матрица C")
print(E)

count = 0
sum = 0
for i in range(n):                  #обрабатываем условия
    for j in range(n):
        if j % 2 == 0 and E[i][j] > k:
            count += 1
        if i % 2 != 0:
            sum += E[i][j]

if count > sum:                     #меняем подматрицы местами согласно условиям
    for i in range(n):
        for j in range(n):
            F[i][j + n + N % 2], F[N - 1 - i][j + n + N % 2] = F[N - 1 - i][j + n + N % 2], F[i][j + n + N % 2]
else:
    for i in range(n):
        for j in range(n):
            F[i][j], F[i][N // 2 + N % 2 + j] = F[i][N // 2 + N % 2 + j], F[i][j]
print("Матрица F")
print(F)

if np.linalg.det(A) == 0 or np.linalg.det(F) == 0:
    print("Нельзя вычислить")

elif np.linalg.det(A) > np.trace(F):
    a = ((np.linalg.inv(A)).dot(np.transpose(A)))-(k*np.linalg.inv(F))  #A^-1*AT – K * F^-1

else:
    a = (np.linalg.inv(A)+np.linalg.inv(np.tril(F))) * k #(A^-1+G-F^-1)*K

print ("\nОтвет:")
for i in a:
    for j in i:
        print ("%5d" % j, end = ' ')
    print ()

finish = (time.time() - start)
print ("\n", "Время работы программы:", finish, "секунды")