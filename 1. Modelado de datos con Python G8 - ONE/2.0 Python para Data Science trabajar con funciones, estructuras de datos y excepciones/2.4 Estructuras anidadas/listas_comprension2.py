datos = [
    [3, -1, 5],
    [-2, 0, 4],
    [7, -3, 2]
]

negativos = [numero for fila in datos for numero in fila if numero>0]
print(negativos)

productos = {
    "manzana": 120,
    "banana": 80,
    "pera": 150,
    "naranja": 90,
    "melon": 200
}


lista_producto =[producto for producto, precio in productos.items() if precio<100 ]
print(lista_producto)



def aprobaron(nombres: list[str], promedios: list[float]) -> dict[str, float]:
    # tu código aquí
    resultado ={nombre:promedio for nombre , promedio in zip(nombres,promedios) if promedio<=6}
    return resultado

nombres = ["Ana", "Luis", "Maria", "Carlos"]
promedios = [7.0, 5.5, 6.8, 4.9]

print(aprobaron(nombres, promedios))
