from flask import Flask
app = Flask(__name__)

@app.route('/hello', methods = ['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return "Hello, Azure GET!"
    
    else if request.method == 'POST':
        return "Hello, Azure POST!"
    
    else:
        return {}, 405
