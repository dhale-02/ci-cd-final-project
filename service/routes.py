"""Counter Routes"""
from flask import Flask, jsonify, abort

app = Flask(__name__)
counters = {}


@app.route("/", methods=["GET"])
def index():
    """Root URL"""
    return jsonify(name="Counter Service", version="1.0"), 200


@app.route("/counters/<name>", methods=["POST"])
def create_counter(name):
    """Create a counter"""
    if name in counters:
        abort(409, f"Counter {name} already exists")
    counters[name] = 0
    return jsonify({name: counters[name]}), 201


@app.route("/counters/<name>", methods=["GET"])
def read_counter(name):
    """Read a counter"""
    if name not in counters:
        abort(404, f"Counter {name} does not exist")
    return jsonify({name: counters[name]}), 200


@app.route("/counters/<name>", methods=["PUT"])
def update_counter(name):
    """Update (increment) a counter"""
    if name not in counters:
        abort(404, f"Counter {name} does not exist")
    counters[name] += 1
    return jsonify({name: counters[name]}), 200


@app.route("/counters/<name>", methods=["DELETE"])
def delete_counter(name):
    """Delete a counter"""
    if name not in counters:
        abort(404, f"Counter {name} does not exist")
    del counters[name]
    return "", 204
