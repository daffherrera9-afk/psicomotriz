from voz import hablar

movimientos = [
    {"id": 1, "instruccion": "Toca tu cabeza",    "emoji": "🤚", "descripcion": "Lleva tu mano a la cabeza",  "parte_cuerpo": "cabeza"},
    {"id": 2, "instruccion": "Levanta los brazos", "emoji": "🙌", "descripcion": "Sube ambos brazos bien alto", "parte_cuerpo": "brazos"},
    {"id": 3, "instruccion": "Toca tu nariz",      "emoji": "👆", "descripcion": "Lleva tu dedo a la nariz",   "parte_cuerpo": "nariz"},
    {"id": 4, "instruccion": "Aplaude",            "emoji": "👏", "descripcion": "Junta tus dos manos",        "parte_cuerpo": "manos"},
    {"id": 5, "instruccion": "Toca tu barriga",    "emoji": "✋", "descripcion": "Lleva tu mano a la barriga", "parte_cuerpo": "barriga"}
]

def dar_instrucciones():
    hablar("Bienvenido al juego Imitar Movimientos. Escucha cada instruccion, espera la cuenta regresiva y haz el movimiento correcto. Vamos alla!")

def anunciar_movimiento(instruccion):
    hablar(f"Ahora debes: {instruccion}. Preparate!")

def contar(numero):
    hablar(str(numero))

def ya():
    hablar("Ya!")

def resultado_correcto(instruccion):
    hablar(f"Lo hiciste muy bien! Correcto!")

def resultado_incorrecto():
    hablar("Ese es el movimiento incorrecto. Vuelve a intentarlo!")

def juego_completado():
    hablar("Felicidades! Completaste todos los movimientos. Eres increible!")