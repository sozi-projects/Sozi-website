Title: Sozi Präsentationen in HTML-Seiten einbetten
Slug: tutorial-embedding
Lang: de
Authors: Guillaume Savaton, Alfred Bergkemper
Status: hidden
Translation: true

Mit einem `<iframe>`-Element kann man eine Sozi-Präsentation mit wenigen Zeilen in eine Web-Seite einbauen:

```html
<iframe src="my-presentation.sozi.html">
    Meine Sozi-Präsentation sollte hier ablaufen.
</iframe>
```


Breite und Höhe des Ansichtsbereichs können entweder als Attribute des `<iframe>`-Elements eingestellt werden
oder mittels CSS. Ein Beispiel finden Sie nachstehend.
[Lesen Sie mehr über `<iframe>` Elemente](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe).

<iframe class="sozi" src="{static}/presentations/this-is-not-a-slideshow.sozi.html">
    Ihr Browser kann diesen Inhalt nicht darstellen.
</iframe>  


Der Präsentation den Tastatur-Focus übergeben
---------------------------------------------

Beim Laden einer HTML-Seite übergibt der Browser den Tastatur-Focus an das erste Element, das 
ihn sich greifen kann (Hyperlink, Formularfeld etc.).
Aus diesem Grund reagiert eine eingebettete Präsentation direkt nach dem Laden eventuell nicht sofort 
auf Tastatureingaben. Durch Drücken der `TAB`-Taste kann der Focus an das jeweils nächste Element weitergegeben 
werden.

Man kann diese Aufgabe auch einem Script übergeben. Angenommen, das `<iframe>`-Element mit Ihrer Präsentation ist 
das erste `<iframe>`-Element auf Ihrer Seite, dann können Sie ihm mit dem folgenden Script den Focus automatisch 
übergeben.

```html
<script>
    window.addEventListener("load", function () {
        document.querySelector("iframe").focus();
    }, false);
</script>
```

Steuern Sie die Präsentation von der HTML-Seite aus
---------------------------------------------------

Im folgenden Beispiel werden der HTML-Seite *zwei Buttons* hinzugefügt, mit denen die Präsentation
jeweils ein Bild vor oder zurück gestellt werden kann.
Zwischen den beiden Buttons erscheint in einem `<span>`-Element sogar *der Titel* des gerade angezeigten 
Frames.

```html
Klicken Sie die Buttons, um das nächste /letzte Bild anzuzeigen:
<input id="btn-prev" type="button" value="&larr;" title="Zum nächsten Bild">
<span  id="frame-title">Loading&hellip;</span>
<input id="btn-next" type="button" value="&rarr;" title="Ein Bild zurück">

<iframe src="my-presentation.sozi.html">
    Meine Sozi-Präsentation sollte hier ablaufen.
</iframe>

<script>
    window.addEventListener("load", function () {
        var frame     = document.querySelector("iframe");
        var btnPrev   = document.getElementById("btn-prev");
        var btnNext   = document.getElementById("btn-next");
        var spanTitle = document.getElementById("frame-title");

        var player = frame.contentWindow.sozi.player;

        spanTitle.innerHTML = player.currentFrame.title;

        btnPrev.addEventListener("click", function () {
            player.moveToPrevious();
        }, false);

        btnNext.addEventListener("click", function () {
            player.moveToNext();
        }, false);

        player.addListener("frameChange", function () {
            spanTitle.innerHTML = player.currentFrame.title;
        });
    }, false);
</script>
```

Hier das Ergebnis:

Klicken Sie die Buttons, um das nächste /letzte Bild anzuzeigen:  
<input id="sozi-first-presentation-prev" title="Nächstes Bild" type="button" value="&larr;">
<span  id="sozi-first-presentation-title">Loading&hellip;</span>
<input id="sozi-first-presentation-next" title="Bild zurück" type="button" value="&rarr;">

<iframe class="sozi" id="sozi-first-presentation" src="{static}/presentations/tutorial-first/first-presentation.sozi.html">
    Ihr Browser kann diesen Inhalt nicht darstellen.
</iframe>

<script>
    window.addEventListener("load", function () {
        var frame      = document.getElementById("sozi-first-presentation");
        var btnPrev    = document.getElementById("sozi-first-presentation-prev");
        var btnNext    = document.getElementById("sozi-first-presentation-next");
        var spanTitle = document.getElementById("sozi-first-presentation-title");

        var player = frame.contentWindow.sozi.player;

        spanTitle.innerHTML = player.currentFrame.title;

        btnPrev.addEventListener("click", function () {
            player.moveToPrevious();
        }, false);

        btnNext.addEventListener("click", function () {
            player.moveToNext();
        }, false);

        player.addListener("frameChange", function () {
            spanTitle.innerHTML = player.currentFrame.title;
        });
    }, false);
</script>
