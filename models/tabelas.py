from sqlalchemy import Column, ForeignKey, Integer, String,Date,Float,DateTime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
import datetime
from sqlalchemy.orm import relationship

#Base = declarative_base()
db = SQLAlchemy()

#from app import db


class Owner(db.Model):
	__tablename__ = "owners" 
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String)
	cpf = db.Column(db.String, unique = True)
	senha = db.Column(db.String)
	
	@property
	def is_authenticated(self):
		return True
		
	@property
	def is_active(self):
		return True	
	
	@property
	def is_anonymous(self):
		return False
		
	def get_id(self):		
		return str(self.id)
	
	def __init__(self, nome, email, senha):
		self.nome = nome
		self.email = email
		self.senha = senha
		
	def __repr__(self):
		return "<Professor %r>" % self.nome

class Pet(db.Model):
	__tablename__ = "pet"
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String)
	code = db.Column(db.String, unique = True)
	birth = db.Column(db.DateTime)
	specie = db.Column(db.String)
	race = db.Column(db.String)
	collars = db.relationship('Collar', backref = 'pet')

	def __init__(self, name, code, birth,specie,race):
		self.name = name
		self.code = code
		self.birth = birth
		self.specie = specie
		self.race = race
		#self.collars = collars
		
	def __repr__(self):
		return "<pet name %r>" % self.name

class Collar(db.Model):
	__tablename__ = "collar"
	id = db.Column(db.Integer, primary_key = True)
	code = db.Column(db.String)
	pet_id = db.Column(db.Integer,db.ForeignKey('pet.id'))
	telemetries = db.relationship('Telemetry',backref='collar')

	def __init__(self, code, pet_id):
		self.code = code
		self.pet_id = pet_id

class Telemetry(db.Model):
	__tablename__ = "telemetries"
	id = db.Column(db.Integer, primary_key = True)
	code = db.Column(db.String)
	temperature = db.Column(db.Integer)
	humidity = db.Column(db.Integer)
	heartbeat = db.Column(db.Integer)
	oxigen = db.Column(db.Integer)
	latitude = db.Column(db.Float)
	longitude = db.Column(db.Float)
	x_axis = db.Column(db.Integer)
	y_axis = db.Column(db.Integer)
	z_axis = db.Column(db.Integer)
	x_ang = db.Column(db.Integer)
	y_ang = db.Column(db.Integer)
	z_ang = db.Column(db.Integer)
	timestamp = db.Column(db.DateTime)
	collar_code = db.Column(db.Integer,db.ForeignKey('collar.code'))
	
	
	def __init__(self,temperature,humidity,heartbeat,oxigen,latitude,longitude,x_axis,y_axis,z_axis,x_ang,y_ang,z_ang,collar_code):
		self.temperature = temperature
		self.humidity = humidity
		self.heartbeat = heartbeat
		self.oxigen = oxigen
		self.latitude = latitude
		self.longitude = longitude
		self.x_axis = x_axis
		self.y_axis = y_axis
		self.z_axis = z_axis
		self.x_ang = x_ang
		self.y_ang = y_ang
		self.z_ang = z_ang
		self.timestamp = datetime.datetime.now()
		self.collar_code = collar_code

		
	def __repr__(self):
		return "<Collar code%r>" % self.code
