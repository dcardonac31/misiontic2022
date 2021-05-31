# Elabore un programa en Python que lea un entero de tres dígitos y produzca como salida los dígitos del número leído con su correspondiente mensaje. Por ejemplo, si el número leído es 271, la salida deberá ser (sin texto adicional):
# 2
# 7
# 1

number = int(input("input three-digit number: "))
# while number < 100 or number > 999:
#   number = int(input("input three-digit number: "))

str_number = str(number)

for item in str_number:
  print(item)