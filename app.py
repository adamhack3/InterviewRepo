from flask import Flask, render_template
from main import addresses_for_postcode


app = Flask(__name__)

#TODO: Input to set postcode from frontend

@app.route("/")
def hello_world():
    addresses = addresses_for_postcode("E8 3LH")
    assert type(addresses) == list
    return render_template("index.jinja", address_list=addresses)

if __name__ == "__main__":
    app.run(debug=True)