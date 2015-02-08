Title: Frequently Asked Questions and Troubleshooting
Slug: faq
Lang: en
Author: Guillaume Savaton
Status: hidden

How do I set a background color?
--------------------------------

Inkscape allows to set a background color in the *document properties* dialog.
Unfortunately, the chosen color is only visible in Inkscape and in images exported from your document.
It is ignored by web browsers.

To set a background color that will show in a web browser, you can use the
XML editor provided by Inkscape.
Select the root `<svg:svg>` element, add an `<svg:style>` child element and a text node
inside like in the following screenshot:

![Setting a background color in Inkscape](|filename|/images/faq/background.png)

> Replace `rgb(255, 200, 255)` with your preferred [CSS color](https://developer.mozilla.org/en/docs/Web/CSS/color_value).

If you prefer to use a text editor, open your SVG document and add the following
element as a child of the root `<svg>` element:

    :::xml
    <style>
        svg {
            background: rgb(255, 200, 255);
        }
    <style>


Some graphics do not render correctly when playing my Sozi presentation
-----------------------------------------------------------------------

Several users have reported issues when their SVG document contains
*flowed text*, i.e. text that fits automatically to a given shape (a rectangle in Inkscape).
This feature is currently not stable in the SVG standard.
The Inkscape wiki provides [explanations on this subject](http://wiki.inkscape.org/wiki/index.php/FAQ#What_about_flowed_text.3F)
with the following warning:

> [...] you should not use flowed text in documents that you intend to use outside of Inkscape.

More generally, Sozi is not responsible for rendering your document on the screen.
This is the job of your web browser.
Sozi only handles the *presentation* logic: applying geometric transformations to
the layers of your document, controlling the animation, reacting to user input.
If you find that some graphics are not rendered correctly,
the issue is likely to come from either your SVG editor or your web browser.

Please do not send us bug reports on this topic unless you have strong
reasons to believe that the bug is in Sozi.
If unsure, you can ask for advice on [the Sozi users discussion group](http://groups.google.com/group/sozi-users).


Inkscape reports a syntax error when running Sozi
-------------------------------------------------

This problem has been reported mainly by Windows users.
When running Sozi from the Inkscape extensions menu, a dialog shows the following error:

    :::pytb
    Traceback (most recent call last):
      File "sozi.py", line 30, in from sozi.document import *
      File "C:\Program Files (x86)\Inkscape\share\extensions\sozi\document.py", line 96
        self.layers = { l.attrib[group_attr] : SoziLayer(self, l) for l in self.xml.xpath("sozi:layer", namespaces=inkex.NSS) if group_attr in l.attrib }
    SyntaxError: invalid syntax

This error happens when Inkscape tries to run Sozi using Python 2.6 instead of Python 2.7.
Usually, it means that Python 2.7 has not been installed, or not at the correct location.
Check that you have followed the [installation instructions](http://sozi.baierouge.fr/pages/install-windows.html)
correctly.

Though this has not been confirmed, it seems that some users experience this problem when installing the
*portable* version of Inkscape. Please use the *installer* instead.