Title: Embedding Sozi presentations in HTML documents
Slug: tutorial-embedding
Lang: en
Authors: Guillaume Savaton
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

Controlling the presentation from the main HTML page
----------------------------------------------------

In the following example, we add two buttons to the main HTML page to
move to the previous or next frame.
Between the buttons, a `<span>` element will show the title of the current frame.

    :::html
    Press these buttons to move to the previous/next frame:
    <input id="btn-prev" type="button" value="&larr;" title="Move to the previous frame">
    <span  id="frame-title">Loading&hellip;</span>
    <input id="btn-next" type="button" value="&rarr;" title="Move to the next frame">

    <iframe src="my-presentation.sozi.html">
        My Sozi presentation should play here.
    </iframe>

    <script>
        window.addEventListener("load", function () {
            var frame     = document.querySelector("iframe");
            var btnPrev   = document.getElementById("btn-prev");
            var btnNext   = document.getElementById("btn-next");
            var spanTitle = document.getElementById("frame-title");

            var player = frame.contentWindow.sozi.player;

            spanTitle.innerHTML = player.currentFrame.title;

            btnPrev.addEventListener("click", function () {
                player.moveToPrevious();
            }, false);

            btnNext.addEventListener("click", function () {
                player.moveToNext();
            }, false);

            player.addListener("frameChange", function () {
                spanTitle.innerHTML = player.currentFrame.title;
            });
        }, false);
    </script>

Here is an overview of the result:

Press these buttons to move to the previous/next frame:
<input id="sozi-first-presentation-prev" title="Move to the previous frame" type="button" value="&larr;">
<span  id="sozi-first-presentation-title">Loading&hellip;</span>
<input id="sozi-first-presentation-next" title="Move to the next frame" type="button" value="&rarr;">

<iframe class="sozi" id="sozi-first-presentation" src="|filename|/presentations/tutorial-first/first-presentation.sozi.html">
    Your browser cannot display this content.
</iframe>

<script>
    window.addEventListener("load", function () {
        var frame      = document.getElementById("sozi-first-presentation");
        var btnPrev    = document.getElementById("sozi-first-presentation-prev");
        var btnNext    = document.getElementById("sozi-first-presentation-next");
        var spanTitle = document.getElementById("sozi-first-presentation-title");

        var player = frame.contentWindow.sozi.player;

        spanTitle.innerHTML = player.currentFrame.title;

        btnPrev.addEventListener("click", function () {
            player.moveToPrevious();
        }, false);

        btnNext.addEventListener("click", function () {
            player.moveToNext();
        }, false);

        player.addListener("frameChange", function () {
            spanTitle.innerHTML = player.currentFrame.title;
        });
    }, false);
</script>
