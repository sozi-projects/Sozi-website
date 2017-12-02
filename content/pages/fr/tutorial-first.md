Title: Votre première présentation
Slug: tutorial-first
Lang: fr
Author: Guillaume Savaton
Translation: true
Status: hidden

Ce tutoriel est une introduction aux principes de base de Sozi.
Vous apprendrez à créer vos premières vues et à jouer la présentation dans un navigateur web.


Téléchargez et ouvrez le document de base
-----------------------------------------

Ce tutoriel se base sur un simple document SVG qui contient les éléments visuels nécessaires à notre présentation.
[Téléchargez le document SVG de base](https://github.com/senshu/Sozi/raw/master/samples/first-presentation.svg)
(Cliquez avec le bouton droit sur le lien et choisissez *Enregistrer la cible du lien sous*).
Ouvrez-le avec l'éditeur de présentation Sozi.

![Ouvrir le document SVG dans l'éditeur de présentation](|filename|/images/tutorial-first/first-presentation-screenshot-01.fr.png)


Créez la première vue de votre présentation
-------------------------------------------

Pressez le bouton *+* pour créer une nouvelle vue.

Nous allons centrer la première vue sur la forme violette avec le chiffre 1.
Vous pouvez modifier son titre en éditant le champ *Titre* dans le panneau de droite.
Ensuite, dans le panneau de prévisualisation&nbsp;:

* Positionnez la caméra en déplaçant la souris et en maintenant le bouton gauche pressé.
* Zoomez en déplaçant la souris et en maintenant pressés le bouton gauche et la touche *Alt* du clavier.

![La première vue de la présentation](|filename|/images/tutorial-first/first-presentation-screenshot-02.fr.png)


Créez trois autres vues
-----------------------

Ajoutez trois nouvelles vues.
Chacune est représentée par une colonne dans la chronologie (panneau du bas).
Vous pouvez cliquer sur le numéro ou le titre d'une vue pour la sélectionner.

Donnez un titre à chaque vue et modifiez la position de la caméra de manière à afficher
successivement les formes orange (2), jaune (3) et bleue (4).
Pour effectuer une rotation, déplacez la souris en maintenant pressés le bouton gauche et la touche *Maj* (*Shift*)
du clavier.

![La deuxième vue de la présentation](|filename|/images/tutorial-first/first-presentation-screenshot-03.fr.png)


Enregistrer la présentation
---------------------------

En principe, votre présentation s'enregistre automatiquement.
Si ce n'est pas le cas, vous pouvez presser le bouton *Enregistrer la présentation* de la barre d'outils.

Sozi ne modifie pas le document SVG original.
À chaque enregistrement, l'éditeur met à jour les deux fichiers suivants&nbsp;:

* `first-presentation.sozi.json` contient les données de la présentation. Ce fichier est utilisé
  par l'éditeur de présentation Sozi. Il doit toujours être dans le même dossier que le document SVG
  et doit porter le même nom.
* `first-presentation.sozi.html` contient votre présentation complète. Vous pouvez l'afficher dans
  un navigateur web pour jouer votre présentation.

Si vous souhaitez partager votre présentation avec d'autres personnes,
il suffit de leur donner le fichier qui porte l'extension `.sozi.html`.


Jouez la présentation dans un navigateur web
--------------------------------------------

Ouvrez le fichier `first-presentation.sozi.html` dans un navigateur web.
La caméra se place automatiquement sur la première vue.
Cliquez à l'intérieur de la présentation pour passer à la vue suivante.
(voir aussi&nbsp;: [Jouer une présentation](|filename|play.md)).

[Téléchargez la présentation complète](https://github.com/senshu/Sozi/raw/master/samples/first-presentation.sozi.html)
(Cliquez avec le bouton droit sur le lien et choisissez *Enregistrer la cible du lien sous*).
