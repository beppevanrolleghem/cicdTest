from flask import Flask
import requests

app = Flask(__name__)

URL = "http://server-check:6000"

@app.errorhandler(404)
def page_not_found(error):
   return "beppe's 404 error"

@app.route('/')
def doRequest():
    return "it works"

@app.route('/server-a')
def checkThis():
	return "server-a is apparently something to worry abt"

@app.route("/server-a/check")
def itAlsoWorks():
	return requests.get(URL).json()

@app.route('/check')
def itWorks():
    return requests.get(URL).json()

@app.route('/text')
def hope():
    return requests.get(URL).text


@app.route('/find/<name>/<port>')
def findServer(name, port):
    return requests.get("http://"+name+":"+port)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
