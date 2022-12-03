import pymysql
from tkinter import messagebox
import datetime


def connect_to_server():

	conn = pymysql.connect(
        host='localhost',
        user='root', 
        password = "josue",
        db='gestion_personel'
        )

	return conn
	 
def create_table():
    # creation table employee
    try:
    	connexion = connect_to_server()
    	cur = connexion.cursor()
    	req="""CREATE TABLE employee(idEmploye INT PRIMARY KEY AUTO_INCREMENT,nomEmploye VARCHAR(100),postnomEmploye VARCHAR(100),prenomEmploye VARCHAR(255),matriculeEmploye VARCHAR(255),dateNaissanceEmploye VARCHAR(255), idDep INT NOT NULL, FOREIGN KEY(idDep) REFERENCES departement(idDep))"""
    	cur.execute(req)
    	conn.commit()
    except Exception:
    	print("Table employee éxiste déjà")

    #creation table departemnt
    #connexion = connect_to_server()
    #cur = conn.cursor()
    try:
    	req="""CREATE TABLE departement(idDep INT PRIMARY KEY AUTO_INCREMENT,codeDep VARCHAR(100),nomDep VARCHAR(100))"""
    	cur.execute(req)
    	connexion.commit()
    except Exception as exc:
    	print(exc)
    	print("Table departement éxiste déjà")
    cur.close()
    connexion.close()

def insert_employe(root,nom,postnom,prenom,mat,dateN,idDep ):
	#print(nom, postnom, prenom, mat,dateN)
	#dt=date(2022,0,2)
	#req="INSERT INTO employee(nomEmploye, postnomEmploye, prenomEmploye, matriculeEmploye, dateNaissanceEmploye) VALUES(:nomEmploye,:postnomEmploye,:prenomEmploye,:matriculeEmploye,:dateNaissanceEmploye)",nomEmploye=nom,postnomEmploye=postnom,prenomEmploye=prenom,matriculeEmploye=mat,dateNaissanceEmploye=dt
	value=(nom,postnom,prenom,mat,dateN)
	connexion=connect_to_server()
	cur=connexion.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS employee(idEmploye INT PRIMARY KEY AUTO_INCREMENT,nomEmploye VARCHAR(100),postnomEmploye VARCHAR(100),prenomEmploye VARCHAR(255),matriculeEmploye VARCHAR(255),dateNaissanceEmploye VARCHAR(255), idDep INT NOT NULL, FOREIGN KEY(idDep) REFERENCES departement(idDep))")
	cur.execute("INSERT INTO employee(nomEmploye, postnomEmploye, prenomEmploye, matriculeEmploye, dateNaissanceEmploye, idDep) VALUES(%s,%s,%s,%s,%s,%s)",(str(nom),str(postnom),str(prenom),str(mat),str(dateN),idDep))
	connexion.commit()
	cur.close()
	connexion.close()
	messagebox.showinfo("Successfull", "Employer enrégistrer avec succès", parent=root)

def commando():
	#create table
	create_table()

#commando()