from funciones import *
import helpers
import menu


def inicio():

    finalizar= False
    helpers.clear() #Limpia la terminal

    while (not finalizar):
        opcion = menu.menu()
        if opcion==1:
            
            edad_media(citizens)
            print()
            education(citizens)
            print()
            tipos_educacion(citizens)
            print()
            tipos_ocupacion(citizens)
            print()
            lista_diccionarios(citizens)
            print()
            salario_medio_ocupacion(citizens)
            print()
            salario_medio_educacion(citizens)
            print()
            lista_diccionarios_ocupacion(citizens)
            print()
            lista_diccionarios_ocupacion_lambda(citizens)
            print()
            lista_cadenas(citizens)



    print(Fore.GREEN  + "Nos vemos otro dia :)")
    print(Fore.WHITE)




