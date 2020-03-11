from flask import Flask
from flask import jsonify
app = Flask(__name__)


@app.route('/')
def doRequest():
    data = {
        "serverName": "server-b",
        "version": "master",
        "success": "true"
    }
    return jsonify(data)



@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def doRequest(path):
    return path + "\nserver-b"


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
