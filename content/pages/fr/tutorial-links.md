Title: URL d'une vue et hyperliens
Slug: tutorial-links
Lang: fr
Author: Guillaume Savaton
Translation: true
Status: hidden

Dans ce tutoriel, vous apprendrez à ajouter des liens dans les présentations Sozi
et à créer des liens vers les vues d'une présentation.

Téléchargez et ouvrez le document de base
-----------------------------------------

Ce tutoriel se base sur un simple document SVG qui contient les éléments visuels nécessaires à notre présentation.
[Téléchargez le document SVG de base](|filename|/presentations/tutorial-links/tutorial-links.svg)
(Cliquez avec le bouton droit sur le lien et choisissez *Enregistrer la cible du lien sous*).

Ce document SVG a été créé avec [Inkscape](https://inkscape.org).
Nous vous recommandons d'installer Inkscape avant de continuer.

Créez les vues de la présentation
---------------------------------

Ouvrez `tutorial-links.svg` dans l'éditeur de présentation Sozi.

![Document de base dans Sozi](|filename|/images/tutorial-links/sozi-links-tutorial-screenshot-01.fr.png)

Créez cinq vues comme représenté dans les captures d'écran ci-dessous&nbsp;:

![Vue 1 (Accueil)](|filename|/images/tutorial-links/sozi-links-tutorial-screenshot-02.fr.png)
![Vue 2 (Haut gauche)](|filename|/images/tutorial-links/sozi-links-tutorial-screenshot-03.fr.png)
![Vue 3 (Haut droite)](|filename|/images/tutorial-links/sozi-links-tutorial-screenshot-04.fr.png)
![Vue 4 (Bas droite)](|filename|/images/tutorial-links/sozi-links-tutorial-screenshot-05.fr.png)
![Vue 5 (Bas gauche)](|filename|/images/tutorial-links/sozi-links-tutorial-screenshot-06.fr.png)

Éditez les titres des vues et leurs ID de la manière suivante&nbsp;:

<table>
    <tr>
        <th>Numéro de la vue</th>
        <th>Titre</th>
        <th>ID</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Accueil</td>
        <td>accueil</td>
    </tr>
    <tr>
        <td>2</td>
        <td>En haut à gauche</td>
        <td>haut-gauche</td>
    </tr>
    <tr>
        <td>3</td>
        <td>En haut à droite</td>
        <td>haut-droite</td>
    </tr>
    <tr>
        <td>4</td>
        <td>En bas à droite</td>
        <td>bas-droite</td>
    </tr>
    <tr>
        <td>5</td>
        <td>En bas à gauche</td>
        <td>bas-gauche</td>
    </tr>
</table>

Vous pouvez dès à présent ouvrir la présentation dans un navigateur web
pour vérifier si toutes les vues sont correctement définies.

URL d'un vue
------------

Quand un navigateur web affiche une présentation Sozi, le contenu de la barre
d'adresse change à chaque fois que vous passez d'une vue à une autre.

![URL d'une vue dans la barre d'adresse d'un navigateur web](|filename|/images/tutorial-links/sozi-links-tutorial-screenshot-07.fr.png)

Dans l'exemple ci-dessus, la barre d'adresse indique l'URL suivante&nbsp;:

    file://.../tutorial-links.sozi.html#haut-droite

Si votre document est servi par un serveur web, le premier élément de l'URL sera
`http` ou `https` au lieu de `file`.
Dans l'URL ci-dessus, le nom du fichier HTML est suivi du caractère *dièse* (`#`)
et de l'identifiant de la vue courante (`haut-droite`).

Par conséquent, si vous partagez une présentation sur le web, il sera possible
de créer un lien direct vers n'importe quel vue.

Créer des liens dans une présentation
-------------------------------------

> Le standard SVG prend en charge les liens nativement.
> Pour cette raison, Sozi ne fournit aucune fonctionnalité spécifique concernant
> la création de liens dans vos présentations.
> Vous devez les ajouter dans vos documents SVG en utilisant Inkscape ou un
> autre éditeur de dessin vectoriel SVG.

Ouvrez le document `tutorial-links.svg` dans Inkscape.
Cliquez avec le bouton droit sur la grosse flèche qui pointe vers le haut et vers
la gauche, puis choisissez *Créer un lien*.

![Créer un lien avec Inkscape](|filename|/images/tutorial-links/sozi-links-tutorial-screenshot-08.fr.png)

Cette action ouvre une boîte de dialogue *Attributs de l'objet* où vous pouvez
éditer les propriétés du lien.

Pour créer un lien vers la vue située en haut à gauche, il suffit d'affecter
la valeur `#haut-gauche` au champ `Href`&nbsp;:

![Édition de l'attribut href d'un lien](|filename|/images/tutorial-links/sozi-links-tutorial-screenshot-09.fr.png)

Procédez de la même manière pour les autres vues&nbsp;:
pour chaque flèche, créez un lien vers l'ID de la vue correspondante.
Pour finir, sélectionnez le cercle bleu et créez un lien vers `#accueil`.

Mettez à jour et visionnez la présentation
------------------------------------------

Enregistrez le document SVG dans Inkscape.
Revenez dans la fenêtre de Sozi pour mettre à jour le contenu SVG de la
présentation.
L'opération de mise à jour est automatique.

Ouvrez le fichier `tutorial-links.sozi.html` dans un navigateur Web.
La caméra est automatiquement positionnée sur la première vue de la présentation.
Cliquez dans le fond blanc de l'image pour passer à la vue suivante.
(voir aussi: [Jouer une présentation](|filename|play.md))
ou cliquez sur une des flèches pour aller directement à la vue correspondante.

[Téléchargez la présentation complète](|filename|/presentations/tutorial-links/tutorial-links.fr.sozi.html)
(Cliquez avec le bouton droit sur le lien et choisissez *Enregistrer la cible du lien sous*).
