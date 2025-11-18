def dictionairy():    
	key_value = {}        
	key_value[2] = 56    
	key_value[1] = 2    
	key_value[5] = 12    
	key_value[4] = 24    
	key_value[6] = 18    
	key_value[3] = 323        

	print("key_value", key_value)     

	for i in sorted(key_value.keys()):        
		print(i, end=" ") 
def main():   
	dictionairy() 

if __name__ == "__main__":    
		main()
print('-cheile sortate in ordine crescatoare')


def dictionairy_2():
    key_value = {}
    key_value[2] = '56'
    key_value[1] = '2'
    key_value[4] = '12'
    key_value[5] = '24'
    key_value[6] = '18'
    key_value[3] = '323'

    lista_sortata = sorted(key_value.keys())
    for i in lista_sortata:
        print(key_value[i], end=" ")

def main():
    dictionairy_2()

if __name__ == "__main__":
    main()
print('-valorile sortate in ordine crescatoare dupa cheie')


def dictionairy_3():
    key_value = {}
    key_value[2] = '56'
    key_value[1] = '2'
    key_value[4] = '12'
    key_value[5] = '24'
    key_value[6] = '18'
    key_value[3] = '323'

    for k in sorted(key_value.keys()):
        print(k, end=" ")
    print()

    for v in sorted(key_value.values(), key=lambda x: int(x)):
        print(v, end=" ")

def main():
    dictionairy_3()

if __name__ == "__main__":
    main()
print('-cheile sortate in ordine crescatoare dupa valoare')

def dictionairy_4():
    key_value = {}
    key_value[2] = '56'
    key_value[1] = '2'
    key_value[4] = '12'
    key_value[5] = '24'
    key_value[6] = '18'
    key_value[3] = '323'

    lista = list(key_value.items())
    lista_sortata = sorted(lista, key=lambda x: int(x[1]))
    print(lista_sortata)

def main():
    dictionairy_4()

if __name__ == "__main__":
    main()
print('-valorile sortate im ordine crescatoare dupa cheie sii valoare')

