# Finance Tracker API
This is a Flask API implementation of a simple finance tracker application. The API allows users to manage their transactions and budgets.

# Features
The API supports the following features:

Add a new transaction
View all transactions
View a specific transaction by ID
Update a transaction by category
Delete a transaction by category
Add a new budget
View all budgets
View a specific budget by ID
Update a budget by category
Delete a budget by category
Dependencies
Python 3.6+
Flask 2.0.1
PyMongo 3.12.0
Marshmallow 3.14.0
# Setup
To set up the API, follow these steps:

Clone this repository to your local machine.
Install the dependencies listed above using pip or another package manager.
Start the MongoDB server on your local machine.
Create a new database called "finance".
Open a terminal in the project directory and run the command python app.py to start the Flask server.
Usage
Once the server is running, you can use a tool like Postman or the Request HTTP extension for Visual Studio Code to send requests to the API endpoints.

Here are some examples of how to use the API:

Add a new transaction
Send a POST request to http://localhost:5000/transactions with the following JSON data:

json
{
    "category": "Groceries",
    "amount": 50.0
}
View all transactions
Send a GET request to http://localhost:5000/transactions.

View a specific transaction by ID
Send a GET request to http://localhost:5000/transactions/<transaction_id> where <transaction_id> is the ID of the transaction you want to retrieve.

Update a transaction by category
Send a PUT request to http://localhost:5000/transactions/<category> where <category> is the category of the transaction you want to update. Include the new transaction data in the request body in JSON format.

Delete a transaction by category
Send a DELETE request to http://localhost:5000/transactions/<category> where <category> is the category of the transaction you want to delete.

Add a new budget
Send a POST request to http://localhost:5000/budgets with the following JSON data:

json
{
    "category": "Groceries",
    "amount": 200.0
}
View all budgets
Send a GET request to http://localhost:5000/budgets.

View a specific budget by ID
Send a GET request to http://localhost:5000/budgets/<budget_id> where <budget_id> is the ID of the budget you want to retrieve.

Update a budget by category
Send a PUT request to http://localhost:5000/budgets/<category> where <category> is the category of the budget you want to update. Include the new budget data in the request body in JSON format.

Delete a budget by category
Send a DELETE request to http://localhost:5000/budgets/<category> where <category> is the category of the budget you want to delete.

License
This project is licensed under the MIT License. See the LICENSE file for details.

