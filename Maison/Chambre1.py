#Les Bibliotheque a importer
from subprocess import call
from tkinter import ttk, Tk
from tkinter import *
from tkinter import messagebox
import mysql.connector

#Fonction Connecter
def Seconnecter():
    surnom = txtnomUtilisateur.get()
    mdp = txtmdp.get()
    if (surnom == "" and mdp == ""):
        messagebox.showerror("", "il faut rentrer les Données")
        txtmdp.delete("0", "end")
        txtnomUtilisateur.delete("0", "end")
    elif (surnom == "admin" and mdp == "admin"):
        messagebox.showinfo("", "Bienvenue")
        txtnomUtilisateur.delete("0", "end")
        txtmdp.delete("0", "end")
        root.destroy()
        call(["python", "Chambre2.py"])

    else:
        messagebox.showwarning("", "Erreur de Connexion")
        txtmdp.delete("0", "end")
        txtnomUtilisateur.delete("0", "end")

def Inscription():
    call(["python", "Accueil.py"])

#La fenetre
root  = Tk()

root.title("Aller on se connecte")
root.geometry("400x300+450+400")
root.resizable(False, False)
root.configure(background="#FFE4C4")

#Ajouter le nom et mdp
lbltitre = Label(root,borderwidth = 3, relief = SUNKEN
                 , text = "Formulaire de connexion", font = ("Sans Serif", 25), background = "#A52A2A", foreground="white")
lbltitre.place(x = 0, y = 0, width = 400)

lblnomUtilisateur = Label (root, text="Nom Utilisateur :", font=("Arial", 14),bg="#FFE4C4", fg="black")
lblnomUtilisateur.place(x = 5, y = 100,width = 150 )
txtnomUtilisateur = Entry(root,bd=4, font=("Arial", 13))
txtnomUtilisateur.place(x=150,y=100,width=200,height=30)

lblmdp = Label (root, text="Mot de Passe :", font=("Arial", 14),bg="#FFE4C4", fg="black")
lblmdp.place(x = 5, y = 150,width = 150 )
txtmdp = Entry(root,show="*",bd=4, font=("Arial", 13))
txtmdp.place(x=150,y=150,width=200,height=30)

#Bouton Connecter
btnenregistrer = Button(root, text = "Connexion", font = ("Arial", 16),bg ="#A52A2A", fg = "white", command=Seconnecter)
btnenregistrer.place(x=150, y= 200, width=200)

#Bouton S'inscrire
btninscription = Button(root, text = "S'inscrire", font = ("Arial", 16),bg ="#A52A2A", fg = "white", command=Inscription)
btninscription.place(x=150, y= 250, width=200)



#Execution
root.mainloop()