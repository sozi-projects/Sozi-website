Title: FAQ: Häufig gestellte Fragen und Antworten
Slug: faq
Lang: de
Authors: Guillaume Savaton, Andrej Barth
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

Bei Inkscape kannst Du die Hintergrundfarbe in den *Dokumenteneinstellungen* setzen.

![Setting a background color in Inkscape](|filename|/images/faq/background-en.png)
