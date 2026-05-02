from flask import Flask, render_template, request, jsonify
from engine import BookingEngine, ShopEngine

app = Flask(__name__)

booking_engine = BookingEngine()
shop_engine = ShopEngine()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/slots", methods=["POST"])
def get_slots():
    data = request.json
    return jsonify(booking_engine.get_slots(data["date"], data["court"]))

@app.route("/api/book", methods=["POST"])
def book():
    data = request.json
    return jsonify(booking_engine.book_slot(
        data["date"], data["court"], data["slot"]
    ))

@app.route("/api/cart", methods=["POST"])
def add_cart():
    data = request.json
    return jsonify(shop_engine.add_to_cart(data["item"]))

@app.route("/api/cart")
def get_cart():
    return jsonify(shop_engine.get_cart())

@app.route("/api/member", methods=["POST"])
def member():
    return jsonify({"status": "success"})

@app.route("/api/event", methods=["POST"])
def event():
    return jsonify({"status": "registered"})

@app.route("/api/contact", methods=["POST"])
def contact():
    return jsonify({"status": "message received"})

if __name__ == "__main__":
    app.run(debug=True)
