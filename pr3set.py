U = set(range(200))

X = set(range(0,200,4))
Y = set(range(0,200,6))
Z = set(range(0,200,9))

Xc = U - X
Yc = U - Y
Zc = U - Z

stanga1 = U - (X | Y | Z)
dreapta_1 = Xc & Yc & Zc
stanga2 = U - (X & Y & Z)
dreapta2 = Xc | Yc | Zc

print('a) Legea 1 este',stanga1== dreapta_1)
print('a) Legea 1 este',stanga2== dreapta2)