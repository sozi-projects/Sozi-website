Title: Installation
Slug: install
Lang: en
Status: hidden
Authors: Guillaume Savaton

If you use Sozi and would like to support its development,
you can [contribute](|filename|contribute.md),
or [buy something](https://www.spreadshirt.fr/user/Guillaume+Savaton),
[buy me a coffee](https://www.buymeacoffee.com/THtbNvnqE),
or [make a donation by another mean](|filename|donate.md).

* [Download the latest release](https://github.com/senshu/Sozi/releases/latest)
* [Download a preview version of the next release](https://drive.google.com/open?id=0ByRUreHgekjMWG9teGM2dE8wck0) (for testers)
* [Installing for GNU/Linux](#installing-for-gnulinux)
* [Installing for Windows](#installing-for-windows)
* [Installing for OS X](#installing-for-os-x)
* [Installing from a Docker image](#installing-from-a-docker-image)

Installing for GNU/Linux
------------------------

> As far as we know, the available Debian, Ubuntu, and Fedora repositories
> provide very outdated versions of Sozi.
> You can still install them, but be aware that no documentation or support
> will be available.

Starting from Sozi 18, we provide packages of the presentation editor
for Debian, Ubuntu, and their derivatives.
Download the `.deb` file that corresponds to your platform (`i386` or `amd64`),
open a terminal and run the following command:

```bash
sudo dpkg -i sozi_{version}_{arch}.deb
```

Archlinux users can install Sozi from the [Archlinux User Repository](https://aur.archlinux.org/packages/sozi).

### Installing from a zip archive

In other cases, download the `.tgz` file that corresponds to your platform (`linux-ia32` or `linux-x64`).
In a terminal, execute the following commands:

```bash
tar xzf Sozi-{version}.tgz

# Install Sozi globally for all users
sudo ./Sozi-{version}/install/install.sh

# Or install Sozi locally in your home folder.
# All files are kept in their current location,
# symbolic links are created in $HOME/.local and $HOME/bin.
# Add $HOME/bin to your PATH variable if needed.
./Sozi-{version}/install/install-local.sh

# Run Sozi
sozi
```

After installation, Sozi can be run either from your desktop applications menu,
or from the command-line as `sozi` (in lower case).

Installing for Windows
----------------------

Sozi for Windows is only distributed in the form of a zip archive.
No installer is provided.
Download one of the following files:

* `sozi-{version}-windows-ia32.zip` for Windows, 32-bit.
* `sozi-{version}-windows-ia64.zip` for Windows, 64-bit.

Extracting the archive will create a folder with the same name.
Then you can run Sozi directly by launching the `Sozi` executable inside that folder.

Installing for OS X
-------------------

Sozi for OS X is distributed in the form of a zip archive named
`sozi-{version}-osx-ia64.tgz` (for Sozi 17 or below, the file was named
`sozi-{version}-darwin-ia64.tgz`).

Extract the archive.
It will create a folder with the same name, containing a subbolder `Sozi.app`.
Drag `Sozi.app` to your `Applications` folder and execute it like any other
OS X application.

Installing from a Docker image
------------------------------

For Linux or OS X, this solution installs Sozi, Inkscape and the
[presentation conversion tools](|filename|tutorial-converting.md)
in a single Docker container.

After installing Docker, Sozi can be installed using this command:

```bash
docker pull escalope/inkscape-sozi
```

In the following examples, the current folder is mounted as `/foo`.

To run Inkscape:

```bash
xhost +172.17.0.1

docker run --user $UID -ti --rm -e DISPLAY=unix$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix -w /foo -v "`pwd`":/foo \
    escalope/inkscape-sozi:latest \
    inkscape
```

To run Sozi:

```bash
xhost +172.17.0.1

docker run --user $UID -ti --rm -e DISPLAY=unix$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix -w /foo -v "`pwd`":/foo \
    escalope/inkscape-sozi:latest \
    sozi
```

To convert a presentation to a video:

```bash
docker run --user $UID -ti --rm \
    -w /foo -v "`pwd`":/foo \
    escalope/inkscape-sozi:latest \
    sozi-to-video my-presentation.sozi.html
```

This image has been created by [Jorge Gomez](https://github.com/escalope).
It is hosted in [the inkscape-sozi Docker Hub repository](https://hub.docker.com/r/escalope/inkscape-sozi).
The source Dockerfile can be found in [the dockerfile-sozi GitHub repository](https://github.com/escalope/dockerfile-sozi).

Sozi 13
-------

Sozi 13.11 is still available if you need it, but it is no longer maintained:

* [Download it](https://github.com/senshu/Sozi/releases/download/13.11/sozi-release-13.11-30213629.zip)
* [See the release notes](|filename|/Releases/release-13.11.md)
* [Install Sozi 13 on GNU/Linux](|filename|sozi-13-install-linux.md)
* [Install Sozi 13 on Windows](|filename|sozi-13-install-windows.md)
* [Install Sozi 13 on Mac OS X](|filename|sozi-13-install-osx.md)
