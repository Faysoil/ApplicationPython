# Les Bibliotheque a importer
import tkinter
from cProfile import label
from tkinter import ttk, Tk
from tkinter import *
from subprocess import call
from tkinter import messagebox
import services as serv

import mysql.connector


def Ajouter():
    matricule = txtNumero.get()
    nom = txtnom.get()
    prenom = txtprenom.get()
    sexe = valeurSexe.get()
    phone = txtphone.get()
    adresse = txtaddress.get()
    mail = txtmail.get()

    maBase = mysql.connector.connect(
        host="localhost", user="root", password="", database="gestion_contact")
    meConnect = maBase.cursor()

    try:
        conn = mysql.connector.connect(
            host="localhost", user="root", password="", database="gestion_contact")
        cursor = conn.cursor()
        cursor.execute(
            "select * from personne where nom=%s and prenom=%s", (nom, prenom))
        row = cursor.fetchone()
        if row == None:
            sql = "INSERT INTO personne (id, nom, prenom, sexe, phone, adresse, mail) VALUES (%s, %s, %s,%s, %s, %s, %s) "
            val = (matricule, nom, prenom, sexe, phone, adresse, mail)
            meConnect.execute(sql, val)
            maBase.commit()
            derniereMatricule = meConnect.lastrowid
            messagebox.showinfo(
                "information", "Contact ajouté avec succès")
            root.destroy()
            call(["python", "Maison/Accueil.py"])

        else:
            messagebox.showerror("Erreur", "Ce contact n'existe pas")

            # retour
            maBase.rollback()
            maBase.close()

    except Exception as ex:
        messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}")


def Modifer():
    matricule = txtNumero.get()
    nom = txtnom.get()
    prenom = txtprenom.get()
    sexe = valeurSexe.get()
    phone = txtphone.get()
    adresse = txtaddress.get()
    mail = txtmail.get()

    maBase = mysql.connector.connect(
        host="localhost", user="root", password="", database="gestion_contact")
    meConnect = maBase.cursor()

    try:
        sql = "update personne set  nom=%s,prenom= %s,sexe= %s,phone=%s,adresse= %s,mail= %s where id= %s "
        val = (nom, prenom, sexe, phone, adresse, mail, matricule)
        meConnect.execute(sql, val)
        maBase.commit()
        derniereMatricule = meConnect.lastrowid
        messagebox.showinfo("information", "Contact modifié avec succès")
        root.destroy()
        call(["python", "Maison/Accueil.py"])

    except Exception as e:
        print(e)

        # retour
        maBase.rollback()
        maBase.close()


def Supprimer():
    matricule = txtNumero.get()

    maBase = mysql.connector.connect(
        host="localhost", user="root", password="", database="gestion_contact")
    meConnect = maBase.cursor()

    try:
        sql = "delete from personne where id= %s "
        val = (matricule,)
        meConnect.execute(sql, val)
        maBase.commit()
        derniereMatricule = meConnect.lastrowid
        messagebox.showinfo("information", "Contact supprimé avec succès")
        root.destroy()
        call(["python", "Maison/Accueil.py"])

    except Exception as e:
        print(e)
        # retour
        maBase.rollback()
        maBase.close()


# Ma fenetre
root = Tk()

root.title("Menu principal")
root.geometry("1350x700+0+0")
root.resizable(False, False)
root.configure(background="#FFE4C4")

# Ajouter le titre
lbltitre = Label(root, borderwidth=3, relief=SUNKEN, text="Gestion de contact", font=(
    "Sans Serif", 25), background="#A52A2A", fg="#FFFAFA")
lbltitre.place(x=0, y=0, width=1350, height=100)

# Matricule
lblNumero = Label(root, text="Id", font=(
    "Arial", 18), bg="#A52A2A", fg="white")
lblNumero.place(x=70, y=150, width=150)
txtNumero = Entry(root, bd=4, font=("Arial", 14))
txtNumero.place(x=250, y=150, width=150)

# Nom
lblnom = Label(root, text="Nom", font=("Arial", 18), bg="#A52A2A", fg="white")
lblnom.place(x=70, y=200, width=150)
txtnom = Entry(root, bd=4, font=("Arial", 14))
txtnom.place(x=250, y=200, width=300)
# Prenom
lblprenom = Label(root, text="Prénom", font=(
    "Arial", 18), bg="#A52A2A", fg="white")
lblprenom.place(x=70, y=250, width=150, )
txtprenom = Entry(root, bd=4, font=("Arial", 14))
txtprenom.place(x=250, y=250, width=300)

# sexe

