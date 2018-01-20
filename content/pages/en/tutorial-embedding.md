Title: Embedding Sozi presentations in HTML documents
Slug: tutorial-embedding
Lang: en
Author: Guillaume Savaton
Status: hidden

To embed a Sozi presentation in a web page, you can use an `<iframe>`
element like this:


    :::html
    <iframe src="my-presentation.sozi.html">
        My Sozi presentation should play here.
    </iframe>

The width and height of the viewport for the embedded document can be set either as attributes
of the `<iframe>` element, or using CSS.
An example is shown below.
[Read more about the `<iframe>` element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe).

<iframe class="sozi" src="|filename|/presentations/this-is-not-a-slideshow.sozi.html">
    Your browser cannot display this content.
</iframe>

Giving the keyboard focus to the Sozi presentation
--------------------------------------------------

When loading an HTML page, the browser gives the keyboard focus to the first element
that can accept it (hyperlink, form element, etc).
For this reason, in many cases, the embedded Sozi presentation will not respond to keyboard events
immediately on load.
One solution is to repeatedly hit the `TAB` key
until the `<iframe>` that displays your presentation receives focus.

You can also add the following script to your HTML document to automatically focus the
`<iframe>` containing your presentation (assuming it is the first `<iframe>`
element in the page).

    :::html
    <script>
        window.addEventListener("load", function () {
            document.querySelector("iframe").focus();
        }, false);
    </script>
