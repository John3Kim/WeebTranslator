# Main page for the weeb translator
from flask import Flask, request, render_template, flash
from wtforms import Form, TextField, validators
from eng_to_ja import run
import os

app = Flask(__name__)
app.secret_key = os.urandom(16)

class TranslateField(Form): 
	text_to_translate = TextField("Text to translate:", validators = [validators.required()])


@app.route('/', methods = ["GET","POST"])
def translate_text(): 
	form = TranslateField(request.form)
    
	if request.method == "POST": 
		text_to_translate = request.form["text_to_translate"]
		
		if form.validate():
			text_to_translate = run(text_to_translate)
			flash(text_to_translate)
		else: 
			flash("Add text kudasai!")
		
	return render_template("main.html",form = form)
	
if __name__ == "__main__":
    app.run()
