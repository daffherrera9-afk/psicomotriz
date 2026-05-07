from flask import Flask, render_template, jsonify
from flask_cors import CORS
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'modules'))

from imitar import (dar_instrucciones, anunciar_movimiento, contar, ya,
                    resultado_correcto, resultado_incorrecto,
                    juego_completado as imitar_completado, movimientos)

from reconocer import (dar_instrucciones_animales, dar_instrucciones_colores,
                       animal_correcto, animal_incorrecto,
                       color_correcto, color_incorrecto,
                       juego_completado as reconocer_completado,
                       animales, colores)

from rompecabezas import (dar_instrucciones as rompe_instrucciones,
                           pieza_correcta, pieza_incorrecta,
                           puzzle_completado, puzzles)

from dibujo import (dar_instrucciones as dibujo_instrucciones,
                    cambiar_color, dibujo_guardado, lienzo_limpiado)

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/modulo/<nombre>')
def modulo(nombre):
    return render_template(f'modulo_{nombre}.html')

# ===== MÓDULO 3 - IMITAR =====

@app.route('/imitar/instrucciones')
def imitar_instrucciones():
    dar_instrucciones()
    return jsonify({'ok': True})

@app.route('/imitar/movimientos')
def imitar_movimientos():
    return jsonify(movimientos)

@app.route('/imitar/anunciar/<int:idx>')
def imitar_anunciar(idx):
    if 0 <= idx < len(movimientos):
        anunciar_movimiento(movimientos[idx]['instruccion'])
        return jsonify({'ok': True, 'movimiento': movimientos[idx]})
    return jsonify({'error': 'índice inválido'}), 400

@app.route('/imitar/correcto/<int:idx>')
def imitar_correcto(idx):
    if 0 <= idx < len(movimientos):
        resultado_correcto(movimientos[idx]['instruccion'])
        return jsonify({'ok': True})
    return jsonify({'error': 'índice inválido'}), 400

@app.route('/imitar/incorrecto')
def imitar_incorrecto():
    resultado_incorrecto()
    return jsonify({'ok': True})

@app.route('/imitar/completado')
def imitar_completado_ruta():
    imitar_completado()
    return jsonify({'ok': True})

# ===== MÓDULO 1 - RECONOCER =====

@app.route('/reconocer/animales')
def reconocer_animales():
    return jsonify(animales)

@app.route('/reconocer/colores')
def reconocer_colores():
    return jsonify(colores)

@app.route('/reconocer/instrucciones/animales')
def reconocer_instrucciones_animales():
    dar_instrucciones_animales()
    return jsonify({'ok': True})

@app.route('/reconocer/instrucciones/colores')
def reconocer_instrucciones_colores():
    dar_instrucciones_colores()
    return jsonify({'ok': True})

@app.route('/reconocer/animal/correcto/<int:idx>')
def reconocer_animal_correcto(idx):
    if 0 <= idx < len(animales):
        animal_correcto(animales[idx]['nombre'])
        return jsonify({'ok': True})
    return jsonify({'error': 'índice inválido'}), 400

@app.route('/reconocer/animal/incorrecto')
def reconocer_animal_incorrecto():
    animal_incorrecto()
    return jsonify({'ok': True})

@app.route('/reconocer/color/correcto/<int:idx>')
def reconocer_color_correcto(idx):
    if 0 <= idx < len(colores):
        color_correcto(colores[idx]['nombre'])
        return jsonify({'ok': True})
    return jsonify({'error': 'índice inválido'}), 400

@app.route('/reconocer/color/incorrecto')
def reconocer_color_incorrecto():
    color_incorrecto()
    return jsonify({'ok': True})

@app.route('/reconocer/completado')
def reconocer_completado_ruta():
    reconocer_completado()
    return jsonify({'ok': True})

@app.route('/imitar/contar/<int:numero>')
def imitar_contar(numero):
    contar(numero)
    return jsonify({'ok': True})

@app.route('/imitar/ya')
def imitar_ya():
    ya()
    return jsonify({'ok': True})

# ===== MÓDULO 2 - ROMPECABEZAS =====

@app.route('/rompecabezas/puzzles')
def rompe_puzzles():
    return jsonify(puzzles)

@app.route('/rompecabezas/instrucciones')
def rompe_instrucciones_ruta():
    rompe_instrucciones()
    return jsonify({'ok': True})

@app.route('/rompecabezas/pieza/correcta/<int:numero>')
def rompe_pieza_correcta(numero):
    pieza_correcta(numero)
    return jsonify({'ok': True})

@app.route('/rompecabezas/pieza/incorrecta')
def rompe_pieza_incorrecta():
    pieza_incorrecta()
    return jsonify({'ok': True})

@app.route('/rompecabezas/completado/<nombre>')
def rompe_completado(nombre):
    puzzle_completado(nombre)
    return jsonify({'ok': True})

# ===== MÓDULO 4 - DIBUJO =====

@app.route('/dibujo/instrucciones')
def dibujo_instrucciones_ruta():
    dibujo_instrucciones()
    return jsonify({'ok': True})

@app.route('/dibujo/color/<nombre>')
def dibujo_color(nombre):
    cambiar_color(nombre)
    return jsonify({'ok': True})

@app.route('/dibujo/guardado')
def dibujo_guardado_ruta():
    dibujo_guardado()
    return jsonify({'ok': True})

@app.route('/dibujo/limpiar')
def dibujo_limpiar():
    lienzo_limpiado()
    return jsonify({'ok': True})

if __name__ == '__main__':
    app.run(debug=True, port=5000)