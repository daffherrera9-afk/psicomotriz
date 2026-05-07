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
    t.join(timeout=10)

# Rompecabezas disponibles
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
    hablar("Bienvenido al Rompecabezas Interactivo. Arrastra cada pieza hacia su lugar correcto para completar la imagen sorpresa. ¡Vamos allá!", "rompe_instrucciones")

def pieza_correcta(numero):
    hablar(f"¡Muy bien! Pieza {numero} en su lugar. ¡Sigue así!", f"rompe_pieza_{numero}")

def pieza_incorrecta():
    hablar("Esa pieza no va ahí. ¡Inténtalo de nuevo!", "rompe_incorrecta")

def puzzle_completado(nombre):
    hablar(f"¡Felicidades! Completaste el rompecabezas. ¡Es {nombre}! ¡Eres increíble!", "rompe_completado")