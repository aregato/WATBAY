from flask import Flask, request, render_template
from watbay import *
import os


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/api/v1/watbay", methods=['POST'])
def watbay_post():
    '''
    Sparar och kontrollerar bilden som inkommer från användaren.
    Returnerar svaret i form av json.
    '''
    picture = request.files['file']
    picture.save("src/picture.jpg")
    size = os.path.getsize("src/picture.jpg")
    if size > 2000000:
        return "Error, bilden är för stor"
    else:
        result = watson_ebay()
        json_result = generate_json(result)
        return json_result

@app.route("/dokumentation")
def docs():
    return render_template("Dokumentation.html")
