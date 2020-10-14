import os
import os.path
import datetime
import json
import glob
import os
from flask import Flask, jsonify, request, url_for, session, flash,render_template
import plotly
import plotly.graph_objs as go

import pandas as pd
import json
import numpy as np
from flask_sqlalchemy import SQLAlchemy
#from tables import db, Pet,Collar

from models.tabelas import db,Pet,Collar,Telemetry
#import Models


def create_app():
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir,'collarapp.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()


    @app.route('/home', methods=['POST', 'GET'])
    @app.route('/', methods=['POST', 'GET'])
    def index_page():
        error = None
        if request.method == 'POST':
            json_data = request.get_json()
            pet_tracked = Pet(name=str(json_data["name"]),
                              code=str(json_data["code"]),
                              birth=str(json_data["birth"]),
                              race=str(json_data["race"])
                                  )

            collar = Collar(heart_frequency=int(json_data["heart_frequency"]),
                            temperature=str(json_data["temperature"]),
                            x_axis=str(json_data["x_axis"]),
                            y_axis=int(json_data["y_axis"]),
                            pet=pet_tracked

            )
            db.session.add(pet_tracked)
            db.session.add(collar)
            db.session.commit()
        return render_template('index.html')

    @app.route('/resultados')

    def exibirmedicoes(dados=None):
        query = db.session.query(Pet).order_by(Pet.id).all()
        for item in query:
            print(item.name)
        return render_template('results.html', dados=query)


    @app.route('/teste', methods=['POST', 'GET'])
    def data():

        pet_teste = Pet(
                        name=str("Leoa"),
                        code=str("1234"),
                        birth=datetime.datetime.now(),
                        specie=str("dog"),
                        race=str("bulldog")
                        )
        '''
        collar = Collar(
                        code=str("01234"),
                        pet_id=0,
                        )
        '''
        telemetry_1 = Telemetry(
                        code=str("12345"),
                        temperature=float("35"),
                        heartbeat=int("85"),
                        x_axis=int("10"),
                        y_axis=int("10"),
                        collar_id=0
                        )
        telemetry_2 = Telemetry(
            code=str("12345"),
            temperature=float("35"),
            heartbeat=int("85"),
            x_axis=int("10"),
            y_axis=int("10"),
            collar_id=0
        )


        db.session.add(pet_teste)
        #db.session.add(collar)
        db.session.add(telemetry_1)
        db.session.add(telemetry_2)
        db.session.commit()
        return render_template('results.html')
    return app

if __name__ == "__main__":
    application = create_app()
    port = int(os.environ.get("PORT", 5000))
    application.run(host='0.0.0.0', port=port)
