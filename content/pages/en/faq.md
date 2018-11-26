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
    </style>
