#include <stdio.h>
#include <string.h>

typedef struct {
    int id;
    char nom[50];
    float note;
} Etudiant;

void tri_bulles(Etudiant arr[], int n) {
    Etudiant temp;
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j].note < arr[j+1].note) {
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

int recherche_binaire(Etudiant arr[], int n, int target_id) {
    /* Assumes arr is sorted by id ascending */
    int low = 0, high = n - 1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (arr[mid].id == target_id) return mid;
        else if (arr[mid].id < target_id) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}

int main() {
    Etudiant etudiants[] = {
        {1, "Alami", 15.5},
        {2, "Bennani", 12.0},
        {3, "Chakir", 18.0}
    };
    int n = sizeof(etudiants) / sizeof(etudiants[0]);

    tri_bulles(etudiants, n);
    printf("=== Classement par note (desc) ===\n");
    for (int i = 0; i < n; i++) {
        printf("%d. %s -> %.1f\n", i+1, etudiants[i].nom, etudiants[i].note);
    }

    /* Recherche par id (tri par id avant recherche binaire) */
    Etudiant par_id[] = {
        {1, "Alami", 15.5},
        {2, "Bennani", 12.0},
        {3, "Chakir", 18.0}
    };
    int idx = recherche_binaire(par_id, n, 2);
    if (idx >= 0)
        printf("\nRecherche id=2 : %s (note: %.1f)\n", par_id[idx].nom, par_id[idx].note);
    else
        printf("\nEtudiant non trouve.\n");

    return 0;
}
