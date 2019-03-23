Title: Den Ablauf der Präsentation flüssiger gestalten
Slug: tutorial-performance
Lang: de
Authors: Guillaume Savaton, Alfred Bergkemper
Status: hidden
Translation: true

Eine eine sehr komplexe Sozi-Präsentation kann bei der Darstellung von Animationen 
schon einmal ins Stottern geraten. Das Problem hängt vorrangig von der Qualität 
des benutzten Browsers ab, was das Rendern von SVG-Dateien anbelangt.

Es gibt Möglichkeiten, das Problem zu umgehen:

Konvertieren Sie Texte zu Pfaden
--------------------------------

Einige Browser benötigen zur Darstellung von SVG-Text extrem viel Zeit. 
Diese Wartezeit kann man einsparen, indem man Text-Elemente in *Pfade* umwandelt 
und so dem Browser die Arbeit erleichtert. 
Diese Umwandlung beschleunigt nicht nur die Anzeige, sie stellt auch sicher,
dass der Text in allen Browsern identisch angezeigt wird, selbst wenn die
benutzte Schriftart auf dem Computer, der die Präsentation anzeigen soll, 
nicht vorhanden ist.

Allerdings hat dieses Vorgehen auch einen Nachteil: da der Originaltext entfernt wird,
sind spätere Änderungen nicht mehr möglich. Auch die Indizierung durch Suchmaschinen 
wird verhindert.

> Führen Sie diese Aktion also nicht an den Original-Dokumenten durch
> und legen Sie sicherheitshalber immer Kopien an.

Wählen Sie Inkscape alle Text-Element aus (*Edit* menu / *Find*, or Strg-F).

![Text-Elemente finden](|filename|/images/tutorial-performance/sozi-tutorial-performance-screenshot-01.de.png)

Wählen Sie *Objekt in Pfad umwandeln* aus dem *Pfad*-Menü (Umschalt-Strg-C).

Optimieren Sie ihr Dokument
---------------------------

[Scour](http://www.codedread.com/scour/) ist ein Tool, das Optimierungen an SVG-Dokumenten vornimmt.
Vorrangiges Ziel ist die Reduzierung der Dateigröße, aber weitere
[Operationen](http://www.codedread.com/scour/ops.php) können dabei helfen, die Darstellung zu beschleunigen:

* Entfernen von leeren und nicht benutzten Elementen
* Verschmelzen von verschachtelten Gruppen,
* Vereinfachung von Pfaden und Farbverläufen,
* Entfernen nutzloser Gestaltungen.

Scour kann als eigenständiges Python-Script oder als Inkscape-Erweiterung ablaufen.

> Wenden Sie Scour nicht auf Ihre Original-Dokumente an.
> Legen Sie immer vorher eine Sicherung an.
>
> Wir haben die Auswirkungen von Scour auf Sozi-Präsentationen noch nicht ausführlich getestet.
> Einige Optimierungen können durchaus Informationen entfernen, die von Sozi zur Darstellung gebraucht werden.
