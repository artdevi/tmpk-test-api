from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import psycopg2
conn = psycopg2.connect(dbname='database', user='db_user', password='mypassword', host='localhost')
cursor = conn.cursor()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/testdb'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

#
# class Contract(db.Model):
#     __tablename__ = 'contracts'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(150), nullable=False)
#     balance = db.Column(db.Integer, nullable=False, default=0)
#     is_legal_entity = db.Column(db.Boolean, nullable=False)
#     is_active = db.Column(db.Boolean, nullable=False, default=True)
#
#     def __init__(self, name, is_legal_entity, is_active=True):
#         self.name = name
#         self.is_legal_entity = is_legal_entity
#         self.is_active = is_active
#
#
# class Address(db.Model):
#     __tablename__ = 'addresses'
#     id = db.Column(db.Integer, primary_key=True)
#     contract_id = db.Column(db.Integer, db.ForeignKey('contracts.id'), nullable=False)
#     city = db.Column(db.String(100), nullable=False)
#     street = db.Column(db.String(100), nullable=False)
#     house = db.Column(db.String(16), nullable=False)
#     apartment = db.Column(db.Integer, nullable=False)
#
#
# class Tariff(db.Model):
#     __tablename__ = 'tariffs'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), nullable=False)
#     price = db.Column(db.Integer, nullable=False)
#     start_date = db.Column(db.Date, nullable=False)
#     end_date = db.Column(db.Date)
#
#
# class Transaction(db.Model):
#     __tablename__ = 'transactions'
#     id = db.Column(db.Integer, primary_key=True)
#     contract_id = db.Column(db.Integer, db.ForeignKey('contracts.id'), nullable=False)
#     sum = db.Column(db.Integer, nullable=False)
#     datetime = db.Column(db.DateTime, nullable=False)
#
#
# db.create_all()
# # contract = Contract('Test Name', True, True)
# # db.session.add(contract)
# # db.session.commit()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/contract/<id>', methods=['GET'])
def get_contract_info(id):
    # contact = Contract.query.get(id)
    return jsonify()


@app.route('/balance/<id>', methods=['GET'])
def get_balance(id):
    # contact = Contract.query.get(id)
    return jsonify()


if __name__ == '__main__':
    app.run(debug=True)