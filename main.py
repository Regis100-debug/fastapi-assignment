from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = "products.json"

# ----------------------------
# LOAD PRODUCTS
# ----------------------------
def load_products():

    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        return json.load(file)

# ----------------------------
# SAVE PRODUCTS
# ----------------------------
def save_products(products):

    with open(DATA_FILE, "w") as file:
        json.dump(products, file, indent=4)

# ----------------------------
# HOME ROUTE
# ----------------------------
@app.route('/')
def home():
    return jsonify({
        "message": "Cloud E-commerce API is running"
    })

# ----------------------------
# GET ALL PRODUCTS
# ----------------------------
@app.route('/products', methods=['GET'])
def get_products():

    return jsonify(load_products())

# ----------------------------
# ADD PRODUCT
# ----------------------------
@app.route('/products', methods=['POST'])
def add_product():

    products = load_products()

    data = request.get_json()

    new_product = {
        "id": data["id"],
        "name": data["name"],
        "price": data["price"],
        "stock": data["stock"]
    }

    products.append(new_product)

    save_products(products)

    return jsonify({
        "message": "Product added successfully",
        "product": new_product
    }), 201

# ----------------------------
# GET PRODUCT BY ID
# ----------------------------
@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):

    products = load_products()

    for product in products:

        if product["id"] == id:
            return jsonify(product)

    return jsonify({
        "message": "Product not found"
    }), 404

# ----------------------------
# START SERVER
# ----------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)