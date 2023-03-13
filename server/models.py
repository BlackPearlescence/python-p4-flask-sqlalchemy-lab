from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *

db = SQLAlchemy()

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    birthday = db.Column(db.Date)
    animals = db.relationship('Animal', back_populates="zookeeper")

    # animal = db.relationship('Animal', back_populates='zookeeper')

class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String)
    open_to_visitors = db.Column(db.Integer)
    animals = db.relationship('Animal', back_populates="enclosure")

    # animal = db.relationship('Animal', back_populates='enclosure')

class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)
    zookeeper = db.Column(db.String)
    enclosure = db.Column(db.String)
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'), name="fk_animals_enclosures_id")
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'), name="fk_animals_zookeepers_id")

    enclosure = db.relationship('Enclosure', back_populates='animals')
    zookeeper = db.relationship('Zookeeper', back_populates='animals')