Title: Sozi 17.02 is available
Date: 2017-03-25
Slug: release-17.02
Lang: en
Authors: Guillaume Savaton
Summary:
    Sozi 17.02 is considered as the new stable release after Sozi 16.02.
    It adds a few features, fixes several issues and adds new translations.

This is mainly a bugfix release that adds only one new feature:
while playing a presentation, you can press the "." (dot) key to switch to a blank frame.

The notion of *reference element* for a frame was confusing.
It is still used internally but is now hidden from the main user interface. Additionally, users can define an *outline element* that allows to adjust the selected layers to a given SVG element (e.g. a rectangle).
The user interface is very similar to the previous version, but its behavior is slightly different and hopefully more intuitive and less error-prone.

Under the hood, Sozi is now based on [electron](http://electron.atom.io/), which helped solve several issues.

Sozi 17.02 is available in 14 languages including Russian and Italian.
Unfortunately, most translations are not up to date, so if you don't speak English, French or Esperanto,
you are likely to see some non-translated English text in the user interface of the editor.

If you want to help translate Sozi to your language, you will find [instructions for translators](|filename|/pages/en/translate-editor.md) on this site.
Please [open an issue](https://github.com/sozi-projects/Sozi/issues) if you want us to add a new
completed translation file or update an existing one.


Use Sozi 17.02 now!
-------------------

Sozi 17 can be run either as a standalone desktop application, or as a hosted web application.

* [Download the desktop version](https://github.com/sozi-projects/Sozi/releases/tag/17.02).
  Choose the zip file corresponding to your platform, extract it and run the `Sozi` executable.
* [Try the hosted web application](/demo) (requires a Google Drive account for saving documents).

Contribute
----------

[Report issues](https://github.com/sozi-projects/Sozi/issues) if you find bugs
or want to suggest improvements.
