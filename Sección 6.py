class Atleta:
    def __init__(self, nombre, edad, pais):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais
        self.entrenamiento = 0
        self.descanso = 0
    def entrenar(self, tiempo):
        self.entrenamiento += tiempo

        def descansar(self, tiempo):
            self.descanso += tiempo
            def celebrar_victoria(self):
                print(f"{self.nombre} está celebrando su victoria!")


class Futbollista(Atleta):
    def __init__(self, nombre, edad, pais):
        super().__init__(nombre, edad, pais)
        self.equipo = equipo
        self.posicion = posicion

        def celebrar_victoria(self):
            print(f"{self.nombre} está celebrando la victoria con su equipo de fútbol en el estadio!")


class Tenista(Atleta):
    def __init__(self, nombre, edad, pais):
        super().__init__(nombre, edad, pais)
        self.grand_slams = grand_slams

        def celebrar_victoria(self):
            print(f"{self.nombre} está celebrando la victoria con una raqueta de tenis de mano")


# Crear objeto Atleta
atleta = Atleta("Usain Bolt", 35, "Jamaica")
atleta.entrenar(2)
atleta.descansar(1)
atleta.celebrar_victoria()

#Crear objeto Futbolista
futbolista = Futbolista("Lionel Messi", 34, "Argentina", "Paris Saint-Germain", "Delantero")
futbolista.entrenar(3)
futbolista.descansar(2)
futbolista.celebrar_victoria()

#Crear objeto Tenista
tenista = Tenista("Serena Williams", 40, "Estados Unidos", 23)
tenista.entrenar(1)
tenista.descansar(3)
tenista.celebrar_victoria()3