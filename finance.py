from flask import Flask, jsonify, request
from pymongo import MongoClient
from marshmallow import Schema, fields, ValidationError
from bson.objectid import ObjectId

# Initializing Flask app
app = Flask(__name__)

# database connection
client = MongoClient('mongodb://127.0.0.1:27017/')
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
    
    result = db.transactions.insert_one(transaction)
    return jsonify({'message': 'Transaction added successfully.', 'id': str(result.inserted_id)}), 201


@app.route('/transactions', methods=['GET'])
def get_transactions():
    transactions = list(db.transactions.find({}, {'_id': 0}))
    return jsonify(transactions)


@app.route('/transactions/<transaction_id>', methods=['GET'])
def get_transaction_by_id(transaction_id):
    transaction = db.transactions.find_one({'_id': ObjectId(transaction_id)}, {'_id': 0})
    if transaction:
        return jsonify(transaction), 200
    else:
        return jsonify({'message': 'Transaction not found.'}), 404


@app.route('/transactions/<category>', methods=['PUT'])
def update_transaction(category):
    try:
        query = {'category': category}
        new_transaction = transaction_schema.load(request.json)
        result = db.transactions.update_one(query, {"$set": new_transaction})
        if result.modified_count == 1:
            return jsonify({'message': 'Transaction updated successfully.'}), 200
        else:
            return jsonify({'message': 'Transaction not found.'}), 404
    except ValidationError as err:
        return jsonify(err.messages), 400


@app.route('/transactions/<category>', methods=['DELETE'])
def delete_transaction(category):
    result = db.transactions.delete_one({'category': category})
    if result.deleted_count == 1:
        return jsonify({'message': 'Transaction deleted successfully.'}), 200
    else:
        return jsonify({'message': 'Transaction not found.'}), 404


@app.route('/budgets', methods=['POST'])
def add_budget():
    try:
        budget = budget_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    result = db.budgets.insert_one(budget)
    return jsonify({'message': 'Budget added successfully.', 'id': str(result.inserted_id)}), 201


@app.route('/budgets', methods=['GET'])
def get_budgets():
    budgets = list(db.budgets.find({}, {'_id': 0}))
    return jsonify(budgets)


@app.route('/budgets/<budget_id>', methods=['GET'])
def get_budget_by_id(budget_id):
    budget = db.budgets.find_one({'_id': ObjectId(budget_id)}, {'_id': 0})
    if budget:
        return jsonify(budget), 200
    else:
        return jsonify({'message': 'Budget not found.'}), 404


@app.route('/budgets/<category>', methods=['PUT'])
def update_budget(category):
    try:
        query = {'category': category}
        new_budget = budget_schema.load(request.json)
        result = db.budgets.update_one(query, {"$set": new_budget})
        if result.modified_count == 1:
            return jsonify({'message': 'Budget updated successfully.'}), 200
        else:
            return jsonify({'message': 'Budget not found.'}), 404
    except ValidationError as err:
        return jsonify(err.messages), 400


@app.route('/budgets/<category>', methods=['DELETE'])
def delete_budget(category):
    result = db.budgets.delete_one({'category': category})
    if result.deleted_count == 1:
        return jsonify({'message': 'Budget deleted successfully.'}), 200
    else:
        return jsonify({'message': 'Budget not found.'}), 404

# Run the app
if __name__ == '__main__':
    app.run(debug=True)