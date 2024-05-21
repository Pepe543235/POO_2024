numero=1
multi=0
i=1
for numero in range(1,11):
    print(f"La tabla del {numero} es:")
    for i in range(1,11):
        multi=i*numero
        print(f"{numero} x {i} = {multi}")

    