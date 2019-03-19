Title: Video und Audio in eine Präsentation einbetten
Slug: tutorial-media
Lang: de
Authors: Guillaume Savaton, Alfred Bergkemper
Status: hidden
Translation: true

Mithilfe der *Add video or audio*-Extension für InkScape lassen sich Video- und Audioinhalte in eine
SVG-Datei und damit auch in eine Sozi-Präsentation einfügen.  

Installation
------------

1. Laden Sie die Datei `Sozi-extras-media-[...].zip`
   von der Seite mit den [aktuellsten Sozi-Versionen](https://github.com/senshu/Sozi/releases/) herunter.
2. Das Zip-Archive enthält zwei Dateien: `sozi_extras_media.inx` und `sozi_extras_media.py`.
   Kopieren Sie beide in den Extensions-Ordner:
    * für Linux and OS X: `~/.config/inkscape/extensions`,
    * für Windows: `C:\Program Files\Inkscape\share\extensions`,
3. Öffnen Sie Inkscape. Im *Erweiterungen*-Menü finden Sie ein Untermenü *Sozi extras* mit dem
   Eintrag *Add video or audio*.

Gebrauch
--------

Wenn Sie ein neues Audio- oder Video-Element in eine SVG-Datei einfügen möchten, müssen Sie einige Informationen
in eine Maske eingeben:

* *Media element*: *video* oder *audio*.
* *Width*: die Breite des Elements in Pixeln.
* *Height*: die Höhe des Elements in Pixeln.
* *MIME type*: den Dateityp (z.B. `video/mp4` oder `audio/ogg`).
* *File name or URL*: Name und Ordner der Mediendatei.
* *Play automatically in Sozi frame*: setzen Sie hier ein Häkchen, damit die Mediendatei automatisch
  abgespielt wird, wenn der entsprechende Frame angezeigt wird.
* *Start playing when entering frame (id)*: die Id des Frames, bei dessen Anzeige die Mediendatei starten soll.
* *Stop playing when entering frame (id)*: die Id des Frames, bei dessen Anzeige die Mediendatei stoppen soll.

Beispiel
--------

Die nachfolgende Präsentation spielt ein Video im zweiten und eine Audio-Datei im dritten Frame.
[Download the presentation files](|filename|/presentations/tutorial-media.zip).

<iframe class="sozi" src="|filename|/presentations/tutorial-media/tutorial-media.sozi.html">
    Ihr Browser kann diesen Inhalt nicht anzeigen.
</iframe>

(Wenn das Video nicht korrekt angezeigt wird, laden Sie die Seite bitte in Firefox.)

Browser-Unterstützung
---------------------

Die Wiedergabe von Audio und Video basiert technisch gesehen auf der Nutzung von entsprechenden 
HTML5-Elementen in der SVG-Datei. Aktuelle Web-Browser unterstützen derzeit nicht alle Formate.
Mehr Informationen dazu finden Sie hier:
[Html-Unterstützung von Audio und Video (Mozilla Developer Network)](https://developer.mozilla.org/en-US/docs/HTML/Supported_media_formats).

> Zurzeit werden von Chrome (bis zur Version 73) geometrische Transformationen wie Rotation, 
> Skalierung und Verschiebungen von Video- und Audio-Elementen in SVG Dokumenten nicht unterstützt.
> Dateien werden immer in der linken oberen Ecke des Browser-Fensters angezeigt. 
> Auch Opera hat Probleme mit den Transformationen.
> Soweit bekannt funktioniert die Anzeige derzeit nur in Firefox.

