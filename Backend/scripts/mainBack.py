import sqlalchemy as sqla
import sqlalchemy.orm as sqlaOrm
from flask import Flask,request,jsonify, send_file
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


if __name__ == '__main__':
    base.metadata.create_all(engine)

    app.run(host='0.0.0.0', port=5000)

    session.close()