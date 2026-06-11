import os
from flask import Flask, jsonify, request, render_template  # nosec B104

app = Flask(__name__)

productos = [
    {"id": 1, "nombre": "Laptop", "precio": 1500},
    {"id": 2, "nombre": "Mouse", "precio": 25}
]
next_id = 3

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"}), 200

@app.route('/productos', methods=['GET'])
def get_productos():
    return jsonify(productos), 200

@app.route('/productos/<int:id>', methods=['GET'])
def get_producto(id):
    producto = next((p for p in productos if p["id"] == id), None)
    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404
    return jsonify(producto), 200

@app.route('/productos', methods=['POST'])
def crear_producto():
    global next_id
    data = request.get_json()
    if not data or "nombre" not in data or "precio" not in data:
        return jsonify({"error": "Faltan campos nombre y precio"}), 400
    producto = {"id": next_id, "nombre": data["nombre"], "precio": data["precio"]}
    productos.append(producto)
    next_id += 1
    return jsonify(producto), 201

@app.route('/productos/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    global productos
    producto = next((p for p in productos if p["id"] == id), None)
    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404
    productos = [p for p in productos if p["id"] != id]
    return jsonify({"mensaje": "Producto eliminado"}), 200

if __name__ == '__main__':
    debug = os.environ.get('DEBUG', 'False') == 'True'
    app.run(host='0.0.0.0', port=5000, debug=debug)  # nosec B104