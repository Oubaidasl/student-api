"""
Search utilities for student data.
"""

def linear_search(etudiants: list, nom: str) -> list:
    """Search students by partial name match (case-insensitive)."""
    return [e for e in etudiants if nom.lower() in e["nom"].lower()]


def filter_by_note(etudiants: list, min_note: float = 0, max_note: float = 20) -> list:
    """Filter students within a note range."""
    return [e for e in etudiants if min_note <= e["note"] <= max_note]


if __name__ == "__main__":
    sample = [
        {"id": 1, "nom": "Alami", "note": 15.5},
        {"id": 2, "nom": "Bennani", "note": 12.0},
        {"id": 3, "nom": "Chakir", "note": 18.0},
    ]
    print(linear_search(sample, "al"))
    print(filter_by_note(sample, 13, 20))
