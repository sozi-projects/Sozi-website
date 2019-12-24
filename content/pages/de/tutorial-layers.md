Title: Der Gebrauch von Ebenen
Slug: tutorial-layers
Lang: de
Authors: Guillaume Savaton, Alfred Bergkemper
Status: hidden
Translation: true


Eine Sozi-Präsentation kann aus mehreren Ebenen aufgebaut sein, die sich bei der Anzeige unabhängig 
voneinander verhalten. Eine typische Anwendung wäre ein einheitlicher Hintergrund für die Einzelbilder, 
aber viele weitere Anwendungen sind denkbar.  
Mit etwas Aufwand und Kreativität kann man auch sehr ausgefeilte *Animationen* erstellen. Man sollte 
dabei aber immer im Hinterkopf haben, dass Sozi in erster Linie zur Erstellung von Präsentationen 
gedacht ist und daher nicht alle Möglichkeiten bietet, die ein spezielles Animationsprogramm mit 
sich bringen würde.


Herunterladen und Öffnen der Basis-Datei
----------------------------------------

Dieses Tutorial basiert auf einer SVG-Datei, die die einzelnen Elemente unserer Präsentation enthält.
[Bitte laden Sie die Basis-SVG-Datei]({static}/presentations/tutorial-layers/tutorial-layers.de.svg)
(Rechtsklick auf den Link und dann *verlinkten Inhalt speichern unter*).

