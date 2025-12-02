valoarea_monedei = [1, 5, 10, 25, 50]
def returnschimb(schimb, valoarea_monedei):
  returneaza = [0] * len(valoarea_monedei)

  for pos, moneda in enumerate(reversed(valoarea_monedei)):
    while moneda <= schimb:
     schimb = schimb - moneda
     returneaza[pos] +=1
  return(returneaza)
suma=float(input('Dati suma necesara='))
print('Valoarea monedei',[50,25,10,5,1])
print('Numarul de monede',returnschimb(suma,
valoarea_monedei))

bancnote = [1,2,5,10,20,50,100,200,500,1000]

def schimb(suma, bancnote):
    rezultat = [0] * len(bancnote)
    for i, b in enumerate(bancnote):
        while b <= suma:
            suma -= b
            rezultat[i] += 1
    return rezultat

suma = int(input("Introdu salariul: "))
print("Bancnote:", bancnote)
print("Numar:", schimb(suma, bancnote))