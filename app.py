from flask import Flask
app = Flask(__name__)

@app.route('/hello', methods = ['GET'])
def hello():
    if request.method == 'GET':
        return "Hello, Azure GET!"    
    else:
        return {}, 405
