from flask import Flask
app = Flask(__name__)

@app.route('/hello', methods = ['POST'])
def hello():
    return "Hello, Azure GET!"    

