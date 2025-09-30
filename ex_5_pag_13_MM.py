a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = float(input("d = "))
i = int(input("i = "))
j = int(input("j = "))
k = int(input("k = "))
m = int(input("m = "))
n = int(input("n = "))

# a
def suma_reale(a, b, c, d):
    return a + b + c + d

print("Suma numerelor reale este:", suma_reale(a, b, c, d))


# b
def media_intregi(i, j, k, m):
    return (i + j + k + m) / 4

print("Media numerelor întregi este:", media_intregi(i, j, k, m))


# c
def minimum_4(a, b, c, d):
    minim = a
    if b < minim:
        minim = b
    if c < minim:
        minim = c
    if d < minim:
        minim = d
    return minim

print("Cel mai mic număr este:", minimum_4(a, b, c, d))


# d
text = input("Scrie un text: ")

def numar_vocale(s):
    vocale = "aeiouăâîAEIOUĂÂÎ"
    nr = 0
    for ch in s:
        if ch in vocale:
            nr += 1
    return nr

print("Numărul de vocale este:", numar_vocale(text))


# e
def numar_consoane(s):
    vocale = "aeiouăâîAEIOUĂÂÎ"
    nr = 0
    for ch in s:
        if ch.isalpha() and ch not in vocale:
            nr += 1
    return nr

print("Numărul de consoane este:", numar_consoane(text))


# f
def radacina(a, b):
    if a != 0:
        return -b / a
    else:
        return "Nu are soluție unică (a = 0)"

print("Rădăcina ecuației ax + b = 0 este:", radacina(a, b))


# g
def cel_mai_mic_divizor(n):
    d = 2
    while d <= n:
        if n % d == 0:
            return d
        d += 1

print("Cel mai mic divizor al lui n este:", cel_mai_mic_divizor(n))


# h
def cmmdc(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

print("CMMDC-ul dintre a și b este:", cmmdc(int(a), int(b)))


# i
def cmmmc(a, b):
    return int(a * b // cmmdc(int(a), int(b)))

print("CMMMC-ul dintre a și b este:", cmmmc(a, b))


# j
def ultima_cifra(n):
    return n % 10

print("Ultima cifră a lui n este:", ultima_cifra(n))


# k
def numar_cifre(n):
    cnt = 0
    while n > 0:
        cnt += 1
        n //= 10
    return cnt

print("Numărul de cifre al lui n este:", numar_cifre(n))


# l
def cifra_superioara(n):
    while n >= 10:
        n //= 10
    return n

print("Cifra din stânga a lui n este:", cifra_superioara(n))


# m
text = input("Scrie un text: ")
ch = input("Introdu caracterul căutat: ")

def numar_aparitii(s, ch):
    cnt = 0
    for c in s:
        if c == ch:
            cnt += 1
    return cnt

print("Caracterul apare de", numar_aparitii(text, ch), "ori.")