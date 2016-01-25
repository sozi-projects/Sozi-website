Title: Convertir une présentation Sozi en PDF ou en vidéo
Slug: tutorial-converting
Lang: fr
Author: Guillaume Savaton
Status: hidden

`sozi-to-pdf` et `sozi-to-video` sont des outils en ligne de commande permettant d'exporter une présentation
vers un document PDF ou une vidéo.
Le code source de ces outils est disponible dans le dépôt [Sozi-export](https://github.com/senshu/Sozi-export).
Ces outils sont développés indépendamment de l'éditeur de présentation.
Ils ont été testés seulement sous GNU/Linux.


Installation
------------

L'outil d'exportation en PDF dépend de [pdfjam](http://www2.warwick.ac.uk/fac/sci/statistics/staff/academic-research/firth/software/pdfjam), un script shell pour manipuler des documents PDF.
L'outil d'exportation en vidéo repose sur [libav](https://libav.org).
Les utilisateurs de distributions basées sur Debian peuvent installer les paquets
*texlive-extra-utils* et *libav-tools* packages.

    :::bash
    apt-get install texlive-extra-utils libav-tools

Les deux outils sont fournis dans un même paquet NPM.
Installez [node.js](https://nodejs.org/) 0.10 ou une version ultérieure
(les utilisateurs de Linux peuvent utiliser les [distributions NodeSource](https://github.com/nodesource/distributions)),
puis&nbsp;:

    :::bash
    npm install -g sozi-export


Convertir une présentation Sozi presentation en PDF
---------------------------------------------------

    :::bash
    sozi-to-pdf [options] presentation.sozi.html

Options:

* `-h`, `--help` Afficher de l'aide
* `-o`, `--output <file>` Le nom du fichier de sortie
* `-W`, `--width <number>` La largeur de la page (29.7 par défaut)
* `-H`, `--height <number>` La hauteur de la page (21 par défaut)
* `-r`, `--resolution <number>` Pixels par unité de hauteur/largeur (72 par défaut)
* `-p`, `--paper <size>` Un format de papier LaTeX ('a4paper' par défaut)
* `-P`, `--portrait` Définir l'orientation du papier en portrait (désactivé par défaut)
* `-i`, `--include <list>` Les vues à inclure ('all' par défaut)
* `-x`, `--exclude <list>` Les vues à exclure ('none' par défaut)

Les options de largeur, hauteur et résolution déterminent la géométrie de la fenêtre du
navigateur où la présentation sera rendue.
Le format et l'orientation du papier définissent le format de page du document PDF final.

L'option `include` est toujours appliquée avant l'option `exclude`.
Les listes de vues doivent respecter la syntaxe suivante&nbsp;:

* `all` sélectionne toutes les vues de la présentation.
* `none` ne sélectionne aucune vue.
* Une liste de numéros de vues ou d'intervalles séparés par des virgules.
  Un intervalle est de la forme `premier:dernier` ou `premier:deuxième:dernier`.
  Ici, `premier`, `deuxième` et `dernier` sont des numéros de vues.

Par exemple&nbsp;: `-i 2,4:6,10:12:18` inclura les vues 2, 4, 5, 6, 10, 12, 14, 16, 18.

Convert a Sozi presentation to video
------------------------------------

    :::bash
    sozi-to-video [options] presentation.sozi.html

Options:

* `-h`, `--help` Afficher de l'aide
* `-o`, `--output <file>` Le nom du fichier de sortie
* `-W`, `--width <number>` La largeur de la vidéo, en pixels (1024 par défaut)
* `-H`, `--height <number>` La hauteur de la vidéo, en pixels (768 par défaut)
* `-b`, `--bit-rate <number>` Le débit binaire de la vidéo (2M par défaut)

Problèmes connus et limitations
-------------------------------

Ces outils utilisent un navigateur web *headless* pour le rendu.
[PhantomJS](http://phantomjs.org) et [SlimerJS](https://slimerjs.org/) ont chacun des avantages
et des inconvénients&nbsp;:

* PhantomJS peut exporter une page web vers un document PDF, ce qui préserve les graphismes vectoriels et le texte.
  Cependant, PhantomJS 1.9.19 ne parvient pas à rendre le contenu SVG d'une présentation Sozi.
* SlimerJS rends le contenu SVG correctement mais ne prend pas en charge le format PDF.

Pour le moment, l'outil d'export en PDF effectue le rendu de chaque vue vers une image PNG
puis les rassemble dans un document PDF.