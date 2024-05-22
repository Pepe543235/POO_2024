#Crear un programa que calcule y obtenga el total a pagar por un producto determinado. Se debera de solicitar el nombre o descripcion
#del producto, codigo del producto, cantidad del producto, precio unitario.
#El total a pagar incluye el IVA y el descuento.
#Si se compran de 1 a 5 productos se otorga el 10% de descuento, si se compran de 6 a 10 el 15% y si se compran mas de 10 el 20%

nom=input("Escriba el nombre del producto: ")
codigo=int(input("Ingrese el codigo del producto: "))
can=int(input("Ingrese la cantidad que quiere comprar: "))
precio=int(input("Ingrese el precio del producto: "))

subt= can*precio
subt2=subt*0.16
if can==1 and can<=5:
    desc=subt*0.10
    total=subt+subt2-desc
    print(f"El total a pagar es: ")
else:
    if can==6 and can<=10:
        desc=subt*0.15
        total=subt+subt2-desc
    else:
        if can>10:
            desc=subt*0.20
            total=subt+subt2-desc