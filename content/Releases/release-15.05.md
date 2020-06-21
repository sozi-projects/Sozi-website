Title: Sozi 15.05 is available for testers and translators
Date: 2015-05-15
Slug: release-15.05
Lang: en
Authors: Guillaume Savaton
Summary:
    This is the first official preview release of Sozi 15.
    Though it can no longer be considered a prototype, it is still primarily intended for testers.

A new presentation editor has been under development since the beginning of 2014.
Development went at a slow pace and only [an early prototype was
officially announced in October 2014](|filename|release-14.10.md).
In 2015, it was followed by a long series of fixes and improvements.
Several users started to use it daily, found issues and helped me fix them.

Sozi 15.05 is the latest in this series.
I believe it is the right time to release it officially so that more people can try it,
translate it, package it and report issues left unnoticed.

What's new in Sozi 15?
----------------------

Until version 13.11, the editor for Sozi was provided as an Inkscape extension.
The extension system of Inkscape had not been designed for this kind of use,
so Sozi was not well integrated in Inkscape and the overall user experience was poor.
Moreover, the editor depended on several other frameworks and libraries
(Python 2.7, GTK2, PyGTK) that needed to be manually installed in Windows and OS X.
Some of them are now deprecated.
For all these reasons, Sozi has been almost completely rewritten with the following concerns:

* It is no longer an Inkscape extension.  It is a standalone application that can be used with any SVG editor.
* Its user interface allows to edit frames and manage layers visually.
* It does not modify the original SVG document but saves the presentation in a separate HTML file.
* It is easier to install in Windows and OS X.
* It is based on web technologies (HTML, JavaScript, SVG).

A new user interface
--------------------

Frames are created and modified using three panes:

* The *timeline* pane (bottom) features a grid where each row represents a layer and each column
  represents a frame. Select layers and frames using the mouse.
  Use the `Shift` and `Ctrl` keys for multiple selections.
* The *preview* pane (top left) contains a view of the current frame.
  Use the mouse to move, zoom or rotate the camera in the selected layers,
  or define a clipping rectangle.
* The *properties* pane (top right) contains a form where you can modify various
  properties of frames and transitions.

It is no longer required to draw rectangles to delimit frames but it can help in some cases.
Tutorials on this topic will be published soon.

The editor saves the presentation automatically each time the window loses focus
and before quitting.
If you modify the SVG document while Sozi is running, it will be reloaded automatically when
Sozi gets the focus again.
If saving and reloading do not happen automatically, you can still use the *Save* and *Reload*
buttons.

A new file format
-----------------

If you have used earlier versions of Sozi, you will notice that the new editor
stores the presentation in separate files along your SVG document.
For instance, if your original SVG document is `my_presentation.svg`, Sozi 15 will create
two files:

* `my_presentation.sozi.json` stores the presentation data. It is used internally by the editor.
* `my_presentation.sozi.html` is the resulting Sozi presentation. Open it in a web browser to play it.

Technically, the HTML file contains a copy of your SVG document, a copy of the presentation data,
and the Sozi player software.
It is a standalone document: if you want to share a presentation, you do not need to give the
SVG and JSON files.

Sozi 15 can import presentations made with Sozi 13.

Known issues
------------

The current version of the new editor does not display linked images.
SVG documents that contain embedded images are displayed correctly
but they can be slower to load if they contain a lot of big images.

Try Sozi 15 now!
----------------

Sozi 15 can be run either as a standalone desktop application, or as a hosted web application.

* [Download the desktop version](https://github.com/sozi-projects/Sozi/releases/tag/15.05-preview).
  Choose the zip file corresponding to your platform, extract it and run the `Sozi` executable.
* [Try the hosted web application](/demo) (requires a Google Drive account for saving documents).

Contribute
----------

[Report issues](https://github.com/sozi-projects/Sozi/issues) if you find bugs
or want to suggest improvements.
Please indicate clearly that you are using Sozi 15.

[Translate Sozi](|filename|/pages/en/translate-editor.md) to your native language.
