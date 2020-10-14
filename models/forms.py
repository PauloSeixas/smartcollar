from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, DateTimeField,SelectField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateTimeLocalField


class LoginForm(FlaskForm):
	username = StringField("username", validators = [DataRequired()])
	password = PasswordField("password", validators = [DataRequired()])
	remember_me = BooleanField("remember-me")


class CadastroForm(FlaskForm):
	username = StringField("username", validators = [DataRequired()])
	email = StringField("email", validators = [DataRequired()])
	password = PasswordField("password", validators = [DataRequired()])
	remember_me = BooleanField("remember-me")


class SalasForm(FlaskForm):
	name = StringField("name", validators = [DataRequired()])
	code = StringField("code", validators = [DataRequired()])
	
class AgendamentosForm(FlaskForm):
	username = SelectField("username", choices=[], validators = [DataRequired()])
	roomname = SelectField("roomname", choices=[],validators = [DataRequired()])
	datescheduled = DateTimeLocalField("date",format='%Y-%m-%dT%H:%M')
	
class PetRegisteForm(FlaskForm):
	pet_name = SelectField("Petname", choices=[], validators=[DataRequired()])
	pet_code = SelectField("Petcode",choices=[], validators=[DataRequired()])
	pet_species = SelectField("Petspecie", choices=[], validators=[DataRequired()])
	pet_race = SelectField("Petrace", choices=[], validators=[DataRequired()])
	pet_birth = DateTimeLocalField("Petbirth",format='%Y-%m-%dT%H:%M)
'''
	temperature = db.Column(db.Float)
	heartbeat = db.Column(db.Integer)
	x_axis = db.Column(db.Integer)
	y_axis = db.Column(db.Integer)
	timestamp = db.Column(db.DateTime)
	collar_id = db.Column(db.Integer,db.ForeignKey('pet.id'))
'''
class ColarRegisteForm(FlaskForm):
	collar_code = SelectField("Collarcode", choices=[], validators=[DataRequired()])
	pet_id= SelectField("Petid",choices=[], validators=[DataRequired()])

class TelemetryRegisterForm(FlaskForm):
	telemetry_temperature = SelectField("Telemetrytemperature", choices=[], validators=[DataRequired()])
	telemetry_heartbeat = SelectField("Telemetryheartbeat", choices=[], validators=[DataRequired()])
	telemetry_x_axis = SelectField("Telmetryxaxis", choices=[], validators=[DataRequired()])
	telemetry_y_axis = SelectField("Telmetryyaxis", choices=[], validators=[DataRequired()])
	telemetry_timestamp = SelectField("Telmetrytimestamp", choices=[], validators=[DataRequired()])