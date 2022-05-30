#Les Bibliotheque a importer
import tkinter
from cProfile import label
from tkinter import ttk, Tk
from tkinter import *
from subprocess import call
from tkinter import messagebox
#cd AppData\Local\Programs\Python\Python39
#python -m pip install mysql-connector-python
import mysql.connector

def Ajouter():
    matricule = txtNumero.get()
    nom = txtnom.get()
    prenom = txtprenom.get()
    sexe = valeurSexe.get()
    classe = comboClasse.get()
    matiere  = combomatiere.get()
    note  = txtnote.get()

    maBase = mysql.connector.connect(host="localhost", user="root",password="", database="note_eleve")
    meConnect = maBase.cursor()

    try:
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="note_eleve")
        cursor = conn.cursor()
        cursor.execute("select * from personne where nom=%s and prenom=%s", (nom, prenom))
        row = cursor.fetchone()
        if row == None:
            messagebox.showerror("Erreur", "Cet employé n'existe pas")
        else:
            try:
                sql = "INSERT INTO note (code, nom, prenom, sexe, classe, matiere, notes) VALUES (%s, %s, %s,%s, %s, %s, %s) "
                val = (matricule, nom,prenom, sexe,classe, matiere ,note )
                meConnect.execute(sql, val)
                maBase.commit()
                derniereMatricule = meConnect.lastrowid
                messagebox.showinfo("information", "Note ajouter")
                root.destroy()
                call(["python", "Chambre2.py"])

            except Exception as e:
                print(e)

            #retour
            maBase.rollback()
            maBase.close()

    except Exception as ex:
        messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}")


"""def Modifer():
    matricule = txtNumero.get()
    nom = txtnom.get()
    prenom = txtprenom.get()
    sexe = valeurSexe.get()
    classe = comboClasse.get()
    matiere  = combomatiere.get()
    note  = txtnote.get()

    maBase = mysql.connector.connect(host="localhost", user="root",password="", database="note_eleve")
    meConnect = maBase.cursor()

    try:
        sql = "update note set  nom=%s,prenom= %s,sexe= %s,classe=%s,matiere= %s,notes= %s where code= %s "
        val = (nom,prenom, sexe,classe, matiere ,note, matricule )
        meConnect.execute(sql, val)
        maBase.commit()
        derniereMatricule = meConnect.lastrowid
        messagebox.showinfo("information", "Note modifier")
        root.destroy()
        call(["python", "Chambre2.py"])

    except Exception as e:
        print(e)

        #retour
        maBase.rollback()
        maBase.close()"""



"""def Supprimer():
    matricule = txtNumero.get()

    maBase = mysql.connector.connect(host="localhost", user="root",password="", database="note_eleve")
    meConnect = maBase.cursor()

    try:
        sql = "delete from note where code= %s "
        val = ( matricule,)
        meConnect.execute(sql, val)
        maBase.commit()
        derniereMatricule = meConnect.lastrowid
        messagebox.showinfo("information", "Note Supprimer")
        root.destroy()
        call(["python", "Chambre2.py"])

    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close()"""


#Ma fenetre
root  = Tk()

root.title("Menu principal")
root.geometry("1350x700+0+0")
root.resizable(False, False)
root.configure(background="#FFE4C4")

#Ajouter le titre
lbltitre = Label(root,borderwidth = 3, relief = SUNKEN
                 , text = "Gestion de notes d'employés", font = ("Sans Serif", 25), background = "#A52A2A", fg="#FFFAFA")
lbltitre.place(x = 0, y = 0, width = 1350, height=100)

#Matricule
lblNumero = Label(root, text="Id", font=("Arial", 18), bg="#A52A2A", fg="white")
lblNumero.place(x=70, y=150, width=150)
txtNumero = Entry(root,bd=4, font=("Arial", 14))
txtNumero.place(x=250,y=150,width=150)

