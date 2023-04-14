Flask API for Personal Finance

This is a simple Flask API for managing personal finance data. The API allows users to create, and read financial transactions.

Getting Started
To use this API, follow the steps below:

Clone the repository.

Install the required dependencies ( 'pip install flask', 'pip install pymongo', 'pip install marshmallow')

Run 'python finance.py' to start the server.

The API will be available at http://localhost:5000.

Endpoints
The API has the following endpoints:

GET /transactions
This endpoint returns a list of all transactions in a json format.

GET /budgets
This endpoint returns a list of all budgets in ajson format.

POST /transactions

POST http://localhost:5000/transactions HTTP/1.1
content-type: application/json

{
    "category":"rent", 
    "amount":500
}

POST /budgets

POST http://localhost:5000/budgets HTTP/1.1
content-type: application/json

{
    "category":"rent", 
    "amount":500
}
