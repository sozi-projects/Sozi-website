Title: Download and install
Slug: 20-install
Lang: en
Authors: Guillaume Savaton


Select your environment and release version
-------------------------------------------

* [Install the latest release for GNU/Linux](#installing-for-gnulinux)
* [Install the latest release for Windows](#installing-for-windows)
* [Install the latest release for OS X](#installing-for-os-x)
* [Install Sozi from a Docker image](#installing-from-a-docker-image)
* [Browse all stable and preview releases](https://github.com/sozi-projects/Sozi/releases){:target="_blank"}

Installing for GNU/Linux
------------------------

> As far as we know, the available Debian, Ubuntu, and Fedora repositories
> provide very outdated versions of Sozi.
> You can still install them, but be aware that no documentation or support
> will be available.
> Starting from Sozi 18, we provide packages of the Sozi executable
> for Debian, Ubuntu, and their derivatives.

### Debian, Ubuntu and their derivatives

From the [download page for the latest release](https://github.com/sozi-projects/Sozi/releases/latest){:target="_blank"},
download the `.deb` file that corresponds to your platform (`i386` or `amd64`).
Open a terminal and run the following command:

```bash
sudo dpkg -i sozi_{version}_{arch}.deb
```

### Fedora, CentOS Stream

From the [download page for the latest release](https://github.com/sozi-projects/Sozi/releases/latest){:target="_blank"},
download the `.rpm` file that corresponds to your platform (`i386` or `amd64`).
Open a terminal and run the following command:

```bash
sudo rpm -i sozi-{version}.{arch}.rpm
```

### Archlinux

Archlinux users can install Sozi from the [Archlinux User Repository](https://aur.archlinux.org/packages/sozi).

### Other distributions

From the [download page for the latest release](https://github.com/sozi-projects/Sozi/releases/latest){:target="_blank"},
download the `.tar.xz` file that corresponds to your platform (`linux-ia32` or `linux-x64`).
In a terminal, execute the following commands:

```bash
tar xJf Sozi-{version}.tar.xz

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

Sozi for Windows is only distributed in the form of a zip archive, no installer is provided.
From the [download page for the latest release](https://github.com/sozi-projects/Sozi/releases/latest){:target="_blank"},
download one of the following files:

* `sozi-{version}-windows-ia32.zip` for Windows, 32-bit.
* `sozi-{version}-windows-ia64.zip` for Windows, 64-bit.

Several tools are available to extract this archive.
If unsure, you can use [7-Zip](https://www.7-zip.org/).

Extracting the archive will create a folder with the same name.
Then you can run Sozi directly by launching the `Sozi` executable inside that folder.

Installing for OS X
-------------------

Sozi for OS X is distributed in the form of a "tar.xz" archive.
From the [download page for the latest release](https://github.com/sozi-projects/Sozi/releases/latest){:target="_blank"},
download the file `sozi-{version}-osx-ia64.tar.xz`.

Several tools are available to extract this archive.
If unsure, you can use [The Unarchiver](https://theunarchiver.com/).

Extracting the archive will create a folder with the same name, containing a subbolder `Sozi.app`.
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
