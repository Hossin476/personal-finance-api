from flask import Flask, jsonify, request
from pymongo import MongoClient
from marshmallow import Schema, fields, ValidationError

# Initializing Flask app
app = Flask(__name__)

# database connection
client = MongoClient('mongodb://127.0.0.1:27017')
db = client['finance']

# Defining the schema for transactions and budgets
class TransactionSchema(Schema):
    category = fields.String(required=True)
    amount = fields.Float(required=True)

class BudgetSchema(Schema):
    category = fields.String(required=True)
    amount = fields.Float(required=True)

# Instantiating the schema objects
transaction_schema = TransactionSchema()
budget_schema = BudgetSchema()

# implementation of the routes for transactions and budgets
@app.route('/transactions', methods=['POST'])
def add_transaction():
    try:
        transaction = transaction_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    db.transactions.insert_one(transaction)
    return jsonify({'message': 'Transaction added successfully.'}), 201


@app.route('/transactions', methods=['GET'])
def get_transactions():
    transactions = list(db.transactions.find({}, {'_id': 0}))
    return jsonify(transactions)


@app.route('/budgets', methods=['POST'])
def add_budget():
    try:
        budget = budget_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    db.budgets.insert_one(budget)
    return jsonify({'message': 'Budget added successfully.'}), 201


@app.route('/budgets', methods=['GET'])
def get_budgets():
    budgets = list(db.budgets.find({}, {'_id': 0}))
    return jsonify(budgets)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)