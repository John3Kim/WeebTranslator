# Main page for the weeb translator
from flask import Flask
app = Flask(__name__)

@app.route('/')
#def hello_world():
#    return('Hello, World!')

def render_main():
    return render_template("main.html")
