from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Hello from Back-End!"

@app.route('/process', methods=['POST'])
def process_form():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    response = {
        'message': f'Thank you {name}, we have received your email: {email}'
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
