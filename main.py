from tkinter import *
from tkcalendar import *
from tkinter import messagebox
from config import insert_employe, connect_to_server
from tkinter import ttk

class MainWindow:
    """Cette classe présente la fenêtre principale"""
    def __init__(self, root):
        # création du widget principal
        self.root = root
        self.root.title("Gestion du personnelle")
        self.root.geometry("1920x1080+-10+-2")
        # création du cadre
        cadre = Frame(self.root, bg="grey")
        cadre.place(x=300, y=200, width=700, height=400)

        # création des tous les widgets enfant
        title= Label(cadre, text="Gestion Du Personnelle", bg="grey", fg="black", font=("castellar", 24, "bold"))
        title.place(x=138, y=30)

        # create a new departement button
        btn1 = Button(cadre, text="Créer un département", bg="#2874A6", fg="black", font=("time new rom", 15, "bold"))
        btn1.config(command=ChildWindow().create_departement)
        btn1.place(x=50, y=100, width=250)
        
        # print list of all departement button
        btn2 = Button(cadre, text="Afficher départements", bg="green", fg="black", font=("time new rom", 15, "bold"))
        btn2.config(command=AfficheDepartements.affiche_departement)
        btn2.place(x=370, y=100, width=250)
        
        # addition of a worker in the departement
        btn3 = Button(cadre, text='Ajouter un employé', bg="yellow", fg="black", font=("time new rom", 15, "bold"))
        btn3.config(command=self.open_form_addEmp)
        btn3.place(x=50, y=160, width=250)
        
        # print all worker in the departement
        btn4 = Button(cadre, text="Afficher employés", bg="orange", fg="black", font=("time new rom", 15, "bold"))
        btn4.config(command=AfficheEmployes().affiche_employe)
        btn4.place(x=370, y=160, width=250)

        # quit button
        btn_quit = Button(cadre, text='Quitter', bg="lightgrey" ,font=("time new rom", 15, "bold"), fg="black")
        btn_quit.config(command=root.quit)
        btn_quit.place(x=260, y=300, width=150)

    def open_form_addEmp(self):
        self.form=AjoutEmploye()

    # def open_other_form_addEmp_To_Dep(self):
    #     self.other_form = AddWokerToDepartement()

class ChildWindow:
    """Ceci est une fenêtre enfant qui s'ouvre lorsqu'on appui sur le bouton 
    Créer un département
     """
    @classmethod
    def create_departement(cls):
        root = Toplevel()
        root.title("Création d'un nouveau département")
        root.geometry("1980x1080+-10+-2")

        cadre = Frame(root, bg="grey")
        cadre.place(x=300, y=200, width=680, height=400)

        # titre du cadre
        titre = Label(cadre, text="Creez un nouveau département", font=("courier new", 22, "bold"), bg="grey", fg="black")
        titre.place(x=105, y=30)

        # numéro du departement
        Label(cadre, text='Code du département', bg="grey", fg="black", font=("time new rom", 15)).place(x=50, y=100)
        entre_num = Entry(cadre, font=('time new rom', 15), bg="lightgrey")
        # EMPLACEMENT DANS LE CADRE
        entre_num.place(x=50, y=130)
        
        # nom du département
        Label(cadre, text='Nom du département', bg='grey', font=("time new rom", 15)).place(x=370, y=100)
        entre_nom = Entry(cadre, font=("time new rom", 15), bg="lightgrey")
        # EMPLACEMENT DANS LE CADRE
        entre_nom.place(x=370, y=130)


        def valider():
            nom_departement = entre_nom.get()
            num_departement = entre_num.get()
            if (num_departement != "") and (nom_departement != ""):
                db = connect_to_server()
                c = db.cursor()
                c.execute("CREATE TABLE IF NOT EXISTS departement(idDep INT PRIMARY KEY AUTO_INCREMENT,codeDep VARCHAR(100),nomDep VARCHAR(100))")
                c.execute("INSERT INTO departement(codeDep, nomDep) VALUES(%s,%s)",(str(num_departement),str(nom_departement)))
                db.commit()
                db.close()
                messagebox.showinfo("Successfull", "Département créé avec succès", parent=root)
                entre_num.delete(0, END)
                entre_nom.delete(0, END)

                
            else:
                messagebox.showerror("Erreur", "Remplissez tout les champs", parent=root)

        btn_valider = Button(cadre, text="Créer", font=("time new rom", 15, 'bold'), fg="black", bg="lightgrey")
        btn_valider.config(command=valider)
        btn_valider.place(x=160, y=220, width=150)


        # BOUTTON QUITTER
        btn_quit = Button(cadre, text="Retour", font=("time new rom", 15, "bold"), fg="black", bg="lightgrey")
        btn_quit.config(command=root.destroy)
        btn_quit.place(x=360, y=220, width=150)


