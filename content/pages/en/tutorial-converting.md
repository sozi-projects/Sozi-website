Title: Converting Sozi presentations to PDF or video
Slug: tutorial-converting
Lang: en
Authors: Guillaume Savaton
Status: hidden

> Sozi-export is now considered obsolete.
> Since Sozi 21.02, the conversion tool has been integrated into the presentation editor.
>
> Documentation for this new feature will be available soon.

Sozi-export is a set of command-line tools that you can use to convert a Sozi presentation
into a PDF document, a video, or a PowerPoint presentation.
The source code is available in the [Sozi-export](https://github.com/sozi-projects/Sozi-export)
repository.
These tools are independent from the presentation editor.
They have been tested only for GNU/Linux.


Install
-------

Sozi-export depends on the following software that you must install separately:

* [pdfjam](http://www2.warwick.ac.uk/fac/sci/statistics/staff/academic-research/firth/software/pdfjam), a shell script for manipulating PDF files.
* [libav](https://libav.org), tools and library to manipulate multimedia files.

Users of Debian-based distributions can install the *texlive-extra-utils* and *libav-tools* packages.

    :::bash
    apt-get install texlive-extra-utils libav-tools

Sozi-export is provided as an NPM package.
Install [node.js](https://nodejs.org/) 0.10 or later
(Linux users can use the [NodeSource distributions](https://github.com/nodesource/distributions)),
then:

    :::bash
    npm install -g sozi-export


Convert a Sozi presentation to PDF
----------------------------------

    :::bash
    sozi-to-pdf [options] presentation.sozi.html

Options:

* `-h`, `--help` Usage information
* `-o`, `--output <file>` Output file
* `-W`, `--width <number>` Page width (defaults to 29.7)
* `-H`, `--height <number>` Page height (defaults to 21)
* `-r`, `--resolution <number>` Pixels per width/height unit (defaults to 72)
* `-p`, `--paper <size>` A LaTeX paper size (defaults to 'a4paper')
* `-P`, `--portrait` Set the paper orientation to portrait (disabled by default)
* `-c`, `--png-compression <number>` Compression level of the generated PNG files (0 to 100, higher means smaller files, defaults to 100)
* `-i`, `--include <list>` Frames to include (defaults to 'all')
* `-x`, `--exclude <list>` Frames to exclude (defaults to 'none')

The width, height and resolution options specify the geometry of the browser window
where the presentation is rendered.
The default values are suitable for generating a printable document with A4 page format.
The paper and portrait options specify the page format to use in the final PDF document.

The `include` option is always applied before the `exclude` option.
Frames lists have the following syntax:

* `all` selects all frames in the presentation.
* `none` selects no frame.
* A comma-separated list of frame numbers or ranges.
  A range is in the form `first:last` or `first:second:last` where `first`, `second` and `last` are frame numbers.

For instance: `-i 2,4:6,10:12:18` will include frames 2, 4, 5, 6, 10, 12, 14, 16, 18.

Convert a Sozi presentation to video
------------------------------------

    :::bash
    sozi-to-video [options] presentation.sozi.html

Options:

* `-h`, `--help` Usage information
* `-o`, `--output <file>` Output file
* `-W`, `--width <number>` Video width, in pixels (defaults to 1024)
* `-H`, `--height <number>` Video height (defaults to 768)
* `-b`, `--bit-rate <number>` Video bit rate (defaults to 2M)
* `-c`, `--png-compression <number>` Compression level of the generated PNG files (0 to 100, higher means smaller files, defaults to 100)

Convert a Sozi presentation to a PowerPoint presentation
--------------------------------------------------------

This tool creates a PowerPoint document with the PPTX format.
It supports a subset of the options for `sozi-to-pdf`.

    :::bash
    sozi-to-pptx [options] presentation.sozi.html

Options:

* `-h`, `--help` Usage information
* `-o`, `--output <file>` Output file
* `-W`, `--width <number>` Page width (defaults to 29.7)
* `-H`, `--height <number>` Page height (defaults to 21)
* `-r`, `--resolution <number>` Pixels per width/height unit (defaults to 72)
* `-c`, `--png-compression <number>` Compression level of the generated PNG files (0 to 100, higher means smaller files, defaults to 100)
* `-i`, `--include <list>` Frames to include (defaults to 'all')
* `-x`, `--exclude <list>` Frames to exclude (defaults to 'none')

Known issues and limitations
----------------------------

These tools uses a *headless* web browser for rendering.
[PhantomJS](http://phantomjs.org) and [SlimerJS](https://slimerjs.org/) both have benefits and limitations:

* PhantomJS can render a web page to a PDF document, which preserves the vector graphics and text.
  However, PhantomJS 1.9.19 fails to render the SVG content of a Sozi presentation.
* SlimerJS renders SVG content correctly but it does not support the PDF format.

Currently, the PDF export tool renders each frame to a PNG image and joins them into a PDF document.
