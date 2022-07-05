print("¡Bienvenidx!")

numo=input("Escribe un número:")
numt=input("Escribe otro número:")

def menorque(numo, numt):
    if numo > numt:
        print ("El mayor es", numo )
    elif numt > numo:
        print ("El mayor es", numt)
    else:
        print ("Los números son iguales.")

menorque(numo, numt)