import sys
import os

# Pour importer depuis src/algorithms
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from algorithms.sort_students import (
    tri_bulles,
    recherche_binaire,
    calculer_moyenne,
    meilleur_etudiant
)

# ── Données de test ───────────────────────────────────────
etudiants_test = [
    {"id": 1, "nom": "Alami",    "note": 15.5},
    {"id": 2, "nom": "Bennani",  "note": 12.0},
    {"id": 3, "nom": "Chakir",   "note": 18.0},
    {"id": 4, "nom": "Dahbi",    "note": 9.5},
    {"id": 5, "nom": "El Fassi", "note": 16.0},
]

# ── Test tri_bulles ───────────────────────────────────────
def test_tri_bulles():
    resultat = tri_bulles(etudiants_test.copy())
    assert resultat[0]["note"] == 18.0, "❌ Erreur : meilleure note pas en premier"
    assert resultat[-1]["note"] == 9.5, "❌ Erreur : moins bonne note pas en dernier"
    print("✅ test_tri_bulles : OK")

# ── Test recherche_binaire ────────────────────────────────
def test_recherche_binaire():
    tries = tri_bulles(etudiants_test.copy())
    resultat = recherche_binaire(tries, 16.0)
    assert resultat is not None,             "❌ Erreur : étudiant non trouvé"
    assert resultat["nom"] == "El Fassi",    "❌ Erreur : mauvais étudiant retourné"
    print("✅ test_recherche_binaire : OK")

def test_recherche_binaire_inexistant():
    tries = tri_bulles(etudiants_test.copy())
    resultat = recherche_binaire(tries, 99.0)
    assert resultat is None, "❌ Erreur : devrait retourner None"
    print("✅ test_recherche_binaire_inexistant : OK")

# ── Test calculer_moyenne ─────────────────────────────────
def test_calculer_moyenne():
    moyenne = calculer_moyenne(etudiants_test)
    assert round(moyenne, 2) == 14.2, "❌ Erreur : moyenne incorrecte"
    print("✅ test_calculer_moyenne : OK")

def test_calculer_moyenne_vide():
    moyenne = calculer_moyenne([])
    assert moyenne == 0, "❌ Erreur : moyenne liste vide devrait être 0"
    print("✅ test_calculer_moyenne_vide : OK")

# ── Test meilleur_etudiant ────────────────────────────────
def test_meilleur_etudiant():
    meilleur = meilleur_etudiant(etudiants_test)
    assert meilleur["nom"] == "Chakir", "❌ Erreur : mauvais meilleur étudiant"
    print("✅ test_meilleur_etudiant : OK")

# ── Lancer tous les tests ─────────────────────────────────
if __name__ == "__main__":
    print("=== Lancement des tests ===\n")
    test_tri_bulles()
    test_recherche_binaire()
    test_recherche_binaire_inexistant()
    test_calculer_moyenne()
    test_calculer_moyenne_vide()
    test_meilleur_etudiant()
    print("\n=== Tous les tests sont passés ✅ ===")