from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "Model API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    return jsonify({"received": data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

