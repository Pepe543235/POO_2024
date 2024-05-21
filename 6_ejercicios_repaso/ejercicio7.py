n1=int(input("Escriba el primer numero: "))
n2=int(input("Escriba el segundo numero: "))

for n in range(n1+1,n2):
    if (n % 2) == 1:
        print(n)