Title: Usando camadas
Slug: tutorial-layers
Lang: pt_br
Author: Guillaume Savaton, Marcelo Vaz Pupo
Translation: true
Status: hidden

Uma apresentação do Sozi pode ser organizada em uma ou mais camadas, que podem ser movimentadas de forma independente.
Um exemplo bem comum de uso de camadas é inserir um fundo, fixo, para os quadros,
mas existem muitas outras possibilidades.
Com algum trabalho e engenhosidade, é possível criar animações bem sofisticadas.
Mas lembre-se: como o objetivo do Sozi é editar apresentações,
ele não tem recursos que outros programas, dedicados às animações, geralmente têm.

Baixar e abrir o documento de exemplo
-------------------------------------

Esse tutorial utiliza um documento SVG (desenho vetorial) que contém alguns elementos para nossa apresentação.
[Baixe o arquivo SVG](https://github.com/senshu/Sozi/raw/master/samples/tutorial-layers.svg)
(Clique com o botão da direita no link e escolha *Salvar link como...*).

Esse documento SVG foi criado no [Inkscape](https://inkscape.org).
Recomendamos sua instalação antes de seguir no tutorial.
Antes de criar a apresentação, veremos como os desenhos estão organizados.

Abra `tutorial-layers.svg` pelo Inkscape.

![Documento de exemplo no Inkscape](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-01.png)

Organização de camada
---------------------

É possível organizar um documento no Inkscape em camadas.
Você pode abrir o painel de camadas clicando em *Organize, adicione, exclua camadas* na barra de ferramenta,
ou clicando no item *Gerenciador de camadas;* no menu *Camada* menu.

![Mostrar camadas](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-02.png)

Nesse exemplo, o documento contém três camadas:

* *Captions*: é a camada de primeiro plano com os elementos de texto.
* *Landscape*: camada intermediária com o desenho da árvore.
* *Sky*: camada de fundo com um grande círculo azul e o sol, a lua e as estrelas.

Cada camada tem uma subcamada chamada *Frames*. Essas subcamadas contém retângulos
que ajudam no alinhamento dos desenhos quando formos criar a apresentação no Sozi.

> É possível mostrar ou esconder uma camada clicando no ícone de olho correspondente, na caixa de diálogo *Gerenciador de camada*.
> Experimente mostrar e esconder cada camada e subcamada para identificar quais elementos pertencem a qual camada.
> Tenha certeza de que todas as camadas estão visíveis antes de seguir para o próximo passo.

Criar os quadros da apresentação do Sozi
----------------------------------------

Abra `tutorial-layers.svg` no editor de apresentação do Sozi.

![Documento de exemplo no Sozi](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-03.png)

Adicione quatro quadros usando o botão *+* no painel da linha do tempo.
Para cada quadro, preencha o campo *Título* com os seguintes títulos:

1. "Morning",
2. "Noon",
3. "Evening",
4. "Night".

A linha do tempo deve ficar assim:

![Linha do tempo com quatro quadros](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-04.png)

Adicione uma camada fixa (Landscape)
------------------------------------

Pressione o botão *Adicionar camada* e escolha *Landscape*.
Na linha do tempo, selecione a célula que corresponde ao primeiro quadro
e a camada *Landscape* como mostra a figura abaixo.

![Selecione a camada Landscape para o quadro 1](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-05.png)

Na área de visualização, use a rodinha do mouse para dar um zoom e ampliar a camada *Landscape*
até que o retângulo com a árvore quase preencha toda a área.
Tenha certeza de que apenas os elementos da camada *Landcape* sejam movidos.

![Zoom na camada Landcape](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-06.png)

No painel de propriedades do lado direito, no campo *Exposição do elemento Id* deve estar escrito
"rect-landscape".
Esse é o identificador SVG do grande retângulo vermelho que envolve o desenho da árvore.
Se o botão *selecionar elemento automaticamente* estiver acionado, o Sozi alinha automaticamente
esse retângulo como o contorno do quadro corrente.

* Pressione o botão *Ajuste tamanho ao elemento* a direita: agora a camada *Landscape* foi
  ajudatada de forma que o retângulo adjusted so that the rectangle fills the preview area.
* Press the *Hide element* button to hide the rectangle.

![Outline element selection](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-07.png)

If the presentation is played in a web browser window that has a different aspect
ratio, we want to hide the graphics outside the currently visible area.
At the top right of the properties pane, press the *Clip* button.

We have set up a layer that will not move during the presentation.
Now let us create an animated layer.

![Fitted Landscape layer](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-08.png)

Add an animated layer (Captions)
--------------------------------

Press the *Add layer* button and choose *Captions*.
In the timeline, select the cell that corresponds to the first frame and the
*Captions* layer as shown below.

![Select layer Captions for frame 1](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-09.png)

In the preview area, zoom in (mouse wheel) and move the *Captions* layer
until the rectangle containing the text "Morning" almost fills the area.
Make sure that only the elements from the *Captions* layer are affected.

![Zoom in the Captions layer](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-10.png)

The field *Outline element Id* should read "rect-text-morning".
Press the *Fit to element*, *Hide element* and *Clip* buttons.

Apply the same process to the frames "Noon", "Evening" and "Night".
The preview area for each frame should look like this:

![Adjusted frame 1 in Captions layer](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-11.png)
![Adjusted frame 2 in Captions layer](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-12.png)
![Adjusted frame 3 in Captions layer](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-13.png)
![Adjusted frame 4 in Captions layer](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-14.png)

Add an animated layer (Sky)
--------------------------------

At this stage, all the graphics that do not belong to the *Landscape* or *Captions* layers
are represented by the *Default* row of the timeline.
Generally, *Default* is not really a layer: it groups all layers that have not been added to the timeline
and all the elements that do not belong to a layer (you should take care to avoid this, but it can happen).
If you add a new layer to the SVG document in Inkscape, it will fall automatically into
the *Default* category in Sozi.

Press the *Add layer* button and choose *Sky*.
The *Default* row should disappear.

For convenience, we will hide layers *Landscape* and *Captions*.
Click on the "eye" icons on the left in the rows corresponding to these layers.

![Select layer Captions for frame 1](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-15.png)

> The "eye" icon allows to hide a layer in the editor while you want to work on other layers.
> The hidden layers are still visible when playing the presentation.
>
> If you want to hide a layer when playing the presentation, set its *Layer opacity*
> to zero.

Proceed like you did for the *Captions* layer.
For each frame:

1. In the *Sky* row of the timeline, select the cell that corresponds to the frame you want to edit.
2. In the preview area, zoom (mouse wheel), move, and rotate (Shift + mouse wheel) the layer until the desired rectangle almost fills the area.
3. Check the field *Outline element Id*, then press the *Fit to element*, *Hide element* and *Clip* buttons.

Show the *Landscape* and *Captions* layers again.
The preview area should look like this:

![Adjusted frame 1 in Sky layer](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-16.png)
![Adjusted frame 2 in Sky layer](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-17.png)
![Adjusted frame 3 in Sky layer](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-18.png)
![Adjusted frame 4 in Sky layer](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-19.png)

Save and play the presentation
------------------------------

The editor should save your presentation automatically.
If it does not, you can still press the *Save* button in the tool bar.

Open the file `tutorial-layers.sozi.html` in a web browser.
The camera is automatically set to the first frame of the presentation.
Click inside the browser window to move to the next frame.
(see also: [Play](|filename|play.md)).

[Download the full presentation](https://github.com/senshu/Sozi/raw/master/samples/tutorial-layers.sozi.html)
(Right-click on the link and choose *Save link target as*).
