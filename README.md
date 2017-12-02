Building the website of Sozi
============================

Install the build tools
-----------------------

    sudo apt-get install python-pip
    sudo pip install pelican Markdown

Build
-----

    make html

Publish
-------

    make rsync_upload
