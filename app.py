from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from models import db, ListaSpesa

#inizializza l'app Flask
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///listaSpesa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()


#rotta principale
@app.route('/')
def home():
    lista_spesa = ListaSpesa.query.all()
    return render_template('index.html', lista_spesa=lista_spesa)
    
@app.route('/aggiungi', methods=['POST'])
def aggiungi_prodotto():
    elemento = request.form['elemento']
    prodotto = ListaSpesa(elemento=elemento)
    if prodotto:
        db.session.add(prodotto)
        db.session.commit()
    return (redirect(url_for('home')))

@app.route('/rimuovi/<int:indice>', methods=['POST'])
def rimuovi_oggetto(indice):
    elemento_da_rimuovere = ListaSpesa.query.get(indice)
    if elemento_da_rimuovere:
        db.session.delete(elemento_da_rimuovere)
        db.session.commit()
    return(redirect(url_for('home')))

@app.route('/svuota', methods=['POST'])
def svuota_lista():
    ListaSpesa.query.delete()
    db.session.commit() 
    return redirect(url_for('home'))


#avvio dell'app Flask - Sempre mettere alla fine
if __name__ == '__main__':
    app.run(debug=True)
