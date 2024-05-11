from personaje import Personaje
import random

def enfrentamiento(personaje_jugador, orco):
    probabilidad_ganar = personaje_jugador.calcular_probabilidad_ganar(orco)
    opcion = Personaje.dialogo_enfrentamiento(probabilidad_ganar)
    
    while opcion == 1:
        resultado_ataque = "Gana" if random.uniform(0, 1) <= probabilidad_ganar / 100 else "Perdi"
        if resultado_ataque == "Gana":
            personaje_jugador.set_estado(50)
            orco.set_estado(-30)
        else:
            personaje_jugador.set_estado(-30)
            orco.set_estado(50)
        print(f"¡Le has {resultado_ataque.lower()}do al orco, felicidades!")
        print(f"¡Recibirás {50 if resultado_ataque == 'Gana' else -30} puntos de experiencia!")
        print(personaje_jugador.get_estado())
        print(orco.get_estado())
        probabilidad_ganar = personaje_jugador.calcular_probabilidad_ganar(orco)
        opcion = Personaje.dialogo_enfrentamiento(probabilidad_ganar)

        if opcion != 1:
            break
    
    if opcion == 2:
        print("¡Has huido! El orco ha quedado atrás.")
    else:
        print("¡Te ha vencido el orco! ¡Vuelve a intentarlo!")

def main():
    print("¡Bienvenido a Gran Fantasía!")
    nombre_personaje = input("Por favor indique nombre de su personaje: ")
    personaje_jugador = Personaje(nombre_personaje)
    print(personaje_jugador.get_estado())

    orco = Personaje("Orco")
    enfrentamiento(personaje_jugador, orco)

if __name__ == "__main__":
    main()
