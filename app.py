from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/echo', methods=['GET'])
def echo():
    return jsonify(message="handball time")

if __name__ == '__main__':
    app.run(debug=True)
