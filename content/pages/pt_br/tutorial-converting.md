Title: Convertendo apresentações do Sozi para PDF ou vídeo
Slug: tutorial-converting
Lang: pt_br
Authors: Guillaume Savaton, Marcelo Vaz Pupo
Translation: true
Status: hidden

> Sozi-export is now considered obsolete.
> Since Sozi 21.02, the conversion tool has been integrated into the presentation editor.
>
> Documentation for this new feature will be available soon.

> Read this page in English for an up-to-date version.

`sozi-to-pdf` e `sozi-to-video` são ferramentas de comando de linha que podem ser usadas para exportar uma apresentação
como um único documento PDF ou como um vídeo.
O código fonte está disponível no repositório [Sozi-export](https://github.com/sozi-projects/Sozi-export).
Estas ferramentas funcionam independentemente do editor de apresentação.
Elas foram testadas apenas em sistemas GNU/Linux.

Instalar
--------

A exportação em PDF depende do [pdfjam](http://www2.warwick.ac.uk/fac/sci/statistics/staff/academic-research/firth/software/pdfjam), um script do shell para manipulação de arquivos PDF.
A exportação de vídeo é baseada em [libav](https://libav.org).
Usuários de distribuições baseadas em Debian podem instalar os pacotes *texlive-extra-utils* e *libav-tools*.

    :::bash
    apt-get install texlive-extra-utils libav-tools

As duas ferramentas estão disponíveis no pacote NPM.
Instale [node.js](https://nodejs.org/) 0.10 ou versões mais atuais
(Usuários Linux podem usar [distribuições NodeSource](https://github.com/nodesource/distributions)),
então:

    :::bash
    npm install -g sozi-export


Converter uma apresentação do Sozi para PDF
-------------------------------------------

    :::bash
    sozi-to-pdf [options] presentation.sozi.html

Opções:

* `-h`, `--help` informação de uso
* `-o`, `--output <file>` arquivo de saída
* `-W`, `--width <number>` largura da página (padrão é 29.7)
* `-H`, `--height <number>` altura da página (padrão é 21)
* `-r`, `--resolution <number>` pixels por unidade de largura/altura (padrão é 72)
* `-p`, `--paper <size>` tamanho da página (padrão é tamanho A4)
* `-P`, `--portrait` orientação de retrato para a página (padrão é desabilitado)
* `-i`, `--include <list>` quadros a serem incluídos (padrão é 'all' - todos)
* `-x`, `--exclude <list>` quadros a serem excluídos (padrão é 'none' - nenhum)

As opções de largura, altura e resolução especificam a geometria da janela do navegador
onde a apresentação é renderizada.
As opções de página e retrato especificam o formato de página do documento PDF final.
A opção `include` sempre é usada antes da opção `exclude`.
A sintaxe de quadros é a seguinte:

* `all` seleciona todos os quadros da apresentação.
* `none` não seleciona nenhum quadro.
* Uma vírgula separa número de quadros ou um intervalo.
  Um intervalo segue a forma `first:last` ou `first:second:last` onde `first`, `second` e `last` representam números de quadros.

Por exemplo: `-i 2,4:6,10:12:18` incluirá os quadros 2, 4, 5, 6, 10, 12, 14, 16, 18.

Converter uma apresentação do Sozi para vídeo
---------------------------------------------

    :::bash
    sozi-to-video [options] presentation.sozi.html

Opções:

* `-h`, `--help` informações de uso
* `-o`, `--output <file>` arquivo de saída
* `-W`, `--width <number>` largura do vídeo, em pixels (padrão é 1024)
* `-H`, `--height <number>` altura do vídeo (padrão é 768)
* `-b`, `--bit-rate <number>` taxa de bit (bit rate) do vídeo (padrão é 2M)

Problemas e limitações
----------------------

Essas ferramentas utilizam  um navegador de internet *headless* para renderização.
[PhantomJS](http://phantomjs.org) e [SlimerJS](https://slimerjs.org/) têm vantagens e limitações:

* PhantomJS pode renderizar uma página da internet em um documento PDF, preservando os desenhos vetoriais e o texto.
  Porém, PhantomJS 1.9.19 não é capaz de renderizar o conteúdo SVG de uma apresentação do Sozi.
* SlimerJS renderiza conteúdo SVG corretamente, mas não tem suporte para o formato PDF.

Atualmente a ferramenta de exportação de PDF renderiza cada quadro como uma imagem PNG e as reúne em um documento PDF.
