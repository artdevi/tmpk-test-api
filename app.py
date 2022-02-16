import json

from flask import Flask, jsonify, render_template
import models
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(dbname='testdb', user='postgres', password='password', host='localhost')
cursor = conn.cursor()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/contract/<id>', methods=['GET'])
def get_contract_info(id):
    cursor.execute(f"""SELECT contracts.id, contracts.name, tariffs.name, contracts.is_active, addresses.city, addresses.street, 
        addresses.house, addresses.apartment
        FROM contracts 
        LEFT JOIN addresses ON contracts.id = addresses.contract_id 
        LEFT JOIN tariffs ON contracts.id = tariffs.contract_id
        WHERE contracts.id = {id} AND tariffs.end_date is NULL;""")

    data = cursor.fetchone()
    result = models.ContractInfo(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])

    if data is not None:
        return json.dumps(result.__dict__)
    else:
        return 'No such contracts, please check the correctness of the entered data', 400


@app.route('/balance/<id>&<date>', methods=['GET'])
def get_balance(id, date):
    cursor.execute(f'SELECT * FROM contracts WHERE id = {id};')
    userdata = cursor.fetchone()
    if userdata is None:
        return 'Contract ID not found', 400

    cursor.execute(f"""SELECT
    (SELECT COALESCE(SUM(sum), 0) FROM transactions WHERE contract_id = {id} AND datetime <= '{date}')
    - ((SELECT COALESCE(SUM(date_part('month', age(end_date, start_date)) * price), 0) FROM tariffs
            WHERE contract_id = {id} AND end_date is not NULL AND end_date <= '{date}')
        + (SELECT COALESCE(SUM(date_part('month', age('{date}', start_date)) * price), 0) FROM tariffs
            WHERE (contract_id = {id} AND  end_date IS NULL AND start_date < '{date}') 
            OR (end_date > '{date}' AND contract_id = {id} AND start_date <= '{date}')));""")

    balance = cursor.fetchone()
    print(balance)
    return jsonify(balance)


if __name__ == '__main__':
    app.run(debug=True)