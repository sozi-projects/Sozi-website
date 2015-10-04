Title: Installer Sozi sous Windows
Slug: install-windows
Lang: fr
Status: hidden
Author: Guillaume Savaton, IntraCherche

> Cette page fait partie de la documentation de Sozi 13.
> Avec la sortie imminente de Sozi 15, le contenu de cette page
> est considéré comme obsolète.
> Nous le mettrons à jour prochainement.

> Si vous mettez à jour Sozi depuis la version 13.01 ou antérieure,
> il est recommandé de désinstaller cette version précédente
> en supprimant tous les fichiers dont le nom commence par `sozi`
> dans `C:\Program Files\Inkscape\share\extensions`.

Ces instructions ont été testées avec Inkscape 0.48, Python 2.7 et PyGTK 2.24.
Si vous faites la mise à jour depuis une version précédente de Sozi,
vous pouvez sauter directement à l'étape 8.

1. Installez [Inkscape](http://inkscape.org/download/) en utilisant l'installeur Windows 32 bits.
Le dossier d'installation par défaut est  `C:\Program Files\Inkscape`
ou `C:\Program Files (x86)\Inkscape`
2. Installez [Python](http://python.org/download/) 2.7.
Utilisez l'installeur Windows 32 bits par défaut, pas celui pour x86_64.
Le dossier d'installation par défaut est `C:\Python27`
3. Installez [LXML](https://pypi.python.org/pypi/lxml/3.2.4#downloads) pour Python 2.7 et Windows 32-bit (win32-py2.7).
4. Installez [PyGTK](http://ftp.gnome.org/pub/GNOME/binaries/win32/pygtk/2.24/) 2.24.
Choisissez l'installeur tout en un  (*all-in-one*) pour Python 2.7 et Windows 32 bit (win32).
5. Copiez le dossier `C:\Python27` dans `C:\Program Files\Inkscape`
6. Renommez le dossier `C:\Program Files\Inkscape\python` en `C:\Program Files\Inkscape\python26`
7. Renommez le dossier `C:\Program Files\Inkscape\Python27` en `C:\Program Files\Inkscape\python`
8. [Téléchargez Sozi](https://github.com/senshu/Sozi/releases/download/13.11/sozi-release-13.11-30213629.zip)
9. Décompressez l'archive `sozi-release-[...].zip`.
Vous devriez obtenir un dossier nommé `archive sozi-release-[...]`.
Copiez le contenu de ce dossier dans `C:\Program Files\Inkscape\share\extensions`
10. Démarrez ou relancez Inkscape.
Vous devriez maintenant voir une option *Sozi* dans le menu *Extensions*.

Vous pouvez maintenant [créer votre première présentation](|filename|create.md).
