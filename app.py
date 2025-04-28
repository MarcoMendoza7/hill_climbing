from flask import Flask, render_template, request
from tsp import hill_climbing

app = Flask(__name__)

COORDENADAS = {
    'Jiloyork': (19.916012, -99.580580),
    'Toluca': (19.289165, -99.655697),
    'Atlacomulco': (19.799520, -99.873844),
    'Guadalajara': (20.677754472859146, -103.34625354877137),
    'Monterrey': (25.69161110159454, -100.321838480256),
    'QuintanaRoo': (21.163111924844458, -86.80231502121464),
    'Michohacan': (19.701400113725654, -101.20829680213464),
    'Aguascalientes': (21.87641043660486, -102.26438663286967),
    'CDMX': (19.432713075976878, -99.13318344772986),
    'QRO': (20.59719437542255, -100.38667040246602)
}

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        ciudades = request.form.getlist('ciudades')
        ruta, distancia = hill_climbing(ciudades, COORDENADAS)
        resultado = {
            'ruta': ruta,
            'distancia': round(distancia, 2)
        }
    return render_template('index.html', coordenadas=COORDENADAS.keys(), resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