#Nom
lblnom = Label(root, text="Nom", font=("Arial", 18), bg="#A52A2A", fg="white")
lblnom.place(x=70, y=200, width=150)
txtnom = Entry(root,bd=4, font=("Arial", 14))
txtnom.place(x=250,y=200,width=300)
#Prenom
lblprenom = Label(root, text="Prénom", font=("Arial", 18), bg="#A52A2A", fg="white")
lblprenom.place(x=70, y=250, width=150, )
txtprenom = Entry(root,bd=4, font=("Arial", 14))
txtprenom.place(x=250,y=250,width=300)

#sexe

valeurSexe = StringVar()

lblSexeMasculin = Radiobutton(root, text="Homme", value="M",variable=valeurSexe, indicatoron=0, font=("Arial", 14), bg="#A52A2A", fg="#696969")
lblSexeMasculin.place(x=250, y=300, width=130)
txtSexeFeminin = Radiobutton(root,text="Femme",value="F", variable=valeurSexe, indicatoron=0,font=("Arial", 14), bg="#A52A2A", fg="#696969")
txtSexeFeminin.place(x=420,y=300,width=130)

#Classe
lblClasse = Label(root, text="Secteur", font=("Arial", 18), bg="#A52A2A", fg="white")
lblClasse.place(x=70, y=350, width=150, )

comboClasse = ttk.Combobox(root,font=("Arial", 14))
comboClasse['values'] = ['NDRC1', 'NDRC2', 'SIO1 ', 'SIO2']
comboClasse.place(x=250, y=350, width=130)

#Matiere
lblmatiere = Label(root, text="Performance", font=("Arial", 18), bg="#A52A2A", fg="white")
lblmatiere.place(x=70, y=400, width=150, )

combomatiere = ttk.Combobox(root,font=("Arial", 14))
combomatiere['values'] = ['SLAM', 'Anglais', 'Francais ', 'Maths']
combomatiere.place(x=250, y=400, width=130)

#note
lblnote = Label(root, text="NOTE", font=("Arial", 18), bg="#A52A2A", fg="white")
lblnote.place(x=70, y=450, width=150, )
txtnote = Entry(root,bd=4, font=("Arial", 14))
txtnote.place(x=250,y=450,width=200)

#Enregistrer
btnenregistrer = Button(root, text = "Enregistrer", font = ("Arial", 16),bg = "#A52A2A", fg = "white", command=Ajouter)
btnenregistrer.place(x=250, y= 500, width=200)

"""#modifier
btnmodofier = Button(root, text = "Modifier", font = ("Arial", 16),bg = "#A52A2A", fg = "white", command=Modifer)
btnmodofier.place(x=250, y= 550, width=200)

#Supprimer
btnSupprimer = Button(root, text = "Supprimer", font = ("Arial", 16),bg = "#A52A2A", fg = "white", command=Supprimer)
btnSupprimer.place(x=250, y= 600, width=200)"""

#Table
table = ttk.Treeview(root, columns = (1, 2, 3, 4, 5, 6, 7), height = 5, show = "headings")
table.place(x = 560,y = 150, width = 790, height = 450)

#definir les dimentions des colonnes
table.column(1,width = 50)
table.column(2,width = 150)
table.column(3,width = 150)
table.column(4,width = 100)
table.column(5,width = 50)
table.column(6,width = 100)
table.column(7,width = 50)

#Entete
table.heading(1 , text = "Id")
table.heading(2 , text = "Nom")
table.heading(3 , text = "Prénom")
table.heading(4 , text = "Sexe")
table.heading(5 , text = "Secteur")
table.heading(6 , text = "Performance")
table.heading(7 , text = "Note")

# afficher les informations de la table
maBase = mysql.connector.connect(host="localhost", user="root",password="", database="note_eleve")
meConnect = maBase.cursor()
meConnect.execute("select * from note")
for row in meConnect:
    table.insert('', END, value = row)
maBase.close()

#Execution
root.mainloop()