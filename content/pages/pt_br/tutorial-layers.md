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
[Baixe o arquivo SVG](|filename|/presentations/tutorial-layers/tutorial-layers.pt_br.svg)
(Clique com o botão da direita no link e escolha *Salvar link como...*).

Esse documento SVG foi criado no [Inkscape](https://inkscape.org).
Recomendamos sua instalação antes de seguir no tutorial.
Antes de criar a apresentação, veremos como os desenhos estão organizados.

Abra `tutorial-layers.svg` pelo Inkscape.

![Documento de exemplo no Inkscape](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-01.pt_br.png)

Organização em camadas
---------------------

É possível organizar um documento no Inkscape em camadas.
Você pode abrir o painel de camadas clicando em *Organize, adicione, exclua camadas* na barra de ferramenta,
ou clicando no item *Gerenciador de camadas;* no menu *Camada* menu.

![Mostrar camadas](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-02.pt_br.png)

Nesse exemplo, o documento contém três camadas:

* *Legendas*: é a camada de primeiro plano com os elementos de texto.
* *Paisagem*: camada intermediária com o desenho da árvore.
* *Céu*: camada de fundo com um grande círculo azul e o sol, a lua e as estrelas.

Cada camada tem uma subcamada chamada *Quadros*. Essas subcamadas contém retângulos
que ajudam no alinhamento dos desenhos quando formos criar a apresentação no Sozi.

> É possível mostrar ou esconder uma camada clicando no ícone de olho correspondente, na caixa de diálogo *Gerenciador de camada*.
> Experimente mostrar e esconder cada camada e subcamada para identificar quais elementos pertencem a qual camada.
> Tenha certeza de que todas as camadas estão visíveis antes de seguir para o próximo passo.

Criação dos quadros da apresentação no Sozi
----------------------------------------

Abra `tutorial-layers.svg` no editor de apresentação do Sozi.

![Documento de exemplo no Sozi](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-03.pt_br.png)

Adicione quatro quadros usando o botão *+* no painel da linha do tempo.
Para cada quadro, preencha o campo *Título* com os seguintes títulos:

1. "Manhã",
2. "Meio dia",
3. "Tarde",
4. "Noite".

A linha do tempo deve ficar assim:

![Linha do tempo com quatro quadros](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-04.pt_br.png)

Adição de uma camada fixa (Paisagem)
------------------------------------

Pressione o botão *Adicionar camada* e escolha *Paisagem*.
Na linha do tempo, selecione a célula que corresponde ao primeiro quadro
e a camada *Paisagem* como mostra a figura abaixo.

![Selecione a camada Paisagem para o quadro 1](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-05.pt_br.png)

Na área de visualização, use a rodinha do mouse para dar um zoom e ampliar a camada *Paisagem*
até que o retângulo com a árvore quase preencha toda a área.
Tenha certeza de que apenas os elementos da camada *Landcape* sejam movidos.

![Zoom na camada Paisagem](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-06.pt_br.png)

No painel de propriedades do lado direito, no campo *Exposição do elemento Id* deve estar escrito
"rect-landscape".
Esse é o identificador SVG do grande retângulo vermelho que envolve o desenho da árvore.
Se o botão *Selecionar elemento automaticamente* estiver acionado, o Sozi alinha automaticamente
esse retângulo como o contorno do quadro corrente.

* Pressione o botão *Ajuste tamanho ao elemento* a direita: agora a camada *Paisagem* foi
  ajustada de forma que o retângulo ocupe a área de visualização.
* Pressione o botão *Ocultar elemento* para ocultar o retângulo.

![Exposição do elemento selecionado](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-07.pt_br.png)

Caso a apresentação seja exibida na janela de um navegador de internet com uma proporção de tela diferente,
será preciso esconder as partes do desenho que ficarem de fora da área visível.
Para isso, pressione o botão *Cortar* no painel de propriedades.

Nós configuramos uma camada que não será movimentada ao longo da apresentação.
Agora, vamos criar a camada que será animada.

![Camada Paisagem ajustada](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-08.pt_br.png)

Adição de uma camada de animação (Legendas)
----------------------------------------

Pressione o botão *Adicionar camada* e escolha *Legendas*.
Na linha do tempo, selecione a célula que corresponde ao primeiro quadro
e a camada *Legendas* como mostra a figura abaixo.

![Selecione a camada Legendas no quadro 1](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-09.pt_br.png)

Na área de visualização, dê um zoom (rodinha do mouse) e movimente a camada *Legendas*
até que o retângulo com o texto "Morning" ocupe quase toda a área.
Certifique-se de que apenas os elementos da camada *Legendas* sejam movimentados.

![Zoom na camada Legendas](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-10.pt_br.png)

No campo *Exposição do elemento Id* deve estar escrito "rect-text-morning".
Pressione os botões *Ajuste tamanho ao elemento*, *Ocultar elemento* e *Cortar*.

Repita os mesmos procedimentos aos quadros "Noon", "Evening" e "Night".
A área de visualização de cada quadro deve ser vista assim:

![Adjusted frame 1 in Captions layer](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-11.pt_br.png)
![Adjusted frame 2 in Captions layer](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-12.pt_br.png)
![Adjusted frame 3 in Captions layer](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-13.pt_br.png)
![Adjusted frame 4 in Captions layer](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-14.pt_br.png)

Adição de uma camada animada (Céu)
--------------------------------

A essa altura do campeonato, todos os desenhos que não pertencem às camadas *Paisagem* ou *Legendas*
estão inseridos na linha *Padrão* do painel.
De fato, *Padrão* não é exatamente uma camada: é um aglomerado de camadas que não foram ativadas na linha do tempo. Esse
aglomerado pode conter também elementos que não pertencem a nenhuma camada (pode acontecer, mas sugerimos que evite isso).
Toda vez que uma nova camada é criada no documento SVG do Inkscape, ela automaticamente fica inserida no Sozi
através da linha *Padrão*.

Pressione o botão *Adicionar camada* e escolha *Céu*.
A linha *Padrão* irá desaparecer.

Para facilitar, iremos ocultar as camadas *Paisagem* e *Legendas*.
Clique no ícone do "olho" que fica a esquerda da linha dessas camadas.

![Select layer Legendas for frame 1](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-15.pt_br.png)

> O ícone do "olho" permite esconder uma camada no editor para facilitar o trabalho com outras camadas.
> As camadas ocultadas no editor permanecem visíveis quando se exibe a apresentação.
> Caso queira que determinada camada fique oculta durante a apresentação, altere a *Opacidade da camada*.

Repita os procedimentos feitos com a camdada *Legendas*.
Para cada quadro:

1. Na linha *Céu* da linha do tempo, selecione a célula correspondente ao quadro que quer editar.
2. Na área de visualização, dê um zoom (rodinha do mouse), movimente, rotacione (Shift + rodinha do mouse) a camada até que
o retângulo em questão quase ocupe toda a área.
3. Confira o campo *Exposição do elemento Id* e pressione os botões *Ajustar ao elemento*, *Ocultar elemento* e *Cortar*.

Tire do modo oculto as camadas *Paisagem* e *Legendas*.
A área de visualização deve ficar assim:

![Adjusted frame 1 in Sky layer](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-16.pt_br.png)
![Adjusted frame 2 in Sky layer](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-17.pt_br.png)
![Adjusted frame 3 in Sky layer](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-18.pt_br.png)
![Adjusted frame 4 in Sky layer](|filename|/images/tutorial-layers/sozi-layers-tutorial-screenshot-19.pt_br.png)

Salvar e exibir a apresentação
------------------------------

O editor salva a apresentação automaticamente.
Ainda assim, é possível clicar no botão *Salvar* na barra de ferramentas.

Abra o arquivo `tutorial-layers.sozi.html` em um navegador (browser) de internet.
A câmera estára posicionada automaticamente no primeiro quadro da apresentação.
Clique na janela do navegador para movimentar para o próximo quadro.
(veja também: [Apresentar](|filename|play.md)).

[Baixe a apresentação completa](|filename|/presentations/tutorial-layers/tutorial-layers.pt_br.sozi.html)
(Clique com o botão da direita no link e escolha *Salvar link como...*).
