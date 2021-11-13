from flask import Flask
import Modelo

app = Flask(__name__)

@app.route('/')
def index():
    Modelo.registrar('usuario2', 'contraseña', 'email2@email.com', 'nombre', 'apellido', '111112', 'M', '1989--09-26', 'direccion', 'ciudad')
    return '<h1>Hello World!</h1>'



if __name__ == '__main__':
    Modelo.crearTablas()
    app.run(debug=True, port='5000')
    
