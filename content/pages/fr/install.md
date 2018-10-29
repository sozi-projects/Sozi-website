Title: Installation
Slug: install
Lang: fr
Translation: true
Status: hidden
Authors: Guillaume Savaton

> Si vous utilisez Sozi et souhaitez soutenir son développement,
> vous pouvez [contribuer](|filename|contribute.md) ou [faire un don](|filename|donate.md).

  * [Télécharger la dernière version](https://github.com/senshu/Sozi/releases/latest)
  * [Télécharger un aperçu de la prochaine version](https://drive.google.com/open?id=0ByRUreHgekjMWG9teGM2dE8wck0) (pour les testeurs)

Installation pour GNU/Linux
---------------------------

> À notre connaissance, les dépôts Debian, Ubuntu et Fedora proposent des versions
> "périmées" de Sozi.
> Vous pouvez toujours les installer, mais sachez que vous ne trouverez ni
> assistance, ni documentation.

Depuis la version 18, nous fournissons l'éditeur de présentations sous la forme
de paquets pour Debian, Ubuntu et leurs dérivées.
Téléchargez le fichier `.deb` correspondant à votre plate-forme (`i386` ou `amd64`),
ouvrez un terminal et exécutez la commande suivante&nbsp;:

```
sudo dpkg -i sozi_{version}_{arch}.deb
```

Les utilisateurs d'Archlinux peuvent installer Sozi depuis l'[Archlinux User Repository](https://aur.archlinux.org/packages/sozi).

### Installation à partir d'une archive zip

Dans les autres cas, téléchargez le fichier `.tgz` correspondant à votre plate-forme
(`linux-ia32` ou `linux-x64`).
Dans un terminal, exécutez les commandes suivantes&nbsp;:

```bash
tar xzf Sozi-{version}.tgz

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

Sozi pour Windows est distribué uniquement sous la forme d'une archive zip.
Aucun programme d'installation n'est fourni.
Téléchargez l'un des fichiers suivants&nbsp;:

* `sozi-{version}-windows-ia32.zip` pour Windows, 32 bits.
* `sozi-{version}-windows-ia64.zip` pour Windows, 64 bits.

En procédant à l'extraction de cette archive, vous verrez apparaître un dossier
portant le même nom.
Vous pouvez alors démarrer Sozi en ouvrant l'exécutable `Sozi` situé dans ce dossier.

Installation pour OS X
----------------------

Sozi pour OS X est distribué sous la forme d'une archive zip nommée
`sozi-{version}-osx-ia64.tgz` (pour Sozi 17 et les versions précédentes, le
fichier était nommé `sozi-{version}-darwin-ia64.tgz`).

En procédant à l'extraction de cette archive, vous verrez apparaître un dossier
portant le même nom.
Vous y trouverez un sous-dossier `Sozi.app` que vous pourrez
faire glisser dans votre dossier `Applications`.
Vous pourrez ensuite l'exécuter comme n'importe quelle autre application pour OS X.

Sozi 13
-------

Sozi 13.11 est toujours disponible en cas de besoin, mais cette version n'est plus maintenue.

  * [Télécharger cette version](https://github.com/senshu/Sozi/releases/download/13.11/sozi-release-13.11-30213629.zip)
  * [Consulter la liste des nouveautés](|filename|/Releases/release-13.11-fr.md)
  * [Installer Sozi 13 sous GNU/Linux](|filename|sozi-13-install-linux.md)
  * [Installer Sozi 13 sous Windows](|filename|sozi-13-install-windows.md)
  * [Installer Sozi 13 sous Mac OS X](|filename|sozi-13-install-osx.md)
