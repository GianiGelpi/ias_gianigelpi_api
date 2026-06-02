import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"}), 200

@app.route('/productos', methods=['GET'])
def get_productos():
    productos = [
        {"id": 1, "nombre": "Laptop", "precio": 1500},
        {"id": 2, "nombre": "Mouse", "precio": 25}
    ]
    return jsonify(productos), 200

@app.route('/productos/<int:id>', methods=['GET'])
def get_producto(id):
    return jsonify({"id": id, "nombre": "Laptop", "precio": 1500}), 200

if __name__ == '__main__':
    debug = os.environ.get('DEBUG', 'False') == 'True'
    app.run(host='0.0.0.0', port=5000, debug=debug)  # nosec B104