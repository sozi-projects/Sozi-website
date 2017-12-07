Title: Sua primeira apresentação
Slug: tutorial-first
Lang: pt_br
Author: Guillaume Savaton, Marcelo Vaz Pupo
Translation: true
Status: hidden

Esse tutorial apresenta as principais características do Sozi.
Você irá aprender como criar os quadros da sua apresentação e efetivamente usá-la em um navegador de internet.


Baixe o documento de exemplo e abra-o
-------------------------------------

Esse tutorial utiliza um documento SVG (desenho vetorial) que contém alguns elementos para nossa apresentação.
[Baixe o arquivo SVG](https://github.com/senshu/Sozi/raw/master/samples/first-presentation.svg)
(Clique com o botão da direita no link e escolha *Salvar link como...*).
Abra o arquivo com o editor de apresentação Sozi.

![Abra o arquivo SVG com o editor de apresentação](|filename|/images/tutorial-first/first-presentation-screenshot-01.en.png)


Crie o primeiro quadro (slide) da apresentação
-----------------------------------------------

Pressione o botão *+* para criar um novo quadro.

Queremos centralizar o primeiro quadro no objeto roxo com o número 1.
Você pode modificar seu título editando o campo *Título* no painel da direita.
Depois, no painel de visualização:

* Posicione a câmera usando o mouse enquanto pressiona seu botão da esquerda.
* Dê um zoom usando pressionando o botão da esquerda do mouse enquanto mantém pressionada a tecla *Alt* do teclado.

![O primeiro quadro da apresentação](|filename|/images/tutorial-first/first-presentation-screenshot-02.en.png)


Crie os outros três quadros
---------------------------

Adicione três quadros novos.
Cada quadro está representado Each is represented by a column in the timeline (bottom pane).
You can click on the number or the title of a frame to select it.

Set a title for each frame and move the camera in order to show successively:
the orange shape (2), the yellow shape (3), and the blue shape (4).
To rotate, move the mouse while holding the left button and the *Shift* key.

![The second frame of the presentation](|filename|/images/tutorial-first/first-presentation-screenshot-03.en.png)


Save the presentation
---------------------

The editor should save your presentation automatically.
If it does not, you can still press the *Save* button in the tool bar.

Sozi does not alter the original SVG document.
When saving, the editor updates the following two files:

* `first-presentation.sozi.json` contains the presentation data. This file is used
  by the presentation editor. It must reside in the same folder as the SVG document and must have the same name.
* `first-presentation.sozi.html` contains the complete presentation. You can display it in a web browser
  to play the presentation.

If you want to share a presentation with other people, you only need to give them
the file with the extension `.sozi.html`.


Play the presentation in a web browser
--------------------------------------

Open the file `first-presentation.sozi.html` in a web browser.
The camera is automatically set to the first frame of the presentation.
Click inside the browser window to move to the next frame.
(see also: [Play](|filename|play.md)).

[Download the complete presentation](https://github.com/senshu/Sozi/raw/master/samples/first-presentation.sozi.html)
(Right-click on the link and choose *Save link target as*).

