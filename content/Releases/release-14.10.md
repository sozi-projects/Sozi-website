Title: A preview of Sozi 14 is available for testers
Date: 2014-10-11
Slug: release-14.10
Lang: en
Authors: Guillaume Savaton
Summary:
    The new editor for Sozi has been under development for several months.
    Though it is not ready for daily use, you can try it now and tell me what you think.

Sozi 14 was officially announced last February.
As the version number suggests, it was planned to be released in 2014.
So I believe it is time to ship, at least, a preview of the new editor
before the end of the year.

Until version 13.11, the editor for Sozi was provided as an Inkscape extension.
The extension system of Inkscape had not been designed for this kind of use,
so Sozi was not well integrated in Inkscape and the overall user experience was poor.
Moreover, the editor depended on several other frameworks and libraries
(Python 2.7, GTK2, PyGTK) that needed to be manually installed in Windows and OS X.
Some of them are now deprecated.
For all these reasons, I decided that it would be a waste of time to try
to improve this editor again, and I started writing a new one from scratch.
The editor for Sozi 14 has been developed with the following concerns:

* It is no longer an Inkscape extension, and is not tied to a specific SVG editor.
* Its user interface includes a preview of the presentation rather than only a form.
* For a given frame, you can select the visible area in each layer without drawing rectangles.
* It does not modify the original SVG document but saves the presentation in a separate file.
* It is easier to install in Windows and OS X.
* It is based on web technologies (HTML, JavaScript, SVG).

A new user interface
--------------------

Frames are created and modified using three panes:

* The *timeline* pane (bottom) features a grid where each row represents a layer and each column
  represents a frame. Select layers and frames using the mouse.
  Use the `Shift` and `Control` keys for multiple selections.
* The *preview* pane (top left) contains a view of the current frame.
  Use the mouse to modify the geometry of the selected layers in the selected frame.
  Drag using the left button, zoom using the wheel, rotate using the wheel and the `Shift` key.
* The *properties* pane (top right) contains a form where you can modify various
  properties of frames and transitions.

It is no longer required to draw rectangles to delimit frames
but it can help in some cases.
Tutorials on this topic will be published soon.

There is no *Save* button.
The editor saves the current document automatically, each time the window loses focus,
and before quitting.
If you modify the SVG document while Sozi is running, it will be reloaded automatically when
Sozi gets the focus again.

A new file format
-----------------

If you have used earlier versions of Sozi, you will notice that the new editor
stores the presentation in a new format.
For instance, if your original SVG document is `my_presentation.svg`, Sozi 14 will create
two files:

* `my_presentation.sozi.json` stores the presentation data. It is used internally by the editor.
* `my_presentation.sozi.html` is the resulting Sozi presentation. Open it in a web browser to play it.

Technically, the HTML file contains a copy of your SVG document, a copy of the presentation data,
and the Sozi player software.
It is a standalone document: if you want to share a presentation, you do not need to give the
SVG and JSON files.

Sozi 14 can import presentations made with Sozi 13.

> If you have already imported a document in Sozi 14, and if you
> modify it later using Sozi 13, you will need to remove the JSON file to
> restart the import process.

Known issues
------------

The current version of the new editor does not display linked images.
SVG documents that contain embedded images are displayed correctly.

The desktop editor is based on the official build of [node-webkit](https://github.com/rogerwang/node-webkit).
It is known to fail:

* [in GNU/Linux distributions with an old version of glibc](https://github.com/rogerwang/node-webkit/issues/1366),
* [in recent distributions that do not provide libudev.so.0](https://github.com/rogerwang/node-webkit/wiki/The-solution-of-lacking-libudev.so.0).

For the second issue, a quick fix consists in creating a symbolic link like this:

    :::bash
    # Debian, Ubuntu and their derivatives, 32-bit
    sudo ln -sf /lib/i386-linux-gnu/libudev.so.1 /lib/i386-linux-gnu/libudev.so.0
    # Debian, Ubuntu and their derivatives, 64-bit
    sudo ln -sf /lib/x86_64-linux-gnu/libudev.so.1 /lib/x86_64-linux-gnu/libudev.so.0
    # Others 32-bit
    sudo ln -sf /usr/lib/libudev.so.1 /usr/lib/i386-linux-gnu/libudev.so.0
    # Others 64-bit
    sudo ln -sf /usr/lib64/libudev.so.1 /usr/lib64/i386-linux-gnu/libudev.so.0
    
Sozi 14 does not support localization yet.

The following features will be added later, but they will be provided as optional extensions:

* frame numbers,
* table of contents,
* frame URLs.

Try Sozi 14 now!
----------------

A very early preview of the new editor is available for testers.
It can be run either as a standalone desktop application, or as a hosted web application.

> Please note that this software is not ready for production use.
> Use it at your own risk.

* [Download the desktop version](https://drive.google.com/folderview?id=0ByRUreHgekjMemhONHd4TGY4V3M&usp=sharing) (choose the zip file corresponding
to your platform and click the "Download" button at the top of the screen).
* [Try the hosted web application](/demo) (requires a Google Drive account for saving documents).

Contribute
----------

[Report issues](https://github.com/sozi-projects/Sozi/issues) if you find bugs
or want to suggest improvements.
Please indicate clearly that you are using Sozi 14.

Help is needed to implement additional cloud storage backends in the hosted app.
Google Drive is provided as a proof of concept, but we must support alternatives.
The source code is available in the `dev` branch of the repository.
See the files named `sozi.editor.backend.*.js` [in the `js` folder](https://github.com/sozi-projects/Sozi/tree/dev/js).
