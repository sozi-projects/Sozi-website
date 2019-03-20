Title: FAQ: Häufig gestellte Fragen und Antworten
Slug: faq
Lang: de
Authors: Guillaume Savaton, Andrej Barth, Alfred Bergkemper
Translation: true
Status: hidden

Sozi stellt einige Grafiken nicht korrekt dar
---------------------------------------------

Sozi ist nicht für das Rendern, also die Darstellung des Dokuments auf dem Bildschirm zuständig.
Das ist Aufgabe des Browsers.
Sozi kümmert sich nur um den *Ablauf der Präsentation*, um die Logik: geometrische Übergänge auf die Ebenen des Dokuments anwenden, die Animation steuern und Nutzereingaben verarbeiten.
Wenn Grafiken nicht oder nicht richtig dargestellt werden, dann liegt das sehr wahrscheinlich am svg-Editor oder am Web Browser.

> Bitte schicke uns keine Fehlermeldungen zu diesem Thema, es sei denn, Du hast sehr guten Grund zu der Annahme, das der Fehler in Sozi liegt.
> Wenn Du Dir nicht sicher bist, kannst Du in der [Sozi community forum](/community) nachfragen.

Einige Nutzer haben von Problemen berichtet, wenn ihre svg-Dokumente *Fließtext* enthalten.
Das meint Text, der automatisch in einer gewählten Form (einem Rechteck in Inkscape) fließt.
Dieses Feature ist derzeit noch nicht stabil im SVG-Standard.
Die FAQ von Inkscape raten daher [in diesem Punkt](https://inkscape.org/en/learn/faq/#Flowed_text_doesn%27t_show_up_in_exported_file) auch vom Einsatz von *flowed text* ab, falls die Grafik auch außerhalb von Inkscape werden soll:

> [...] you should not use flowed text in documents that you intend to use outside of Inkscape.



Wie setze ich die Hintergrund-Farbe?
------------------------------------

Inkscape kann die Hintergrundfarbe in den *Dokumenteneinstellungen* festlegen
(*Datei*-Menü &rarr; *Dokumenteneinstellungen* &rarr; *Seite*-Tab &rarr; *Hintergrundfarbe*).
Wichtig ist hier, dass der *Alpha-Kanal* (Deckkraft) der Farbe auf 255 eingestellt ist.

![Einstellung der Hintergrundfarbe in Inkscape](|filename|/images/faq/background-de.png)

Sozi erkennt eine in Inkscape eingestellte Hintergrundfarbe und erzeugt eine Präsentation 
mit genau dieser Hintergrundfarbe.

> Diese Eigenschaft ist Inkscape-spezifisch und wird von Web-Browsern u.U. ignoriert, 
> wenn die SVG-Datei selbst geöffnet wird.

Wenn Sie nicht mit Inkscape arbeiten, können Sie die Hintergrundfarbe Ihres SVG-Dokuments
auch direkt im Quelltext festlegen. Öffnen Sie die Datei in einem Texteditor und 
fügen Sie ein `<style>`-Element innerhalb des Root-`<svg>`-Elements wie folgt ein:

```xml
<style>
    svg {
        background: rgb(160, 180, 220);
    }
</style>
```


> Ersetzen Sie `rgb(160, 180, 220)` durch Ihre [CSS Farbe](https://developer.mozilla.org/en/docs/Web/CSS/color_value).


Wie bekomme ich die gestrichelte Linie um den Hyperlink weg, der gerade den Focus hat?
--------------------------------------------------------------------------------------

Wenn Ihr Dokument Hyperlinks enthält, bemerken Sie u.U. eine gestrichelte Linie
um einen Link, den Sie gerade angeklickt haben.

Dieses Rechteck wird vom Browser automatisch hinzugefügt, um anzuzeigen, dass 
dieses Element gerade den Focus hat.
Über eine CSS-Regel lässt sich das Rechteck entfernen. 
Öffnen Sie die Datei in einem Texteditor und 
fügen Sie dieses `<style>`-Element innerhalb des Root-`<svg>`-Elements wie folgt ein:

```xml
<style>
    a:focus {
    	outline: none;
    }
</style>
```
