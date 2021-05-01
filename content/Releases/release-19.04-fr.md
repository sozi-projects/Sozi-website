Title: Sozi 19.04 est disponible
Date: 2019-04-24
Slug: release-19.04
Lang: fr
Authors: Guillaume Savaton
Summary:
    Après un an, Sozi 19.04 est sorti. Il propose un nouveau mode *présentateur* et des améliorations de performances.

La première [demande pour un mode présentateur](https://github.com/sozi-projects/Sozi/issues/211)
dans Sozi a été formulée en 2014.
Au moins deux implémentation on été proposées, l'une par Kai Wegner, sous la forme
d'une application séparée appelée [catchi](https://github.com/kai-wegner/catchi),
l'autre par roggan87, [comme une modification du logiciel de visionnage existant](https://github.com/sozi-projects/Sozi/pull/325).

Sozi 19.04 est un compromis entre les deux approches.
Il réutilise du code écrit par roggan87, mais la console du présentateur reste
en-dehors de la visionneuse Sozi.
Voyons comment cela fonctionne&nbsp;:

Quand Sozi enregistre votre présentation, il crée un fichier HTML (par exemple `exemple.sozi.html`)
qui contient une copie de votre document SVG et le code JavaScript de visionnage.
Avec Sozi 19.04, l'éditeur crée un fichier HTML supplémentaire (`exemple-presenter.sozi.html`)
qui contient la console du présentateur.
Pour jouer votre présentation, vous avez maintenant deux options&nbsp;:

* Ouvrir `exemple.sozi.html` dans un navigateur web et jouer la présentation sans la console du présentateur, comme avec Sozi 18.
* Ouvrir `exemple-presenter.sozi.html` dans un navigateur web. Une console *présentateur* est affichée, contenant un aperçu des vues précédente, courante et suivante, des boutons de navigations et des notes.
  Simultanément, la présentation s'ouvre automatiquement dans une autre fenêtre.

> Les navigateurs web bloquent généralement les fenêtre *pop-up*.
> Quand vous ouvrez le fichier HTML de la console présentateur pour la première fois,
> vous devez confirmer que vous accepter l'ouverture de la présentation dans une autre fenêtre.
> Vous devrez probablement aussi rafraîchir la page après avoir confirmé.

Autres changements depuis Sozi 18.04
-----------------------------------

* Les titres des vues peuvent être organisés de façon hiérarchique dans la liste des vues.
* Dans l'éditeur, vous pouvoir choisir d'enregistrer la présentation, ou de recharger le document SVG, manuellement.
  Cela peut être utile si votre document est volumineux et si vous souhaiter éviter que Sozi perde
  en réactivité lorsque des opérations d'enregistrement ou de rechargement sont déclenchées
  à des moments inattendus.
* Vous pouvez demander à cacher les éléments de contrôle des vidéos et documents audio
  incorporés à vos présentations.
* Un bug rendait l'éditeur de plus en plus lent à chaque fois que le document SVG
  était rechargé. Nous espérons qu'il s'agissait de la cause principale des problèmes
  de performances constatés par plusieurs utilisateurs.
* Un bug dans le logiciel de visionnage affichait une barre de défilement à gauche de
  la présentation lorsque la liste des vues ne tenait pas dans la hauteur de la fenêtre
  du navigateur.

[Installez Sozi 19.04 dès maintenant&nbsp;!](|filename|/pages/fr/install.md).

À propos de Sozi-export
-----------------

Sozi-export est un ensemble d'outils en ligne de commande qui convertissent des
présentations Sozi en vidéos ou en documents imprimables.
Ces outils reposent sur PhantomJS, un moteur de navigateur web qui n'est plus
maintenu.
Pour cette raison, Sozi-export est devenu inutilisable sur plusieurs plates-formes.
À notre connaissance, il n'existe pas de moyen simple de corriger ce problème
à court terme.

En attendant qu'il soit résolu, [l'image Docker](https://hub.docker.com/r/escalope/inkscape-sozi)
préparée par Jorge J. Gomez-Sanz fournit un environnement stable où Sozi-export
fonctionne.
