def vonNeumann(u):
    i = 0
    a = u
    while(i<11):
        a = ((a**2 // 100) % 10000)
        print(f'{a}, ')
        i += 1
def congruencial(u):
    i = 0
    a = u
    numeros = set()
    lenght_index = 0
    flag = False
    while(i<11):
        numeros.add(a)
        a = ((5 * a + 4) % (2**5))
        if((a in numeros) and (not flag)):
            lenght_index = i +1
            flag = True
        print(f'{a}, ')
        i += 1
    print(f'periodo de {lenght_index}')

while(True):
    i = input('semilla \n')
    congruencial(int(i))
#    vonNeumann(int(i))
