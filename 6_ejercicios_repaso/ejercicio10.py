n=0
r=0
a=0
for n in range(1,16):
    alumno=int(input(f"Escriba la calificacion del alumno {n} :"))
    if alumno >= 80:
        print("APROBADO")
        a+=1
    else:
        print("REPROBADO")
        r+=1
print(f"Los alumnos que aprobaron fueron: {a}, los reprobados fueron: {r}")