valeurSexe = StringVar()
lblsexe = Label(root, text="Sexe", font=(
    "Arial", 18), bg="#A52A2A", fg="white")
lblsexe.place(x=70, y=300, width=150, )

lblSexeMasculin = Radiobutton(root, text="Homme", value="M", variable=valeurSexe,
                              indicatoron=0, font=("Arial", 14), bg="#A52A2A", fg="#696969")
lblSexeMasculin.place(x=250, y=300, width=130)
txtSexeFeminin = Radiobutton(root, text="Femme", value="F", variable=valeurSexe,
                             indicatoron=0, font=("Arial", 14), bg="#A52A2A", fg="#696969")
txtSexeFeminin.place(x=420, y=300, width=130)

# Téléphone
lblphone = Label(root, text="Téléphone", font=(
    "Arial", 18), bg="#A52A2A", fg="white")
lblphone.place(x=70, y=350, width=150, )
txtphone = Entry(root, bd=4, font=("Arial", 14))
txtphone.place(x=250, y=350, width=300)


# comboClasse = ttk.Combobox(root, font=("Arial", 14))
# comboClasse['values'] = ['NDRC1', 'NDRC2', 'SIO1 ', 'SIO2']
# comboClasse.place(x=250, y=350, width=130)

# Adresse
lbladdress = Label(root, text="Adresse", font=(
    "Arial", 18), bg="#A52A2A", fg="white")
lbladdress.place(x=70, y=400, width=150, )
txtaddress = Entry(root, bd=4, font=("Arial", 14))
txtaddress.place(x=250, y=400, width=300)

# combomatiere = ttk.Combobox(root, font=("Arial", 14))
# combomatiere['values'] = ['SLAM', 'Anglais', 'Francais ', 'Maths']
# combomatiere.place(x=250, y=400, width=130)

# Mail
lblmail = Label(root, text="Email", font=(
    "Arial", 18), bg="#A52A2A", fg="white")
lblmail.place(x=70, y=450, width=150, )
txtmail = Entry(root, bd=4, font=("Arial", 14))
txtmail.place(x=250, y=450, width=250)

# bouton Enregistrer
btnajouter = Button(root, text="Ajouter", font=(
    "Arial", 16), bg="#A52A2A", fg="white", command=Ajouter)
btnajouter.place(x=250, y=500, width=200)

# bouton modifier
btnmodofier = Button(root, text="Modifier", font=(
    "Arial", 16), bg="#A52A2A", fg="white", command=Modifer)
btnmodofier.place(x=250, y=550, width=200)

# bouton Supprimer
btnSupprimer = Button(root, text="Supprimer", font=(
    "Arial", 16), bg="#A52A2A", fg="white", command=Supprimer)
btnSupprimer.place(x=250, y=600, width=200)


# Table
table = ttk.Treeview(root, columns=(1, 2, 3, 4, 5, 6, 7),
                     height=5, show="headings")
table.place(x=560, y=150, width=790, height=450)

# definir les dimentions des colonnes
table.column(1, width=50)
table.column(2, width=150)
table.column(3, width=150)
table.column(4, width=100)
table.column(5, width=50)
table.column(6, width=100)
table.column(7, width=50)

# Entete
table.heading(1, text="Id")
table.heading(2, text="Nom")
table.heading(3, text="Prénom")
table.heading(4, text="Sexe")
table.heading(5, text="Téléphone")
table.heading(6, text="Adresse")
table.heading(7, text="Email")


# fonction qui affiche les informations de la ligne correspondant au champ cliqué
def get_selected_row(event):
    global selected_row
    index = table.selection()[0]
    selected_row = table.item(index)['values']
    txtNumero.delete(0, END)
    txtNumero.insert(END, selected_row[0])
    txtnom.delete(0, END)
    txtnom.insert(END, selected_row[1])
    txtprenom.delete(0, END)
    txtprenom.insert(END, selected_row[2])
    valeurSexe.set(selected_row[3])
    txtphone.delete(0, END)
    txtphone.insert(END, selected_row[4])
    txtaddress.delete(0, END)
    txtaddress.insert(END, selected_row[5])
    txtmail.delete(0, END)
    txtmail.insert(END, selected_row[6])


# afficher les informations de la table
maBase = mysql.connector.connect(
    host="localhost", user="root", password="", database="gestion_contact")
meConnect = maBase.cursor()
meConnect.execute("select * from personne")
for row in meConnect:
    table.insert('', END, value=row)
table.bind('<ButtonRelease-1>', get_selected_row)
maBase.close()


# Execution
root.mainloop()
