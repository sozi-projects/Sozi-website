Title: Inclure une présentation Sozi dans un document HTML
Slug: tutorial-embedding
Lang: fr
Authors: Guillaume Savaton
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

Agir sur la présentation depuis la page HTML principale
-------------------------------------------------------

Dans l'exemple ci-dessous, nous ajoutons deux boutons à la page HTML principale
pour aller à la vue précédente ou suivante.
Entre les boutons, un élément `<span>` affichera le titre de la vue courante.

    :::html
    Pressez ces boutons pour aller à la vue précédente/suivante&nbsp;:
    <input id="btn-prec" type="button" value="&larr;" title="Aller à la vue précédente">
    <span  id="titre-vue">Chargement&hellip;</span>
    <input id="btn-suiv" type="button" value="&rarr;" title="Aller à la vue suivante">

    <iframe src="ma-presentation.sozi.html">
        Ma présentation Sozi devrait apparaître ici.
    </iframe>

    <script>
        window.addEventListener("load", function () {
            var frame     = document.querySelector("iframe");
            var btnPrec   = document.getElementById("btn-prec");
            var btnSuiv   = document.getElementById("btn-suiv");
            var spanTitre = document.getElementById("titre-vue");

            var player = frame.contentWindow.sozi.player;

            spanTitre.innerHTML = player.currentFrame.title;

            btnPrec.addEventListener("click", function () {
                player.moveToPrevious();
            }, false);

            btnSuiv.addEventListener("click", function () {
                player.moveToNext();
            }, false);

            player.addListener("frameChange", function () {
                spanTitre.innerHTML = player.currentFrame.title;
            });
        }, false);
    </script>

Voici un aperçu du résultat&nbsp;:

Pressez ces boutons pour aller à la vue précédente/suivante&nbsp;:
<input id="sozi-first-presentation-prev" title="Move to the previous frame" type="button" value="&larr;">
<span  id="sozi-first-presentation-title">Loading&hellip;</span>
<input id="sozi-first-presentation-next" title="Move to the next frame" type="button" value="&rarr;">

<iframe class="sozi" id="sozi-first-presentation" src="|filename|/presentations/tutorial-first/first-presentation.sozi.html">
    Your browser cannot display this content.
</iframe>

<script>
    window.addEventListener("load", function () {
        var frame     = document.getElementById("sozi-first-presentation");
        var btnPrec   = document.getElementById("sozi-first-presentation-prev");
        var btnSuiv   = document.getElementById("sozi-first-presentation-next");
        var spanTitre = document.getElementById("sozi-first-presentation-title");

        var player = frame.contentWindow.sozi.player;

        spanTitre.innerHTML = player.currentFrame.title;

        btnPrec.addEventListener("click", function () {
            player.moveToPrevious();
        }, false);

        btnSuiv.addEventListener("click", function () {
            player.moveToNext();
        }, false);

        player.addListener("frameChange", function () {
            spanTitre.innerHTML = player.currentFrame.title;
        });
    }, false);
</script>
