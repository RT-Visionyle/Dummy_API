from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Read API key from environment variable (set later in Render)
VALID_API_KEY = os.getenv("API_KEY", "my-secret-key-123")

PRODUCTS = [
    {"id": 1, "name": "Widget A", "category": "Gadgets", "price": 19.99},
    {"id": 2, "name": "Widget B", "category": "Gadgets", "price": 29.50},
    {"id": 3, "name": "Thingamajig", "category": "Tools", "price": 9.75}
]

@app.route("/")
def home():
    return jsonify({"message": "Welcome to Dummy Product API"}), 200

@app.route("/products", methods=["GET"])
def get_products():
    api_key = request.headers.get("x-api-key")
    if not api_key:
        return jsonify({"error": "API key missing"}), 401

    if api_key != VALID_API_KEY:
        return jsonify({"error": "Invalid API key"}), 401

    category = request.args.get("category")
    if category:
        filtered = [p for p in PRODUCTS if p["category"].lower() == category.lower()]
        return jsonify(filtered), 200

    return jsonify(PRODUCTS), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
