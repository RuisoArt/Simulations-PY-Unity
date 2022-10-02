import time
import controllers.StageBrachOne as stage

class my_works():
    def this_process():
        _estado = True

        while(_estado):
            print("")
            print("----------------------------------------------------------------")
            print("Se inicio el proceso, operarios en alerta del proceso Industrial")
            print("----------------------------------------------------------------")
            print("")
            time.sleep(1)
            stage.StageBrachOne.stage_0()
            stage.StageBrachOne.stage_1()
            stage.StageBrachOne.stage_2()
            stage.StageBrachOne.stage_3()
            stage.StageBrachOne.stage_4()
            stage.StageBrachOne.stage_5()
            stage.StageBrachOne.stage_6()
            stage.StageBrachOne.stage_7()
            stage.StageBrachOne.stage_8()
            stage.StageBrachOne.stage_9()
            stage.StageBrachOne.stage_10()
            stage.StageBrachOne.stage_11()
            stage.StageBrachOne.stage_12()
            stage.StageBrachOne.stage_13()
            stage.StageBrachOne.stage_14()
            stage.StageBrachOne.stage_15()
            stage.StageBrachOne.stage_16()
            time.sleep(1)

            teclado = input("Ingresa [yes] para terminar la ejecucion: ")
            if teclado != "yes":
                print("")
                print("----------------------------------------------------------------")
                print("Se reanuda la ejecucion del proceso")
                print("----------------------------------------------------------------")
                print("")
                time.sleep(3)
                continue
            elif teclado == "yes":
                print("")
                print("----------------------------------------------------------------")
                print("Se Finalizo el proceso, regresando a menu de arranque")
                print("----------------------------------------------------------------")
                print("")
                time.sleep(3)
                _estado = False
            else:
                print("AJA")
        
        

