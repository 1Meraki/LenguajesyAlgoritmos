print("¡Bienvenidx!")
a=input("Por favor, escribe cuatro números a continuación:")
b=input()
c=input()
d=input()

def num_max(a,b,c,d):
    if a > b and a > c and c > d:
        print("El mayor es", a)
    elif b > a and b > c and b > d:
        print ("El mayor es", b)
    elif c > a and c > b and c > d:
        print ("El mayor es", c)
    elif d > a and d > b and d > c:   
        print ("El mayor es", d)
    else:
        print ("Los números son iguales")
    
num_max(a,b,c,d)