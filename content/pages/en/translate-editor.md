Title: Translate the user interface of the editor to your native language
Slug: translate-editor
Lang: en
Status: hidden
Author: Guillaume Savaton

> Please note that the current translation effort is focused on Sozi 15.
> The development of Sozi 13 is currently stopped.
> New contributions to Sozi 13 will not be integrated to any official release.

The localized text for the Sozi editor are defined in *PO* files compatible with
[GNU gettext](https://www.gnu.org/software/gettext/).
There are two ways to participate in the translation of Sozi:

Using the web front-end at Launchpad.net
----------------------------------------

Create an account at [launchpad.net](https://launchpad.net/)
and visit the [translation page for Sozi](https://translations.launchpad.net/sozi).
You can start translating immediately.
When your work is finished, please [open a new issue](https://github.com/senshu/Sozi/issues)
to request the translation to be added to the next release.


Editing the PO files directly
-----------------------------

Fork the [source repository of Sozi at GitHub](https://github.com/senshu/Sozi).
The *PO* files for Sozi 15 can be found in the `locales` folder.

*PO* files can be edited using a general-purpose text editor or a translation editor such as
[Poedit](http://poedit.net/).
If you want to add a new language file, create a copy of `locales/messages.pot`.
Name your language file using the appropriate [IETF language tag](http://www.langtag.net/)
and the `.po` extension.

When your work is finished, please send us a pull request.
