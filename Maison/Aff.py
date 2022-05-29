#Les Bibliotheque a importer
import tkinter
from cProfile import label
from tkinter import ttk, Tk
from PIL import Image,ImageTk
from tkinter import *
from subprocess import call
from tkinter import messagebox
#cd AppData\Local\Programs\Python\Python39
#python -m pip install mysql-connector-python
import mysql.connector

#Ma fenetre
root  = Tk()

root.title("Liste des personnes inscrites")
root.geometry("1350x700+0+0")
root.resizable(False, False)
root.configure(background="#FFE4C4")

#Ajouter le titre
lbltitre = Label(root,borderwidth = 3, relief = SUNKEN
                 , text = "Gestion de notes d'employés", font = ("Sans Serif", 25), background = "#A52A2A", fg="#FFFAFA")
lbltitre.place(x = 0, y = 0, width = 1350, height=100)

#Table
table = ttk.Treeview(root, columns = (1, 2, 3), height = 5, show = "headings")
table.place(x = 560,y = 150, width = 790, height = 450)

#definir les dimentions des colonnes
table.column(1,width = 50)
table.column(2,width = 150)
table.column(3,width = 150)



#Entete
table.heading(1 , text = "Id")
table.heading(2 , text = "Nom")
table.heading(3 , text = "Prénom")

# afficher les informations de la table
maBase = mysql.connector.connect(host="localhost", user="root",password="", database="note_eleve")
meConnect = maBase.cursor()
meConnect.execute("select * from personne")
for row in meConnect:
    table.insert('', END, value = row)
maBase.close()

#Execution
root.mainloop()