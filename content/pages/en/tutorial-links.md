Title: Frame URLs and hyperlinks
Slug: tutorial-links
Lang: en
Authors: Guillaume Savaton
Status: hidden

In this tutorial, you will learn how to add hyperlinks in Sozi documents
and how to link to a Sozi frame.

Download and open the example document
--------------------------------------

This tutorial is based on an SVG document that contains the drawing elements of our presentation.
[Download the base SVG document]({static}/presentations/tutorial-links/tutorial-links.svg)
(Right-click on the link and choose *Save link target as*).

This SVG document has been created with [Inkscape](https://inkscape.org).
We recommend to install Inkscape before proceeding.

Create the frames of the presentation
-------------------------------------

Open `tutorial-links.svg` in the Sozi presentation editor.

![Base document in Sozi]({static}/images/tutorial-links/sozi-links-tutorial-screenshot-01.png)

Create five frames as illustrated by the following screenshots:

![Frame 1 (Home)]({static}/images/tutorial-links/sozi-links-tutorial-screenshot-02.png)
![Frame 2 (Top left)]({static}/images/tutorial-links/sozi-links-tutorial-screenshot-03.png)
![Frame 3 (Top right)]({static}/images/tutorial-links/sozi-links-tutorial-screenshot-04.png)
![Frame 4 (Bottom right)]({static}/images/tutorial-links/sozi-links-tutorial-screenshot-05.png)
![Frame 5 (Bottom left)]({static}/images/tutorial-links/sozi-links-tutorial-screenshot-06.png)

Edit the frame titles and IDs as follows:

<table>
    <tr>
        <th>Frame number</th>
        <th>Title</th>
        <th>ID</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Home</td>
        <td>home</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Top left</td>
        <td>top-left</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Top right</td>
        <td>top-right</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Bottom right</td>
        <td>bottom-right</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Bottom left</td>
        <td>bottom-left</td>
    </tr>
</table>

You can already open the presentation in a web browser to check that all frames are correctly defined.

Frame URLs
----------

When a Sozi document is opened in a web browser, the content of the address bar
changes each time you move from one frame to another.

![Frame URL in the address bar of a web browser]({static}/images/tutorial-links/sozi-links-tutorial-screenshot-07.png)

In the example above the address bar shows the URL:

    file://.../tutorial-links.sozi.html#top-right

If your document is served by a web server, the first element of the URL will be `http` or `https` instead of `file`.
In the URL above, the HTML file name is followed by a *hash* character (`#`)
and the ID of the current frame (`top-right`).

As a result, if you are sharing a presentation on the web, it will be possible to make a
direct link to any frame.

Creating hyperlinks in a Sozi presentation
------------------------------------------

> The SVG standard supports hyperlinks natively.
> For this reason, Sozi provides no specific feature related to the creation
> of links in your presentations.
> You must add them to your SVG documents using Inkscape or any other SVG-compliant
> vector drawing software.

Open the document `tutorial-links.svg` in Inkscape.
Right-click on the big arrow that points in the top-left direction
and choose *Create Link*.

![Creating a link in Inkscape]({static}/images/tutorial-links/sozi-links-tutorial-screenshot-08.png)

This action opens the *Object attributes* dialog where you can edit the properties of the link.

To create a link to the top left frame, we only need to set the `Href` attribute to
`#top-left`:

![Setting the href attribute of a link]({static}/images/tutorial-links/sozi-links-tutorial-screenshot-09.png)

Process similarly for the other frames: for each arrow, create a link to the corresponding frame ID.
Finally, select the blue circle and create a link to `#home`.

Update and play the presentation in a web browser
-------------------------------------------------

Save the SVG document in Inkscape.
Move back to the Sozi window to update the SVG content of the presentation.
The update operation is automatic.

Open the file `tutorial-links.sozi.html` with your favorite web browser.
It will automatically focus on the first frame.
Click inside the white background of the document to move to the next frame
(See also: [Playing a presentation](|filename|play.md))
or click on an arrow to move directly to the corresponding frame.

[Download the full presentation]({static}/presentations/tutorial-links/tutorial-links.sozi.html)
(Right-click on the link and choose *Save link target as*).
