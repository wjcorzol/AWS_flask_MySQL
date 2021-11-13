from flask import Flask
import Modelo

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'



if __name__ == '__main__':
    app.run(debug=True, port='5000')
    Modelo.crearTablas()
