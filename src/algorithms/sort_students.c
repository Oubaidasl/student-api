#include <stdio.h>
#include <string.h>

// Structure Etudiant
typedef struct {
    int id;
    char nom[50];
    float note;
} Etudiant;

// Algorithme de tri par note (tri à bulles)
void tri_bulles(Etudiant arr[], int n) {
    int i, j;
    Etudiant temp;
    for (i = 0; i < n-1; i++) {
        for (j = 0; j < n-i-1; j++) {
            if (arr[j].note < arr[j+1].note) {
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

// Recherche binaire par note
int recherche_binaire(Etudiant arr[], int n, float note) {
    int gauche = 0, droite = n - 1;
    while (gauche <= droite) {
        int milieu = (gauche + droite) / 2;
        if (arr[milieu].note == note)
            return milieu;
        else if (arr[milieu].note < note)
            droite = milieu - 1;
        else
            gauche = milieu + 1;
    }
    return -1;
}

int main() {
    Etudiant etudiants[] = {
        {1, "Alami",   15.5},
        {2, "Bennani", 12.0},
        {3, "Chakir",  18.0},
        {4, "Dahbi",   9.5},
        {5, "El Fassi",16.0}
    };

    int n = 5;

    printf("=== Avant le tri ===\n");
    for (int i = 0; i < n; i++)
        printf("%d. %s -> %.1f\n", i+1, etudiants[i].nom, etudiants[i].note);

    tri_bulles(etudiants, n);

    printf("\n=== Classement apres tri (meilleure note en premier) ===\n");
    for (int i = 0; i < n; i++)
        printf("%d. %s -> %.1f\n", i+1, etudiants[i].nom, etudiants[i].note);

    // Recherche d'un etudiant par note
    float note_cherchee = 16.0;
    int index = recherche_binaire(etudiants, n, note_cherchee);
    if (index != -1)
        printf("\nEtudiant avec note %.1f : %s\n", note_cherchee, etudiants[index].nom);
    else
        printf("\nAucun etudiant avec note %.1f\n", note_cherchee);

    return 0;
}