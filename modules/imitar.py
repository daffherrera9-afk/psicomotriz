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

movimientos = [
    {"id": 1, "instruccion": "Toca tu cabeza",    "emoji": "🤚", "descripcion": "Lleva tu mano a la cabeza",  "parte_cuerpo": "cabeza"},
    {"id": 2, "instruccion": "Levanta los brazos", "emoji": "🙌", "descripcion": "Sube ambos brazos bien alto", "parte_cuerpo": "brazos"},
    {"id": 3, "instruccion": "Toca tu nariz",      "emoji": "👆", "descripcion": "Lleva tu dedo a la nariz",   "parte_cuerpo": "nariz"},
    {"id": 4, "instruccion": "Aplaude",            "emoji": "👏", "descripcion": "Junta tus dos manos",        "parte_cuerpo": "manos"},
    {"id": 5, "instruccion": "Toca tu barriga",    "emoji": "✋", "descripcion": "Lleva tu mano a la barriga", "parte_cuerpo": "barriga"}
]

def dar_instrucciones():
    hablar("Bienvenido al juego Imitar Movimientos. Escucha cada instrucción, espera la cuenta regresiva y haz el movimiento correcto. ¡Vamos allá!", "bienvenida")

def anunciar_movimiento(instruccion):
    hablar(f"Ahora debes: {instruccion}. ¡Prepárate!", f"mov_{instruccion[:10]}")

def contar(numero):
    try:
        ruta = os.path.join(AUDIO_DIR, f"numero_{numero}.mp3")
        pygame.mixer.music.load(ruta)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(f"Error contando: {e}")

def ya():
    try:
        ruta = os.path.join(AUDIO_DIR, "ya.mp3")
        pygame.mixer.music.load(ruta)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(f"Error ya: {e}")

def resultado_correcto(instruccion):
    hablar(f"¡Lo hiciste muy bien! {instruccion} ¡Correcto!", "correcto")

def resultado_incorrecto():
    hablar("Ese es el movimiento incorrecto. ¡Vuelve a intentarlo!", "incorrecto")

def juego_completado():
    hablar("¡Felicidades! Completaste todos los movimientos. ¡Eres increíble!", "completado")