Title: Questions fréquentes et résolution des problèmes
Slug: faq
Lang: fr
Authors: Guillaume Savaton
Status: hidden

Des éléments de mon document ne sont pas affichés correctement
--------------------------------------------------------------

Sozi n'est pas responsable du rendu des éléments graphiques de votre document à l'écran.
Ce travail est effectué par les navigateurs web.
Sozi gère uniquement le déroulement de la présentation&nbsp;: appliquer des transformations géométriques aux calques de votre document,
piloter les animations, réagir aux actions de l'utilisateur.
Si vous observez que des éléments du document ne sont pas affichés correctement, le problème se trouve probablement dans votre logiciel de dessin ou dans votre navigateur web.

> Merci de ne pas signaler ce type de problèmes, à moins que vous n'ayez de très bonnes raisons de croire qu'il s'agit d'un bug dans Sozi.
> En cas de doute, vous pouvez demander de l'aide au [forum de la communauté Sozi](/community).

Plusieurs utilisateurs ont signalé des problèmes d'affichage lorsque leurs documents SVG contiennent
des éléments de texte qui s'adaptent automatiquement à une certaine forme (par exemple un rectangle).
Cette fonctionnalité n'est pas encore considérée comme stable dans le standard SVG.
La FAQ d'Inkscape donne [des explications sur ce sujet](https://inkscape.org/fr/learn/faq/#Flowed_text_doesn%27t_show_up_in_exported_file)
avec l'avertissement suivant&nbsp;:

> La solution est donc de ne pas utiliser de texte en flux si vous prévoyez [...] d'utiliser le fichier avec autre chose qu'Inkscape.

Comment définir une couleur de fond ?
-------------------------------------

Inkscape permet de définir la couleur de fond de la page dans la boîte
de dialogue *propriétés du document*
(menu *Fichiers* &rarr; *Propriétés du document* &rarr; onglet *Page* &rarr; *Couleur de fond*).
Vérifiez que la composante Alpha (opacité) de la couleur vaut 255.

![Comment définir une couleur de fond dans Inkscape]({static}/images/faq/background-fr.png)

Si vous définissez une couleur de fond dans Inkscape, Sozi le détectera
et produira un document HTML avec la même couleur de fond.

> Cette propriété est spécifique à Inkscape et est ignorée par les navigateurs
> web lorsque vous affichez un document SVG seul.

Une solution générale si vous n'utilisez pas Inkscape, ou si vous voulez que votre
document SVG s'affiche avec la couleur de fond de votre choix, consiste à ouvrir
le fichier SVG dans un éditeur de texte et à insérer un élément `<style>`
dans l'élément racine `<svg>` de la manière suivante&nbsp;:

    :::xml
    <style>
        svg {
            background: rgb(160, 180, 220);
        }
    </style>

> Remplacez `rgb(160, 180, 220)` par la [couleur CSS](https://developer.mozilla.org/fr/docs/Web/CSS/color_value) de votre choix.

Comment supprimer la ligne pointillée autour d'un lien qui a le focus&nbsp;?
----------------------------------------------------------------------------

Si votre document contient des liens, vous avez peut-être remarqué qu'après
avoir cliqué sur l'un d'entre eux, il se retrouve entouré par un rectangle pointillé.

Ce rectangle est ajouté par le navigateur web pour indentifier le lien qui a
le focus.
Vous pouvez le supprimer en utilisant une règle CSS.
Ouvrez votre document SVG dans un éditeur de texte et ajouter l'élément `<style>`
suivant à l'intérieur de l'élement racine `<svg>`&nbsp;:

    :::xml
    <style>
        a:focus {
        	outline: none;
        }
    </style>
