Title: Deine erste Präsentation
Slug: tutorial-first
Lang: de
Authors: Guillaume Savaton, Andrej Barth
Translation: true
Status: hidden

> An updated version of this tutorial is available in the [Sozi Guide](http://sozi.guide).
> Follow these links to read it: [in English](http://sozi.guide/en/first-presentation.html),
> or [in French](http://sozi.guide/fr/premiere-presentation.html).
>
> The [Sozi Guide](http://sozi.guide) is a new user manual for Sozi, currently in the process of writing and translating.
> You can help me dedicate some time to work on this book by
> [participating in the ongoing fundraising campaign](https://gofund.me/2f2b11db)
> or by [donating via another service](|filename|donate.md).

Dieses Tutorial beschreibt die wichtigsten Features von Sozi.
Du wirst lernen, die einzelnen Bilder zu erstellen und die Präsentation in einem Browser abzuspielen.


Lade Deine erste Beispiel-Datei herunter
----------------------------------------

Diese Einführung nutzt eine einfache svg-Datei, die die Zeichnung zu unserer Präsentation enthält.
[Download first-presentation.svg]({static}/presentations/tutorial-first/first-presentation.svg)
(Rechts-Klick und *Ziel speichern unter…*).
Öffne die Datei mit dem Sozi-Editor.

![Öffne die svg-Datei mit dem Sozi-Editor]({static}/images/tutorial-first/first-presentation-screenshot-01.de.png)


Erstelle das erste Bild Deiner Präsentation
-------------------------------------------

Klicke auf *+* und erstelle ein neues Bild.

Wir wollen das erste Bild über der lila Form mit der Nummer 1 zentrieren.
Du kannst den Seitentitel im *Titel*-Feld auf der rechten Seite anpassen.
Dann, in der Vorschau links:

* positioniere die Kamera, indem Du die Maus bei gedrückter primärer (linker) Maustaste bewegst.
* zoome, indem Du die Maus bei gedrückter Maustaste und gedrückter *Alt*-Taste auf der Tastatur bewegst.

![Das erste Bild der Präsentation]({static}/images/tutorial-first/first-presentation-screenshot-02.de.png)


Erstelle drei weitere Bilder
----------------------------

Lege drei neue Bilder an.
Jedes Bild erscheint als eine neue Spalte in der Zeitleiste unten.
Du kannst auf die Nummer oder den Titel des Bildes klicken, um es auszuwählen.

Gib jedem Bild einen Title und stelle die Kamera richtig ein,
für die orangene (2), die gelbe (3), und die blaue Form (4).
Zum Rotieren der Kamera bewegst Du die Mause bei gedrückter Maustaste und gedrückter *Shift*-Taste auf der Tastatur.

![Das zweite Bild der Präsentation]({static}/images/tutorial-first/first-presentation-screenshot-03.de.png)


Speichere die Präsentation
--------------------------

Der Editor speichert die Präsentation selbständig.
Unabhängig davon kannst Du jederzeit selbst den Button *Präsentation speichern* in der Werkzeugleiste klicken.

Sozi ändert nicht die svg-Datei.
Beim Speichern aktualisiert der Editor diese beiden Dateien:

* `first-presentation.sozi.json` enthält die Daten zur Präsentation, wird vom Editor genutzt. Sie muss im gleichen Verzeichnis wie das svg-Dokument liegen und den gleichen Namen haben.
* `first-presentation.sozi.html` enthält die eigentliche Präsentation. Du kannst diese Datei im Browser aufrufen, um die Präsentation abzuspielen.

Willst Du die Präsentation an andere Leute weitergeben, dann brauchst Du ihnen nur die Datei mit der Endung `.sozi.html` zu geben.


Zeige die Präsentation in Web-Browser
-------------------------------------

Rufe `first-presentation.sozi.html` in einem Browser auf.
Die Kamera wird automatisch auf das erste Bild gerichtet sein.
Klicke mit der Maus in das Fenster, um zum nächsten Bild weiterzugehen.
(siehe auch: [Zeigen](|filename|play.md)).

[Download der kompletten Präsentation]({static}/presentations/tutorial-first/first-presentation.sozi.html)
(Rechts-Klick mit der Maus und *Ziel speichern unter…*).
