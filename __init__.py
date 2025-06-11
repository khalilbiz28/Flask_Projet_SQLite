from flask import Flask, render_template_string, render_template, jsonify, request, redirect, url_for, session
from flask import json
from urllib.request import urlopen
from werkzeug.utils import secure_filename
import sqlite3

app = flask(name)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # Clé secrète pour les sessions

DATABASE_PATH = 'database.db'  # ✅ Constante pour le chemin de la base de données

# Fonction pour vérifier l'authentification
def est_authentifie():
    return session.get('authentifie')

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/lecture')
def lecture():
    if not est_authentifie():
        return redirect(url_for('authentification'))
    return "<h2>Bravo, vous êtes authentifié</h2>"

@app.route('/authentification', methods=['GET', 'POST'])
def authentification():
    error = False
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'password':  # ⚠ À sécuriser
            session['authentifie'] = True
            return redirect(url_for('lecture'))
        else:
            error = True
    return render_template('formulaire_authentification.html', error=error)  # ✅ Évite duplication

@app.route('/fiche_client/<int:post_id>')
def read_fiche(post_id):  # ✅ Renommage en snake_case
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients WHERE id = ?', (post_id,))
    data = cursor.fetchall()
    conn.close()
    return render_template('read_data.html', data=data)

@app.route('/consultation/')
def read_bdd():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients;')
    data = cursor.fetchall()
    conn.close()
    return render_template('read_data.html', data=data)

@app.route('/enregistrer_client', methods=['GET'])
def formulaire_client():
    return render_template('formulaire.html')

@app.route('/enregistrer_client', methods=['POST'])
def enregistrer_client():
    nom = request.form['nom']
    prenom = request.form['prenom']

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO clients (created, nom, prenom, adresse) VALUES (?, ?, ?, ?)',
        (1002938, nom, prenom, "ICI")
    )
    conn.commit()
    conn.close()
    return redirect('/consultation/')

if name == "main":
    app.run(debug=True)
