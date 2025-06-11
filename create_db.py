import sqlite3

# Constantes
DB_NAME = 'database.db'
SCHEMA_FILE = 'schema.sql'
INSERT_CLIENT_SQL = "INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)"

# Connexion à la base
connection = sqlite3.connect(DB_NAME)

# Exécution du script SQL de création de schéma
with open(SCHEMA_FILE, 'r', encoding='utf-8') as schema_file:
    connection.executescript(schema_file.read())

cur = connection.cursor()

# Liste des clients à insérer
clients = [
    ('DUPONT', 'Emilie', '123, Rue des Lilas, 75001 Paris'),
    ('LEROUX', 'Lucas', '456, Avenue du Soleil, 31000 Toulouse'),
    ('MARTIN', 'Amandine', '789, Rue des Érables, 69002 Lyon'),
    ('TREMBLAY', 'Antoine', '1010, Boulevard de la Mer, 13008 Marseille'),
    ('LAMBERT', 'Sarah', '222, Avenue de la Liberté, 59000 Lille'),
    ('GAGNON', 'Nicolas', '456, Boulevard des Cerisiers, 69003 Lyon'),
    ('DUBOIS', 'Charlotte', '789, Rue des Roses, 13005 Marseille'),
    ('LEFEVRE', 'Thomas', '333, Rue de la Paix, 75002 Paris'),
]

# Insertion des clients
for client in clients:
    cur.execute(INSERT_CLIENT_SQL, client)

# Commit et fermeture
connection.commit()
connection.close()
