
from flask import Flask 


#RUTA SIMPLE
app= Flask(__name__)
@app.route('/')
def home():
    return '¡Bienvenida al Mundo de Flask!'


#RUTA CON PARAMETRO
@app.route('/saludo/<nombre>')
def saludar(nombre):
    return '¡Hola,'+nombre+'!!!'

#RUTA TRY-CATCH
@app.errorhandler(404)
def pagninaNoE(e):
    return '¡Cuidado! ¡Error de capa 8!', 404

#RUTA DOBLE
@app.route('/usuario')
@app.route('/usuaria')
def dobleroute ():
    return '¡Soy el mismo recurso del servidor!'

#RUTA POTS
@app.route('/formulario', methods=['POST'])
def formulario():
    return '¡Soy un formulario!'


if __name__ == '__main__': 
    app.run(port=3000, debug=True)
   
   
   
   