
from flask import Flask 




from flask import Flask, jsonify  
from flask_mysqldb import MySQL   
import MySQLdb                    

app = Flask(__name__)  

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "belenvega"
app.config['MYSQL_DB'] = 'dbflask'
app.config['MYSQL_PORT'] = 3306  # SOLO USAR EN CAMBIO DE PUERTO

mysql = MySQL(app) 





# Ruta para probar la conexión
@app.route('/DBcheck')
def BD_check():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT 1')
        return jsonify({'status': 'Ok', 'Mensaje': 'Conectado a la BD'}), 200
    except MySQLdb.Error as e:
        return jsonify({'status': 'Error', 'Mensaje': 'Error en la BD'}), 500
    


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
def formulario():
    return '¡Soy un formulario!'


if __name__ == '__main__': 
    app.run(port=3000, debug=True)
   
   
   
   