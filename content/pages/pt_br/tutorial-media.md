Title: Inserindo vídeo e áudio
Slug: tutorial-media
Lang: pt_br
Author: Guillaume Savaton, Marcelo Vaz Pupo
Translation: true
Status: hidden

É possível inserir vídeo e áudio em uma apresentação do Sozi,
ou mesmo em qualquer documento SVG, usando a extensão *Add video or audio* para Inkscape.

Instalando
----------

1. Baixe o arquivo `Sozi-extras-media-[...].zip`
   a partir da [última versão do Sozi](https://github.com/senshu/Sozi/releases/).
2. O arquivo zip comtém dois documentos: `sozi_extras_media.inx` and `sozi_extras_media.py`.
   Extraia esses documentos para dentro da pasta de extensão do Inkscape:
    * No GNU/Linux e OS X: `~/.config/inkscape/extensions`,
    * No Windows: `C:\Program Files\Inkscape\share\extensions`,
3. Abra o Inkscape. No menu *Extensões*, você verá o submenu *Sozi extras* com o item *Add video or audio*.

Usar a extensão
---------------

Ao incluir um novo elemento de áudio ou vídeo em um documento SVG, as seguintes informações
serão solicitadas:

* *Media element*: *video* ou *audio*.
* *Width*: largura do elemento em pixels.
* *Height*: altura do elemento em pixels.
* *MIME type*: o tipo do arquivo de midia (ex. `video/mp4` ou `audio/ogg`).
* *File name or URL*: localização do arquivo de mídia.
* *Play automatically in Sozi frame*: marque essa caixa para que o Sozi execute automaticamente a mídia
quando determinado quadro da apresentação é exibido.
* *Start playing when entering frame (id)*: a Id do quadro no qual a mídia deverá ser executada automaticamente.
* *Stop playing when entering frame (id)*: a Id do quadro no qual a execução da mídia deverá ser interrompida automaticamente.

Suporte de navegador
--------------------

Tecnicamente esse recurso está baseado nos elementos HTML5 de `<video>` e `<audio>`
que podem ser inseridos em documentos SVG.
Navegadores de internet não têm a mesma configuração de formatos de mídia.
Para mais informações confira a página abaixo:
[Formatos de mídia suportados pelos elementos HTML de áudio e vídeo (Mozilla Developer Network)](https://developer.mozilla.org/en-US/docs/HTML/Supported_media_formats).

> Atualmente o Chrome (como a versão 33) não realiza transformações geométricas
> (rotação, escala, translação) para elementos de vídeo e áudio inseridos em documentos SVG.
> As mídias sempre serão mostradas no canto superior esquerdo da janela do navegador.
> Até onde sabemos, apenas o Firefox lida corretamente com estas transformações.

