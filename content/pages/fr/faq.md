Title: Questions fréquentes et résolution des problèmes
Slug: faq
Lang: fr
Authors: Guillaume Savaton
Status: hidden

Comment définir une couleur de fond ?
-------------------------------------

Inkscape permet de définir la couleur de fond de la page dans la boîte
de dialogue *propriétés du document*.
Malheureusement, la couleur sélectionnée n'est visible que dans Inkscape
et dans les images exportées à partir de votre document.
Elle est ignorée par les navigateurs web.

Pour définir une couleur de fond qui s'affichera dans un navigateur web,
vous pouvez utiliser l'éditeur XML intégré à Inkscape.
Sélectionner l'élément `<svg:svg>` racine, ajoutez-lui un nœud enfant `<svg:style>`
puis insérez un nœud texte dans ce dernier avec le contenu affiché dans cette capture
d'écran:

![Comment définir une couleur de fond dans Inkscape](|filename|/images/faq/background.png)

> Remplacez `rgb(255, 200, 255)` par la [couleur CSS](https://developer.mozilla.org/fr/docs/Web/CSS/color_value) de votre choix.

Si vous préférez utiliser un éditeur de texte, ouvrez votre document SVG
et ajouter l'élément suivant en tant qu'enfant de l'élément `<svg>` racine:

    :::xml
    <style>
        svg {
            background: rgb(255, 200, 255);
        }
    </style>


Des éléments de mon document ne sont pas affichés correctement
--------------------------------------------------------------

Plusieurs utilisateurs ont signalé des problèmes d'affichage lorsque leurs documents SVG contiennent
des éléments de texte qui s'adaptent automatiquement à une certaine forme (par exemple un rectangle).
Cette fonctionnalité n'est pas encore considérée comme stable dans le standard SVG.
La FAQ d'Inkscape donne [des explications sur ce sujet](https://inkscape.org/fr/learn/faq/#Flowed_text_doesn%27t_show_up_in_exported_file)
avec l'avertissement suivant&nbsp;:

> La solution est donc de ne pas utiliser de texte en flux si vous prévoyez [...] d'utiliser le fichier avec autre chose qu'Inkscape.

Plus généralement, Sozi n'est pas responsable du rendu de votre document à l'écran.
Ce travail est effectué par les navigateurs web &mdash; en fait, l'éditeur de présentation lui-même est construit autour d'un navigateur web.
Sozi gère uniquement le déroulement de la présentation&nbsp;: appliquer des transformations géométriques aux calques de votre document,
piloter les animations, réagir aux actions de l'utilisateur.
Si vous observez que des éléments du document ne sont pas affichés correctement, le problème se trouve probablement dans votre logiciel de dessin ou dans votre navigateur web.

Merci de ne pas signaler ce type de problèmes, à moins que vous n'ayez de très bonnes raisons de croire qu'il s'agit d'un bug dans Sozi.
En cas de doute, vous pouvez demander de l'aide au [forum de la communauté Sozi](/community).
