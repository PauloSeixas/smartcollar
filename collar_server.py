import os
import os.path
import datetime
import json
import os
from flask import Flask, jsonify, request, url_for, session, flash,render_template
from models.tabelas import db,Pet,Collar,Telemetry



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

            telemetry = Telemetry(
                            temperature=int(json_data["temperature"]),
                            humidity=int(json_data["humidity"]),
                            heartbeat=int(json_data["heartbeat"]),
                            oxigen=int(json_data["oxigen"]),
                            latitude=int(json_data["latitude"]),
                            longitude=int(json_data["longitude"]),
                            x_axis=int(json_data["x_axis"]),
                            y_axis=int(json_data["y_axis"]),
                            z_axis=int(json_data["z_axis"]),
                            collar_code=str(json_data["collar_id"]),
            )
            db.session.add(telemetry)
            db.session.commit()
        return render_template('index.html')

    @app.route('/resultados')

    def exibirmedicoes(dados=None):
        query = db.session.query(Telemetry).order_by(Telemetry.id.desc()).all()

        return render_template('results.html', dados=query)


    @app.route('/teste', methods=['POST', 'GET'])
    def data():
        telemetry = Telemetry(
                        temperature=30,
                        humidity=45,
                        heartbeat=65,
                        oxigen=85,
                        latitude=0,
                        longitude=0,
                        x_axis=10,
                        y_axis=10,
                        z_axis=10,
                        collar_code="PA1234"
                        )


        db.session.add(telemetry)
        db.session.commit()
        return render_template('results.html')
    return app

if __name__ == "__main__":
    application = create_app()
    port = int(os.environ.get("PORT", 5000))
    application.run(host='0.0.0.0', port=port)
