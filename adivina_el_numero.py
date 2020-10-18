
import random

def run():
    numerorandom = random.randint(1, 10)
    print(" - Tienes 4 Vidas -"
        "  ")
    numeroelegido = int(input("Introduce un numero del 1 a el 10: "))
    vidas = 4
    while numerorandom != numeroelegido :
        if numerorandom < numeroelegido : 
            print("Elige un numero mas pequeño.")
            vidas -= 1
        elif numerorandom > numeroelegido : 
            print("Elige un numero mas grande.")
            vidas -= 1
        if vidas == 0 :
            print("GAME OVER")
            break
        print("Tienes", vidas, "vidas")
        numeroelegido = int(input("Introduce numero: "))
    if numerorandom == numeroelegido : 
        print("FELICIDADES GANASTE")


if __name__ == "__main__" : 
    run()