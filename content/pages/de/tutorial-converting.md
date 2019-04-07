Title: Sozi Präsentationen in PDF oder Video konvertieren
Slug: tutorial-converting
Lang: de
Authors: Guillaume Savaton, Alfred Bergkemper
Status: hidden
Translation: true

> Diese Übersetzung beruht nicht auf praktischen Erfahrungen und kann daher fehlerhaft sein.
Im Zweifelsfall vergleichen Sie bitte die Originalseite.

Sozi-Export besteht aus einer Reihe von Kommandozeilen-Tools, mit denen man eine Sozi-Präsentation
in eine PDF-Datei, ein Video oder in das Powerpoint-Format konvertieren kann.
Der Quellcode liegt in der [Sozi-export](https://github.com/senshu/Sozi-export)
Repository.

Diese Tools arbeiten unabhängig vom Präsentations-Editor und sind nur unter GNU/Linux getestet.



Installation
------------

Sozi-Export basiert auf folgenden Programmpaketen, die separat installiert werden müssen:

* [pdfjam](http://www2.warwick.ac.uk/fac/sci/statistics/staff/academic-research/firth/software/pdfjam), ein Shell-Script zur Bearbeitung von PDF-Dateien.
* [libav](https://libav.org), Tools und Bibliothek zur Bearbeitung von Multimedia-Dateien.

Nutzer von Debian-basierten Distributionen können die *texlive-extra-utils* und *libav-tools* Pakete installieren.

    :::bash
    apt-get install texlive-extra-utils libav-tools

Sozi-export wird als NPM-Paket bereitgestellt.
Installieren Sie [node.js](https://nodejs.org/) 0.10 oder jünger
(Linux-Nutzer können die [NodeSource Distributionen](https://github.com/nodesource/distributions)) nutzen,
und dann:

    :::bash
    npm install -g sozi-export


Eine Sozi-Präsentation nach PDF konvertieren
--------------------------------------------

    :::bash
    sozi-to-pdf [options] presentation.sozi.html

Options:

* `-h`, `--help` zeigt Hilfe zum Gebrauch an
* `-o`, `--output <Datei>` Output-Datei
* `-W`, `--width <Zahl>` Papierbreite (voreingestellt 29.7)
* `-H`, `--height <Zahl>` Papierhöhe (voreingestellt 21)
* `-r`, `--resolution <Zahl>` Auflösung (Pixels/Inch) (voreingestellt ist 72)
* `-p`, `--paper <size>` A LaTeX paper size (voreingestellt ist 'a4paper')
* `-P`, `--portrait` Setzt die Seitenausrichtung auf 'hochkant' (voreingestellt ist 'quer')
* `-i`, `--include <list>` Liste der einzubeziehenden Frames (voreingestellt ist 'alle')
* `-x`, `--exclude <list>` Liste der auszuschließenden Frames (voreingestellt ist 'keiner')

Breite, Höhe und Auflösung definieren das Browserfenster, in dem die Präsentation
abgespielt wird.
Die voreingestellten Werte eignen sich zur Erzeugung einer druckbaren A4-Seite.
Die Papier- und Ausrichtungsoptionen beziehen sich auf das erzeugte PDF-Dokument.

Die `Include`-Option wird immer *vor* der `Exclude`-Option angewandt.
Frame-Listen haben folgende Syntax:

* `all` wählt *alle* Frames der Präsentation aus.
* `none` wählt *keinen* Frame aus.
* Eine Komma-separierte Liste von Frame-Nummern oder -bereichen.
  Ein Bereich hat die Form `erster:letzter` oder `erster:zweiter:letzter`
  wobei `letzter`, `zweiter` und `last` Frame-Nummern sind.

Zum Beispiel: `-i 2,4:6,10:12:18` bezieht die Frames 2, 4, 5, 6, 10, 12, 14, 16, 18 ein.

Eine Sozi-Präsentation nach Video konvertieren
----------------------------------------------

    :::bash
    sozi-to-video [options] presentation.sozi.html

Options:

* `-h`, `--help` zeigt Hilfe zum Gebrauch an
* `-o`, `--output <Datei>` Output-Datei
* `-W`, `--width <Zahl>` Video-Breite in Pixeln (voreingestellt ist 1024)
* `-H`, `--height <Zahl>` Video-Höhe (voreingestellt ist 768)
* `-b`, `--bit-rate <Zahl>` Video-Bitrate (voreingestellt ist 2M)


Eine Sozi-Präsentation in eine PowerPoint-Präsentation konvertieren
-------------------------------------------------------------------

Dieses Tool erzeugt eine PowerPoint-Datei im PPTX-Format.
Es unterstützt eine Teilmenge der `sozi-to-pdf`-Optionen.

    :::bash
    sozi-to-pptx [options] presentation.sozi.html

Options:

* `-h`, `--help` zeigt Hilfe zum Gebrauch an
* `-o`, `--output <Datei>` Output-Datei
* `-W`, `--width <Zahl>` Papierbreite (voreingestellt 29.7)
* `-H`, `--height <Zahl>` Papierhöhe (voreingestellt 21)
* `-r`, `--resolution <Zahl>` Auflösung (Pixels/Inch) (voreingestellt ist 72)
* `-i`, `--include <list>` Liste der einzubeziehenden Frames (voreingestellt ist 'alle')
* `-x`, `--exclude <list>` Liste der auszuschließenden Frames (voreingestellt ist 'keiner')


Bekannte Probleme und Einschränkungen
-------------------------------------

Diese Tools nutzen einen *Headless* Browser für die Darstellung, d.h. die Oberfläche ist nicht sichtbar.
[PhantomJS](http://phantomjs.org) und [SlimerJS](https://slimerjs.org/) haben beide Vor- und Nachteile:

* PhantomJS behält bei der Übersetzung ins PDF-Format Text und Vektor-Grafiken bei.
  PhantomJS 1.9.19 scheitert allerdings bei der Übersetzung von SVG-Inhalt einer Sozi-Präsentation.
* SlimerJS übersetzt SVG-Inhalt korrekt, unterstützt aber das PDF-Format nicht.

Zurzeit übersetzt das PDF-Export-Tool jeden Frame in ein PNG-Bild und fügt diese zu einer PDF-Datei zusammen.
