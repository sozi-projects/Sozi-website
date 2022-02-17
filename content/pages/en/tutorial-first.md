Title: Your first presentation
Slug: tutorial-first
Lang: en
Authors: Guillaume Savaton
Status: hidden


> An updated version of this tutorial is available in the [Sozi Guide](http://sozi.guide).
> Follow this link to read it: [First presentation: show off your Big Ideas](http://sozi.guide/en/first-presentation.html).
>
> The [Sozi Guide](http://sozi.guide) is a new user manual for Sozi, currently in the process of writing and translating.
> You can help me dedicate some time to work on this book by
> [participating in the ongoing fundraising campaign](https://gofund.me/2f2b11db)
> or by [donating via another service](|filename|donate.md).

This tutorial will introduce the basic features of Sozi.
You will learn how to create frames and play the presentation in a web browser.


Download and open the base document
-----------------------------------

This tutorial is based on a simple SVG document that contains the drawing elements of our presentation.
[Download the base SVG document]({static}/presentations/tutorial-first/first-presentation.svg)
(Right-click on the link and choose *Save link target as*).
Open it with the Sozi presentation editor.

![Open the SVG document with the presentation editor]({static}/images/tutorial-first/first-presentation-screenshot-01.en.png)


Create the first frame of your presentation
-------------------------------------------

Press the button *+* to create a new frame.

We want to center the first frame on the purple shape with the number 1.
You can modify its title by editing the *Title* field in the right pane.
Then, in the preview pane:

* Position the camera by moving the mouse while holding the left button.
* Zoom by moving the mouse while holding the left button and the *Alt* key of the keyboard.

![The first frame of the presentation]({static}/images/tutorial-first/first-presentation-screenshot-02.en.png)


Create three other frames
-------------------------

Add three new frames.
Each is represented by a column in the timeline (bottom pane).
You can click on the number or the title of a frame to select it.

Set a title for each frame and move the camera in order to show successively:
the orange shape (2), the yellow shape (3), and the blue shape (4).
To rotate, move the mouse while holding the left button and the *Shift* key.

![The second frame of the presentation]({static}/images/tutorial-first/first-presentation-screenshot-03.en.png)


Save the presentation
---------------------

The editor should save your presentation automatically.
If it does not, you can still press the *Save* button in the tool bar.

Sozi does not alter the original SVG document.
When saving, the editor updates the following two files:

* `first-presentation.sozi.json` contains the presentation data. This file is used
  by the presentation editor. It must reside in the same folder as the SVG document and must have the same name.
* `first-presentation.sozi.html` contains the complete presentation. You can display it in a web browser
  to play the presentation.

If you want to share a presentation with other people, you only need to give them
the file with the extension `.sozi.html`.


Play the presentation in a web browser
--------------------------------------

Open the file `first-presentation.sozi.html` in a web browser.
The camera is automatically set to the first frame of the presentation.
Click inside the browser window to move to the next frame.
(see also: [Play](|filename|play.md)).

[Download the complete presentation]({static}/presentations/tutorial-first/first-presentation.sozi.html)
(Right-click on the link and choose *Save link target as*).
