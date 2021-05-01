Title: Sozi 19.04 is available
Date: 2019-04-24
Slug: release-19.04
Lang: en
Authors: Guillaume Savaton
Summary:
    After one year, Sozi 19.04 is out with a new presenter console and performance fixes.

The first [request for a presenter mode](https://github.com/sozi-projects/Sozi/issues/211)
in Sozi was made in 2014.
At least two implementations were proposed, one by Kai Wegner as a separate
application called [catchi](https://github.com/kai-wegner/catchi),
and another by roggan87, [as a modified version of the existing Sozi player](https://github.com/sozi-projects/Sozi/pull/325).

Sozi 19.04 is a trade-off between both approaches.
It reuses some code written by roggan87, but the presenter console is kept outside
of the Sozi player.
Let's see how it works:

When Sozi saves your presentation, it creates an HTML file (e.g. `example.sozi.html`)
that contains a copy of your SVG document and the JavaScript code of the Sozi player.
In Sozi 19.04, the editor creates an additional HTML file (`example-presenter.sozi.html`)
that contains the presenter console.
To play your presentation, you now have two options:

* Open `example.sozi.html` in a web browser and play it without the presenter console like in Sozi 18.
* Open `example-presenter.sozi.html` in a web browser. This will show a presenter view with the previous, current, and next frames, navigation buttons, and notes.
  It will also open the presentation automatically in a separate window.

> Web browsers usually block pop-up windows.
> When you open a Sozi presenter HTML file for the first time, you will need to confirm
> that you accept to open the presentation in another window.
> You may also need to refresh the presenter document.

Additional changes since Sozi 18.04
-----------------------------------

* Frame titles can be organized hierarchichally in the frame list.
* In the editor, you can choose to save the presentation, or reload the SVG document, manually.
  This can help if your document is big and you don't want Sozi to become unresponsive
  when saving/reloading operations are triggered unexpectedly.
* You can now hide the controls of the embedded video and audio documents.
* A bug caused the editor to become slower and slower each time the SVG document was reloaded.
  Hopefully, this was the main cause of the performance issues that some users observed.
* A bug in the player showed a scrollbar on the left of the presentation
  when the frame list did not fit in the browser window.

[Install Sozi 19.04 now!](|filename|/pages/en/install.md)

About Sozi-export
-----------------

Sozi-export is a set of command-line tools that convert Sozi presentations to
videos or printable documents.
These tools are based on PhantomJS, a headless browser engine that is no longer
maintained.
As a consequence, Sozi-export has become unusable on several platforms.
As far as we know, there is no easy fix to make it work again in the short term.

Until this is solved, the [Docker image](https://hub.docker.com/r/escalope/inkscape-sozi)
made by Jorge J. Gomez-Sanz provides a stable environment where Sozi-export
is known to work reliably.
