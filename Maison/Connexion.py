# Les Bibliotheque a importer
from subprocess import call
from tkinter import ttk, Tk
from tkinter import *
from tkinter import messagebox
import mysql.connector
import services as serv


# Fonction Connecter


def Seconnecter():
    surnom = txtnomUtilisateur.get()
    mdp = txtmdp.get()
    if surnom == "" or mdp == "":
        messagebox.showerror(
            "Erreur", "Veuillez saisir le nom et le mot de passe")
    else:
        try:
            conn = mysql.connector.connect(
                host="localhost", user="root", password="", database="gestion_contact")
            cursor = conn.cursor()
            cursor.execute(
                "select * from admin where nom=%s and mdp=%s", (surnom, mdp))
            row = cursor.fetchone()
            if row == None:
                messagebox.showerror("Erreur", "Invalide")
            else:
                messagebox.showinfo(
                    "", "Bienvenue  " + surnom + "!")
                txtnomUtilisateur.delete("0", "end")
                txtmdp.delete("0", "end")
                root.destroy()
                call(["python", "Maison/Accueil.py"])
                conn.close()

        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}")


# La fenetre
root = Tk()

root.title("Connexion")
root.geometry("400x300+450+400")
root.resizable(False, False)
root.configure(background="#FFE4C4")

# Ajouter le nom et mdp
lbltitre = Label(root, borderwidth=3, relief=SUNKEN, text="Formulaire de connexion", font=(
    "Sans Serif", 25), background="#A52A2A", foreground="white")
lbltitre.place(x=0, y=0, width=400)

lblnomUtilisateur = Label(root, text="Nom  :", font=(
    "Arial", 14), bg="#FFE4C4", fg="black")
lblnomUtilisateur.place(x=5, y=100, width=150)
txtnomUtilisateur = Entry(root, bd=4, font=("Arial", 13))
txtnomUtilisateur.place(x=150, y=100, width=200, height=30)

lblmdp = Label(root, text="Mot de Passe :", font=(
    "Arial", 14), bg="#FFE4C4", fg="black")
lblmdp.place(x=5, y=150, width=150)
txtmdp = Entry(root, show="*", bd=4, font=("Arial", 13))
txtmdp.place(x=150, y=150, width=200, height=30)

# Bouton Connecter
btnenregistrer = Button(root, text="Connexion", font=(
    "Arial", 16), bg="#A52A2A", fg="white", command=Seconnecter)
btnenregistrer.place(x=150, y=200, width=200)


# Execution
root.mainloop()
