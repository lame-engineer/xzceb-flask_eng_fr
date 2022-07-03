from machinetranslation import translator
from flask import Flask, render_template, request
import json
from machinetranslation import translator

app = Flask(__name__)

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    french_text = translator.english_to_french(textToTranslate)
    return french_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    english_text = translator.french_to_english(textToTranslate)
    return english_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)