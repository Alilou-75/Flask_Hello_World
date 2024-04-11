from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route("/contact/")
def MaPremiereAPI():
    return render_template("contact.html")

@app.route('/exercices/')
def exercices():
    return render_template('exercices.html')
  
@app.route('/calcul_carre/<int:val_user>')
def carre(val_user):
    return "<h2>Le carré de votre valeur est : </h2>" + str(val_user * val_user)
  
@app.route('/somme/<int:valeur1>/<int:valeur2>')
def somme(valeur):
    return "<h2>La somme de vos 2 valeurs est : </h2>" + str(valeur1 + valeur2)
                                                                                                               
if __name__ == "__main__":
  app.run(debug=True)
