class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0
        self.vidas = 3

    def get_estado(self):
        return f"NOMBRE: {self.nombre} NIVEL: {self.nivel} EXP: {self.experiencia} VIDAS: {self.vidas}"

    def set_estado(self, experiencia):
        temp_exp = self.experiencia + experiencia
        if temp_exp >= 500:
            self.vidas += 1
            print("¡Has ganado una vida extra!")
        self.experiencia = temp_exp
        self.nivel = temp_exp // 100 + 1

        if self.experiencia < 0:
            if self.vidas > 0:
                self.vidas -= 1
                self.experiencia = 0
                self.nivel = max(1, self.nivel - 1)
            else:
                print("¡Has muerto! El orco te ha matado. ¡Vuelve a jugar!")
                exit()

        if self.vidas == 0:
            print("¡Felicidades! ¡Has vencido al orco!")
            exit()

    def calcular_probabilidad_ganar(self, otro_personaje):
        if self.nivel < otro_personaje.nivel:
            return 33
        elif self.nivel > otro_personaje.nivel:
            return 66
        else:
            return 50

    @staticmethod
    def dialogo_enfrentamiento(probabilidad):
        print("¡Oh no!, ¡Ha aparecido un Orco!")
        print(f"Con tu nivel actual, tienes {probabilidad}% de probabilidades de ganarle al Orco.")
        print("Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.")
        print("Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.")
        opcion = int(input("¿Qué deseas hacer?\n1. Atacar\n2. Huir\n"))
        return opcion
