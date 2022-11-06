#Numero de bucles
def bucles_teclado():
    while True:
        try:
            teclado = int( input( "Ingrese por favor el numero de bucles que desea: " ) )
            break
        except ValueError:
            print("El dato ingresado no es un numero, intentalo nuevamente ... ")

    return teclado

