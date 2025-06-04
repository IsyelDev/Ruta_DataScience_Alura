notas_separadas =[
    [8.0,9.0,10.0],
    [9.0,7.0,6.0],
    [3.4,7.0,7.0],
    [5.5,6.6,8.0],
    [6.0,10.0,9.5]
                  ]

promedios = [sum(fila) / len(fila) for fila in notas_separadas]
print(promedios)

print("*"*40)

print(notas_separadas)
print(len(notas_separadas))
print(sum(sum(fila) for fila in notas_separadas))

def promedio(lista: list=[0])->float:
    calculo = sum(lista) /len(lista)
    return calculo

promedio = [round(promedio(n),1) for n in notas_separadas]
print(promedio)

prom =[9.0, 7.3, 5.8, 6.7, 8.5]
nombres = [
    ("Juan", "j32"),
    ("Ana", "a45"),
    ("Luis", "l28"),
    ("María", "m91"),
    ("Carlos", "c77"),
    ("Sofía", "s63"),
    ("Pedro", "p10"),
    ("Lucía", "l85"),
    ("Diego", "d14"),
    ("Elena", "e99")
]

nombre =[nombre[0] for nombre in nombres]
print(nombre)
nom = ['Juan', 'Ana', 'Luis', 'María', 'Carlos', 'Sofía', 'Pedro', 'Lucía', 'Diego', 'Elena']

estudiantes = list(zip(nom,prom))
print(estudiantes)
candidatos = [n[0] for n in estudiantes if n[1]>=8]
print(candidatos)
import os

os.system("cls")
notas = [
    [7, 8, 9],
    [5, 6, 7],
    [10, 9, 8],
    [6, 7, 8]
]

calificaciones = [nota[1] for nota in notas]
print(calificaciones)


estudiantes = [
    ("Juan", 6.5),
    ("Ana", 7.2),
    ("Luis", 8.0),
    ("María", 5.9),
    ("Carlos", 7.8)
]

promedio = [estudiante[0] for estudiante in estudiantes if estudiante[1]>=7]
print(promedio)



promedios = [5.5, 7.0, 8.2, 4.9, 6.0]
lista_promedios = ["Aprobado" if promedio>=6 else "Reprobado" for promedio in promedios]
print(lista_promedios)

