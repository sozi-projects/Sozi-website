Title: Installer Sozi sous GNU/Linux
Slug: install-linux
Lang: fr
Status: hidden
Authors: Guillaume Savaton, Vincent Garibal

> Cette page fait partie de la documentation de Sozi 13.
> [Suivez ce lien si vous souhaitez installer une version plus récente](|filename|install.md).

Distributions proposant Sozi
----------------------------

Sozi est disponible dans les dépôts des distributions suivantes :

* [Archlinux (AUR)](http://aur.archlinux.org/packages.php?ID=42270)
* [Ubuntu (PPA)](https://launchpad.net/~sunab/+archive/sozi-release)
* [Debian](http://packages.banuscorp.eu/debian/)
* [Fedora](https://apps.fedoraproject.org/packages/inkscape-sozi)

Installation manuelle
---------------------

Sozi dépend des paquets suivants :

* [Inkscape](http://inkscape.org) 0.48,
* [Python](http://python.org/) 2.7,
* [PyGTK](http://www.pygtk.org/) 2.24 et les bindings Python pour Glade2 (Ubuntu les fournit dans des paquets séparés, `python-gtk2` et `python-glade2`),
* [LXML](http://lxml.de/) pour Python 2.

Les extensions Inkscape peuvent être installées dans deux endroits différents :

* dans le dossier d'extensions pour tous les utilisateurs (`/usr/share/inkscape/extensions/`)
* dans votre dossier personnel (`~/.config/inkscape/extensions`)

> Si vous mettez à jour depuis la version 13.01 ou antérieure,
vous devez désinstaller la version précédente en supprimant tous les fichiers dont le nom commence par `sozi`.

1. [Télécharger Sozi](https://github.com/sozi-projects/Sozi/releases/download/13.11/sozi-release-13.11-30213629.zip)
2. Décompresser l'archive `sozi-release-[...].zip`.
Vous devriez obtenir un dossier nommé `archive sozi-release-[...]`.
3. Copier le contenu de ce dossier dans le dossier des extensions Inkscape.
4. Vérifier que le sous-dossier `sozi` possède les permissions *execute*.
5. Lancer ou redémarrer Inkscape.
Vous devriez voir un item *Sozi* dans le menu *Extensions*.

Maintenant vous pouvez [créer votre première présentation](|filename|create.md).
