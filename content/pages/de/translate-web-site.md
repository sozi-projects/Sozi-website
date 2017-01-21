Title: Übersetze die Web Site in Deine Muttersprache
Slug: translate-web-site
Lang: de
Status: hidden
Author: Guillaume Savaton, Andrej Barth
Translation: true

Die Web Site von Sozi ist eine statische Site und wird mit Hilfe von [Pelican](http://blog.getpelican.com/) generiert.
Sie hat keinen Online-Editor.

Die Quelldateien der Site sind Text-Dateien in einfacher [Markdown](http://daringfireball.net/projects/markdown/syntax)-Syntax.
Diese Dateien liegen im [Repository der Sozi-website auf GitHub](https://github.com/senshu/Sozi-website), im Verzeichnis
[content/](https://github.com/senshu/Sozi-website/tree/master/content).
Im Verzeichnis [content/pages/](https://github.com/senshu/Sozi-website/tree/master/content/pages) liegt die Dokumentation von Sozi.
Die jeweiligen Markdown-Sprachdateien liegen in Unterverzeichnissen &ndash; `en` für Englisch, `de` für Deutsch usw).

Wenn Du mit dem Übersetzen beginnen möchtest, dann empfehlen wir die folgende Vorgehensweise:

1. [Fork das Repository](https://github.com/senshu/Sozi-website/fork).
2. Erstelle ein Unterverzeichnis für Deine Sprache in `content/pages/`, falls dieses noch nicht existiert.
3. Finde die Seite, die Du übersetzen möchtest im `en`-Verzeichnis und kopiere sie mit dem gleichen Namen ins Verzeichnis mit Deiner Sprache.
4. Übersetze die Seite.
5. Du kannst, musst aber nicht, eine Vorschau der Seite mit einer eigenen, lokalen Pelican-Installation ansehen.
6. Wenn Du mit der Übersetzung zufrieden bist, dann `commit` und `push` Deine Änderungen in Dein GitHub Repository und sende einen `pull request` ans offizielle Sozi Repository.

Der Header der übersetzten Markdown-Dateien sollte diese Deklarationen enthalten:

* `Title`: den Titel der Seite, übersetzt in Deine Sprache.
* `Author`: Autor des Originals und Übersetzer, mit Komma getrennt.
* `Slug`: das Slug der Original-Datei, unverändert.
* `Lang`: den Sprachcode der Übersetzung, z.B. de.
* `Translation`: `true`.
