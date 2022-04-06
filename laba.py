K = 0
with open ("D:\learning\laba.txt","r") as f:
    print("Введите число K")
    K = int(input())
    for i in f:
         if len(i)>K:
             print(i)
