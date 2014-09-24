Title: Frequently Asked Questions
Slug: faq
Lang: en
Author: Guillaume Savaton
Status: hidden

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
