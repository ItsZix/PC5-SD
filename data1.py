class Cancha:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
        self.reservada = False

class Usuario:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
        self.reserva = None  # Ahora es un diccionario para almacenar más detalles
        # Agrega más atributos según sea necesario
        self.numero_cancha_reservada = None
        self.fecha_hora_reserva = None

# Base de datos simulada
base_de_datos = {
    "70398195": Usuario("Sofia Bobadilla", "70398195"),
    "98765432": Usuario("Ana González", "98765432"),
    "75998960": Usuario("Alvaro De la Cruz", "75998960"),
    "73340787": Usuario("Anghelo Silva", "73340787"),
    "70878872": Usuario("Jamil Casaverde", "70878872"),
    "78546906": Usuario("Ubaldo Olazábal", "78546906"),
    # Agrega más usuarios según sea necesario
}

canchas = [Cancha(i, "futbol") for i in range(1, 6)]  # 5 canchas de fútbol
