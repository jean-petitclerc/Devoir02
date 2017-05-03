from flask import Flask, session, redirect, url_for, request, render_template, flash, g, abort
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
manager = Manager(app)

# Read the configurations
app.config.from_pyfile('config/config.py')

db = SQLAlchemy(app)


# Database Model
class Ami(db.Model):
    __tablename__ = 't_amis'
    id_ami = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    prenom = db.Column(db.String(30), nullable=False)
    nom_de_famille = db.Column(db.String(30), nullable=False)

    def __init__(self, prenom, nom_de_famille):
        self.prenom = prenom
        self.nom_de_famille = nom_de_famille

    def __repr__(self):
        return '<ami: {}>'.format(self.nom_de_famille)


# The following functions are views
@app.route('/')
def index():
    empty_db()
    fill_db()
    amis = Ami.query.order_by(Ami.prenom).all()
    return render_template('index.html', amis=amis)


def fill_db():
    amis = [Ami('Jean', 'Petitclerc'), Ami('Diem', 'Ha'), Ami('Victoria', 'Leon')]
    for ami in amis:
        db.session.add(ami)
    db.session.commit()


def empty_db():
    amis = Ami.query.all()
    for ami in amis:
        db.session.delete(ami)
    db.session.commit()


# Start the server for the application
if __name__ == '__main__':
    manager.run()