class AjoutEmploye:
    def __init__(self):
        self.root = Toplevel()
        self.root.title("Ajout d'un employé dans la liste des départements")
        self.root.geometry("1980x1080+-10+-2")

        cadre = Frame(self.root, bg="grey")
        cadre.place(x=300, y=200, width=700, height=400)

        # titre du cadre
        titre = Label(cadre, text="Ajoutez un nouvel employé", font=("courier new",22, "bold"), bg="grey", fg="black")
        titre.place(x=130, y=30)

        # nom
        text_nom = Label(cadre, text="Nom", font=("time new rom", 15), bg="grey", fg="black").place(x=50, y=100)
        self.ecr_nom = Entry(cadre, font=("time new rom", 15), bg="lightgrey")
        self.ecr_nom.place(x=50, y=130)

        # prenom
        text_prenom = Label(cadre, text="Prénom", font=("time new rom", 15), bg="grey", fg="black").place(x=370, y=100)
        self.ecr_prenom = Entry(cadre, font=("time new rom", 15), bg="lightgrey")
        self.ecr_prenom.place(x=370, y=130)

        # postnom
        text_postnom = Label(cadre, text="Post-Nom", font=("time new rom", 15), bg="grey", fg="black").place(x=50, y=160)
        self.ecr_postnom = Entry(cadre, font=("time new rom", 15), bg="lightgrey")
        self.ecr_postnom.place(x=50, y=190)

        # matricule
        text_mat = Label(cadre, text="Matricule", font=("time new rom", 15), bg="grey", fg="black").place(x=370, y=160)
        self.ecr_mat= Entry(cadre, font=("time new rom", 15), bg="lightgrey")
        self.ecr_mat.place(x=370, y=190)

        # date de naissance
        text_date = Label(cadre, text="Né le", font=("time new rom", 15), bg="grey", fg="black").place(x=50, y=220)
        self.ecr_date = DateEntry(cadre, font=("time new rom", 15), bg="lightgrey", date_pattern="dd-mm-yyyy", state="readonly")
        self.ecr_date.place(x=50, y=250)
        #donnee_employee(root, ecr_nom.get(), ecr_postnom.get(), ecr_prenom.get(), ecr_mat.get(), ecr_date.get())

        # text_departement
        text_dep = Label(cadre, text="Département n°", font=("time new rom", 15), bg="grey").place(x=370, y=220)
        self.ecr_dep = Entry(cadre, font=("time new rom", 15), bg="lightgrey")
        self.ecr_dep.place(x=370, y=250, width=200)

        # bouton enregistrer
        btn_enr = Button(cadre, text='Enrégistrer', font=("time new rom", 15, "bold"), bg="lightgrey")
        btn_enr.config(command=self.save_employe)
        btn_enr.place(x=180, y=320, width=150)

        # # bouton ajouter au département 
        # btn_ajout = Button(cadre, text='Ajouter au département', font=('time new rom', 15, "bold"))
        # btn_ajout.config(command=self.save_id_employe)
        # btn_ajout.place(x=230, y=320)

        # BOUTON quitter
        btn_quit = Button(cadre, text='Retour', font=("time new rom", 15, "bold"), bg="lightgrey")
        btn_quit.config(command=self.root.destroy)
        btn_quit.place(x=370, y=320, width=150)

    def reinitialise(self):
         self.ecr_nom.delete(0, END)
         self.ecr_postnom.delete(0, END)
         self.ecr_prenom.delete(0, END)
         self.ecr_mat.delete(0, END)
         self.ecr_dep.delete(0, END)
    
    def save_employe(self):
        if self.ecr_nom.get()=="" or self.ecr_postnom.get() =="" or self.ecr_prenom.get()== "" or self.ecr_dep.get() == "":
            messagebox.showerror("Erreur", "Remplissez tout les champs", parent=self.root)
        else:
            insert_employe(self.root, self.ecr_nom.get(), self.ecr_postnom.get(), self.ecr_prenom.get(), self.ecr_mat.get(), self.ecr_date.get(), self.ecr_dep.get())
            self.reinitialise()


