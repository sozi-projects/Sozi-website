Title: Sozi 21.02 is available
Date: 2021-02-21
Slug: release-21.02
Lang: en
Authors: Guillaume Savaton
Summary:
    New features: custom scripts and stylesheets; export from the presentation editor.

Sozi 21.02 comes with two new features:

* Custom stylesheets and scripts can be added to a presentation without manually editing the generated HTML.
* The conversion tool (formerly known as [Sozi-export](https://github.com/sozi-projects/Sozi-export)) has been integrated into the main presentation editor.
  [Sozi-export](https://github.com/sozi-projects/Sozi-export) as a nodejs module is now considered obsolete.

Since Sozi 20.05, the editor has also undergone a modernization of its internal design.
The affected features are related to file management (loading, saving and refreshing).
In most cases, you should not notice any visible change.

Exporting Sozi presentations to other formats
---------------------------------------------

Sozi presentations can be converted to the following document types and formats:

* Portable Document Format (PDF)
* Microsoft PowerPoint (PPTX)
* Video (PNG image sequence, MPEG-4, WebM, Ogg Vorbis, Windows Media Video)

Exporting to PDF, PPTX, and PNG sequence should work out of the box. No additional software is required.

Sozi uses FFPMEG to export to other video formats. A copy of FFMPEG is included in the Windows and OS X releases.
Linux users must install FFMPEG using the package manager of their distribution.

Video export has been tested on the following operating systems:
Ubuntu 20.04 64-bit, Windows 10 64-bit.
Feedback from users of OS X will be welcome.

[Install Sozi 21.02 now!](|filename|/pages/en/install.md)
