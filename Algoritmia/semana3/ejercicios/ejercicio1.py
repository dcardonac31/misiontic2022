from classVector import Vector
import random
import math


def solucion():
    n = random.randint(15, 30)
    vec1 = Vector(n)
    for i in range(1,n):
        vec1.V[i] = random.randint(1, 29)

    vec1mod = vec1
    for i in range(1,n):
        print(vec1.V[i])
    print("-------------------")
    for i in range(1,n):
        print(vec1mod.V[i])

    #vec1mod.intercambiar(vec1mod.mayor(),vec1mod.menor())


    return vec1, vec1mod


if __name__ == '__main__':
    solucion()
