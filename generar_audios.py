import requests
import os

API_KEY = "sk_f9dfe647908ba2149ff5edbe78a26a264fdc4e283a258690"
VOICE_ID = "zl7szWVBXnpgrJmAalgz"

# Carpeta donde se guardan los audios
os.makedirs("static/audio", exist_ok=True)

AUDIOS = {
    "bienvenida_1": "Hola! Bienvenido al juego de imitar movimientos!",
    "bienvenida_2": "Yo te voy a decir qué movimiento debes hacer.",
    "bienvenida_3": "Cuando yo diga YA... hazlo frente a la cámara!",
    "bienvenida_4": "Vamos a comenzar!",
    "mov1_corto": "Muestra 4 dedos",
    "mov1_largo": "Levanta cuatro dedos. Dobla solo el dedo gordo hacia adentro.",
    "mov2_corto": "Haz un puño cerrado",
    "mov2_largo": "Cierra toda tu mano bien fuerte. Todos los dedos juntos adentro.",
    "mov3_corto": "Señala con un solo dedo",
    "mov3_largo": "Levanta solo el dedo índice. El dedito que usas para tocar la pantalla.",
    "mov4_corto": "Muestra dos dedos en V",
    "mov4_largo": "Levanta el dedo índice y el dedo del medio juntos. Como la letra V de victoria!",
    "mov5_corto": "Abre toda la mano",
    "mov5_largo": "Estira todos los cinco dedos bien abiertos. Como un abanico grande!",
    "preparate": "Prepárate...",
    "tres": "3",
    "dos": "2",
    "uno": "1",
    "ya": "Ya! Hazlo ahora!",
    "muy_bien": "Muy bien!",
    "inteligente": "Lo lograste! Eres muy inteligente!",
    "no_preocupes": "No te preocupes!",
    "intenta": "Vuelve a intentarlo!",
    "felicidades": "Felicidades! Completaste todos los movimientos!",
    "campeon": "Eres un campeón!",
}

for nombre, texto in AUDIOS.items():
    print(f"Generando: {nombre}...")
    r = requests.post(
        f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}",
        headers={
            "xi-api-key": API_KEY,
            "Content-Type": "application/json"
        },
        json={
            "text": texto,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.8,
                "style": 0.3,
                "use_speaker_boost": True
            }
        }
    )
    if r.status_code == 200:
        with open(f"static/audio/{nombre}.mp3", "wb") as f:
            f.write(r.content)
        print(f"  ✅ {nombre}.mp3 guardado")
    else:
        print(f"  ❌ Error: {r.status_code} - {r.text}")

print("\n🎉 Todos los audios generados! Ya puedes hacer git push.")