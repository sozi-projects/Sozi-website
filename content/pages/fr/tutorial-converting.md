Title: Convertir une présentation Sozi en PDF ou en vidéo
Slug: tutorial-converting
Lang: fr
Authors: Guillaume Savaton
Status: hidden

> Sozi-export est désormais considéré comme obsolète.
> Depuis Sozi 21.02, l'outil de conversion est intégré à l'éditeur de présentations.
>
> La documentation de cette nouvelle fonctionnalité sera disponible bientôt.

Sozi-export est un ensemble d'outils en ligne de commande permettant de convertir une
présentation Sozi en un document PDF, une vidéo ou une présentation PowerPoint.
Le code source de ces outils est disponible dans le dépôt [Sozi-export](https://github.com/sozi-projects/Sozi-export).
Ces outils sont développés indépendamment de l'éditeur de présentation.
Ils ont été testés seulement sous GNU/Linux.


Installation
------------

Sozi-export dépend des logiciels suivants, qui vous devez installer séparément&nbsp;:

* [pdfjam](http://www2.warwick.ac.uk/fac/sci/statistics/staff/academic-research/firth/software/pdfjam), un script shell pour manipuler des documents PDF.
* [libav](https://libav.org), un ensemble d'outils et une bibliothèque pour manupuler des fichiers multimédia.

Les utilisateurs de distributions basées sur Debian peuvent installer les paquets
*texlive-extra-utils* et *libav-tools*.

    :::bash
    apt-get install texlive-extra-utils libav-tools

Sozi-export est disponible sous la forme d'un paquet NPM.
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
* `-c`, `--png-compression <number>` Niveau de compression des fichiers PNG générés (0 à 100, une plus grande valeur implique de plus petits fichiers, 100 par défaut)
* `-i`, `--include <list>` Les vues à inclure ('all' par défaut)
* `-x`, `--exclude <list>` Les vues à exclure ('none' par défaut)

Les options de largeur, hauteur et résolution déterminent la géométrie de la fenêtre du
navigateur où la présentation sera rendue.
Les valeurs par défaut sont adaptées à la génération d'un document pour impression
sur du papier au format A4.
Le format et l'orientation du papier définissent le format de page du document PDF final.

L'option `include` est toujours appliquée avant l'option `exclude`.
Les listes de vues doivent respecter la syntaxe suivante&nbsp;:

* `all` sélectionne toutes les vues de la présentation.
* `none` ne sélectionne aucune vue.
* Une liste de numéros de vues ou d'intervalles séparés par des virgules.
  Un intervalle est de la forme `premier:dernier` ou `premier:deuxième:dernier`.
  Ici, `premier`, `deuxième` et `dernier` sont des numéros de vues.

Par exemple&nbsp;: `-i 2,4:6,10:12:18` inclura les vues 2, 4, 5, 6, 10, 12, 14, 16, 18.

Convertir une présentation Sozi en vidéo
----------------------------------------

    :::bash
    sozi-to-video [options] presentation.sozi.html

Options:

* `-h`, `--help` Afficher de l'aide
* `-o`, `--output <file>` Le nom du fichier de sortie
* `-W`, `--width <number>` La largeur de la vidéo, en pixels (1024 par défaut)
* `-H`, `--height <number>` La hauteur de la vidéo, en pixels (768 par défaut)
* `-b`, `--bit-rate <number>` Le débit binaire de la vidéo (2M par défaut)
* `-c`, `--png-compression <number>` Niveau de compression des fichiers PNG générés (0 à 100, une plus grande valeur implique de plus petits fichiers, 100 par défaut)

Convertir une presentation Sozi en présentation PowerPoint
----------------------------------------------------------

Cet outil crée un document PowerPoint au format PPTX.
Il accepte un sous-ensemble des options de `sozi-to-pdf`.

    :::bash
    sozi-to-pptx [options] presentation.sozi.html

Options:

* `-h`, `--help` Afficher de l'aide
* `-o`, `--output <file>` Le nom du fichier de sortie
* `-W`, `--width <number>` La largeur de la page (29.7 par défaut)
* `-H`, `--height <number>` La hauteur de la page (21 par défaut)
* `-r`, `--resolution <number>` Pixels par unité de hauteur/largeur (72 par défaut)
* `-c`, `--png-compression <number>` Niveau de compression des fichiers PNG générés (0 à 100, une plus grande valeur implique de plus petits fichiers, 100 par défaut)
* `-i`, `--include <list>` Les vues à inclure ('all' par défaut)
* `-x`, `--exclude <list>` Les vues à exclure ('none' par défaut)

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
