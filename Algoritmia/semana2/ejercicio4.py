# Elabore programa en Python que le permita al usuario ingresar números enteros de manera indefinida, hasta que ingrese un número negativo, y al final imprimir la suma de los números enteros pares sin incluir el número negativo en la suma.

number = 0
sum_of_number = 0

while number >= 0:
  number = int(input("Input a number: "))
  if number % 2 == 0 and number > 0:
    sum_of_number +=  number

print(f"Sum of numbers: {sum_of_number}")    
