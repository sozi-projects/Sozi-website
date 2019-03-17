Title: Einzelbild URLs und Hyperlinks
Slug: tutorial-links
Lang: de
Authors: Guillaume Savaton, Alfred Bergkemper
Status: hidden
Translation: true

In diesem Tutorial lernen Sie, wie man Hyperlinks in Sozi Dokumente einfügt und wie man
Einzelbilder direkt verlinkt (Querverweise).

Herunterladen und Öffnen der Beispiel-Datei
-------------------------------------------

Dieses Tutorial basiert auf einer SVG-Datei, die die einzelnen Elemente unserer Präsentation enthält.
[Bitte laden Sie die Basis-SVG-Datei](|filename|/presentations/tutorial-links/tutorial-links.de.svg)
(Rechtsklick auf den Link und dann *verlinkten Inhalt speichern unter*).

Die Datei wurde mit [Inkscape](https://inkscape.org) erstellt.
Wir gehen davon aus, dass Inkscape bereits installiert ist.  

Erzeugen Sie die Einzelbilder der Präsentation
----------------------------------------------

Öffnen Sie `tutorial-links.de.svg` im Sozi-Editor.

![Base document in Sozi](|filename|/images/tutorial-links/sozi-links-tutorial-screenshot-01.de.png)

Erzeugen Sie fünf Einzelbilder (Frames), wie in den folgenden Screenshots gezeigt:

![Frame 1 (Home)](|filename|/images/tutorial-links/sozi-links-tutorial-screenshot-02.de.png)
![Frame 2 (Oben links)](|filename|/images/tutorial-links/sozi-links-tutorial-screenshot-03.de.png)
![Frame 3 (Oben rechts)](|filename|/images/tutorial-links/sozi-links-tutorial-screenshot-04.de.png)
![Frame 4 (Unten rechts)](|filename|/images/tutorial-links/sozi-links-tutorial-screenshot-05.de.png)
![Frame 5 (Unten links)](|filename|/images/tutorial-links/sozi-links-tutorial-screenshot-06.de.png)

Ändern Sie **die IDs** der Einzelbilder wie folgt (Keine Großbuchstaben, keine Leerzeichen):

<table>
    <tr>
        <th>Bild Nr.</th>
        <th>Titel</th>
        <th>ID</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Home</td>
        <td>home</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Oben links</td>
        <td>oben-links</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Oben rechts</td>
        <td>oben-rechts</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Unten rechts</td>
        <td>unten-rechts</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Unten links</td>
        <td>unten-links</td>
    </tr>
</table>

Sie können die Präsentation bereits in einem Web-Browser öffen, um die korrekten Bezeichnungen zu kontrollieren.  

URLs der Einzelbilder
---------------------

Wenn eine Sozi-Präsentation im Browser geöffnet wird, ändert sich die Adresszeile bei jedem neuen Einzelbild.

![Frame URL in the address bar of a web browser](|filename|/images/tutorial-links/sozi-links-tutorial-screenshot-07.de.png)

Im Beispiel zeigt die Adresszeile den URL:

    file://.../tutorial-links.sozi.html#oben-rechts

Wenn die Präsentation von einem Web-Server geladen wird, wird das erste Element des URLs `http` oder `https`
anstelle von `file`. Im URL oben wird der HTML-Name gefolgt von einer Doppelraute (Hash-Zeichen), dann kommt die
ID des gerade angezeigten Einzelbildes (`oben-rechts`).

Dadurch ist es möglich, ein Einzelbild einer Online-Präsentation direkt zu verlinken.  

Hyperlinks in einer Sozi-Präsentation
------------------------------------------

> Der SVG-Standard unterstützt Hyperlinks von Natur aus.
> Sozi bietet daher keine eigene Option, Links in Ihre Präsentation einzufügen.
> Wenn Sie Querverweise möchten, müssen Sie die Links in Inkscape oder einem
> anderen SVG-Editor einfügen.

Öffnen Sie die Datei `tutorial-links.de.svg` in Inkscape.
Ein Rechtsklick auf den großen Pfeil, der in die linke obere Ecke zeigt, öffnet
das Kontextmenü. Wählen Sie *Verknüpfung erstellen*.

![Creating a link in Inkscape](|filename|/images/tutorial-links/sozi-links-tutorial-screenshot-08.de.png)

Dadurch öffnet sich das Andockfenster *Objekteigenschaften*, in dem Sie den Link eintragen können.

Um zum Einzelbild *Oben links* zu verlinken, tragen Sie einfach `#oben-links` in die Zeile `Href:` ein:

![Eintrag des href-Attributs eines Links](|filename|/images/tutorial-links/sozi-links-tutorial-screenshot-09.de.png)

Verfahren Sie sinngemäß mit den anderen Einzelbildern: erzeugen Sie für jeden Pfeil einen Link zur
entsprechenden Einzelbild-ID. Zum Schluss wählen Sie den blauen Kreis und erzeugen dort einen Link nach #home.  

Aktualisieren Sie die Präsentation und spielen Sie sie im Browser
-----------------------------------------------------------------

*Speichern* Sie die SVG-Datei in InkScape.
Wechseln Sie zum Sozi-Fenster, um dort die aktualisierte SVG-Datei neu einzulesen (geschieht automatisch).

Öffnen Sie die Datei `tutorial-links.sozi.de.html` mit Ihrem Lieblingsbrowser.
Es wird automatisch das erste Einzelbild angezeigt.
Klicken Sie auf den weißen Hintergrund um zum nächsten Einzelbild zu gelangen
(Siehe auch: [Eine Präsentation abspielen](|filename|play.md))
oder klicken Sie auf einen der Pfeile, um direkt zum entsprechenden
Einzelbild zu springen.

[Laden Sie hier die fertige Präsentation herunter](|filename|/presentations/tutorial-links/tutorial-links.de.sozi.html)
(Rechtsklick auf den Link und dann *verlinkten Inhalt speichern unter*).
