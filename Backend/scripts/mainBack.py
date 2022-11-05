import sqlalchemy as sqla
import sqlalchemy.orm as sqlaOrm
from flask import Flask, request, jsonify, send_file
import logging
from logging.handlers import RotatingFileHandler
from Backend.model.DBModels import base, engine, DBModel
from dotenv import dotenv_values

environments = dotenv_values("../.env")
app = Flask(__name__)

"""========================================START OF LOGGER SECTION========================================"""

Log_Format = '%(asctime)s - %(threadName)s - %(name)s - %(levelname)s - %(message)s'

logging.basicConfig(format=Log_Format,
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.ERROR)

fileHandled = RotatingFileHandler(environments.get("LOGS.PATH"),
                                  mode="a",
                                  maxBytes=1024 * 500,
                                  backupCount=1)
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logging.Formatter(Log_Format))
fileHandled.setFormatter(logging.Formatter(Log_Format))
rootLogger = logging.getLogger()
rootLogger.addHandler(fileHandled)

"""========================================END OF LOGGER SECTION========================================"""

Session = sqlaOrm.sessionmaker(engine)
session = Session()


@app.route('/getAllOrganizations')
def getAllUsers():
    users = session.query(DBModel.Organization).all()
    app.logger.info('Read all Organizations')
    return jsonify([u.toDict() for u in users])


@app.route('/register', methods=['POST'])
def register():
    if len(session.query(DBModel.Organization).filter(
            DBModel.Organization.name == request.args.get('name')).all()) != 0:
        app.logger.warning('Tried to register already registered Organization')

        errorUser = DBModel.Organization()
        errorUser.name = "Organization already exist"
        errorUser.phoneNumber = "ERROR"
        errorUser.password = "ERROR"

        return jsonify(errorUser.toDict())
    else:
        toAddOrganization = DBModel.Organization()
        toAddOrganization.name = request.args.get("name")
        toAddOrganization.city = request.args.get("city")
        toAddOrganization.address = request.args.get("address")
        toAddOrganization.street = request.args.get("street")
        toAddOrganization.number = request.args.get("number")
        toAddOrganization.postcode = request.args.get("postcode")
        toAddOrganization.KRS = request.args.get("KRS")
        toAddOrganization.NIP = request.args.get("NIP")
        toAddOrganization.email = request.args.get("email")
        toAddOrganization.password = request.args.get("password")
        toAddOrganization.phoneNumber = request.args.get("phoneNumber")

        app.logger.info(f'New user: {toAddOrganization.email} registered')

        session.add(toAddOrganization)
        session.commit()
    return jsonify(toAddOrganization.toDict())


@app.route("/editOrganization", methods={'POST'})
def editOrganization():
    toEditOrganization = DBModel.Organization()
    toEditOrganization.name = request.args.get("name")
    toEditOrganization.city = request.args.get("city")
    toEditOrganization.address = request.args.get("address")
    toEditOrganization.street = request.args.get("street")
    toEditOrganization.number = request.args.get("number")
    toEditOrganization.postcode = request.args.get("postcode")
    toEditOrganization.KRS = request.args.get("KRS")
    toEditOrganization.NIP = request.args.get("NIP")
    toEditOrganization.email = request.args.get("email")
    toEditOrganization.password = request.args.get("password")
    toEditOrganization.phoneNumber = request.args.get("phoneNumber")

    session.query(DBModel.Organization).filter(
        DBModel.Organization.name == request.args.get('email'),
    ).update(toEditOrganization)

    return toEditOrganization.toDict()


@app.route('/login', methods={'POST'})
def login():
    if logingUser := session.query(DBModel.Organization).filter(
            DBModel.Organization.email == request.args.get('email'),
            DBModel.Organization.password == request.args.get('password')).first():
        app.logger.info('User: ' + logingUser.email + " logged")
        return jsonify(logingUser.toDict())
    app.logger.info('User: ' + request.args.get('email') + " logged failed")

    errorUser = DBModel.Organization()
    errorUser.email = "ERROR"
    errorUser.name = "No User found"
    errorUser.phoneNumber = "ERROR"
    errorUser.password = "ERROR"
    errorUser.role = 0

    return jsonify(errorUser.toDict())


@app.route("/addRequest", methods={'POST'})
def addRequest():
    toAddRequest = DBModel.Requests()
    toAddRequest.name = request.args.get("name")
    toAddRequest.description = request.args.get("description")
    toAddRequest.addedDate = request.args.get("addedDate")
    toAddRequest.endDate = request.args.get("endDate")

    session.add(toAddRequest)
    session.commit()
    app.logger.info(f"added Reservation: {toAddRequest.name}")
    return toAddRequest.toDict()


@app.route("/editRequest", methods={'POST'})
def editRequest():
    toEditRequest = DBModel.Requests()
    toEditRequest.name = request.args.get("name")
    toEditRequest.description = request.args.get("description")
    toEditRequest.addedDate = request.args.get("addedDate")
    toEditRequest.endDate = request.args.get("endDate")

    session.query(DBModel.Requests).filter(
        DBModel.Requests.name == request.args.get('name'),
        DBModel.Requests.description == request.args.get('password')
    ).update(toEditRequest)

    return toEditRequest.toDict()


@app.route("/addEvent", methods={'POST'})
def addEvent():
    toAddEvent = DBModel.Events()

    toAddEvent.name = request.args.get("name")
    toAddEvent.description = request.args.get("description")
    toAddEvent.country = request.args.get("country")
    toAddEvent.state = request.args.get("state")
    toAddEvent.city = request.args.get("city")
    toAddEvent.street = request.args.get("street")
    toAddEvent.number = request.args.get("number")
    toAddEvent.postcode = request.args.get("postcode")
    toAddEvent.latitude = request.args.get("latitude")
    toAddEvent.longitude = request.args.get("longitude")
    toAddEvent.type = request.args.get("type")
    toAddEvent.start_date = request.args.get("start_date")
    toAddEvent.end_date = request.args.get("end_date")

    session.add(toAddEvent)
    session.commit()
    app.logger.info(f"added Event: {toAddEvent.name}")
    return toAddEvent.toDict()


@app.route("/editEvent", methods={'POST'})
def editEvent():
    toEditEvent = DBModel.Events()

    toEditEvent.name = request.args.get("name")
    toEditEvent.description = request.args.get("description")
    toEditEvent.country = request.args.get("country")
    toEditEvent.state = request.args.get("state")
    toEditEvent.city = request.args.get("city")
    toEditEvent.street = request.args.get("street")
    toEditEvent.number = request.args.get("number")
    toEditEvent.postcode = request.args.get("postcode")
    toEditEvent.latitude = request.args.get("latitude")
    toEditEvent.longitude = request.args.get("longitude")
    toEditEvent.type = request.args.get("type")
    toEditEvent.start_date = request.args.get("start_date")
    toEditEvent.end_date = request.args.get("end_date")

    session.query(DBModel.Events).filter(
        DBModel.Requests.name == request.args.get('name'),
    ).update(toEditEvent)

    return toEditEvent.toDict()


@app.route("/test", methods={'POST'})
def test():
    return request.args


if __name__ == '__main__':
    base.metadata.create_all(engine)

    app.run(host='0.0.0.0', port=5000)

    session.close()
