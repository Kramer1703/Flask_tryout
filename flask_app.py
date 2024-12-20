from flask import flask
app =Flask(__name__)
@app.route('/')
def home():
    return (f"<p>Hello world!</p>")