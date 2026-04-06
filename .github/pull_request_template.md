## Ajout d'un guest / cuistot

### Informations

- **Nom** :
- **Rôle** : `guest` / `cuistot`
- **Titre** :
- **Bio** :

### Checklist

- [ ] Entrée ajoutée dans `guests.json` avec tous les champs obligatoires (`id`, `name`, `title`, `role`, `bio`, `avatar`, `tags`)
- [ ] L'`id` est unique et suit la séquence existante
- [ ] Le fichier `cuistops-guests.opml` a été regénéré (`node generate-opml.mjs cuistops-guests.opml`) si un flux RSS a été ajouté
- [ ] `guests.json` est valide (JSON bien formé)
