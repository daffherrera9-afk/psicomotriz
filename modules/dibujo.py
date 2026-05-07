from voz import hablar

def dar_instrucciones():
    hablar("Bienvenido al juego Dibujo con Movimiento. Usa tu dedo indice frente a la camara para dibujar. Elige un color y comienza tu obra de arte.")

def cambiar_color(color):
    hablar(f"Seleccionaste el color {color}")

def dibujo_guardado():
    hablar("Tu dibujo fue guardado. Que bonita obra de arte!")

def lienzo_limpiado():
    hablar("Lienzo limpio. Listo para un nuevo dibujo!")