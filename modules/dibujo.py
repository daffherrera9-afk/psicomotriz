import pyttsx3
import threading

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')
for voice in voices:
    if 'spanish' in voice.name.lower() or 'es' in voice.id.lower():
        engine.setProperty('voice', voice.id)
        break

def hablar(texto):
    def _hablar():
        engine.say(texto)
        engine.runAndWait()
    t = threading.Thread(target=_hablar)
    t.daemon = True
    t.start()

def dar_instrucciones():
    hablar("Bienvenido al juego Dibujo con Movimiento. Usa tu dedo índice frente a la cámara para dibujar. Elige un color y comienza tu obra de arte. ¡Diviértete!")

def cambiar_color(color):
    hablar(f"Seleccionaste el color {color}")

def dibujo_guardado():
    hablar("¡Tu dibujo fue guardado! ¡Qué bonita obra de arte!")

def lienzo_limpiado():
    hablar("Lienzo limpio. ¡Listo para un nuevo dibujo!")