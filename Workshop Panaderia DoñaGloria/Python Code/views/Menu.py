import controllers.MyWorks

def run_processes():
    estado = True
        
    while (estado):
        print("")
        print("---------------------------------------------")
        print("          PASTELERIA DOÑA GLORIA")
        print("---------------------------------------------")
        print("")
        print(" Para iniciar el proceso o cerrar este       ")
        print(" programa ingresa a continuacion el numero ")
        print(" correspondiente")
        print("")
        print(" [1] Iniciar el proceso (M - Marcha)")
        print(" [2] Finalizar el programa")
        print("")
        print("---------------------------------------------")
        print("")

        while True:
            try:
                teclado = int(input("Escribe aqui tu seleccion: "))
                break
            except ValueError:
                print("Error ingresado, vuelva a intentar.")

        if teclado == 1:
            print("")
            print("---------------------------------------------")
            print("Inicia el proceso . . .")
            print("---------------------------------------------")
            print("")
            controllers.MyWorks.my_works.this_process()

        elif teclado == 2:
            print("")
            print("---------------------------------------------")
            print("Finaliza el programa, nos vemos luego")
            print("---------------------------------------------")
            print("")
            estado = False

        else:
            print("")
            print("---------------------------------------------")
            print("Opcion equivocada, vuelve a intentarlo")
            print("---------------------------------------------")
            print("")
    
