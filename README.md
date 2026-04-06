# CuistOps — Guests

Interface web listant les speakers et blogueurs de la communauté du live DevOps francophone CuistOps.

## Ajouter une personne

Toutes les données sont dans [`guests.json`](guests.json). Ajouter une entrée dans le tableau en respectant la structure ci-dessous.

### Structure d'une entrée

```json
{
  "id": 42,
  "roles": ["blog"],
  "name": "Prénom NOM",
  "title": "Poste chez Entreprise",
  "bio": "Courte description de la personne.",
  "avatar": "https://example.com/photo.jpg",
  "linkedin": "https://linkedin.com/in/handle",
  "bluesky": "https://bsky.app/profile/handle.bsky.social",
  "github": "https://github.com/handle",
  "blog": "https://monblog.dev",
  "rss": "https://monblog.dev/index.xml",
  "tags": ["Tag1", "Tag2", "Tag3"]
}
```

### Champs

| Champ | Type | Obligatoire | Description |
|-------|------|-------------|-------------|
| `id` | entier | oui | Identifiant unique |
| `roles` | tableau de `"speaker"` \| `"blog"` | oui | Catégories de la personne — peut contenir les deux |
| `name` | chaîne | oui | Nom complet |
| `title` | chaîne | oui | Poste et entreprise |
| `bio` | chaîne | oui | Courte biographie |
| `avatar` | URL | oui | URL de la photo de profil |
| `linkedin` | URL \| `null` | non | Profil LinkedIn |
| `bluesky` | URL \| `null` | non | Profil Bluesky |
| `github` | URL \| `null` | non | Profil GitHub |
| `blog` | URL \| `null` | non | Blog personnel — affiché en bouton mis en valeur sur la carte |
| `rss` | URL \| `null` | non | Flux RSS du blog |
| `tags` | tableau de chaînes | oui | Mots-clés (2-4 recommandés) |

> Les champs optionnels absents ou à `null` n'affichent pas le bouton correspondant.

## Déploiement

Un push sur `main` déclenche automatiquement le workflow GitHub Actions qui :

1. Valide le JSON (`guests.json`)
2. Publie le site sur GitHub Pages

Pour activer GitHub Pages : **Settings → Pages → Source → GitHub Actions**.
