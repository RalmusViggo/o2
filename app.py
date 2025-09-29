from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/brukersjekk.html')
def sjekk_brukere():
    brukere = {
    "alice": "passord123",
    "bob": "hemmelig",
    "carol": "abc123"
    }
    sjekk_bruker = "bob"
    return render_template("brukersjekk.html")
    
if __name__ == "__main__":
    app.run()