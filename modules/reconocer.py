import threading
import os
from gtts import gTTS
import pygame

pygame.mixer.init()

AUDIO_DIR = os.path.join(os.path.dirname(__file__), '..', 'static', 'audio')
os.makedirs(AUDIO_DIR, exist_ok=True)

def hablar(texto, archivo_id="voz"):
    def _hablar():
        try:
            ruta = os.path.join(AUDIO_DIR, f"{archivo_id}.mp3")
            tts = gTTS(text=texto, lang='es', slow=False)
            tts.save(ruta)
            pygame.mixer.music.load(ruta)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        except Exception as e:
            print(f"Error de voz: {e}")
    t = threading.Thread(target=_hablar)
    t.daemon = False
    t.start()
    t.join(timeout=10)  # ← Espera hasta 10 segundos a que termine

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
    hablar("Bienvenido a Mover y Reconocer. Arrastra cada animal hacia su sombra correcta. ¡Vamos allá!", "instruccion_animales")

def dar_instrucciones_colores():
    hablar("Ahora vamos con los colores. Arrastra cada color hacia su lugar correcto. ¡Tú puedes!", "instruccion_colores")

def animal_correcto(nombre):
    hablar(f"¡Muy bien! Ese es el animal correcto. Es un {nombre}. ¡Excelente!", f"animal_{nombre}")

def animal_incorrecto():
    hablar("Ese no es el lugar correcto. ¡Inténtalo de nuevo!", "animal_incorrecto")

def color_correcto(nombre):
    hablar(f"¡Correcto! Ese es el color {nombre}. ¡Muy bien hecho!", f"color_{nombre}")

def color_incorrecto():
    hablar("Ese color no va ahí. ¡Vuelve a intentarlo!", "color_incorrecto")

def juego_completado():
    hablar("¡Felicidades! Completaste todos los animales y colores. ¡Eres un campeón!", "completado")