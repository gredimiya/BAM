# Politique de Sécurité

## Signaler une Vulnérabilité

Si vous découvrez une vulnérabilité de sécurité, **ne la publiez pas publiquement**. À la place :

1. **N'ouvrez pas une issue GitHub publique**
2. **Envoyez un email privé** à l'administrateur du projet avec :
   - Description de la vulnérabilité
   - Étapes pour reproduire le problème
   - Impact potentiel
   - Suggestion de correction (optionnel)

## Versions Supportées

| Version | Statut | Supportée jusqu'à |
|---------|--------|------------------|
| 1.0.0   | Stable | 2026-12-31       |

## Bonnes Pratiques de Sécurité

Quand vous utilisez BAM :

- ✅ Gardez Python et les dépendances à jour
- ✅ Utilisez HTTPS pour accéder à l'application en production
- ✅ Sécurisez votre base de données SQLite
- ✅ Limitez l'accès à l'application
- ✅ Sauvegarder régulièrement vos données

Ne faites pas :
- ❌ Partagez pas votre base de données publiquement
- ❌ Utilisez pas des credentials par défaut
- ❌ Exposez pas l'application directement à Internet sans authentification
- ❌ Stockez pas de données sensibles non chiffrées

## Dépendances

Les dépendances Python utilisées sont listées dans `requirements.txt`. Mettez-les à jour régulièrement :

```bash
pip install --upgrade -r requirements.txt
```

## Divulgation des Risques Connus

Aucune vulnérabilité connue actuellement.

## Processus de Réponse

1. Nous accusons réception dans les 48 heures
2. Nous enquêtons et développons un correctif
3. Nous publions une version corrigée
4. Nous accréditons le chercheur (si souhaité)
