my_lista = [[1,2,3],
            [4,5,6],
            [7,8,9]]


for elemento in my_lista:
    print(elemento)
    for elemt in elemento:
        if not elemt%2 == 0:
            print(elemt)

nombres = ["ansiedad","miedo","desprecion"]

patata = list(map(lambda n : n + " nombramiento " ,nombres))

numeros = [n for n in range(10) if n % 2 == 0]

print(numeros)