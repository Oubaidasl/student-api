"""
Sorting algorithms for student management.
Implements bubble sort and binary search on student data.
"""

def bubble_sort(etudiants: list, reverse: bool = True) -> list:
    """
    Sort students by note using bubble sort.
    reverse=True → descending (highest note first)
    """
    arr = etudiants.copy()
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            condition = arr[j]["note"] < arr[j+1]["note"] if reverse else arr[j]["note"] > arr[j+1]["note"]
            if condition:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def binary_search(etudiants: list, target_id: int) -> dict | None:
    """
    Binary search for a student by id.
    Assumes the list is sorted by id in ascending order.
    Returns the student dict or None if not found.
    """
    sorted_list = sorted(etudiants, key=lambda e: e["id"])
    low, high = 0, len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid]["id"] == target_id:
            return sorted_list[mid]
        elif sorted_list[mid]["id"] < target_id:
            low = mid + 1
        else:
            high = mid - 1
    return None


if __name__ == "__main__":
    sample = [
        {"id": 1, "nom": "Alami", "note": 15.5},
        {"id": 2, "nom": "Bennani", "note": 12.0},
        {"id": 3, "nom": "Chakir", "note": 18.0},
    ]
    sorted_students = bubble_sort(sample)
    print("=== Classement par note (desc) ===")
    for i, s in enumerate(sorted_students, 1):
        print(f"{i}. {s['nom']} -> {s['note']}")

    result = binary_search(sample, 2)
    print(f"\nRecherche id=2 : {result}")
# Algorithmes de gestion des étudiants

etudiants = [
    {"id": 1, "nom": "Alami",    "note": 15.5},
    {"id": 2, "nom": "Bennani",  "note": 12.0},
    {"id": 3, "nom": "Chakir",   "note": 18.0},
    {"id": 4, "nom": "Dahbi",    "note": 9.5},
    {"id": 5, "nom": "El Fassi", "note": 16.0},
]

# ── Tri à bulles ──────────────────────────────────────────
def tri_bulles(liste):
    n = len(liste)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if liste[j]["note"] < liste[j+1]["note"]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste

# ── Recherche binaire par note ────────────────────────────
def recherche_binaire(liste, note_cherchee):
    gauche, droite = 0, len(liste) - 1
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        if liste[milieu]["note"] == note_cherchee:
            return liste[milieu]
        elif liste[milieu]["note"] < note_cherchee:
            droite = milieu - 1
        else:
            gauche = milieu + 1
    return None

# ── Calcul de la moyenne ──────────────────────────────────
def calculer_moyenne(liste):
    if not liste:
        return 0
    return sum(e["note"] for e in liste) / len(liste)

# ── Meilleur étudiant ─────────────────────────────────────
def meilleur_etudiant(liste):
    return max(liste, key=lambda e: e["note"])

# ── Main ──────────────────────────────────────────────────
if __name__ == "__main__":
    print("=== Avant le tri ===")
    for e in etudiants:
        print(f"  {e['id']}. {e['nom']} -> {e['note']}")

    tries = tri_bulles(etudiants.copy())
    print("\n=== Classement après tri (meilleure note en premier) ===")
    for i, e in enumerate(tries, 1):
        print(f"  {i}. {e['nom']} -> {e['note']}")

    print(f"\n=== Moyenne de la classe : {calculer_moyenne(etudiants):.2f} ===")

    meilleur = meilleur_etudiant(etudiants)
    print(f"=== Meilleur étudiant : {meilleur['nom']} avec {meilleur['note']} ===")

    print("\n=== Recherche de l'étudiant avec note 16.0 ===")
    resultat = recherche_binaire(tries, 16.0)
    if resultat:
        print(f"  Trouvé : {resultat['nom']}")
    else:
        print("  Aucun étudiant trouvé")
