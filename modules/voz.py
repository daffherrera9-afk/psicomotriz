from gtts import gTTS
import os
import threading

def hablar(texto):
    def _hablar():
        try:
            tts = gTTS(text=texto, lang='es')
            tts.save('voz_temp.mp3')
        except Exception as e:
            print(f"Error de voz: {e}")
    t = threading.Thread(target=_hablar)
    t.daemon = True
    t.start()