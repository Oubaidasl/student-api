from flask import Flask, jsonify, request

app = Flask(__name__)

etudiants = [
    {"id": 1, "nom": "Alami", "note": 15.5},
    {"id": 2, "nom": "Bennani", "note": 12.0},
    {"id": 3, "nom": "Chakir", "note": 18.0},
]

@app.route('/etudiants', methods=['GET'])
def get_etudiants():
    return jsonify(etudiants)

@app.route('/etudiants/<int:id>', methods=['GET'])
def get_etudiant(id):
    e = next((e for e in etudiants if e["id"] == id), None)
    return jsonify(e) if e else (jsonify({"erreur": "Non trouvé"}), 404)

@app.route('/etudiants', methods=['POST'])
def add_etudiant():
    data = request.json
    if not data or "id" not in data or "nom" not in data or "note" not in data:
        return jsonify({"erreur": "Données invalides"}), 400
    etudiants.append(data)
    return jsonify(data), 201

@app.route('/etudiants/<int:id>', methods=['DELETE'])
def delete_etudiant(id):
    global etudiants
    etudiant = next((e for e in etudiants if e["id"] == id), None)
    if not etudiant:
        return jsonify({"erreur": "Non trouvé"}), 404
    etudiants = [e for e in etudiants if e["id"] != id]
    return jsonify({"message": f"Etudiant {id} supprimé"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
