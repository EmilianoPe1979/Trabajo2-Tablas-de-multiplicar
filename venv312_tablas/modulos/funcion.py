#***************************************#
# CENTRO DE BIOTECNOLOGIA AGROPECUARIA  #
# NOMBRE EMILIANO PERILLA AGUILAR       #
# VERSION : 3.0                         #
# Fecha: 07/06/2024                     #
#***************************************#

#Este es un programa cuya funcionalidad es mostrar tablas de multiplicar de manera aleatoria
# el numero de la tabla a multiplicar es generador aleatoriamente por randint y el rrecorido 
# es generado atrvez de un bucle for.


def tablas_multi(num): # Defino funcion tablas_multi
  print("\nLas tablas de Multiplicar")
  print(f"El numero aleatorio es:  {num}") # Genera numero de aleatorio de la tablas a mostrar
  # input ("Oprima enter...")
  print()
  for j in range (1,num+1): # De acuerdo al numero aleatorio muestra la cantidad de tablas 
    input ("Presione enter para continuar...")
    for i in range (11): # Genera la tabla multiplicando del 1 al 10
      print(f"{j} x {i} = {j*i}") # Operacion conjunta de tabla y cantidad de tablas  











