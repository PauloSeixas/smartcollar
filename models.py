import os
import os.path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from sqlalchemy.ext.declarative import declarative_base
from tables import Base,Pet,Collar

class Models:
    def __init__(self):
        print("Initialize test")
        basedir = os.path.abspath(os.path.dirname(__file__))
        engine = create_engine('sqlite:///' + os.path.join(basedir, 'collarapp.db'), echo=False)
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)


    def pet_create (self,code,name,birth,race):
        print("create")
        session = self.Session()
        result = 0
        try:
            query = session.query(Pet).filter(Pet.code == code).count()
            if query == 0:
                pet = Pet(code=code, name=name, birth=birth,race=race)
                session.add(pet)
                session.commit()
        except ValueError:
            print(ValueError)
        session.close()
        return

    def pet_read (self,code):
        print("read")
        session = self.Session()
        result = 0
        try:
            pet = session.query(Pet).filter(Pet.code == code).all()
            session.close()
            return result, pet
        except ValueError:
            print(ValueError)
        session.close()
        return

    def pet_update (self,code,new_name,new_birth,new_race):
        print("update")
        session = self.Session()
        result = 0
        try:
            pet = session.query(Pet).filter(Pet.code == code).one()
            print(pet)
            pet.name = new_name
            pet.birth = new_birth
            pet.race = new_race
            session.commit()
        except ValueError:
            print(ValueError)
        session.close()
        return


    def pet_delete(self,code):
        session = self.Session()
        result = 0
        try:
            pet = session.query(Pet).filter_by(Pet.code==code).all()
            if pet > 0:
                collars = session.query(Collar).filter_by(pet.code == code ).all()

        except ValueError:
            print(ValueError)

        session.close()
        return result

if __name__=='__main__':
    models = Models()
    models.pet_create(code=123,name='Leoa',birth=datetime.datetime.now(),race='Mongreal')
    print(models.pet_read(123))
    print(models.pet_read(321))
    models.pet_update(code=123,new_name='Madame Lê',new_birth=datetime.datetime.now(),new_race='Pitbull')
    pet = models.pet_read(123)
    print(pet)
    #print(str(pet.name)+" "+str(pet.birth)+" "+str())
