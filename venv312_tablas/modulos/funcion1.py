
from random import randint # Importo randit genera numeros aleatorios
num=randint (1,15) # Rango de numeros aleatorios entre 1 y 15 
from modulos import funcion as fun  # Importo la funcion tablas_multi

def respuesta(): # Defino la funcion respuesta 
    
    while True: # Bucle para repetir la operacion de las tablas 
        # num=randint (1,15)  # Llamo generador de numeros aleatorios
        respuesta = input ("Desea continuar con el ejercicio de las tablas enter:  ")
        # Pregunta si deseo o no continuar con la operacion de tablas

        while respuesta not in ["si", "no"]:# Este bucle me condiciona SI/NO para
        #   print("Ingrese si o no")          # seguir o no generando las tablas
          respuesta = control_letras("Digite si/no: ")
        # Se define la respuesta SI/NO 

        if respuesta == "si": # Respuesta SI llame tablas_multi
          fun.tablas_multi()
            
        elif respuesta == "no": # Respuesta NO fin del programa 
            print("FIN DEL PROGRAMA")
            break       # En cado de respuesta NO el brake rompe el programa    
        else:
            continue    # En caso contrario continue el programa
            break

def control_letras(prompt):
    while True:
      entrada = input(prompt)
      if (entrada.replace("","").isalpha()):
        break
      else:
        print("Solo digite caracteres alfabeticos")
    return entrada