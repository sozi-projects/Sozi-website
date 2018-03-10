Title: Questões Frequêntes e Solução de Problemas
Slug: faq
Lang: pt_br
Author: Guillaume Savaton, Marcelo Vaz
Status: hidden

Como definir uma cor de fundo?
--------------------------------

O Inkscape permite definir uma cor de fundo no ítem *propriedades do desenho*.
Infelizmente a cor escolhida é visível apenas no Inkscape e em imagens geradas pelo programa.
A cor escolhida é ignorada pelos browsers de navegação na internet.

Para definir uma cor que será vista no browser, você pode usar o
editor de XML editor do Inkscape.
Selecione a raiz `<svg:svg>`, adicione um novo nó elementar `<svg:style>` e um novo nó de texto
como mostra a figura abaixo:

![Definindo uma cor de fundo no Inkscape](|filename|/images/faq/background.png)

> Substitua `rgb(255, 200, 255)` pela cor que deseja [CSS color](https://developer.mozilla.org/en/docs/Web/CSS/color_value).

Caso prefira usar um editor de texto, abra um documento SVG e adicione o seguinte
elemento como um elemento flho da raiz `<svg>`:

    :::xml
    <style>
        svg {
            background: rgb(255, 200, 255);
        }
    </style>


Alguns gráficos não renderizam corretamente quando estou exibindo minha apresentação do Sozi
--------------------------------------------------------------------------------------------

Diversas pessoas têm informado problemas quando o documento SVG contém
*fluir em molde*, isto é, um texto que acompanha certo objeto (um retângulo, p.ex) no Inkscape.
Atualmente esta funcionalidade não é estável nos padrões SVG.
O wiki do Inkscape apresenta [um esclarecimento nesse assunto](http://wiki.inkscape.org/wiki/index.php/FAQ#What_about_flowed_text.3F)
como seguinte alerta:

> [...] não é recomendável que se use texto fluído em molde em documentos que serão usados fora do Inkscape.

Enfim, o Sozi não é responsável pela renderização de seus documentos na tela.
Isso é um trabalho para seu browser de internet.
O Sozi apenas lida com a lógica da *apresentação*: aplicar transformações geométricas às
camadas de seu documento, controlar a animação, responder aos comandos do usuário.
Caso você encontre gráficos renderizados de forma incorreta,
o problema provavelmente deve ser do editor de SVG ou do browser.

Por favor não nos informe problemas relacionados a esse tópico a não ser que tenha fortes
razões para acreditar que o problema está no Sozi.
Caso não tenha certeza, procure conselhos no [grupo de discussão de usuários do Sozi](/community).


Inkscape relata um problema de syntax quando uso o Sozi 13
----------------------------------------------------------

Na maioria das vezes este problema foi informado por usuários do Windows.
Ao usar o Sozi a partir do menu de extensões do Inkscape, uma caixa de diálogo aparece com o seguinte erro:

    :::pytb
    Traceback (most recent call last):
      File "sozi.py", line 30, in from sozi.document import *
      File "C:\Program Files (x86)\Inkscape\share\extensions\sozi\document.py", line 96
        self.layers = { l.attrib[group_attr] : SoziLayer(self, l) for l in self.xml.xpath("sozi:layer", namespaces=inkex.NSS) if group_attr in l.attrib }
    SyntaxError: invalid syntax

Esse erro acontece quando o Inkscape tenta rodar o Sozi usando Python 2.6 ao invés do Python 2.7.
Normalmente, isso significa que o Python 2.7 não foi instalado, ou pelo menos não no lugar certo.
Verifique se você seguiu as [instruções de instalação](http://sozi.baierouge.fr/pages/install-windows.html)
corretamente.

Embora não tenha sido confirmado, parece que alguns usuários tiveram esse problema ao instalar a
versão *portable* do Inkscape. Por favor use a versão *installer*.
