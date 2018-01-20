Title: Inclure une présentation Sozi dans un document HTML
Slug: tutorial-embedding
Lang: fr
Author: Guillaume Savaton
Status: hidden

Pour insérer une présentation Sozi dans une page web, vous pouvez
utiliser un élément `<iframe>` comme ceci&nbsp;:


    :::html
    <iframe src="ma-presentation.sozi.html">
        Ma présentation Sozi devrait apparaître ici.
    </iframe>

La largeur et la hauteur d'affichage du document inclus peut être
modifiée au moyen d'attributs de l'élément `<iframe>` ou
en utilisant CSS.
Un exemple est visible ci-dessous.
[Plus d'informations sur l'élément `<iframe>`](https://developer.mozilla.org/fr/docs/Web/HTML/Element/iframe).

<iframe class="sozi" src="|filename|/presentations/ceci-nest-pas-un-diaporama.sozi.html">
    Votre navigateur ne peut pas afficher ce contenu.
</iframe>

Focaliser le clavier sur la présentation Sozi
-----------------------------------------------

Au chargement d'une page HTML, le navigateur donne le focus au premier
élément qui peut l'accepter (lien, élément de formulaire, etc).
Pour cette raison, dans de nombreux cas, une présentation Sozi incluse dans
une page web ne réagira pas aux actions sur le clavier immédiatement
après le chargement.
Une première solution consiste à presser la touche `TAB` de manière répétée
jusqu'à ce que l'`<iframe>` qui affiche votre présentation reçoive le focus.

Vous pouvez également ajouter le script suivant à votre document HTML
pour donner automatiquement le focus à la première `<iframe>` de la page
au chargement&nbsp;:

    :::html
    <script>
        window.addEventListener("load", function () {
            document.querySelector("iframe").focus();
        }, false);
    </script>
