from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def helloword():
    return "Hello World!!"

@app.route("/get_data")
def getdata():
    data = {
        'name': 'my name',
        'url': 'my url'
    }
    return json.dumps(data)

if __name__ == "__main__":
    app.run()
