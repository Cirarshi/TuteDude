from flask import Flask, request, jsonify, render_template
from business.get_data import read_data

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/api', methods=['GET'])
def api():
    data = read_data()
    data = {'dara': data}
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=8000,host='0.0.0.0', debug=True)
