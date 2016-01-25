Title: Embedding video and audio
Slug: tutorial-media
Lang: en
Author: Guillaume Savaton
Status: hidden

You can insert video and audio into a Sozi presentation,
or even into any SVG document, using the *Add video or audio* extension for Inkscape.

Installing
----------

1. Download the `Sozi-extras-media-[...].zip`
   from the [latest release of Sozi](https://github.com/senshu/Sozi/releases/).
2. The zip archive contains two files: `sozi_extras_media.inx` and `sozi_extras_media.py`.
   Extract them to the Inkscape extensions folder:
    * for Linux and OS X: `~/.config/inkscape/extensions`,
    * for Windows: `C:\Program Files\Inkscape\share\extensions`,
3. Open Inkscape. In the *Extensions* menu, you should find a *Sozi extras* submenu with the item *Add video or audio*.

Using
-----

When adding a new audio or video element to an SVG document, you are asked to provide the following
information:

* *Media element*: *video* or *audio*.
* *Width*: the width of the element, in pixels.
* *Height*: the height of the element, in pixels.
* *MIME type*: the type of the media file (e.g. `video/mp4` or `audio/ogg`).
* *File name or URL*: the location of the media file.
* *Play automatically in Sozi frame*: check the box to start playing automatically when a Sozi presentation
  enters a given frame.
* *Start playing when entering frame (id)*: the Id of the frame where the media should start playing automatically.
* *Stop playing when entering frame (id)*: the Id of the frame where the media should stop playing automatically.

Browser support
---------------

Technically, this feature relies on the HTML5 `<video>` and `<audio>`
elements that can be embedded into SVG documents.
Web browsers do not support the same set of media formats.
See the follwing page for more information:
[Media formats supported by the HTML audio and video elements (Mozilla Developer Network)](https://developer.mozilla.org/en-US/docs/HTML/Supported_media_formats).

> Currently, Chrome (as of version 33) does not apply geometrical transformations
> (rotation, scaling, translation) to video elements embedded in SVG documents.
> Videos will always show in the top-left corner of the browser window.
> As far as we know, only Firefox handles videos correctly.
