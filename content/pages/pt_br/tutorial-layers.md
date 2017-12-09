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

Adicionar uma camada fixa (Landscape)
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
Se o botão *Selecionar elemento automaticamente* estiver acionado, o Sozi alinha automaticamente
esse retângulo como o contorno do quadro corrente.

* Pressione o botão *Ajuste tamanho ao elemento* a direita: agora a camada *Landscape* foi
  ajustada de forma que o retângulo ocupe a área de visualização.
* Pressione o botão *Ocultar elemento* para ocultar o retângulo.

![Exposição do elemento selecionado](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-07.png)

Caso a apresentação seja exibida na janela de um navegador de internet com uma proporção de tela diferente,
será preciso esconder as partes do desenho que ficarem de fora da área visível.
Para isso, pressione o botão *Cortar* no painel de propriedades.

Nós configuramos uma camada que não será movimentada ao longo da apresentação.
Agora, vamos criar a camada que será animada.

![Camada Landscape ajustada](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-08.png)

Adicionar a camada de animação (Captions)
----------------------------------------

Pressione o botão *Adicionar camada* e escolha *Captions*.
Na linha do tempo, selecione a célula que corresponde ao primeiro quadro
e a camada *Captions* como mostra a figura abaixo.

![Selecione a camada Captions no quadro 1](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-09.png)

Na área de visualização, dê um zoom (rodinha do mouse) e movimente a camada *Captions*
até que o retângulo com o texto "Morning" ocupe quase toda a área.
Certifique-se de que apenas os elementos da camada *Captions* sejam movimentados.

![Zoom na camada Captions](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-10.png)

No campo *Exposição do elemento Id* deve estar escrito "rect-text-morning".
Pressione os botões *Ajuste tamanho ao elemento*, *Ocultar elemento* e *Cortar*.

Repita os mesmos procedimentos aos quadros "Noon", "Evening" e "Night".
A área de visualização de cada quadro deve ser vista assim:

![Adjusted frame 1 in Captions layer](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-11.png)
![Adjusted frame 2 in Captions layer](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-12.png)
![Adjusted frame 3 in Captions layer](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-13.png)
![Adjusted frame 4 in Captions layer](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-14.png)

Adicionar uma camada animada (Sky)
--------------------------------

A essa altura do campeonato, todos os desenhos que não pertencem às camadas *Landscape* ou *Captions*
estão inseridos na linha *Padrão* da linha do tempo.
De fato, *Padrão* não é exatamente uma camada: é um grupo de camadas que não foram ativadas na linha do tempo
e também contém elementos que não pertencem a nenhuma camada (pode acontecer, mas sugerimos que evite que isso aconteça).
Toda vez que uma nova camada é criada no documento SVG do Inkscape, ela automaticamente fica inserida
na categoria *Padrão* no Sozi.

Pressione o botão *Adicionar camada* e escolha *Sky*.
A linha *Padrão* irá desaparecer.

Para facilitar, iremos ocultar as camadas *Landscape* e *Captions*.
Clique no ícone do "olho" que fica a esquerda da linha dessas camadas.

![Select layer Captions for frame 1](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-15.png)

> O ícone do "olho" permite esconder uma camada no editor para facilitar o trabalho com outras camadas.
> As camadas ocultadas no editor permanecem visíveis quando se exibe a apresentação.
> Caso queira que determinada camada fique oculta durante a apresentação, altere sua *Opacidade da camada*.

Repita os procedimentos feitos com a camdada *Captions*.
Para cada quadro:

1. Na linha *Sky* da linha do tempo, selecione a célula correspondente ao quadro que quer editar.
2. Na área de visualização, dê um zoom (rodinha do mouse), move, and rotate (Shift + mouse wheel) the layer until the desired rectangle almost fills the area.
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
