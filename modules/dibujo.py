from voz import hablar

animales = [
    {"id":1,"nombre":"perro","emoji":"🐶","color":"azul"},
    {"id":2,"nombre":"conejo","emoji":"🐰","color":"verde"},
    {"id":3,"nombre":"tortuga","emoji":"🐢","color":"amarillo"}
]

colores = [
    {"id":1,"nombre":"rojo","hex":"#ef4444"},
    {"id":2,"nombre":"azul","hex":"#3b82f6"},
    {"id":3,"nombre":"verde","hex":"#22c55e"},
    {"id":4,"nombre":"amarillo","hex":"#eab308"}
]

def dar_instrucciones_animales():
    hablar("Bienvenido al juego Mover y Reconocer. Mueve tu mano y coloca cada animal en su lugar correcto.")

def dar_instrucciones_colores():
    hablar("Ahora reconoce los colores. Mueve cada color a su lugar correcto.")

def animal_correcto(nombre):
    hablar(f"Muy bien! Ese es el animal correcto. Es un {nombre}!")

def animal_incorrecto():
    hablar("Ese no es el lugar correcto. Vuelve a intentarlo!")

def color_correcto(nombre):
    hablar(f"Correcto! Ese es el color {nombre}!")

def color_incorrecto():
    hablar("Ese no es el color correcto. Intentalo de nuevo!")

def juego_completado():
    hablar("Felicidades! Completaste todos los animales y colores. Eres muy inteligente!")