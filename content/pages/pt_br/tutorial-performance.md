Title: Melhorando a performance de renderização
Slug: tutorial-performance
Lang: pt_br
Author: Guillaume Savaton, Marcelo Vaz Pupo
Translation: true
Status: hidden

A exibição de uma apresentação do Sozi baseada em um documento SVG complexo
pode apresentar dificuldades com as animações.
Geralmente esse problema está relacionado a capacidade de renderização SVG feita pelo seu navegador de internet.

Existem diversas soluções para esse problema:

Converter texto em caminho
--------------------------

Em alguns navegadores, o tempo de renderização SVG pode aumentar signficativamente se seu
documento contém muitos textos.
Convertê-los em caminho facilita o trabalho dos navegadores através de précomputação
das formas e dos caracteres.
Esse procedimento também garante que o texto será renderizado da mesma forma em todos os navegadores,
mesmo se a fonte utilizada no documento não estiver disponível no computador onde a apresentação está sendo exibida.

Porém, essa operação tem uma desvantagem: ela elemina o texto original do seu documento,
inviabilizando modificações no texto e indexação em motores de busca.

> Não realize essa operação no documento original.
> Tenha sempre uma cópia backup antes de realizar essa operação.

No Inkscape, selecione todos os textos (menu *Editar* / *Encontrar*, ou Ctrl-F).

![Encontre os elementos de texto](|filename|/images/tutorial-performance/sozi-tutorial-performance-screenshot-01.png)

A partir do menu *Caminho*, selecione *Converter em caminho* (Shift-Ctrl-C).

Optimize your document
----------------------

[Scour](http://www.codedread.com/scour/) is a tool that performs optimizations on
SVG documents.
While the primary goal is to reduce file size, some
[operations](http://www.codedread.com/scour/ops.php) can help reduce the
rendering time:

* removing empty and unused elements,
* merging nested groups,
* reducing path and gradient data,
* removing useless style properties.

Scour can be run as a standalone Python script or as an Inkscape extension.

> Do not run Scour on your original document.
> Always save a copy of your document before.
>
> We have not thoroughly tested the use of Scour with Sozi presentations.
> Some optimizations may also remove information needed by the presentation engine.

