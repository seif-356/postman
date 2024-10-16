from flask import Flask, request, jsonify

TOKEN = "secrettoken1"

def authenticate_token():
    token = request.headers.get("Authorization")
    if not token or token != f"Bearer {TOKEN}":
        return jsonify({"error": "unauthorization"}),401