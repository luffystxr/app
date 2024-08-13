# backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow all origins

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/api/hello', methods=['GET'])
def get_hello():
    return jsonify({'message': 'Hello from Flask!'})

if __name__ == "__main__":
    app.run(debug=True)
