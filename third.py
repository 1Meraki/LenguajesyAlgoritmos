print("¡Bienvenidx!")
a=input("Por favor, escribe tres números a continuación:")
b=input()
c=input()


def num_max_min(a,b,c):
    if a>b>c:
        print("El mayor es", a ," y el menor es", c)
    elif a>c>b:
        print("El mayor es", a ,"y el menor es", b)
    elif b>a>c:
        print("El mayor es", b ,"y el menor es", c)
    elif b>c>a:
        print("El mayor es", b ,"y el menor es", a)
    elif c>a>b:
        print("El mayor es", c ,"y el menor es", b)
    elif c>b>a:
        print("El mayor es", c ,"y el menor es", a)
    else: 
        print("Los números ingresados son iguales.")

num_max_min(a,b,c)
