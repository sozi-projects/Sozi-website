Title: Utiliser les calques
Slug: tutorial-layers
Lang: fr
Author: Guillaume Savaton, Hervé Julier
Translation: true
Status: hidden


Une présentation Sozi peut être organisée en un ou plusieurs calques qui bougent indépendamment l'un de l'autre.
On utilise souvent les calques pour ajouter un arrière-plan fixe à vos vues par exemple,
mais il y a beaucoup d'autres possibilités.
Avec un peu de travail et d'ingéniosité, vous pouvez faire des animations sophistiquées.
Mais rappelez-vous : puisque le but principal de Sozi est de créer des présentations,
il ne fournira pas les possibilités que vous attendez d'un éditeur d'animation à usage plus général.

Téléchargez et ouvrez le document de base
-----------------------------------------

Ce tutoriel se base sur un document SVG qui contient les éléments visuels de notre présentation.
[Téléchargez le document SVG de base] (https://github.com/senshu/Sozi/raw/master/samples/tutorial-layers.svg)
(Cliquez avec le bouton droit sur le lien et choisissez *Enregistrer la cible du lien sous*).

Ce document SVG a été créé avec [Inkscape] (https://inkscape.org).
Nous vous recommandons d'installer Inkscape avant de continuer.
Avant de commencer à créer la présentation, nous verrons l'organisation
des éléments graphiques.

Ouvrez `tutorial-layers.svg` dans Inkscape.

![Document de base dans Inkscape](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-01.fr.png)

Organisation des calques
------------------------

Inkscape permet d'organiser un document en calques.
Vous pouvez ouvrir le panneau des calques en cliquant sur le bouton *Afficher les calques* dans la barre d'outils,
ou en choisissant l'item *Calques&hellip;* dans le menu *Calques*.

![Montrer les calques](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-02.fr.png)

Dans cet exemple, le document contient trois calques :

* *Légendes*: le calque de premier plan avec des éléments de texte.
* *Paysage*: le calque intermédiaire contient un dessin d'un arbre.
* *Ciel*: le calque de fond contient un grand cercle bleu avec le soleil, la lune et les étoiles.

Chaque calque a un sous-calque nommé *Vues*. Ces sous-calques contiennent des rectangles
qui aideront à aligner le graphique lors de la création de la présentation Sozi.

> Vous pouvez afficher ou masquer un calque en cliquant sur l'icône correspondante "œil" dans la boîte de dialogue *Calques*.
> Essayez d'afficher puis masquer chaque calque et sous-calque pour identifier quels éléments appartiennent à quel calque.
>
> Assurez-vous que tous les calques sont visibles avant de passer à la section suivante.

Créez les vues de la présentation Sozi
--------------------------------------

Ouvrez `tutorial-layers.svg` dans l'éditeur de présentation Sozi.

![Document de base dans Sozi](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-03.fr.png)

Créez quatre vues à l'aide du bouton *+* dans le panneau du bas représentant une chronologie.
Pour chaque vue, remplissez le champ *Titre* avec les titres suivants :

1. "Matin",
2. "Midi",
3. "Soir",
4. "Nuit".

La chronologie devrait ressembler à ceci :

![Chronologie avec 4 vues](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-04.fr.png)

Ajoutez un calque fixe (Paysage)
--------------------------------

Appuyez sur le bouton *Ajouter un calque* et choisissez *Paysage*.
Dans la chronologie, sélectionnez la cellule correspondant à la première vue et à la
vue *Paysage* comme indiqué ci-dessous.

![Sélectionnez le calque Paysage pour la vue 1](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-05.fr.png)

Dans la zone d'aperçu, effectuez un zoom avant (molette de la souris) et déplacez le calque *Paysage*
jusqu'à ce que le rectangle contenant l'arbre remplisse presque la zone.
Assurez-vous que seuls les éléments du calque *Paysage* soient affectés.

![Zoom dans le calque Paysage](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-06.fr.png)

Dans le volet des propriétés à droite, le champ *Id de l'élément à utiliser comme contour* doit contenir
"rect-paysage".
C'est l'identifiant SVG du grand rectangle rouge qui entoure le dessin de
l'arbre.
Puisque le bouton *Sélectionner l'élément automatiquement* est activé, Sozi propose automatiquement d'utiliser ce
rectangle comme contour pour la vue actuelle.

* Appuyez sur le bouton *Ajuster à l'élément* sur la droite : maintenant le calque *Paysage* a été
  ajusté de sorte que le rectangle remplisse la zone d'aperçu.
* Appuyez sur le bouton *Cacher l'élément* pour masquer le rectangle.

![Sélection de l'élément de contour](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-07.fr.png)

Si la présentation est lue dans un navigateur web qui a des dimensions avec un
ratio différent, nous voulons cacher les éléments graphiques qui sont en dehors de la zone actuellement visible.
En haut à droite du volet des propriétés, appuyez sur le bouton *Rogner*.

Nous avons mis en place un calque qui ne bougera pas pendant la présentation.
Maintenant, créons un calque animé.

![Calque de paysage ajusté](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-08.fr.png)

Ajoutez un calque animé (légendes)
----------------------------------

Appuyez sur le bouton *Ajouter un calque* et choisissez *Légendes*.
Dans la chronologie, sélectionnez la cellule correspondant à la première vue et au calque
*Légendes* comme indiqué ci-dessous.

![Sélection du calque Légendes pour la vue 1](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-09.fr.png)

Dans la zone d'aperçu, effectuez un zoom avant (molette de la souris) et déplacez le calque *Légendes*
jusqu'à ce que le rectangle contenant le texte "Matin" remplisse presque la zone.
Assurez-vous que seuls les éléments du calque *Légendes* soient affectés.

![Zoomez dans le calque Légendes](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-10.fr.png)

Le champ *Id de l'élément à utiliser comme contour* doit contenir "rect-text-matin".
Appuyez sur les boutons *Ajuster à l'élément*, *Cacher l'élément* et *Rogner*.

Appliquez le même procédé aux vues "Midi", "Soir" et "Nuit".
La zone d'aperçu pour chaque vue doit ressembler à ceci:

![Vue ajustée 1 dans le calque Légendes](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-11.fr.png)
![Vue ajustée 2 dans le calque Légendes](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-12.fr.png)
![Vue ajustée 3 dans le calque Légendes](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-13.fr.png)
![Vue ajustée 4 dans le calque Légendes](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-14.fr.png)

Ajoutez un calque animé (Ciel)
------------------------------

À ce stade, tous les éléments graphiques qui n'appartiennent pas aux calques *Paysage* ou *Légendes*
sont représentés par la ligne *Par défaut* de la chronologie.
Généralement, *Par défaut* n'est pas vraiment un calque : il regroupe tous les calques qui n'ont pas été ajoutés à la chronologie
et tous les éléments qui n'appartiennent pas à un calque (vous devriez éviter cela autant que possible, mais cela peut arriver).
Si vous ajoutez un nouveau calque au document SVG dans Inkscape, il tombera automatiquement dans
la catégorie *Par défaut* dans Sozi.

Appuyez sur le bouton *Ajouter un calque* et choisissez *Ciel*.
La ligne *Par défaut* devrait disparaître.

Pour plus de facilité, nous allons cacher les calques *Paysage* et *Légendes*.
Cliquez sur les icônes "œil" à gauche dans les lignes qui correspondent à ces calques.

![Sélection du calque Ciel pour la vue 1](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-15.fr.png)

> L'icône "œil" permet de masquer un calque dans l'éditeur pendant que vous voulez travailler sur d'autres calques.
> Les calques cachés sont toujours visibles lors de la lecture de la présentation.
>
> Si vous souhaitez masquer un calque lors de la lecture de la présentation, définissez son *Opacité du calque*
> à zéro.

Procédez comme vous l'avez fait pour le calque *Légendes*.
Pour chaque vue :

1. Dans la ligne *Ciel* du scénario, sélectionnez la cellule correspondant à la vue que vous souhaitez modifier.
2. Dans la zone d'aperçu, effectuez un zoom (molette de la souris), déplacez et faites pivoter (Maj + molette de la souris) le calque jusqu'à ce que le rectangle souhaité remplisse presque la zone.
3. Cochez la case *Id de l'élément à utiliser comme contour*, puis appuyez sur les boutons *Ajuster à l'élément*, *Cacher l'élément* et *Rogner*.

Affichez les calques *Paysage* et *Légendes* à nouveau.
La zone d'aperçu devrait ressembler à ceci:

![Vue ajustée 1 dans le calque Ciel](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-16.fr.png)
![Vue ajustée 2 dans le calque Ciel](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-17.fr.png)
![Vue ajustée 3 dans le calque Ciel](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-18.fr.png)
![Vue ajustée 4 dans le calque Ciel](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-19.fr.png)

Enregistrez et lisez la présentation
------------------------------------

L'éditeur devrait enregistrer votre présentation automatiquement.
Si ce n'est pas le cas, vous pouvez toujours appuyer sur le bouton *Enregistrer la présentation* dans la barre d'outils.

Ouvrez le fichier `tutorial-layers.sozi.html` dans un navigateur Web.
La caméra est automatiquement définie sur la première vue de la présentation.
Cliquez dans la fenêtre du navigateur web pour passer à la vue suivante.
(voir aussi: [Play] (| filename | play.md)).

[Télécharger la présentation complète] (https://github.com/senshu/Sozi/raw/master/samples/tutorial-layers.sozi.html)
(Cliquez avec le bouton droit sur le lien et choisissez * Enregistrer la cible du lien sous *).



Click inside the browser window to move to the next frame.
(see also: [Jouer une présentation](|filename|play.md)).

[Téléchargez la présentation complète](https://github.com/senshu/Sozi/raw/master/samples/tutorial-layers.sozi.html)
(Cliquez avec le bouton droit sur le lien et choisissez *Enregistrer la cible du lien sous*).
