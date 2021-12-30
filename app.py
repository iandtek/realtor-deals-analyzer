from flask import Flask
import json

app = Flask(__name__)

@app.route("/properties")
def properties():
    return {'properties': json.load(open('properties.json'))}

if __name__ == "__main__":
    app.run()