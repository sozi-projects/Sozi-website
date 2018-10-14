Title: Melhorando a performance de renderização
Slug: tutorial-performance
Lang: pt_br
Authors: Guillaume Savaton, Marcelo Vaz Pupo
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

Otimizar o documento
--------------------

[Scour](http://www.codedread.com/scour/) é uma ferramenta que otimiza a performance em
documentos SVG.
Apesar do objetivo principal dessa ferramenta seja a redução do tamanho do arquivo,
algumas [operações](http://www.codedread.com/scour/ops.php) auxiliam a reduzir o
tempo de renderização:

* remoção de elementos vazios e não utilizados,
* união de grupos aninhados,
* redução de caminhos e informação de gradientes,
* remoção de estilos de propriedades desnecessários.

Scour pode ser rodado como um script Python independente ou como uma extensão do Inkscape.

> Não utilize Scour em seu documento original.
> Mantenha sempre uma cópia backup de seu documento antes de utilizar essa ferramenta.
> Não testamos completamente o Scour com apresentações do Sozi.
> Algumas otimizações podem remover informações ncessárias para o funcionamento da apresentação.
