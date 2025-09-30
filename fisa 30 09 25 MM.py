x,y=int(input('x=')),int(input('y='))
# 1. Cel mai mare divizor comun (CMMD)
def cmmd(x, y):
    if x < y:
        minim = x
    else:
        minim = y
    
    rezultat = 1
    for i in range(1, minim + 1):
        if x % i == 0 and y % i == 0:
            rezultat = i
    return rezultat


# 2. Cel mai mic multiplu comun (CMMMC)
def cmmmc(x, y):
    if x > y:
        maxim = x
    else:
        maxim = y
    
    for i in range(maxim, x * y + 1):
        if i % x == 0 and i % y == 0:
            return i


# 3. Divizorii comuni ai numerelor x și y
def divizori_comuni(x, y):
    lista = []
    if x < y:
        minim = x
    else:
        minim = y

    for i in range(1, minim + 1):
        if x % i == 0 and y % i == 0:
            lista.append(i)
    return lista


# 4. 5 multipli ai numerelor x și y
def multipli(x, y):
    lista_x = []
    lista_y = []
    for i in range(1, 6):
        lista_x.append(x * i)
        lista_y.append(y * i)
    return lista_x, lista_y


# 5. Cifrele care apar în ambele numere
def cifre_comune(x, y):
    cifre_x = []
    cifre_y = []
    for c in str(x):
        if c not in cifre_x:
            cifre_x.append(c)
    for c in str(y):
        if c not in cifre_y:
            cifre_y.append(c)

    comune = []
    for c in cifre_x:
        if c in cifre_y:
            comune.append(c)
    return comune


# 6. Cifrele care apar în x dar nu în y
def cifre_diferente(x, y):
    cifre_x = []
    cifre_y = []
    for c in str(x):
        if c not in cifre_x:
            cifre_x.append(c)
    for c in str(y):
        if c not in cifre_y:
            cifre_y.append(c)

    diferenta = []
    for c in cifre_x:
        if c not in cifre_y:
            diferenta.append(c)
    return diferenta


# 7. PRIETENE dacă numărul de divizori e egal
def prietene(x, y):
    nr_div_x = 0
    nr_div_y = 0

    for i in range(1, x + 1):
        if x % i == 0:
            nr_div_x += 1
    for j in range(1, y + 1):
        if y % j == 0:
            nr_div_y += 1

    if nr_div_x == nr_div_y:
        return "PRIETENE"
    else:
        return "NU SUNT PRIETENE"


print("Cel mai mare divizor comun este,:", cmmd(x, y))
print("Cel mai mic divizor comun este,:", cmmmc(x, y))
print("Divizorii comuni ai numerelor x,y sunt:", divizori_comuni(x, y))
print("5 multipli ai numerelor x,y sunt:", multipli(x, y))
print("Cifrele comune in x și y sunt:", cifre_comune(x, y))
print("Cifrele în x dar nu în y sunt:", cifre_diferente(x, y))
print("Sunt prietene cele 2 numere?:", prietene(x, y))
