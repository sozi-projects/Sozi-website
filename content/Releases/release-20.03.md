Title: Sozi 20.03 is available for testers and translators
Date: 2020-03-28
Slug: release-20.03
Lang: en
Authors: Guillaume Savaton
Summary:
    Beta versions 19.11, 20.01 and 20.02 have been available for a few months now.
    After some fixes and improvements, Sozi 20.03 could be the last pre-release before
    the next stable release.

Since Sozi 19.04, a lot of internal changes have been made to Sozi: code clean-up
and refactoring, upgrade of Electron and JavaScript libraries, build process.
Ideally, these changes should be transparent for users, but further tests are
needed before considering this release as stable.

> If you are already using Sozi 20.02, this release is the same software with an updated Brazilian translation.

Sozi 20.03 can be downloaded from the [release page of Sozi at GitHub](https://github.com/sozi-projects/Sozi/releases/tag/v20.03-beta).
It introduces the following visible changes:

Presentation editor
-------------------

* We are now using a custom in-app notification system instead of native notifications.
  This will make notifications work better on some platforms, and they should be less annoying.
* Selecting and using an *outline element* requires fewer actions.
* A new button allows to [add all layers to the timeline](https://github.com/sozi-projects/Sozi/issues/453).
* An option has been added to [enable or disable the browser's *back* button in the player](https://github.com/sozi-projects/Sozi/issues/458).
* Install files for Linux and OS X now use the [xz format](https://en.wikipedia.org/wiki/XZ_Utils), which results in smaller downloads.
* Bug fix: [workaround for issues related to text elements](https://github.com/sozi-projects/Sozi/issues/398)
* Bug fix: inconsistent state when moving the canvas using the mouse during an animated transition
* Bug fix: some preferences were not saved
* Bug fix: [fields reset in the properties pane when hitting Ctrl-S](https://github.com/sozi-projects/Sozi/issues/472)
* Performance tweaks
* Updated translations

Presenter console
-----------------

* Updated layout based on [a proposal](https://github.com/sozi-projects/Sozi/issues/211#issuecomment-486816698) by [@ejvindh](https://github.com/ejvindh),
  now with resizable areas for previews and notes.
* Keyboard support
* Bug fix: [comply with same-origin policy in recent web browsers](https://github.com/sozi-projects/Sozi/issues/466)
* Bug fix: [the presenter console now works in Chromium-based browsers](https://github.com/sozi-projects/Sozi/issues/467)
* Bug fix: [handle hyperlinks between the presenter window and the main window](https://github.com/sozi-projects/Sozi/issues/469).

Player
------

* [Show current frame title in the title bar of the browser](https://github.com/sozi-projects/Sozi/issues/459)
* Bug fix: [frame numbers in the frame list were not aligned properly](https://github.com/sozi-projects/Sozi/issues/460)
* Bug fix: the JavaScript code of the player was incompatible with older browsers and Sozi-export

About Sozi-export
-----------------

Sozi-export is a set of command-line tools that convert Sozi presentations to
videos or printable documents.
These tools are based on PhantomJS, a headless browser engine that is no longer
maintained.
As a consequence, Sozi-export has become unusable on several platforms.
As far as we know, there is no easy fix to make it work again in the short term.

If you think this feature is important and want to help, you can support it at
[BountySource](https://www.bountysource.com/issues/68941076-migrate-from-phantomjs):

* by enrolling as a developer if you think you can solve this issue,
* by backing the development work financially.
