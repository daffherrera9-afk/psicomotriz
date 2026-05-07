from voz import hablar

animales = [
    {"id": 1, "nombre": "Perro",     "emoji": "🐶", "sombra": "🐕", "color_fondo": "#FEF3C7"},
    {"id": 2, "nombre": "Gato",      "emoji": "🐱", "sombra": "🐈", "color_fondo": "#FEE2E2"},
    {"id": 3, "nombre": "Conejo",    "emoji": "🐰", "sombra": "🐇", "color_fondo": "#F3E8FF"},
    {"id": 4, "nombre": "Pato",      "emoji": "🐥", "sombra": "🦆", "color_fondo": "#ECFCCB"},
    {"id": 5, "nombre": "Elefante",  "emoji": "🐘", "sombra": "🐘", "color_fondo": "#E0F2FE"},
]

colores = [
    {"id": 1, "nombre": "Rojo",     "hex": "#EF4444", "emoji": "🔴"},
    {"id": 2, "nombre": "Azul",     "hex": "#3B82F6", "emoji": "🔵"},
    {"id": 3, "nombre": "Amarillo", "hex": "#EAB308", "emoji": "🟡"},
    {"id": 4, "nombre": "Verde",    "hex": "#22C55E", "emoji": "🟢"},
    {"id": 5, "nombre": "Morado",   "hex": "#A855F7", "emoji": "🟣"},
]

def dar_instrucciones_animales():
    hablar("Bienvenido a Mover y Reconocer. Arrastra cada animal hacia su sombra correcta. Vamos alla!")

def dar_instrucciones_colores():
    hablar("Ahora vamos con los colores. Arrastra cada color hacia su lugar correcto. Tu puedes!")

def animal_correcto(nombre):
    hablar(f"Muy bien! Ese es el animal correcto. Es un {nombre}. Excelente!")

def animal_incorrecto():
    hablar("Ese no es el lugar correcto. Intentalo de nuevo!")

def color_correcto(nombre):
    hablar(f"Correcto! Ese es el color {nombre}. Muy bien hecho!")

def color_incorrecto():
    hablar("Ese color no va ahi. Vuelve a intentarlo!")

def juego_completado():
    hablar("Felicidades! Completaste todos los animales y colores. Eres un campeon!")