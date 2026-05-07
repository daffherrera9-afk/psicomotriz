from voz import hablar

puzzles = [
    {
        "id": 1,
        "nombre": "El Sol",
        "emoji": "☀️",
        "descripcion": "Un sol brillante",
        "piezas": 9,
        "color": "#FEF3C7"
    },
    {
        "id": 2,
        "nombre": "El Arcoíris",
        "emoji": "🌈",
        "descripcion": "Un arcoíris colorido",
        "piezas": 9,
        "color": "#EDE9FE"
    },
    {
        "id": 3,
        "nombre": "La Casa",
        "emoji": "🏠",
        "descripcion": "Una casa bonita",
        "piezas": 9,
        "color": "#DCFCE7"
    }
]

def dar_instrucciones():
    hablar("Bienvenido al Rompecabezas Interactivo. Arrastra cada pieza hacia su lugar correcto para completar la imagen sorpresa. Vamos alla!")

def pieza_correcta(numero):
    hablar(f"Muy bien! Pieza {numero} en su lugar. Sigue asi!")

def pieza_incorrecta():
    hablar("Esa pieza no va ahi. Intentalo de nuevo!")

def puzzle_completado(nombre):
    hablar(f"Felicidades! Completaste el rompecabezas. Es {nombre}! Eres increible!")