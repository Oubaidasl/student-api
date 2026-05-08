# Workflow du Projet student-api

## 🔧 Outils utilisés
- **GitHub** : versioning et collaboration
- **ZenHub** : gestion de projet Agile (Kanban + Sprints)
- **Python** : algorithmes et tests unitaires
- **C** : algorithmes de tri et recherche

## 🌿 Stratégie de branches
- `main` : version stable et finale
- `develop` : intégration du travail de l'équipe
- `feature/*` : branches de développement individuelles

## 👥 Équipe et répartition
| Membre | Rôle | Branche |
|--------|------|---------|
| Membre 1 | Setup GitHub + DevOps + Webhook | main/develop |
| Membre 2 | Backend API Flask (Python) | feature/api-flask |
| Membre 3 | Algorithmes C/Python + ZenHub | feature/algorithms-zenhub |
| Membre 4 | Tests + Documentation + Rapport | feature/docs-tests |

## 🔄 Workflow Git
1. Chaque membre travaille sur sa branche `feature/*`
2. Une fois la tâche terminée, il soumet une **Pull Request** vers `develop`
3. Le Membre 1 review et merge la PR
4. A la fin du projet, `develop` est mergé dans `main`

## 📋 Organisation Agile

### Sprint 1 — Initialisation
- Création du repo GitHub
- Structure du projet
- Configuration ZenHub
- Développement algorithmes C/Python

### Sprint 2 — Développement
- API Flask
- Tests unitaires
- Documentation
- Webhook GitHub
- Merge Requests

## ✅ Commandes Git utilisées
```bash
git clone       # Cloner le repo
git checkout -b # Créer une nouvelle branche
git add         # Stager les fichiers
git commit -m   # Commiter avec message
git push        # Pousser vers GitHub
git merge       # Merger les branches
```

## 🔗 Liens utiles
- Repository GitHub : https://github.com/Oubaidasl/student-api
- Board ZenHub : (lien à ajouter)