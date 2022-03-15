K = 0
with open ("D:\learning\laba.txt","r") as f:
    print("Введите число K")
    K = int(input())
    while True:
        temp = str(f.readline())
        if (len(temp) > K):
            print(temp)
        if (len(temp) == 0):
            break


