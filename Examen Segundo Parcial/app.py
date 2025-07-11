from flask import Flask, render_template, request, redirect, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "secreto123"

# Crear la base de datos si no existe
def init_db():
    try:
        with sqlite3.connect("contactos.db") as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS contactos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    correo TEXT NOT NULL,
                    telefono TEXT NOT NULL,
                    edad INTEGER NOT NULL
                )
            ''')
    except Exception as e:
        print("Error al crear la base de datos:", e)

init_db()

@app.route('/')
def index():
    try:
        with sqlite3.connect("contactos.db") as conn:
            contactos = conn.execute("SELECT * FROM contactos").fetchall()
        return render_template("index.html", contactos=contactos)
    except Exception as e:
        print("Error al cargar contactos:", e)
        return "Error interno", 500

@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form['nombre']
    correo = request.form['correo']
    telefono = request.form['telefono']
    edad = request.form['edad']

    if not nombre or not correo or not telefono or not edad:
        flash("Todos los campos son obligatorios.")
        return redirect('/')

    try:
        edad = int(edad)
        if edad < 1 or edad > 105:
            flash("La edad debe estar entre 1 y 105.")
            return redirect('/')
    except ValueError:
        flash("Edad inválida.")
        return redirect('/')

    try:
        with sqlite3.connect("contactos.db") as conn:
            conn.execute("INSERT INTO contactos (nombre, correo, telefono, edad) VALUES (?, ?, ?, ?)",
                         (nombre, correo, telefono, edad))
        flash("Contacto agregado exitosamente.")
    except Exception as e:
        print("Error al agregar contacto:", e)
        flash("Error al agregar contacto.")
    return redirect('/')

@app.route('/editar/<int:id>')
def editar(id):
    try:
        with sqlite3.connect("contactos.db") as conn:
            contacto = conn.execute("SELECT * FROM contactos WHERE id=?", (id,)).fetchone()
        return render_template("editar.html", contacto=contacto)
    except Exception as e:
        print("Error al cargar contacto:", e)
        return "Error interno", 500

@app.route('/actualizar/<int:id>', methods=['POST'])
def actualizar(id):
    nombre = request.form['nombre']
    correo = request.form['correo']
    telefono = request.form['telefono']
    edad = request.form['edad']

    if not nombre or not correo or not telefono or not edad:
        flash("Todos los campos son obligatorios.")
        return redirect(f'/editar/{id}')

    try:
        edad = int(edad)
        if edad < 1 or edad > 105:
            flash("La edad debe estar entre 1 y 105.")
            return redirect(f'/editar/{id}')
    except ValueError:
        flash("Edad inválida.")
        return redirect(f'/editar/{id}')

    try:
        with sqlite3.connect("contactos.db") as conn:
            conn.execute("UPDATE contactos SET nombre=?, correo=?, telefono=?, edad=? WHERE id=?",
                         (nombre, correo, telefono, edad, id))
        flash("Contacto actualizado correctamente.")
    except Exception as e:
        print("Error al actualizar contacto:", e)
        flash("Error al actualizar contacto.")
    return redirect('/')

@app.route('/eliminar/<int:id>')
def eliminar(id):
    try:
        with sqlite3.connect("contactos.db") as conn:
            conn.execute("DELETE FROM contactos WHERE id=?", (id,))
        flash("Contacto eliminado correctamente.")
    except Exception as e:
        print("Error al eliminar contacto:", e)
        flash("Error al eliminar contacto.")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
