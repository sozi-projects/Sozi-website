Title: Sua primeira apresentação
Slug: tutorial-first
Lang: pt_br
Author: Guillaume Savaton, Marcelo Vaz Pupo
Translation: true
Status: hidden

Esse tutorial apresenta as principais características do Sozi.
Você irá aprender como criar os quadros da sua apresentação e efetivamente usá-la em um navegador de internet.


Baixar e abrir o documento de exemplo
-------------------------------------

Esse tutorial utiliza um documento SVG (desenho vetorial) que contém alguns elementos para nossa apresentação.
[Baixe o arquivo SVG](https://github.com/senshu/Sozi/raw/master/samples/first-presentation.svg)
(Clique com o botão da direita no link e escolha *Salvar link como...*).
Abra o arquivo com o editor de apresentação Sozi.

![Abra o arquivo SVG com o editor de apresentação](|filename|/images/tutorial-first/first-presentation-screenshot-01.en.png)


Criar o primeiro quadro da apresentação
---------------------------------------

Pressione o botão *+* para criar um novo quadro.

Queremos centralizar o primeiro quadro no objeto roxo com o número 1.
Você pode modificar seu título editando o campo *Título* no painel da direita.
Depois, no painel de visualização:

* Posicione a câmera usando o mouse enquanto pressiona seu botão da esquerda.
* Dê um zoom usando pressionando o botão da esquerda do mouse enquanto mantém pressionada a tecla *Alt* do teclado.

![O primeiro quadro da apresentação](|filename|/images/tutorial-first/first-presentation-screenshot-02.en.png)


Criar os outros três quadros
----------------------------

Adicione três quadros novos.
O painel inferior representa cada quadro inserido por uma coluna na linha do tempo.
É possível selecionar o quadro clicando no seu respectivo número ou título.

Defina um título para cada quadro e movimente a câmera para que sejam exibidos em sequência:
o objeto laranja (2), o objeto amarelo (3) e o objeto azul (4).
Para rotacionar, pressione a tecla *Shift* e segure o botão esquerdo do mouse e movimente-o.


![O segundo quadro da apresentação](|filename|/images/tutorial-first/first-presentation-screenshot-03.en.png)


Salvar a apresentação
---------------------

O editor salva a apresentação automaticamente.
Ainda assim, é possível clicar no botão *Salvar* na barra de ferramentoas.

Sozi não realiza modificação alguma no documento SVG de origem.
Ao salvar a apresentação, o editor atualiza os seguintes arquivos:

* `first-presentation.sozi.json` contém dos dados da apresentação. Esse arquivo é utilizado
  pelo editor de apresentação. Ele deve permanecer na mesma pasta do arquivo SVG e ter, necessariamente, o mesmo nome.
* `first-presentation.sozi.html` contém a apresentação completa. É possível exibí-la em um navegador de internet 
para realizar a apresentação.

Caso queira compartilhar sua apresentação com outras pessoas basta enviar o 
arquivo que tem a extensão `.sozi.html`.


Exibir a apresentação em um navegador de internet
-------------------------------------------------

Abra o arquivo `first-presentation.sozi.html` em um navegador (browser) de internet.
Automaticamente a câmera estará posicionada no primeiro quadro da apresentação.
Clique na janela do navegador para movimentar para o próximo quadro.
(veja também: [Apresentar](|filename|play.md)).

[Baixe a apresentação completa](https://github.com/senshu/Sozi/raw/master/samples/first-presentation.sozi.html)
(Clique com o botão da direita no link e escolha *Salvar link como...*).
