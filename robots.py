import random

class Robot:
    def __init__(self, nombre, bateria, escudo, vida):
        self.nombre = nombre
        self.bateria = bateria
        self.escudo = escudo
        self.vida = vida

    def esta_vivo(self):
        return self.vida > 0

    def recibir_daño(self, daño):
        print(f"{self.nombre} recibe {daño} de daño.")

        if self.escudo >= daño:
            self.escudo -= daño
        else:
            daño_restante = daño - self.escudo
            self.escudo = 0
            self.vida -= daño_restante

        if self.vida < 0:
            self.vida = 0

    def mostrar_estado(self):
        print(f"{self.nombre} -> Vida: {self.vida}, Escudo: {self.escudo}, Batería: {self.bateria}")


class RobotAtaque(Robot):
    def atacar(self, objetivo):
        if self.bateria < 10:
            print(f"{self.nombre} no tiene suficiente batería para atacar.")
            return

        daño = random.randint(8, 15)
        self.bateria -= 10

        print(f"{self.nombre} ataca a {objetivo.nombre} ⚔️")
        objetivo.recibir_daño(daño)


class RobotDefensa(Robot):
    def recargar(self):
        if self.bateria < 8:
            print(f"{self.nombre} no tiene suficiente batería para recargar.")
            return

        aumento = random.randint(10, 20)
        self.escudo += aumento
        self.bateria -= 8

        print(f"{self.nombre} recarga su escudo en {aumento} puntos 🛡️")

    def reparar(self):
        if self.bateria < 12:
            print(f"{self.nombre} no tiene batería para repararse.")
            return

        cura = random.randint(8, 15)
        self.vida += cura
        self.bateria -= 12

        print(f"{self.nombre} se repara {cura} puntos ❤️")


# ---------------- JUEGO ----------------

def turno_robot_ataque(robot, objetivo):
    print(f"\nTurno de {robot.nombre} (Ataque)")
    accion = input("¿Qué quieres hacer? (1: Atacar, 2: Pasar): ")

    if accion == "1":
        robot.atacar(objetivo)
    else:
        print(f"{robot.nombre} decide no hacer nada.")


def turno_robot_defensa(robot):
    print(f"\nTurno de {robot.nombre} (Defensa)")
    accion = input("¿Qué quieres hacer? (1: Recargar, 2: Reparar, 3: Pasar): ")

    if accion == "1":
        robot.recargar()
    elif accion == "2":
        robot.reparar()
    else:
        print(f"{robot.nombre} decide no hacer nada.")


def juego():
    print("=== 🤖 BATALLA DE ROBOTS 🤖 ===")

    nombre1 = input("Nombre del robot de ataque: ")
    nombre2 = input("Nombre del robot de defensa: ")

    r1 = RobotAtaque(nombre1, bateria=1000, escudo=100, vida=100)
    r2 = RobotDefensa(nombre2, bateria=50, escudo=100, vida=100)

    turno = 1

    while r1.esta_vivo() and r2.esta_vivo():
        print(f"\n====== TURNO {turno} ======")

        r1.mostrar_estado()
        r2.mostrar_estado()

        turno_robot_ataque(r1, r2)
        if not r2.esta_vivo():
            break

        turno_robot_defensa(r2)

        turno += 1

    print("\n=== FIN DEL JUEGO ===")
    r1.mostrar_estado()
    r2.mostrar_estado()

    if r1.esta_vivo():
        print(f"🏆 {r1.nombre} gana!")
    else:
        print(f"🏆 {r2.nombre} gana!")


# Ejecutar juego
if __name__ == "__main__":
    juego()