Die Datei wurde mit [Inkscape](https://inkscape.org) erstellt.
Wir gehen davon aus, dass Inkscape bereits installiert ist.
Öffnen Sie die Datei in InkScape, um die Organisation der Grafiken näher zu betrachten.

![Base document in Inkscape]({static}/images/tutorial-layers/sozi-layers-tutorial-screenshot-01.de.png)


Organisation der Ebenen
------------------------

Öffnen Sie das Andockfenster ›Ebenen‹ durch Klick auf das entsprechende Icon, die 
Tastenkombination **Strg-Umsch-L** oder Klick auf ›Ebenen‹ im Ebenen-Menü.

![Ebenen anzeigen]({static}/images/tutorial-layers/sozi-layers-tutorial-screenshot-02.de.png)

Unser Dokument enthält drei Ebenen:

* *Überschriften:*   Die Vordergrundebene mit den Textelementen
* *Himmel:*           Die Hintergrundebene enthält einen großen blauen Kreis mit Sonne, Mond und Sternen.
* *Landschaft:*      Die zwischen den beiden anderen liegende Ebene enthält das Bild eines Baumes.

Jede Ebene hat eine *Unterebene* mit dem Namen ›Frame‹, die jeweils nur die Rechtecke enthält, die Sozi 
später zur Ausrichtung der Grafiken benutzt.

> Durch Klick auf das *Auge-Symbol* im Andockfenster lässt sich jede Ebene ein- bzw. ausblenden.
> Blenden Sie jede Ebene und Unterebene mal kurz aus, um zu sehen, welches Element zu welcher Ebene gehört.
>
> Stellen Sie sicher, dass alle Ebenen sichtbar sind und *speichern Sie die Datei*, bevor Sie zum nächsten Teil weitergehen.



Erzeugen Sie die Einzelbilder der Präsentation
----------------------------------------------

Öffnen Sie `tutorial-layers.de.svg` im Sozi-Editor.

![Base document in Sozi]({static}/images/tutorial-layers/sozi-layers-tutorial-screenshot-03.de.png)

Erzeugen Sie durch Klicks auf den *+* Button in der Zeitleiste vier neue Einzelbilder und benennen Sie
sie durch folgende Einträge im Titel-Feld:

1. "Morgen",
2. "Mittag",
3. "Abend",
4. "Nacht".


Die Zeitleiste sollte jetzt folgendermaßen aussehen:

![Timeline with 4 frames]({static}/images/tutorial-layers/sozi-layers-tutorial-screenshot-04.de.png)  
  
  

Fügen Sie die Ebene ›Landschaft‹ hinzu (fixed Layer)
----------------------------------------------------

Klicken Sie auf *Ebene hinzufügen* und wählen Sie *Landschaft*. Klicken Sie in der Zeitleiste
auf die Zelle in der Spalte ›Morgen‹ und Zeile ›Landschaft‹. Diese ist damit ausgewählt (blau hinterlegt).

![Select layer Landscape for frame 1]({static}/images/tutorial-layers/sozi-layers-tutorial-screenshot-05.de.png)

Schieben Sie nun mit der Maus das Rechteck mit dem Baum etwa in die Mitte des Vorschaufensters.
Wenn Sie bisher alles richtig gemacht haben, sollte sich dabei *nur dieses Rechteck mitsamt Baum* 
bewegen. *Vergrößern* Sie (mit dem Mausrad) Rechteck und Baum, bis sie nahezu das ganze Fenster 
ausfüllen.

![Zoom in the Landcape layer]({static}/images/tutorial-layers/sozi-layers-tutorial-screenshot-06.de.png)

Im Eigenschaftsfenster rechts sollte im Feld *Outline-Element-ID* der Begriff ›rect-landscape‹ auftauchen. 
Dabei handelt es sich um die SVG-Kennung des roten Rechtecks, das den Baum umschließt.
Da der Button *Element automatisch auswählen* aktiviert (blau hinterlegt) ist, erkennt Sozi die
SVG-Kennung und schlägt automatisch vor, dieses Objekt zur Größenanpassung des ersten 
Einzelbilds zu verwenden.

![Outline element selection]({static}/images/tutorial-layers/sozi-layers-tutorial-screenshot-07.de.png)

* klicken Sie auf den Button *An SVG_Element anpassen* und die Ebene ›Landschaft‹ wird automatisch 
  so verschoben und vergrößert, dass das Rechteck maximal groß im Vorschaufeld angezeigt wird.
* Ein Klick auf *Element verstecken* blendet das Rechteck aus.

Direkt unter dem Titel ›Ebene‹ im Einstellungsfenster gibt es den Button *Nicht sichtbare 
Elemente entfernen*, mit dem man alles außerhalb des Rechtecks verstecken kann. Diese Option 
ist sehr sinnvoll, wenn die bei der Präsentation benutzte Anzeige ein anderes Seitenverhältnis 
hat, als es für diese Präsentation in Sozi eingestellt wurde.

Nachdem wir jetzt eine feste Ebene eingestellt haben, geht es jetzt an die animierten Teile.

![Fitted Landscape layer]({static}/images/tutorial-layers/sozi-layers-tutorial-screenshot-08.de.png)


Fügen Sie eine animierte Ebene hinzu (Überschriften)
----------------------------------------------------

Klicken Sie auf *Ebene hinzufügen* und wählen Sie *Überschriften*. Klicken Sie in der Zeitleiste
auf die Zelle in der Spalte ›Morgen‹ und Zeile ›Überschriften‹ und wählen Sie sie damit aus (blau hinterlegt).

![Select layer Captions for frame 1]({static}/images/tutorial-layers/sozi-layers-tutorial-screenshot-09.de.png)

Verschieben Sie jetzt das Rechteck mit dem Text ›Morgen‹ etwa in die Mitte des Vorschaufensters 
und vergrößern Sie es, bis es das Fenster nahezu ausfüllt.

![Zoom in the Captions layer]({static}/images/tutorial-layers/sozi-layers-tutorial-screenshot-10.de.png)

Im Eigenschaftsfenster rechts sollte im Feld *Outline-Element-ID* der Begriff ›rect-text-morning‹ auftauchen. 
Ein Klick auf *An SVG-Element anpassen* sollte die Feinarbeit machen und das Rechteck auf
die Größe des Vorschaufensters anpassen. Verbergen Sie wie zuvor das Rechteck und blenden 
Sie den Rest aus.

Verfahren Sie in gleicher Weise mit den Rechtecken für "Mittag", "Abend" und "Nacht" in den drei anderen Frames. 
Das Vorschaufenster sollte jeweils so aussehen:

![Adjusted frame 1 in Captions layer]({static}/images/tutorial-layers/sozi-layers-tutorial-screenshot-11.de.png)
![Adjusted frame 2 in Captions layer]({static}/images/tutorial-layers/sozi-layers-tutorial-screenshot-12.de.png)
![Adjusted frame 3 in Captions layer]({static}/images/tutorial-layers/sozi-layers-tutorial-screenshot-13.de.png)
![Adjusted frame 4 in Captions layer]({static}/images/tutorial-layers/sozi-layers-tutorial-screenshot-14.de.png)


Fügen Sie eine weitere animierte Ebene hinzu (Himmel)
-----------------------------------------------------

In diesem Stadium werden alle Grafiken, die *nicht* in den Ebenen ›Landschaft‹ und ›Überschrift‹ liegen,
durch die Zeile ›Standard‹ der Zeitleiste angezeigt.

Hierbei handelt es sich nicht um eine *Ebene* sondern hier werden alle Ebenen zusammengefasst, 
die nicht explizit zur Zeitleiste hinzugefüht wurden. Hier tauchen auch
Grafiken auf, die überhaupt keiner Ebene zugeordnet sind (kann vorkommen, sollte aber vermieden werden).  
Wird der InkScape-Datei irgendwann eine neue Ebene hinzugefügt, taucht sie in Sozi automatisch in 
der Zeile *Standard* auf.

Klicken Sie auf *Ebene hinzufügen* und wählen Sie *Himmel*. Die Zeile ›Standard‹ sollte verschwinden.

Der Einfachheit halber *verbergen* wir die Ebenen ›Landschaft‹ und ›Überschrift‹. Klicken Sie dazu 
auf das ›Auge‹-Icon ganz links in der jeweiligen Zeile der Zeitliste.

![Select layer Captions for frame 1]({static}/images/tutorial-layers/sozi-layers-tutorial-screenshot-15.de.png)

> Das Auge-Icon verbirgt die Anzeige der entsprechenden Ebene in *Sozi* und hilft dadurch bei der 
> Bearbeitung der anderen Ebenen.
> Die so verborgenen Ebenen sind bei der Präsentation im Browser immer noch sichtbar.
>
> Wenn Sie eine Ebene während der Präsentation ausblenden wollen, stellen Sie ihre *Deckkraft* mit
> dem Schieberegler auf Null.

Verfahren Sie jetzt wie bei der Ebene ›Überschriften‹. Für jedes Einzelbild:

1. Wählen Sie das entsprechende Feld in der Zeile ›Himmel‹ aus.
2. Im Vorschaufenster schieben/rotieren/zoomen Sie die Ebene, bis das gewünschte Rechteck beinahe
   das ganze Fenster ausfüllt und seine SVG-Kennung im Feld *Outline-Element-ID* auftaucht.
3. Aktivieren Sie die Buttons *An SVG-Element anpassen*, *Element verstecken* und  *Nicht sichtbare 
   Elemente entfernen*.

Machen Sie die beiden ausgeblendeten Ebenen ›Landschaft‹ und ›Überschrift‹ wieder sichtbar und 
das Vorschaufenster sollte etwa so aussehen:

![Adjusted frame 1 in Sky layer]({static}/images/tutorial-layers/sozi-layers-tutorial-screenshot-16.de.png)
Stören Sie sich bitte nicht an den drei roten Rahmen, die verschwinden automatisch, wenn Sie die 
nächsten drei Einzelbilder bearbeiten.
![Adjusted frame 2 in Sky layer]({static}/images/tutorial-layers/sozi-layers-tutorial-screenshot-17.de.png)
![Adjusted frame 3 in Sky layer]({static}/images/tutorial-layers/sozi-layers-tutorial-screenshot-18.de.png)
![Adjusted frame 4 in Sky layer]({static}/images/tutorial-layers/sozi-layers-tutorial-screenshot-19.de.png)


Speichern Sie die Präsentation und betrachten Sie sie im Browser
-----------------------------------------------------------------

Der Sozi-Editor sollte die Präsentation eigentlich automatisch speichern. Falls das nicht passiert 
sein sollte, klicken Sie auf den *Save-Button* in der Werkzeugleiste über der Zeitleiste.

Öffnen Sie die Datei `tutorial-layers.de.sozi.html` in einem Browser. Angezeigt wird automatisch das
erste Einzelbild. Klicken Sie innerhalb des Browserfensters, um das nächste Bild anzuzeigen. 
(siehe auch: [Play](|filename|play.md)).

[Laden Sie die ganze Präsentation herunter]({static}/presentations/tutorial-layers/tutorial-layers.de.sozi.html)
(Rechtsklick auf den Link und dann *verlinkten Inhalt speichern unter*).
