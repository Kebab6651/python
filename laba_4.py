"""ИСТБД-11 Смирнов Вадим вариант - 12
Формируется матрица F следующим образом:
если в В количество простых чисел в нечетных столбцах в области 2 больше,
чем сумма чисел в четных строках в области 1, то поменять в Е симметрично области 1 и 2 местами,
иначе С и Е поменять местами несимметрично. При этом матрица А не меняется.
После чего вычисляется выражение: ((К*A)*А– K*AT .
Выводятся по мере формирования А, F и все матричные операции последовательно.
"""
import random
import time


def isitPrime(k):                               #функция для определения простое ли число
    if k==2 or k==3: return True
    if k%2==0 or k<2: return False
    for i in range(3, int(k**0.5)+1, 2):
        if k%i==0:
            return False

    return True

def print_matrix(M,matr_name,tt):
        print ( "матрица " + matr_name + " промежуточное время = " + str(format(tt, '0.2f')) + " seconds.")
        for i in M:            # делаем перебор всех строк матрицы
            for j in i:     # перебираем все элементы в строке 
                print("%5d" % j, end = ' ')
            print() 
  
print("\n-----Результат работы программы-------")
try:
    row_q = int(input("Введите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100:"))
    while row_q < 6 or row_q>100:
        row_q = int(input("Вы ввели неверное число\nВведите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100: "))
    K = int(input("Введите число К = "))
    start = time.time()
    A, F, AA, AT = [], [], [], []                      # задаем матрицы
    for i in range(row_q):
        A.append([0]*row_q)
        F.append([0]*row_q)
        AA.append([0] * row_q)
        AT.append([0] * row_q)
    time_next = time.time()
    print_matrix(F, "F", time_next-start)

    for i in range(row_q):      # заполняем матрицу А         
        for j in range(row_q):            
            A[i][j] = random.randint(-10, 10)
                      
    time_prev = time_next
    time_next = time.time()
    print_matrix(A, "A", time_next-time_prev)
    for i in range(row_q):      # F
        for j in range(row_q):
            F[i][j] = A[i][j]    
    time_prev = time_next
    time_next = time.time()
    print_matrix(F, "F", time_next-time_prev)

    B = []                      # задаем матрицу B
    size = row_q//2
    for i in range(size):
        B.append([0]*size)
    
    for i in range(size):      # формируем подматрицу B
        for j in range(size):
            B[i][j] = F[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(B, "B", time_next-time_prev)
    
    quantity = 0
    sum = 0
    for i in range(size):      # обрабатываем подматрицу B
        for j in range(0, size-i-1, 1):
            if j%2 == 1 and j >= i and (isitPrime(B[i][j])):
                quantity += 1
            elif j%2 == 0 and j <= i:
                sum += B[i][j]
            
    if quantity > sum:
        for i in range(1, size//2, 1):      # меняем подматрицу B
            for j in range(0, i, 1):
                B[i][j], B[j][i] = B[j][i], B[i][j]
        for i in range(size//2, size, 1):
            for j in range(0, i, 1):
                B[i][j], B[j][i] = B[j][i], B[i][j]
        print_matrix(B, "B", 0)
        for i in range(0, size, 1):      # формируем матрицу F
            for j in range(0, size, 1):
                F[i][j] = B[i][j]
    else:
       for j in range(row_q//2+row_q%2, row_q, 1):
            for i in range(row_q//2):
                F[i][j], F[row_q//2+row_q%2+i][j] = F[row_q//2+row_q%2+i][j], F[i][j]
                                    
    time_prev = time_next
    time_next = time.time()
    print_matrix(F,"F",time_next-time_prev)
    print_matrix(A,"A",time_next-time_prev)

    for i in range(row_q):      # K*A
        for j in range(row_q):
            A[i][j] = K*A[i][j]    
    time_prev = time_next
    time_next = time.time()
    print_matrix(A, "K*A", time_next-time_prev)
    
    for i in range(row_q):      # K*A*A
        for j in range(row_q):
            s = 0
            for m in range(row_q):
                s = s + A[i][m] * A[m][j]
            AA[i][j] = s
    time_prev = time_next
    time_next = time.time()
    print_matrix(AA, "K*A*A", time_next - time_prev)
    
    for i in range(row_q):      # AT
        for j in range(i,row_q,1):
            AT[i][j], AT[j][i] = A[j][i], A[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AT, "A^T", time_next - time_prev)
                
    for i in range(row_q):      # K*AT
        for j in range(row_q):
            AT[i][j] = K * AT[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AT, "K*A^T", time_next - time_prev)
    
    for i in range(row_q):      # (K*A)*A+K*AT
        for j in range(row_q):
            AA[i][j] = AA[i][j] + AT[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AA, "(K*A)*A+K*A^T", time_next - time_prev)
    
    finish = time.time()
    result = finish - start
    print("Program time: " + str(result) + " seconds.")    

#except ValueError:
#    print("\nэто не число") 
                    
except FileNotFoundError:
    print("\nФайл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")
