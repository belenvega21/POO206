from flask import Flask, jsonify, request, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
app.secret_key = 'tequieromucho123'

# Configuración de conexión a MySQL en Docker
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:belenvega@127.0.0.1:3307/dbflask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo Usuario
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)

    def to_dict(self):
        return {'id': self.id, 'nombre': self.nombre, 'correo': self.correo}

# Modelo Album
class Album(db.Model):
    __tablename__ = 'Album'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    artista = db.Column(db.String(100), nullable=False)
    año = db.Column("Año", db.String(4), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'titulo': self.titulo, 'artista': self.artista, 'año': self.año}

# Verificar conexión
@app.route('/DBcheck')
def db_check():
    try:
        db.session.execute(text('SELECT 1'))
        return jsonify({'status': 'ok', 'message': 'Conexión exitosa'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

# Página principal - mostrar álbumes
@app.route('/')
def home():
    try:
        consultaTodo = Album.query.all()
        return render_template('formulario.html', errores={}, albums=consultaTodo)
    except Exception as e:
        print('Error al consultar todo:', str(e))
        return render_template('formulario.html', errores={}, albums=[])


#RUTA DETALLE
@app.route('/detalle/<int:id>')
def detalle(id):
    try:
        consultaId = Album.query.get(id)
        if consultaId is None:
            raise Exception(f"No se encontró el álbum con ID {id}")
        return render_template('consulta.html', album=consultaId)
    except Exception as e:
        print('ERROR AL CONSULTAR DETALLE:', str(e))  
        return render_template('consulta.html', album=None)


# RUTA PARA MOSTRAR ACTUALIZACIÓN 
@app.route('/formUpdate/<int:id>')
def form_update(id):
    album = Album.query.get(id)
    if not album:
        return pagina_no_encontrada(404)
    return render_template('formUpdate.html', album=album)

#RUTA PARA ACTUALIZAR UN ÁLBUM
@app.route('/actualizarAlbum/<int:id>', methods=['POST'])
def actualizar_album(id):
    album = Album.query.get(id)
    if not album:
        return pagina_no_encontrada(404)

    errores = {}

    titulo = request.form.get('titulo', '').strip()
    artista = request.form.get('artista', '').strip()
    año = request.form.get('año', '').strip()

    if not titulo:
        errores['titulo'] = 'El título es obligatorio.'
    if not artista:
        errores['artista'] = 'El artista es obligatorio.'
    if not año:
        errores['año'] = 'El año es obligatorio.'
    elif not año.isdigit() or int(año) < 1800 or int(año) > 2030:
        errores['año'] = 'Ingresa un año válido.'

    if errores:
        return render_template('formUpdate.html', album=album, errores=errores)

    try:
        album.titulo = titulo
        album.artista = artista
        album.año = año
        db.session.commit()
        flash('Album Actualizado en BD')
        return redirect(url_for('home'))

    except Exception as e:
        db.session.rollback()
        flash('Error al actualizar: ' + str(e))
        return redirect(url_for('home'))



# Página adicional
@app.route('/consulta')
def consulta():
    return render_template('consulta.html')

# Insertar usuario
@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    data = request.get_json()
    nombre = data.get('nombre')
    correo = data.get('correo')

    if not nombre or not correo:
        return jsonify({'error': 'Faltan datos'}), 400

    nuevo_usuario = Usuario(nombre=nombre, correo=correo)
    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({'mensaje': 'Usuario creado', 'usuario': nuevo_usuario.to_dict()}), 201

# Obtener todos los usuarios
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([u.to_dict() for u in usuarios]), 200

# Guardar álbum
@app.route('/guardarAlbum', methods=['POST'])
def guardar_album():
    errores = {}
    try:
        titulo = request.form.get('txtTitulo', '').strip()
        artista = request.form.get('txtArtista', '').strip()
        año = request.form.get('txtAño', '').strip()

        if not titulo:
            errores['txtTitulo'] = 'El título es obligatorio.'
        if not artista:
            errores['txtArtista'] = 'El artista es obligatorio.'
        if not año:
            errores['txtAño'] = 'El año es obligatorio.'
        elif not año.isdigit() or int(año) < 1800 or int(año) > 2030:
            errores['txtAño'] = 'Ingresa un año válido.'

        if errores:
            albums = Album.query.all()
            return render_template('formulario.html', errores=errores, albums=albums)

        nuevo_album = Album(titulo=titulo, artista=artista, año=año)
        db.session.add(nuevo_album)
        db.session.commit()

        flash('Álbum guardado exitosamente.')
        return redirect(url_for('home'))

    except Exception as e:
        db.session.rollback()
        flash('Algo falló: ' + str(e))
        return redirect(url_for('home'))

# Ver todos los álbumes (opcional)
@app.route('/albums')
def ver_albums():
    albums = Album.query.all()
    return render_template('ver_albums.html', albums=albums)

# Página 404 personalizada
@app.errorhandler(404)
def pagina_no_encontrada(e):
    return '¡Cuidado! ¡Error de capa 8!', 404

# Iniciar servidor
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)

