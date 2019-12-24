Title: Frequently Asked Questions and Troubleshooting
Slug: faq
Lang: en
Authors: Guillaume Savaton
Status: hidden

Some graphics do not render correctly in Sozi
---------------------------------------------

Sozi is not responsible for rendering your document on the screen.
This is the job of web browsers.
Sozi only handles the *presentation* logic: applying geometric transformations to
the layers of your document, controlling the animation, reacting to user input.
If you find that some graphics are not rendered correctly,
the issue is likely to come from either your SVG editor or your web browser.

> Please do not send us bug reports on this topic unless you have strong reasons
> to believe that the bug is in Sozi. If unsure, you can ask for advice on the
> [Sozi community forum](/community).

Several users have reported issues when their SVG document contains
*flowed text*, i.e. text that fits automatically to a given shape (a rectangle in Inkscape).
This feature is currently not stable in the SVG standard.
The Inkscape FAQ provides [explanations on this subject](https://inkscape.org/en/learn/faq/#Flowed_text_doesn%27t_show_up_in_exported_file)
with the following warning:

> [...] you should not use flowed text in documents that you intend to use outside of Inkscape.

How do I set a background color?
--------------------------------

Inkscape allows to set a background color in the *document properties* dialog
(*File* menu &rarr; *Document properties* &rarr; *Page* tab &rarr; *Background color*).
Make sure that the Alpha (opacity) component of the color is set to 255.

![Setting a background color in Inkscape]({static}/images/faq/background-en.png)

When you set a background color with Inkscape, Sozi will detect it and will
generate an HTML document with the same background color.

> This property is specific to Inkscape and will be ignored by web browsers when
> you open the SVG document alone.

A general solution if you don't use Inkscape, or if you want your SVG document
to render with the chosen background color, is to open the SVG file in a text
editor and insert a `<style>` element inside the root `<svg>` element as follows:

    :::xml
    <style>
        svg {
            background: rgb(160, 180, 220);
        }
    </style>

> Replace `rgb(160, 180, 220)` with your preferred [CSS color](https://developer.mozilla.org/en/docs/Web/CSS/color_value).

How can I remove the dashed outline around a focused hyperlink?
---------------------------------------------------------------

If your document contains hyperlinks, you may notice that after clicking on
a link, it gets surrounded by a dashed rectangle.

This rectangle is added by the web browser to identify the link that has the
focus.
You can remove it using a CSS rule.
Open your SVG document in a text editor and add the following `<style>` element
inside the root `<svg>` element:

    :::xml
    <style>
        a:focus {
        	outline: none;
        }
    </style>
