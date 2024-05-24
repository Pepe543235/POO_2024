op=input("¿Desea realizar una captura? ")
calificacionesf= []
nombres= []
carreras= []
while op=="Si" or op=="si":
    nom=input("EScribe tu nombre ")
    carrera=input("Escribe tu carrera ")
    cal1=float(input("Escribe la calificacion del parcial 1 (con decimales como 9.0) "))
    cal2=float(input("Escribe la calificacion del parcial 2 (con decimales como 9.0) "))
    cal3=float(input("EScribe la calificacion del parcial 3 (con decimales como 9.0) "))
    proyectof=float(input("Escribe la calificacion del proyecto final (con decimales como 9.0) "))
    
    prompar=(cal1+cal2+cal3)/3
    calf=(prompar+proyectof)/2
    print(f"Su promedio de los parciales es: {prompar}")
    print(f"Su calificacion final es: {calf}")
    if calf<8.0 and proyectof>5.0:
        print("----Presenta examen extraordinario----")
    
    op=input("¿Desea realizar otra captura? ")
    nombres.append(nom)
    carreras.append(carrera)
    calificacionesf.append(calf)
    if op=="No" or op=="no":
        print(f"El promedio de la calificación de el alumno -{nombres}- de la carrera de -{carreras}- es:")
        print(calificacionesf)
    