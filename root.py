from flask import Flask
import datetime
from flask import render_template
import webbrowser

# l'hôte
HOST = "127.0.0.1"
# le port
PORT = 3000

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def gui():
	"""Cette fonction presente les données de l'interface graphique"""
	title = "Convertisseur Monnaies"
	devises = ["CDF",
                   "USD",
                   "EUR",
                   "BTC"
                   ]
	today = datetime.datetime.now().strftime("%d-%B-%Y")
	years = today.split("-")[2]			# recupération de l'année dans le deuxième index de la liste génerée par split 
	cut_dash = today.split("-")
	today = " ".join(cut_dash)
	return render_template("interface.html", title=title, devises=devises, today=today, years = years)

if __name__ == "__main__":
	print("Vérification de l'accès")
	
	URL = "http://{0}:{1}".format(HOST, PORT)			# formatage de l'url 127.0.0.1:5000
	run_browser = webbrowser.open(URL)					# Ouverture de l'url (127.0.0.1:5000) dans le navigateur
	app.run(host=HOST, port=PORT)