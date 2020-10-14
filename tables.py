from sqlalchemy import Column, ForeignKey, Integer, String,Date,Float,DateTime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
import datetime
from sqlalchemy.orm import relationship

#Base = declarative_base()
db = SQLAlchemy()

class Pet(db.Model):
    __tablename__ = 'pets'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    birth = db.Column(db.Date, nullable=False)
    race = db.Column(db.String(80), nullable=False)

    def __init__(self,name,code,birth,race):
        self.name = name
        self.code = code
        self.birth = birth
        self.race = race

    def __repr__(self):
        return '<Pet name %r>' % self.name

class Collar(db.Model):
    __tablename__ = 'collar'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    heart_frequency = db.Column(db.Integer,  nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    x_axis = db.Column(db.Integer, nullable=False)
    y_axis = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    pet_id = db.Column(db.Integer,ForeignKey('pets.id'),nullable=True )
    pet = relationship('Pet',backref='collars')

    def __init__(self,heart_frequency, temperature, x_axis,y_axis,pet):
        self.heart_frequency = heart_frequency
        self.temperature = temperature
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.timestamp = datetime.datetime.now()

    def __repr__(self):
        return '<Collar id %r>' % self.id

if __name__ == '__main__':
    print('Tables')
    pet = Pet(name='Teste', code = '1234', birth = datetime.datetime.now(),race='bulldog')
    collar = Collar(heart_frequency=55,temperature=35.0,x_axis=25,y_axis=30,pet=pet)
    print('Teste done')


