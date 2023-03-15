import mysql.connector


def connection():
    try:
        conn = mysql.connector.connect(
            host="localhost", user="root", password="", database="gestion_contact")
        print("connexion etablie")

        return conn

    except:
        print("Connexion raté")


def ajouter(personne):
    conn = connection()
    cursor = conn.cursor()

    valeurs = (personne.prenom, personne.nom, personne.photo, personne.mdp)
    cursor.execute(
        """ INSERT INTO personne (prenom, nom, photo, mdp) VALUES(%s, %s, %s, %s) """, valeurs)
    conn.close()


def parcourir(personne):
    conn = connection()
    cursor = conn.cursor

    cursor.execute(""" SELECT * FROM personne """)
    rows = cursor.fetchall()
    return rows
    conn.close()
