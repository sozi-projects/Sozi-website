Title: Instale o Sozi no GNU/Linux
Slug: install-linux
Lang: pt_br
Status: hidden
Authors: Guillaume Savaton, Marcelo Vaz

> Esta página faz parte da documentação do Sozi 13.
> Como estamos no processo de lançar o Sozi 15,
> consideramos o conteúdo dessa página desatualizado.
> Em breve ela será atualizada.

Distribuições com Sozi
----------------------

Sozi está disponível nos repositórios das seguintes distribuições:

* [Archlinux (AUR)](http://aur.archlinux.org/packages.php?ID=42270)
* [Ubuntu (PPA)](https://launchpad.net/~sunab/+archive/sozi-release)
* [Debian](http://packages.banuscorp.eu/debian/)
* [Fedora](https://apps.fedoraproject.org/packages/inkscape-sozi)

Manual de instalação
--------------------

Sozi depende dos seguintes pacotes:

* [Inkscape](http://inkscape.org) 0.48,
* [Python](http://python.org/) 2.7,
* [PyGTK](http://www.pygtk.org/) 2.24 and Python bindings for Glade2 (Ubuntu fornece em pacotes separados `python-gtk2` and `python-glade2`),
* [LXML](http://lxml.de/) for Python 2.

Extensões do Inkscape podem ser instaladas em dois locais:

* na pasta de extensão para todos os usuários (`/usr/share/inkscape/extensions/`)
* na pasta home (`~/.config/inkscape/extensions`)

> Caso esteja atualizando a partir da versão 13.01 ou anterior,
você deve desinstalar a versão anterior removendo todos os arquivos cujo nome começa com `sozi`.

1. [Baixar Sozi](https://github.com/sozi-projects/Sozi/releases/download/13.11/sozi-release-13.11-30213629.zip)
2. Descompacte o arquivo `sozi-release-[...].zip`.
Uma pasta será criada com o nome `archive sozi-release-[...]`.
3. Copie o conteúdo dessa pasta para dentro da pasta de extensões do Inkscape.
4. Verifique se a subpasta `sozi` tem a permissão *execute*.
5. Abra o Inkscape.
O ítem *Sozi* deve aparecer no menu *Extensions*.

Agora você pode [criar sua primeira apresentação](|filename|create.md).
