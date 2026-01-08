def cel_mai_mare(lista):
    maxim = lista[0]
    for numar in lista:
        if numar > maxim:
            maxim = numar
    return maxim

numere = [3, 7, 2, 9, 5]
print("Cel mai mare număr este:", cel_mai_mare(numere))
