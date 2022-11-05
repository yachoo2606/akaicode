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
        login = sqla.Column(sqla.String)
        password = sqla.Column(sqla.String)
        name = sqla.Column(sqla.String)
        surname = sqla.Column(sqla.String)
        email = sqla.Column(sqla.String)
        phoneNumber = sqla.Column(sqla.String)
        organizationId = sqla.Column(sqla.Integer, sqla.ForeignKey('Organization.id'))
        validated = sqla.Column(sqla.Boolean, default=False)
        created_date = sqla.Column(sqla.Date)

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
        address = sqla.Column(sqla.String)
        street = sqla.Column(sqla.String)
        number = sqla.Column(sqla.String)
        postcode = sqla.Column(sqla.String)
        latitude = sqla.Column(sqla.String)
        longitude = sqla.Column(sqla.String)
        type = sqla.Column(sqla.String)
        KRS = sqla.Column(sqla.String, unique=True)
        NIP = sqla.Column(sqla.String, unique=True)
        REGON = sqla.Column(sqla.String, unique=True)
        website = sqla.Column(sqla.String)
        password = sqla.Column(sqla.String)
        email = sqla.Column(sqla.String, unique=True)
        phoneNumber = sqla.Column(sqla.String, unique=True)

        def toDict(self):
            return dict(id=self.id, name=self.name, description=self.description, country=self.country,
                        state=self.state, city=self.city, address=self.address, street=self.street, number=self.number,
                        postcode=self.postcode, latitude=self.latitude, longitude=self.longitude, type=self.type,
                        KRS=self.KRS, NIP=self.NIP, REGON=self.REGON, website=self.website, password=self.password,
                        email=self.email, phoneNumber=self.phoneNumber)

    class Requests(base):
        __tablename__ = 'Requests'

        id = sqla.Column(sqla.Integer, primary_key=True)
        name = sqla.Column(sqla.String)
        description = sqla.Column(sqla.String)
        addedDate = sqla.Column(sqla.Date)
        endDate = sqla.Column(sqla.Date)

        def toDict(self):
            return dict(id=self.id, name=self.name, description=self.description, addedDate=self.addedDate,
                        endDate=self.endDate)

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

        def toDict(self):
            return dict(id=self.id, name=self.name, description=self.description, country=self.country,
                        state=self.state, city=self.city, street=self.street, number=self.number,
                        postcode=self.postcode,
                        latitude=self.latitude, longitude=self.longitude, type=self.type, start_date=self.start_date,
                        end_date=self.end_date)
