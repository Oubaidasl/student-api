# API Documentation

## GET /etudiants

Retourne la liste des étudiants.

### Exemple de réponse

[
  {
    "id": 1,
    "nom": "Alami",
    "note": 15.5
  }
]

---

## GET /etudiants/<id>

Retourne un étudiant selon son ID.

### Exemple

GET /etudiants/1

---

## POST /etudiants

Ajoute un nouvel étudiant.

### JSON attendu

{
  "id": 4,
  "nom": "Karim",
  "note": 14
}

### Réponse

201 Created
