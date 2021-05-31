# Elabore programa en Python que lea el nombre, la estatura (metros) y el peso (kg) de una persona que calcule y muestre el índice de masa corporal de dicha persona. Asuma la estatura y el peso como números reales.

name = input("Input the name: ")
height = float(input("Input the height: "))
weight = float(input("Input the weight: "))

imc = weight / height ** 2

print(f"IMC: {imc}")