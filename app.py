from flask import Flask, render_template
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
    return render_template('index.html')
    

#avvio dell'app Flask - Sempre mettere alla fine
if __name__ == '__main__':
    app.run(debug=True)