class AfficheDepartements:
    @classmethod
    def affiche_departement(cls):
        root = Toplevel()
        root.title("Inventaire du département")
        root.geometry("810x480+230+145")
        # root.config(bg="#17202A")
        tree = ttk.Treeview(root)
        dep = "Liste de tous les départements"

        titre = Label(root, text=dep, font=("Arial bold", 30), bd=2)
        titre.grid(row=0, column=2, columnspan=3, padx=2, pady=20)

        Label(root, text="Id_département:", font=("Arial bold", 15)).grid(row=1, column=1)
        entre_id = Entry(root, font=("Arial bold", 15), bg="white")
        entre_id.grid(row=1, column=2)

        Label(root, text="Code_département:", font=("Arial bold", 15)).grid(row=2, column=1)
        entre_code = Entry(root, font=("Arial bold", 15), bg="white")
        entre_code.grid(row=2, column=2)

        Label(root, text="Nom_département:", font=("Arial bold", 15)).grid(row=3, column=1)
        entre_nom = Entry(root, font=("Arial bold", 15), bg="white")
        entre_nom.grid(row=3, column=2)

        def delete_dep(data):
            db = connect_to_server()
            c = db.cursor()
            c.execute("DELETE FROM departement WHERE idDep=%s", data)
            db.commit()
            messagebox.showinfo("Successfull", "Département supprimé")
            root.destroy()


        def update(idd, code_d, nom_d):
            db = connect_to_server()
            c = db.cursor()
            c.execute("UPDATE departement SET codeDep='{0}', nomDep='{1}' WHERE idDep={2}".format(str(code_d), str(nom_d), idd))
            db.commit()
            messagebox.showinfo("Successfull", "Département modifié")
            db.close()
            root.destroy()


        def supp():
            if entre_id.get() == "":
                messagebox.showerror("Erreur", "Entrez l'identifiant du département que vous voulez supprimer", parent=root)
            else:
                ident = entre_id.get()
                msg = messagebox.askyesno("Question", "Voulez-vous vraiment supprimer ce département ?\nCette action est irréversible", parent=root)
                if msg is False:
                    pass
                else:
                    delete_dep(ident)


        def upgrade():
            ident = entre_id.get()
            match ident:
                case "":
                    messagebox.showerror("Erreur", "Entrez l'identifiant du département que vous voulez modifier", parent=root)
                case _:
                    codee = entre_code.get()
                    name = entre_nom.get()
                    match name and codee:
                        case "":
                            messagebox.showerror("Erreur", "Entrez le nouveau code et le nouveau nom du département", parent=root)
                        case _:
                            update(ident, codee, name)

        btn_delete = Button(root, text="Supprimer", font=("verdana", 15), bg='red', fg="white", command=supp).grid(row=1, column=4)

        btn_updata = Button(root, text="Modifier", font=('verdana', 15), bg='#2874A6', fg="white", command=upgrade).grid(row=3, column=4)



        def affiche_data():
            db = connect_to_server()
            c = db.cursor()
            # c.execute("""CREATE TABLE IF NOT EXISTS departement(idDep INT PRIMARY KEY AUTO_INCREMENT,codeDep VARCHAR(100),nomDep VARCHAR(100)""")
            c.execute("SELECT* FROM departement")
            row = c.fetchall()
            db.commit()
            return row


        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial bold", 15))

        tree["columns"]=("Id_dep", "Code_dep", "Nom_dep")
        tree.column("#0", width=0, stretch=NO)
        tree.column("Id_dep", anchor=S, width=100)
        tree.column("Code_dep", anchor=S, width=200)
        tree.column("Nom_dep", anchor=S, width=370)
        tree.heading("Id_dep", text="Id", anchor=S)
        tree.heading("Code_dep", text="Code du département", anchor=S)
        tree.heading("Nom_dep", text="Nom du département", anchor=S)
        
        for data in tree.get_children():
                tree.delete(data)

        for results in affiche_data():
            tree.insert('', END, values=(results), tag="orow")

        tree.tag_configure('orow', background="#FFFFFF", font=("Arial bold", 15))
        tree.grid(row=5, column=1, columnspan=6, rowspan=6, padx=10, pady=10)

    
