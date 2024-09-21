from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Ruta para servir la página HTML
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para generar los números aleatorios
@app.route('/generate', methods=['GET'])
def generate_numbers():
    random_numbers = random.sample(range(0, 46), 6)  # Genera 6 números únicos entre 0 y 45
    return jsonify(random_numbers)

if __name__ == '__main__':
    app.run(debug=True)
