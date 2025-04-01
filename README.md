# How to

## Table des matières

- [Les fichiers -](#les-fichiers-)
  - [1. `cipher.html`](#1-cipherhtml)
  - [2. `obscure.html`](#2-obscurehtml)
- [La structure des fichiers HTML](#la-structure-des-fichiers-html)
- [Tenir son projet à jour](#tenir-son-projet-à-jour)
- [Mettre à jour le projet](#mettre-à-jour-le-projet)

## Les fichiers -

### 1. `cipher.html`

Contient l'énoncé de la partie 1 du puzzle.

### 2. `obscure.html`

Contient l'énoncé de la partie 2 du puzzle.

## La structure des fichiers HTML

- Chaque contenu est balisé par une balise `<article>`
- Chaque article contient un titre `<h2>`
- Chaque article contient plusieurs paragraphes `<p>`
- Chaque article peut contenir des exemples dans des balises `<pre>` ou `<code>` (pre sauvegardé pour le formatage), (code pour la mise en forme/avant)

## Tenir son projet à jour

Cliquer sur le bouton des flèches circulaires en bas à gauche de l'interface pour synchroniser le projet avec le dépôt distant et récupérer ainsi les dernières modifications du dépôt distant.

## Mettre à jour le projet

Après des changements dans le projet, il faut stager les fichiers, créer un message de commit et pousser/synchroniser les changements sur le dépôt distant.

## Rappels HTML

HTML est un langage de balisage. Chaque balise ouvrante doit être fermée par une balise fermante. Par exemple, `<p>` est la balise ouvrante et `</p>` est la balise fermante. Il existe aussi des balises auto-fermantes comme `<br />`. Ces balises n'ont pas besoin de balise fermante.

> Si en faisant un CTRL+S, et que l'extension de formattage (Prettier) ne formate pas le code, c'est qu'une balise n'est pas fermée correctement. Il faut donc vérifier le code HTML.

Test
