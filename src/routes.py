"""
Routes module - imported by app.py for modular route management.
Can be used to register blueprints in a larger Flask application.
"""
from flask import Blueprint, jsonify, request

etudiant_bp = Blueprint('etudiants', __name__)

_etudiants = [
    {"id": 1, "nom": "Alami", "note": 15.5},
    {"id": 2, "nom": "Bennani", "note": 12.0},
    {"id": 3, "nom": "Chakir", "note": 18.0},
]

@etudiant_bp.route('/etudiants', methods=['GET'])
def get_all():
    return jsonify(_etudiants)

@etudiant_bp.route('/etudiants/<int:id>', methods=['GET'])
def get_one(id):
    e = next((e for e in _etudiants if e["id"] == id), None)
    return jsonify(e) if e else (jsonify({"erreur": "Non trouvé"}), 404)
