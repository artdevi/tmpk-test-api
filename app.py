from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(dbname='testdb', user='postgres', password='password', host='localhost')
cursor = conn.cursor()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/contract/<id>', methods=['GET'])
def get_contract_info(id):
    cursor.execute(f'SELECT * FROM contracts LEFT JOIN addresses ON contracts.id = addresses.contract_id WHERE contracts.id = {id}')

    data = cursor.fetchone()

    if data is not None:
        return jsonify(data)
    else:
        return 'No such contracts, please check the correctness of the entered data', 400


@app.route('/balance/<id>', methods=['GET'])
def get_balance(id):
    # contact = Contract.query.get(id)
    return jsonify()


if __name__ == '__main__':
    app.run(debug=True)