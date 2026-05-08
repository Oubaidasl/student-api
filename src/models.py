class Etudiant:
    def __init__(self, id: int, nom: str, note: float):
        self.id = id
        self.nom = nom
        self.note = note

    def to_dict(self):
        return {"id": self.id, "nom": self.nom, "note": self.note}

    def __repr__(self):
        return f"Etudiant(id={self.id}, nom={self.nom}, note={self.note})"
