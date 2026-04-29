class Robot:
    def __init__(self, nombre, bateria, escudo):
        self.nombre = nombre
        self.bateria = bateria
        self.escudo = escudo

    def mostrar_estado(self):
        print(f"{self.nombre} | Batería: {self.bateria} | Escudo: {self.escudo}")


class RobotAtaque(Robot):
    def atacar(self, objetivo):
        if self.bateria >= 10:
            daño = 15
            objetivo.escudo -= daño
            self.bateria -= 10
            print(f"{self.nombre} ataca a {objetivo.nombre} causando {daño} de daño.")
        else:
            print(f"{self.nombre} no tiene suficiente batería para atacar.")


class RobotDefensa(Robot):
    def recargar(self):
        aumento = 20
        self.escudo += aumento
        self.bateria -= 5
        print(f"{self.nombre} recarga su escudo en {aumento} puntos.")


# Ejemplo de uso
r1 = RobotAtaque("Destructor", 50, 40)
r2 = RobotDefensa("Protector", 50, 60)

r1.mostrar_estado()
r2.mostrar_estado()

r1.atacar(r2)
r2.recargar()

r1.mostrar_estado()
r2.mostrar_estado()