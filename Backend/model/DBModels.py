import sqlalchemy as sqla
import sqlalchemy.orm as sqlaOrm
from dotenv import dotenv_values

environments = dotenv_values("../.env")

engine = sqla.create_engine(environments.get("DATABASE.PATH"), echo=True, connect_args={'check_same_thread': False})

base = sqlaOrm.declarative_base()


class DBModel:
    class User(base):
        __tablename__ = 'Users'

        id = sqla.Column(sqla.Integer, primary_key=True)
        login = sqla.Column(sqla.String, unique=True)
        password = sqla.Column(sqla.String)
        name = sqla.Column(sqla.String)
        surname = sqla.Column(sqla.String)
        email = sqla.Column(sqla.String, unique=True)
        phoneNumber = sqla.Column(sqla.String, unique=True, nullable=True)
        organizationId = sqla.Column(sqla.Integer, sqla.ForeignKey('Organization.id'), nullable=True)
        validated = sqla.Column(sqla.Boolean, default=False)
        created_date = sqla.Column(sqla.Date)

        def __repr__(self):
            return f"<User(id={self.id}, name={self.name}, login={self.login}, phoneNumber={self.phoneNumber}, role={self.role}, created_date={self.created_date})> "

        def toDict(self):
            return dict(id=self.id, name=self.name, login=self.login, phoneNumber=self.phoneNumber,
                        password=self.password, organizationId=self.organizationId)

    class Organization(base):
        __tablename__ = 'Organization'

        id = sqla.Column(sqla.Integer, primary_key=True)
        name = sqla.Column(sqla.String, nullable=False)
        description = sqla.Column(sqla.String)
        country = sqla.Column(sqla.String)
        state = sqla.Column(sqla.String)
        city = sqla.Column(sqla.String)
<<<<<<< HEAD
        address = sqla.Column(sqla.String)
=======
        street = sqla.Column(sqla.String)
        number = sqla.Column(sqla.String)
>>>>>>> origin/main
        postcode = sqla.Column(sqla.String)
        latitude = sqla.Column(sqla.String)
        longitude = sqla.Column(sqla.String)
        type = sqla.Column(sqla.String)
        KRS = sqla.Column(sqla.String)
        NIP = sqla.Column(sqla.String)
        REGON = sqla.Column(sqla.String)
        website = sqla.Column(sqla.String)

    class Requests(base):
        __tablename__ = 'Requests'

        id = sqla.Column(sqla.Integer, primary_key=True)
        name = sqla.Column(sqla.String)
        description = sqla.Column(sqla.String)
        addedDate = sqla.Column(sqla.Date)
        endDate = sqla.Column(sqla.Date)

    class Events(base):
        __tablename__ = 'Events'

        id = sqla.Column(sqla.Integer, primary_key=True)
        name = sqla.Column(sqla.String, nullable=False)
        description = sqla.Column(sqla.String)
        country = sqla.Column(sqla.String)
        state = sqla.Column(sqla.String)
        city = sqla.Column(sqla.String)
        street = sqla.Column(sqla.String)
        number = sqla.Column(sqla.String)
        postcode = sqla.Column(sqla.String)
        latitude = sqla.Column(sqla.String)
        longitude = sqla.Column(sqla.String)
        type = sqla.Column(sqla.String)
        start_date = sqla.Column(sqla.DateTime)
        end_date = sqla.Column(sqla.DateTime)

