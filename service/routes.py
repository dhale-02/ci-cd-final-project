"""Account Service Routes"""
from flask import jsonify, abort, request
from service import app

accounts = {}
next_id = [1]


@app.route("/", methods=["GET"])
def index():
    """Root URL response"""
    return jsonify(name="Account REST API Service", version="1.0"), 200


@app.route("/accounts", methods=["POST"])
def create_account():
    """Create an Account"""
    data = request.get_json()
    if not data:
        abort(400, "No data provided")
    account_id = next_id[0]
    next_id[0] += 1
    accounts[account_id] = data
    accounts[account_id]["id"] = account_id
    return jsonify(accounts[account_id]), 201


@app.route("/accounts", methods=["GET"])
def list_accounts():
    """List all Accounts"""
    return jsonify(list(accounts.values())), 200


@app.route("/accounts/<int:account_id>", methods=["GET"])
def read_account(account_id):
    """Read an Account"""
    if account_id not in accounts:
        abort(404, f"Account with id '{account_id}' was not found.")
    return jsonify(accounts[account_id]), 200


@app.route("/accounts/<int:account_id>", methods=["PUT"])
def update_account(account_id):
    """Update an Account"""
    if account_id not in accounts:
        abort(404, f"Account with id '{account_id}' was not found.")
    data = request.get_json()
    if not data:
        abort(400, "No data provided")
    accounts[account_id].update(data)
    accounts[account_id]["id"] = account_id
    return jsonify(accounts[account_id]), 200


@app.route("/accounts/<int:account_id>", methods=["DELETE"])
def delete_account(account_id):
    """Delete an Account"""
    if account_id not in accounts:
        abort(404, f"Account with id '{account_id}' was not found.")
    del accounts[account_id]
    return "", 204
