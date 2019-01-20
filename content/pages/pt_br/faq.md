Title: Questões Frequêntes e Solução de Problemas
Slug: faq
Lang: pt_br
Authors: Guillaume Savaton, Marcelo Vaz
Status: hidden

Alguns gráficos não renderizam corretamente quando estou exibindo minha apresentação do Sozi
--------------------------------------------------------------------------------------------

O Sozi não é responsável pela renderização de seus documentos na tela.
Isso é um trabalho para seu browser de internet.
O Sozi apenas lida com a lógica da *apresentação*: aplicar transformações geométricas às
camadas de seu documento, controlar a animação, responder aos comandos do usuário.
Caso você encontre gráficos renderizados de forma incorreta,
o problema provavelmente deve ser do editor de SVG ou do browser.

> Por favor não nos informe problemas relacionados a esse tópico a não ser que tenha fortes
> razões para acreditar que o problema está no Sozi.
> Caso não tenha certeza, procure conselhos no [grupo de discussão de usuários do Sozi](/community).

Diversas pessoas têm informado problemas quando o documento SVG contém
*fluir em molde*, isto é, um texto que acompanha certo objeto (um retângulo, p.ex) no Inkscape.
Atualmente esta funcionalidade não é estável nos padrões SVG.
O wiki do Inkscape apresenta [um esclarecimento nesse assunto](http://wiki.inkscape.org/wiki/index.php/FAQ#What_about_flowed_text.3F)
como seguinte alerta:

> [...] não é recomendável que se use texto fluído em molde em documentos que serão usados fora do Inkscape.

Como definir uma cor de fundo?
--------------------------------

O Inkscape permite definir uma cor de fundo no ítem *propriedades do desenho*.

![Setting a background color in Inkscape](|filename|/images/faq/background-en.png)
