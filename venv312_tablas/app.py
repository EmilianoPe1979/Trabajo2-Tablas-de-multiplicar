#***************************************#
# CENTRO DE BIOTECNOLOGIA AGROPECUARIA  #
# NOMBRE EMILIANO PERILLA AGUILAR       #
# VERSION : 3.0                         #
# Fecha: 07/06/2024                     #
#***************************************#

#Este es un programa cuya funcionalidad es mostrar tablas de multiplicar de manera aleatoria
# el numero de la tabla a multiplicar es generador aleatoriamente por randint y el rrecorido 
# es generado atrvez de un bucle for.

from random import randint # # Importo randit genera numeros aleatorios
from colorama import Fore,Back # Importo colorama para color fondo y fuente
from modulos import funcion as fun # Importo modulo tablas_mult


# from modulos import funcion1 as fan # Importo modulo respuesta
def main():
  print(Fore.BLACK + Back.BLUE)# Defino colores fondo y fuente 
  num=randint (1,15) 
  fun.tablas_multi(num) # Llamado modulo tablas_mult

  
if __name__=="__main__":
  main()







