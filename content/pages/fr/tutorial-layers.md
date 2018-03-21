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

* *Sous-titres*: le calque de premier plan avec des éléments de texte.
* *Paysage*: le calque intermédiaire contient un dessin d'un arbre.
* *Ciel*: le calque de fond contient un grand cercle bleu avec le soleil, la lune et les étoiles.

Chaque calque a un sous-calque nommé *Vues*. Ces sous-calques contiennent des rectangles
qui aideront à aligner le graphique lors de la création de la présentation Sozi.

> Vous pouvez afficher ou masquer un calque en cliquant sur l'icône "œil" correspondante dans la boîte de dialogue *Calques*.
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
Assurez-vous que seuls les éléments de la couche *Landcape* soient affectés.

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

![Outline element selection](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-07.png)

If the presentation is played in a web browser window that has a different aspect
ratio, we want to hide the graphics outside the currently visible area.
At the top right of the properties pane, press the *Clip* button.

We have set up a layer that will not move during the presentation.
Now let us create an animated layer.

![Fitted Landscape layer](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-08.png)

Add an animated layer (Captions)
--------------------------------

Press the *Add layer* button and choose *Captions*.
In the timeline, select the cell that corresponds to the first frame and the
*Captions* layer as shown below.

![Select layer Captions for frame 1](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-09.png)

In the preview area, zoom in (mouse wheel) and move the *Captions* layer
until the rectangle containing the text "Morning" almost fills the area.
Make sure that only the elements from the *Captions* layer are affected.

![Zoom in the Captions layer](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-10.png)

The field *Outline element Id* should read "rect-text-morning".
Press the *Fit to element*, *Hide element* and *Clip* buttons.

Apply the same process to the frames "Noon", "Evening" and "Night".
The preview area for each frame should look like this:

![Adjusted frame 1 in Captions layer](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-11.png)
![Adjusted frame 2 in Captions layer](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-12.png)
![Adjusted frame 3 in Captions layer](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-13.png)
![Adjusted frame 4 in Captions layer](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-14.png)

Add an animated layer (Sky)
--------------------------------

At this stage, all the graphics that do not belong to the *Landscape* or *Captions* layers
are represented by the *Default* row of the timeline.
Generally, *Default* is not really a layer: it groups all layers that have not been added to the timeline
and all the elements that do not belong to a layer (you should take care to avoid this, but it can happen).
If you add a new layer to the SVG document in Inkscape, it will fall automatically into
the *Default* category in Sozi.

Press the *Add layer* button and choose *Sky*.
The *Default* row should disappear.

For convenience, we will hide layers *Landscape* and *Captions*.
Click on the "eye" icons on the left in the rows corresponding to these layers.

![Select layer Captions for frame 1](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-15.png)

> The "eye" icon allows to hide a layer in the editor while you want to work on other layers.
> The hidden layers are still visible when playing the presentation.
>
> If you want to hide a layer when playing the presentation, set its *Layer opacity*
> to zero.

Proceed like you did for the *Captions* layer.
For each frame:

1. In the *Sky* row of the timeline, select the cell that corresponds to the frame you want to edit.
2. In the preview area, zoom (mouse wheel), move, and rotate (Shift + mouse wheel) the layer until the desired rectangle almost fills the area.
3. Check the field *Outline element Id*, then press the *Fit to element*, *Hide element* and *Clip* buttons.

Show the *Landscape* and *Captions* layers again.
The preview area should look like this:

![Adjusted frame 1 in Sky layer](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-16.png)
![Adjusted frame 2 in Sky layer](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-17.png)
![Adjusted frame 3 in Sky layer](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-18.png)
![Adjusted frame 4 in Sky layer](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-19.png)

Save and play the presentation
------------------------------

The editor should save your presentation automatically.
If it does not, you can still press the *Save* button in the tool bar.

Open the file `tutorial-layers.sozi.html` in a web browser.
The camera is automatically set to the first frame of the presentation.
Click inside the browser window to move to the next frame.
(see also: [Play](|filename|play.md)).

[Download the full presentation](https://github.com/senshu/Sozi/raw/master/samples/tutorial-layers.sozi.html)
(Right-click on the link and choose *Save link target as*).
