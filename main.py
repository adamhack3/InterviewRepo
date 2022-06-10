from flask import Flask
import json

def fetch_addresses():

    return [
        {
            "lines": [0, 1, 2]
        }
    ]

app = Flask(__name__)

@app.route("/get_addresses")
def hello_world():
    addresses = json.dumps( fetch_addresses() )
    return addresses


if __name__ == "__main__":
    app.run(debug=True)