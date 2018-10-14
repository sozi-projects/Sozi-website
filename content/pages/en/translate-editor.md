Title: Translate the user interface of the editor to your native language
Slug: translate-editor
Lang: en
Status: hidden
Authors: Guillaume Savaton

The localized text for the Sozi editor are defined in *PO* files compatible with
[GNU gettext](https://www.gnu.org/software/gettext/).
There are two ways to participate in the translation of Sozi:

Using the web front-end at Weblate
----------------------------------------

Create an account at [Weblate](https://hosted.weblate.org)
and visit the [translation page for Sozi](https://hosted.weblate.org/projects/sozi/translations/).
You can start translating immediately.
When your work is finished, please [open a new issue](https://github.com/senshu/Sozi/issues)
to request the translation to be added to the next release.

> Even when 100% of the strings are marked as translated, we cannot
> infer that your translation is ready to be published.
> We will publish a translation only if you request it.

<a href="https://hosted.weblate.org/engage/sozi/?utm_source=widget">
<img src="https://hosted.weblate.org/widgets/sozi/-/translations/multi-auto.svg" alt="État de la traduction" />
</a>

Editing the PO files directly
-----------------------------

Fork the [source repository of Sozi at GitHub](https://github.com/senshu/Sozi).
The *PO* files for Sozi can be found in the `locales` folder.

*PO* files can be edited using a general-purpose text editor or a translation editor such as
[Poedit](http://poedit.net/).
If you want to add a new language file, create a copy of `locales/messages.pot`.
Name your language file using the appropriate [IETF language tag](http://www.langtag.net/)
and the `.po` extension.

When your work is finished, please send us a pull request.
