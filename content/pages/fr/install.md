Title: Télécharger et installer
Slug: 20-install
Lang: fr
Translation: true
Authors: Guillaume Savaton

Choisissez votre environnement et version
------------------------------------------

* [Installer la dernière version pour GNU/Linux](#installation-pour-gnulinux)
* [Installer la dernière version pour Windows](#installation-pour-windows)
* [Installer la dernière version pour OS X](#installation-pour-os-x)
* [Installer Sozi à partir d'une image Docker](#installation-a-partir-dune-image-docker)
* [Parcourir la liste des versions stables et des versions de test](https://github.com/sozi-projects/Sozi/releases){:target="_blank"}

Installation pour GNU/Linux
---------------------------

> À notre connaissance, les dépôts Debian, Ubuntu et Fedora proposent des versions
> "périmées" de Sozi.
> Vous pouvez toujours les installer, mais sachez que vous ne trouverez ni
> assistance, ni documentation.
> Depuis la version 18, nous fournissons l'éditeur de présentations sous la forme
> de paquets pour Debian, Ubuntu et les distributions dérivées.

### Debian, Ubuntu et leurs variantes

À partir de la [page des téléchargements pour la version la plus récente de Sozi](https://github.com/sozi-projects/Sozi/releases/latest){:target="_blank"},
téléchargez le fichier `.deb` correspondant à votre plate-forme (`i386` ou `amd64`).
Ouvrez un terminal et exécutez la commande suivante&nbsp;:

```bash
sudo dpkg -i sozi_{version}_{arch}.deb
```

### Fedora, CentOS

Nous ne fournissons pas de paquets au format RPM.
Cependant, les paquets Debian peuvent s'installer à l'aide
de l'utilitaire `alien` disponible dans votre distribution.

À partir de la [page des téléchargements pour la version la plus récente de Sozi](https://github.com/sozi-projects/Sozi/releases/latest){:target="_blank"},
téléchargez le fichier `.deb` correspondant à votre plate-forme (`i386` ou `amd64`).
Ouvrez un terminal et exécutez la commande suivante&nbsp;:

```bash
sudo alien -i sozi_{version}_{arch}.deb
```

### Archlinux

Les utilisateurs d'Archlinux peuvent installer Sozi depuis l'[Archlinux User Repository](https://aur.archlinux.org/packages/sozi).

### Autres distributions

À partir de la [page des téléchargements pour la version la plus récente de Sozi](https://github.com/sozi-projects/Sozi/releases/latest){:target="_blank"},
téléchargez le fichier `.tgz` correspondant à votre plate-forme (`linux-ia32` ou `linux-x64`).
Dans un terminal, exécutez les commandes suivantes&nbsp;:

```bash
tar xJf Sozi-{version}.tar.xz

# Installer Sozi globalement pour tous les utilisateurs

sudo ./Sozi-{version}/install/install.sh

# Ou installer Sozi localement, dans votre dossier personnel.
# Tous les fichiers sont laissés à leur emplacement courant,
# des liens symboliques sont créés dans $HOME/.local et $HOME/bin.
# Ajoutez $HOME/bin à votre variable PATH si nécessaire.
./Sozi-{version}/install/install-local.sh

# Exécuter Sozi
sozi
```

Après installation, Sozi peut être exécuté depuis le menu des applications de votre environnement de bureau ou en ligne de commande en tant que `sozi` (en minuscules).

Installation pour Windows
-------------------------

Sozi pour Windows est distribué uniquement sous la forme d'une archive zip, aucun programme d'installation n'est fourni.
À partir de la [page des téléchargements pour la version la plus récente de Sozi](https://github.com/sozi-projects/Sozi/releases/latest){:target="_blank"},
téléchargez l'un des fichiers suivants&nbsp;:

* `sozi-{version}-windows-ia32.zip` pour Windows, 32 bits.
* `sozi-{version}-windows-ia64.zip` pour Windows, 64 bits.

Il existe différents logiciels pour extraire cette archive.
Dans le doute, vous pouvez utiliser [7-Zip](https://www.7-zip.org/).

En procédant à l'extraction de cette archive, vous verrez apparaître un dossier
portant le même nom.
Vous pouvez alors démarrer Sozi en ouvrant l'exécutable `Sozi` situé dans ce dossier.

Installation pour OS X
----------------------

Sozi pour OS X est distribué sous la forme d'une archive au format "tar.xz".
À partir de la [page des téléchargements pour la version la plus récente de Sozi](https://github.com/sozi-projects/Sozi/releases/latest){:target="_blank"},
téléchargez le fichier `sozi-{version}-osx-ia64.tar.xz`.

Il existe différents logiciels pour extraire cette archive.
Dans le doute, vous pouvez utiliser [The Unarchiver](https://theunarchiver.com/).

En procédant à l'extraction de cette archive, vous verrez apparaître un dossier
portant le même nom.
Vous y trouverez un sous-dossier `Sozi.app` que vous pourrez
faire glisser dans votre dossier `Applications`.
Vous pourrez ensuite l'exécuter comme n'importe quelle autre application pour OS X.

Installation à partir d'une image Docker
----------------------------------------

Sous Linux ou OS X, cette méthode permet d'installer Sozi, Inkscape et les
[outils de conversion de présentations](|filename|tutorial-converting.md)
dans un même conteneur Docker.

Après avoir installé Docker, l'installation de Sozi s'effectue à l'aide de la
commande suivante&nbsp;:

```bash
docker pull escalope/inkscape-sozi
```

Dans les exemples ci-dessous, le dossier courant est monté en tant que
`/foo`.

Pour lancer Inkscape&nbsp;:

```bash
xhost +172.17.0.1

docker run --user $UID -ti --rm -e DISPLAY=unix$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix -w /foo -v "`pwd`":/foo \
    escalope/inkscape-sozi:latest \
    inkscape
```

Pour exécuter Sozi&nbsp;:

```bash
xhost +172.17.0.1

docker run --user $UID -ti --rm -e DISPLAY=unix$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix -w /foo -v "`pwd`":/foo \
    escalope/inkscape-sozi:latest \
    sozi
```

Pour convertir une présentation en vidéo&nbsp;:

```bash
docker run --user $UID -ti --rm \
    -w /foo -v "`pwd`":/foo \
    escalope/inkscape-sozi:latest \
    sozi-to-video ma-presentation.sozi.html
```

Cette image a été créée par [Jorge Gomez](https://github.com/escalope).
Elle est hébergée dans [le dépôt inkscape-sozi sur Docker Hub](https://hub.docker.com/r/escalope/inkscape-sozi).
Le Dockerfile se trouve [dans le dépôt dockerfile-sozi chez GitHub](https://github.com/escalope/dockerfile-sozi).
