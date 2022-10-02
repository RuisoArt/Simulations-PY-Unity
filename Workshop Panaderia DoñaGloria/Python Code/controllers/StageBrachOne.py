import time
import models.Button as btn
import models.Machines as mch
import models.Tasks as w

button = btn.Button(pulsador_marcha=False)
work = w.Tasks(W1=False, W2=False, W3=False, W4=False, W5=False)
machine = mch.Machines(A1=False,A2=False)

class StageBrachOne():

    def stage_0():
        print("")
        print("----------------------------------------------------------------")
        print("                         Etapa 0")
        print("----------------------------------------------------------------")
        print("")
        print("Estados de la variables iniciales")
        print("Boton de Marcha, estado: {}".format(button.pulsador_marcha))
        print("Tarea o Proceso [W1], estado: {}".format(work.W1))
        print("Tarea o Proceso [W2], estado: {}".format(work.W2))
        print("Tarea o Proceso [W2], estado: {}".format(work.W3))
        print("Tarea o Proceso [W2], estado: {}".format(work.W4))
        print("Tarea o Proceso [W2], estado: {}".format(work.W5))
        print("Tanque o Maquina [A1], estado: {}".format(machine.A1))
        print("Tanque o Maquina [A1], estado: {}".format(machine.A2))
        print("")
        print("----------------------------------------------------------------")
        time.sleep(1)
        print("")
        print("----------------------------------------------------------------")
        print("Inicianco proceso en 5 segundos")
        print("----------------------------------------------------------------")
        print("")
        time.sleep(5)
        button.pulsador_marcha = True
        print("")
        print("----------------------------------------------------------------")
        print("Boton Marcha, estado: {}".format(button.pulsador_marcha))
        print("----------------------------------------------------------------")
        print("")
        time.sleep(1)
    
    def stage_1():
        print("")
        print("----------------------------------------------------------------")
        print("                         Etapa 1")
        print("----------------------------------------------------------------")
        print("")
        machine.A1 = True
        work.W1 = True
        print(" Se prende Tanque [A1]: [{}]".format(machine.A1))
        print(" Se inicia Tarea [W1]: [{}]".format(work.W1))
        print(" Inicia Temporizador T1[30s]")
        print("")
        for i in range(0,30):
            print(i+1)
            time.sleep(0.25)
        print("")
        print("T1[30s]: Finalizado")
        time.sleep(1)
        print("----------------------------------------------------------------")
    
    def stage_2():
        print("")
        print("----------------------------------------------------------------")
        print("                         Etapa 2")
        print("----------------------------------------------------------------")
        print("")
        machine.A2 = True
        work.W2 = True
        print(" Se prende Tanque [A2]: [{}]".format(machine.A2))
        print(" Se inicia Tarea [W2]: [{}]".format(work.W2))
        print(" Inicia Temporizador T2[40s]")
        print("")
        for i in range(0,40):
            print(i+1)
            time.sleep(0.25)
        print("")
        print("T2[40s]: Finalizado")
        time.sleep(0.25)
        print("----------------------------------------------------------------")
    
    def stage_3():
        print("")
        print("----------------------------------------------------------------")
        print("                         Etapa 3")
        print("----------------------------------------------------------------")
        print("")
        work.W1 = False
        machine.A1 = False
        print("Finaliza trabajo [W1][{}]  Se apaga ataque[A1][{}]".format(work.W1 , machine.A1))
        print("----------------------------------------------------------------")
    
    def stage_4():
        print("")
        print("----------------------------------------------------------------")
        print("                         Etapa 4")
        print("----------------------------------------------------------------")
        print("")
        work.W2 = False
        machine.A2 = False
        print("Finaliza trabajo [W2][{}]  Se apaga ataque[A2][{}]".format(work.W2 , machine.A2))
        print("----------------------------------------------------------------")
    
    def stage_5():
        print("")
        print("----------------------------------------------------------------")
        print("                         Etapa 5")
        print("----------------------------------------------------------------")
        print("")
        machine.A1 = True
        work.W3 = True
        print(" Se prende Tanque [A1]: [{}]".format(machine.A1))
        print(" Se inicia Tarea [W3]: [{}]".format(work.W3))
        print(" Inicia Temporizador T3[20s]")
        print("")
        for i in range(0,20):
            print(i+1)
            time.sleep(0.25)
        print("")
        print("T3[20s]: Finalizado")
        print("----------------------------------------------------------------")

    def stage_6():
        print("")
        print("----------------------------------------------------------------")
        print("                         Etapa 6")
        print("----------------------------------------------------------------")
        print("")
        work.W1 = True
        machine.A2 = True
        print(" Se prende Tanque [A2]: [{}]".format(machine.A2))
        print(" Se inicia Tarea [W1]: [{}]".format(work.W1))
        print(" Inicia Temporizador T4[50s]")
        print("")
        for i in range(0,50):
            print(i+1)
            time.sleep(0.25)
        print("")
        print("T4[50s]: Finalizado")
        print("----------------------------------------------------------------")

    def stage_7():
        print("")
        print("----------------------------------------------------------------")
        print("                         Etapa 7")
        print("----------------------------------------------------------------")
        print("")
        machine.A1 = False
        work.W3 = False
        print("Finaliza trabajo [W3][{}]  Se apaga ataque[A1][{}]".format(work.W3 , machine.A1))
        print("----------------------------------------------------------------")

    def stage_8():
        print("")
        print("----------------------------------------------------------------")
        print("                         Etapa 8")
        print("----------------------------------------------------------------")
        print("")
        work.W1 = False
        machine.A2 = False
        print("Finaliza trabajo [W1][{}]  Se apaga ataque[A2][{}]".format(work.W1 , machine.A2))
        print("----------------------------------------------------------------")

    def stage_9():
        print("")
        print("----------------------------------------------------------------")
        print("                         Etapa 9")
        print("----------------------------------------------------------------")
        print("")
        machine.A1 = True
        work.W4 = True
        print(" Se prende Tanque [A1]: [{}]".format(machine.A1))
        print(" Se inicia Tarea [W4]: [{}]".format(work.W4))
        print(" Inicia Temporizador T5[30s]")
        print("")
        for i in range(0,30):
            print(i+1)
            time.sleep(0.25)
        print("")
        print("T5[30s]: Finalizado")
        print("----------------------------------------------------------------")

    def stage_10():
        print("")
        print("----------------------------------------------------------------")
        print("                         Etapa 10")
        print("----------------------------------------------------------------")
        print("")
        machine.A2 = True
        work.W3 = True
        print(" Se prende Tanque [A2]: [{}]".format(machine.A2))
        print(" Se inicia Tarea [W3]: [{}]".format(work.W3))
        print(" Inicia Temporizador T6[70s]")
        print("")
        for i in range(0,70):
            print(i+1)
            time.sleep(0.25)
        print("")
        print("T6[70s]: Finalizado")
        print("----------------------------------------------------------------")

    def stage_11():
        print("")
        print("----------------------------------------------------------------")
        print("                         Etapa 11")
        print("----------------------------------------------------------------")
        print("")
        machine.A1 = False
        work.W4 = False
        print("Finaliza trabajo [W4][{}]  Se apaga ataque[A1][{}]".format(work.W4 , machine.A1))
        print("----------------------------------------------------------------")
    
    def stage_12():
        print("")
        print("----------------------------------------------------------------")
        print("                         Etapa 12")
        print("----------------------------------------------------------------")
        print("")
        machine.A2 = False
        work.W3 = False
        print("Finaliza trabajo [W3][{}]  Se apaga ataque[A2][{}]".format(work.W3 , machine.A2))
        print("----------------------------------------------------------------")
    
    def stage_13():
        print("")
        print("----------------------------------------------------------------")
        print("                         Etapa 13")
        print("----------------------------------------------------------------")
        print("")
        machine.A1 = True
        work.W5 = True
        print(" Se prende Tanque [A1]: [{}]".format(machine.A1))
        print(" Se inicia Tarea [W5]: [{}]".format(work.W5))
        print(" Inicia Temporizador T7[50s]")
        print("")
        for i in range(0,50):
            print(i+1)
            time.sleep(0.25)
        print("")
        print("T7[50s]: Finalizado")
        print("----------------------------------------------------------------")

    def stage_14():
        print("")
        print("----------------------------------------------------------------")
        print("                         Etapa 14")
        print("----------------------------------------------------------------")
        print("")
        machine.A1 = False
        work.W5 = False
        print("Finaliza trabajo [W5][{}]  Se apaga ataque[A1][{}]".format(work.W5 , machine.A1))
        print("----------------------------------------------------------------")
    
    def stage_15():
        print("")
        print("----------------------------------------------------------------")
        print("                         Etapa 15")
        print("----------------------------------------------------------------")
        print("")
        machine.A2= True
        work.W5 = True
        print(" Se prende Tanque [A2]: [{}]".format(machine.A2))
        print(" Se inicia Tarea [W5]: [{}]".format(work.W5))
        print(" Inicia Temporizador T8[20s]")
        print("")
        for i in range(0,20):
            print(i+1)
            time.sleep(0.25)
        print("")
        print("T8[20s]: Finalizado")
        print("----------------------------------------------------------------")
    
    def stage_16():
        print("")
        print("----------------------------------------------------------------")
        print("                         Etapa 16")
        print("----------------------------------------------------------------")
        print("")
        machine.A2= False
        work.W5 = False
        print("Finaliza trabajo [W5][{}]  Se apaga ataque[A2][{}]".format(work.W5 , machine.A2))
        print("----------------------------------------------------------------")
        
                