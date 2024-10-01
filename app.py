from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "QR Code Escape Room"

@app.route('/api/scan', methods=['POST'])
def scan_qr():
    data = request.json
    qr_data = data.get('qr_data')
       # Here you would process the QR data and return appropriate response
    return jsonify({"message": "QR code received", "data": qr_data})

if __name__ == '__main__':
    app.run(debug=True)
    