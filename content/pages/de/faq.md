Title: FAQ: Häufig gestellte Fragen und Antworten
Slug: faq
Lang: de
Authors: Guillaume Savaton, Andrej Barth
Translation: true
Status: hidden

Wie setze ich die Hintergrund-Farbe?
------------------------------------

Bei Inkscape kannst Du die Hintergrundfarbe in den *Dokumenteneinstellungen* setzen.
Leider ist diese Farbe nur in Inkscape selbst und in exportierten Grafiken sichtbar.
Von Webbrowsern wird sie ignoriert.

Um die Hintergrundfarbe so zu setzen, dass sie auch vom Browser dargestellt wird, kannst Du den XML-Editor von Inkscape nutzen.
Selektiere das Wurzelelement `<svg:svg>`, erstelle ein Kindelement `<svg:style>` und darin einen Textknoten wie im folgenden Bild:

![Setting a background color in Inkscape](|filename|/images/faq/background.png)

> Ersetze `rgb(255, 200, 255)` mit der [Farbe](https://developer.mozilla.org/en/docs/Web/CSS/color_value) Deiner Wahl.

Wenn Du lieber einen Texteditor einsetzt, dann füge damit im svg-Dokument das folgende Element als Kind des Wurzelelements `<svg>` ein:

    :::xml
    <style>
        svg {
            background: rgb(255, 200, 255);
        }
    </style>


Sozi stellt einige Grafiken nicht korrekt dar
---------------------------------------------

Einige Nutzer haben von Problemen berichtet, wenn ihre svg-Dokumente *Fließtext* enthalten.
Das meint Text, der automatisch in einer gewählten Form (einem Rechteck in Inkscape) fließt.
Dieses Feature ist derzeit noch nicht stabil im SVG-Standard.
Die FAQ von Inkscape raten daher [in diesem Punkt](https://inkscape.org/en/learn/faq/#Flowed_text_doesn%27t_show_up_in_exported_file) auch vom Einsatz von *flowed text* ab, falls die Grafik auch außerhalb von Inkscape werden soll:

> [...] you should not use flowed text in documents that you intend to use outside of Inkscape.

Allgemein gesagt, Sozi ist nicht für das Rendern, also die Darstellung des Dokuments auf dem Bildschirm zuständig.
Das ist Aufgabe des Browsers &ndash; Sozi selbst basiert auch auf einem Web Browser.
Sozi kümmert sich nur um den *Ablauf der Präsentation*, um die Logik: geometrische Übergänge auf die Ebenen des Dokuments anwenden, die Animation steuern und Nutzereingaben verarbeiten.
Wenn Grafiken nicht oder nicht richtig dargestellt werden, dann liegt das sehr wahrscheinlich am svg-Editor oder am Web Browser.

Bitte schicke uns keine Fehlermeldungen zu diesem Thema, es sei denn, Du hast sehr guten Grund zu der Annahme, das der Fehler in Sozi liegt.
Wenn Du Dir nicht sicher bist, kannst Du in der [Sozi community forum](/community) nachfragen.


Inkscape reports a syntax error when running Sozi 13
----------------------------------------------------

This problem has been reported mainly by Windows users.
When running Sozi from the Inkscape extensions menu, a dialog shows the following error:

    :::pytb
    Traceback (most recent call last):
      File "sozi.py", line 30, in from sozi.document import *
      File "C:\Program Files (x86)\Inkscape\share\extensions\sozi\document.py", line 96
        self.layers = { l.attrib[group_attr] : SoziLayer(self, l) for l in self.xml.xpath("sozi:layer", namespaces=inkex.NSS) if group_attr in l.attrib }
    SyntaxError: invalid syntax

This error happens when Inkscape tries to run Sozi using Python 2.6 instead of Python 2.7.
Usually, it means that Python 2.7 has not been installed, or not at the correct location.
Check that you have followed the [installation instructions](http://sozi.baierouge.fr/pages/install-windows.html)
correctly.

Though this has not been confirmed, it seems that some users experience this problem when installing the
*portable* version of Inkscape. Please use the *installer* instead.