class AfficheEmployes:
    @classmethod
    def affiche_employe(cls):
        root = Toplevel()
        root.title("Inventaire de l'employer")
        root.geometry("1178x580+55+100")
        tree = ttk.Treeview(root)
        emp = "Liste de tous les employés"

        titre = Label(root, text=emp, font=("Arial bold", 30), bd=2)
        titre.grid(row=0, column=1, columnspan=6, padx=20, pady=20)


        Label(root, text="Identifiant:", font=("Arial bold", 15)).grid(row=1, column=1)
        entre_id = Entry(root, font=("Arial bold", 15), bg="white")
        entre_id.grid(row=1, column=2)

        Label(root, text="Nom:", font=("Arial bold", 15)).grid(row=2, column=1)
        entre_nom = Entry(root, font=("Arial bold", 15), bg="white")
        entre_nom.grid(row=2, column=2)

        Label(root, text="Post-nom:", font=("Arial bold", 15)).grid(row=3, column=1)
        entre_postnom = Entry(root, font=("Arial bold", 15), bg="white")
        entre_postnom.grid(row=3, column=2)

        Label(root, text="Prénom:", font=("Arial bold", 15)).grid(row=4, column=1)
        entre_prenom = Entry(root, font=("Arial bold", 15), bg="white")
        entre_prenom.grid(row=4, column=2)

        Label(root, text="Matricule:", font=("Arial bold", 15)).grid(row=5, column=1)
        entre_mat = Entry(root, font=("Arial bold", 15), bg="white")
        entre_mat.grid(row=5, column=2)

        Label(root, text="Date de Naissance:", font=("Arial bold", 15)).grid(row=6, column=1)
        entre_dat = DateEntry(root, font=("Arial bold", 15), date_pattern="dd-mm-yyyy", state="readonly")
        entre_dat.grid(row=6, column=2)

        Label(root, text="Département:", font=("Arial bold", 15)).grid(row=7, column=1)
        entre_dep = Entry(root, font=("Arial bold", 15), bg="white")
        entre_dep.grid(row=7, column=2)




        def delete_emp(dat):
            db = connect_to_server()
            c = db.cursor()
            c.execute("DELETE FROM employee WHERE idEmploye=%s", dat)
            db.commit()
            messagebox.showinfo("Successfull", "Employé supprimé")
            root.destroy()


        def updat(idd, nom, postnom, prenom, mat, dateN, dept):
            db = connect_to_server()
            c = db.cursor()
            c.execute("""UPDATE employee SET nomEmploye='{0}', postnomEmploye='{1}', prenomEmploye='{2}', 
                matriculeEmploye='{3}', dateNaissanceEmploye='{4}', idDep={5} WHERE idEmploye={6}""".format(str(nom), str(postnom), str(prenom), str(mat), str(dateN), dept, idd))
            db.commit()
            messagebox.showinfo("Successfull", "Employer modifié")
            db.close()
            root.destroy()


        def suppr():
            if entre_id.get() == "":
                messagebox.showerror("Erreur", "Entrez l'identifiant de l'employé que vous voulez supprimer", parent=root)
            else:
                identf = entre_id.get()
                msg = messagebox.askyesno("Question", "Voulez-vous vraiment supprimer cet employé ?\nCette action est irréversible", parent=root)
                if msg is False:
                    pass
                else:
                    delete_emp(identf)


        def modify():
            identf = entre_id.get()
            match identf:
                case "":
                    messagebox.showerror("Erreur", "Entrez l'identifiant de l'employé que vous voulez modifier", parent=root)
                case _:
                    name = entre_nom.get()
                    postname = entre_postnom.get()
                    prename = entre_prenom.get()
                    mat = entre_mat.get()
                    datn = entre_dat.get()
                    dep = entre_dep.get()
                    match name and postname and prename and dep:
                        case "":
                            messagebox.showerror("Erreur", "Entrez les nouvelles informations de l'employé", parent=root)
                        case _:
                            updat(identf, name, postname, prename, mat, datn, dep)

        btn_delete = Button(root, text="Supprimer", font=("verdana", 15), bg='red', fg="white", command=suppr).grid(row=2, column=3)

        btn_updata = Button(root, text="Modifier", font=('verdana', 15), bg='#2874A6', fg="white", command=modify).grid(row=4, column=3)


        def affiche_employe():
            db = connect_to_server()
            c = db.cursor()
            c.execute("""CREATE TABLE IF NOT EXISTS employee(idEmploye INT PRIMARY KEY AUTO_INCREMENT,nomEmploye VARCHAR(100),postnomEmploye VARCHAR(100),prenomEmploye VARCHAR(255),
                matriculeEmploye VARCHAR(255),dateNaissanceEmploye VARCHAR(255))""")
            c.execute("SELECT* FROM employee")
            row = c.fetchall()
            db.commit()

            return row

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial bold", 15))

        tree["columns"]=("Id_emp", "Nom_emp", "Postnom_emp", "Prenom_emp", "Matricule_emp", "Date_emp", "Id_dep")
        tree.column("#0", width=0, stretch=NO)
        tree.column("Id_emp", anchor=S, width=100)
        tree.column("Nom_emp", anchor=S, width=200)
        tree.column("Postnom_emp", anchor=S, width=200)
        tree.column("Prenom_emp", anchor=S, width=200)
        tree.column("Matricule_emp", anchor=S, width=100)
        tree.column("Id_dep", anchor=S, width=150)
        tree.column("Date_emp", anchor=S, width=200)
        tree.heading("Id_emp", text="Id", anchor=S)
        tree.heading("Nom_emp", text="Nom", anchor=S)
        tree.heading("Postnom_emp", text="Post-Nom", anchor=S)
        tree.heading("Prenom_emp", text="Prénom", anchor=S)
        tree.heading("Matricule_emp", text="Matricule", anchor=S)
        tree.heading("Id_dep", text="Département n°", anchor=S)
        tree.heading("Date_emp", text="Date de Naissance", anchor=S)
        

        for emp in tree.get_children():
            tree.delete(emp)

        for employer in affiche_employe():
            tree.insert('', END, values=(employer), tag="orow")

        tree.tag_configure('orow', background="#FFFFFF", font=("Arial bold", 15))
        tree.grid(row=9, column=1, columnspan=6, rowspan=7, padx=10, pady=10)