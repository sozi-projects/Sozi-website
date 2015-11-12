Title: Instale o Sozi no Windows
Slug: install-windows
Lang: pt_br
Status: hidden
Author: Guillaume Savaton, Marcelo Vaz

> Esta página faz parte da documentação do Sozi 13.
> Como estamos no processo de lançar o Sozi 15,
> consideramos o conteúdo dessa página desatualizado.
> Em breve ela será atualizada.

> Caso esteja atualizando a partir da versão 13.01 ou anterior,
você deve desinstalar a versão anterior removendo todos os arquivos cujo nome começa com `sozi`.
> da pasta `C:\Program Files\Inkscape\share\extensions`.

Essas orientações foram testadas com o Inkscape 0.48, Python 2.7 e PyGTK 2.24.
Se você estiver atualizando a partir de versões anteriores do Sozi, vá direto para o passo 8.

1. Instale [Inkscape](http://inkscape.org/download/) usando o Windows 32-bit installer.
O local padrão de instalação é `C:\Program Files\Inkscape`
ou `C:\Program Files (x86)\Inkscape`
2. Instale [Python](http://python.org/download/) 2.7.
Use o instalador padrão Windows 32-bit, e não o x86_64. O local padrão de instalação é `C:\Python27`
3. Instale [LXML](https://pypi.python.org/pypi/lxml/3.2.4#downloads) para Python 2.7 e Windows 32-bit (win32-py2.7).
4. Instale [PyGTK](http://ftp.gnome.org/pub/GNOME/binaries/win32/pygtk/2.24/) 2.24.
Escolha o instalador *all-in-one* para Python 2.7 e Windows 32-bit (win32).
5. Copie a pasta `C:\Python27` para dentro de `C:\Program Files\Inkscape`
6. Renomeie a pasta `C:\Program Files\Inkscape\python` para `C:\Program Files\Inkscape\python26`
7. Renomeie a pasta `C:\Program Files\Inkscape\Python27` para `C:\Program Files\Inkscape\python`
8. [Baixar Sozi](https://github.com/senshu/Sozi/releases/download/13.11/sozi-release-13.11-30213629.zip)
9. Descompacte o arquivo `sozi-release-[...].zip`.
Uma pasta será criada com o nome `archive sozi-release-[...]`.
Copie o conteúdo dessa pasta para dentro de `C:\Program Files\Inkscape\share\extensions`
10. Abra o Inkscape.
O ítem *Sozi* deve aparecer no menu *Extensions*.

Agora você pode [criar sua primeira apresentação](|filename|create.md).

