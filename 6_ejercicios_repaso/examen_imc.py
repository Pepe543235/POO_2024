op=input("¿Desea realizar una captura? ")
i=0
while op=="Si" or op=="si":
    peso=float(input("Ingrese su peso "))
    altura=float(input("Ingrese su altura "))

    imc=peso/(altura*altura)

    if imc<18.5:
        print("Su peso es inferior al promedio")
    else:
        if imc>18.5 and imc<=24.9:
            print("Su peso es normal")
        else:
            if imc>=25.0 and imc<=29.9:
                print("Su peso es superior al normal")
            else:
                if imc>=30.0:
                    print("Su peso se considera obesidad")
    i=i+1
    op=input("¿Desea realizar otra captura? ")
    
    if op=="No" or op=="no":
        print(f"Los calculos de IMC fueron {i}")

        

