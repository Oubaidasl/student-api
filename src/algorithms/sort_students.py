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
