def MAXIM(a, b):
    return max(a, b)

def MINIM(a, b):
    return min(a, b)

def SUMA():
    global a1, a2, a3, a4, a5, a6, a7, a8, a9, a10
    return round(MAXIM(MINIM(a1, a2), MAXIM(a3, a4)) + MINIM(MAXIM(a5, a6), MINIM(a7, a8)), 2)

def TOTAL():
    global a1, a2, a3, a4, a5, a6, a7, a8, a9, a10
    return round(MINIM(a1, a2) + MINIM(a3, a4) + MINIM(a5, a6) + MINIM(a7, a8) + MINIM(a9, a10) + MAXIM(a1, a2) + MAXIM(a3, a4) + MAXIM(a5, a6) + MAXIM(a7, a8) + MAXIM(a9, a10), 2)


print('Dati numerele reale a1-a10')
a1 = float(input('a1 = '))
a2 = float(input('a2 = '))
a3 = float(input('a3 = '))
a4 = float(input('a4 = '))
a5 = float(input('a5 = '))
a6 = float(input('a6 = '))
a7 = float(input('a7 = '))
a8 = float(input('a8 = '))
a9 = float(input('a9 = '))
a10 = float(input('a10 = '))

print(f'a1 = {a1}')
print(f'a2 = {a2}')
print(f'a3 = {a3}')
print(f'a4 = {a4}')
print(f'a5 = {a5}')
print(f'a6 = {a6}')
print(f'a7 = {a7}')
print(f'a8 = {a8}')
print(f'a9 = {a9}')
print(f'a10 = {a10}')

print('Suma =', SUMA())
print('Total =', TOTAL())