Title: Traduzindo a interface de usuário do editor em sua língua nativa
Slug: translate-editor
Lang: pt_br
Status: hidden
Author: Guillaume Savaton, Marcelo Vaz Pupo

Os textos para tradução do Sozi são definidos como arquivos *PO* compatíveis com
[GNU gettext](https://www.gnu.org/software/gettext/).
Existem duas maneiras caso queira contribuir com as traduções do Sozi:

Usando a interface web em Weblate
----------------------------------------

Crie uma conta em [Weblate](https://hosted.weblate.org)
e entre na [página de tradução do Sozi](https://hosted.weblate.org/projects/sozi/translations/).
É possível traduzir diretamente dessa página.
Quando finalizar seu trabalho, por favor [abra um novo chamado](https://github.com/senshu/Sozi/issues)
para que a nova tradução seja adicionada na próxima versão a ser lançada.

> Mesmo que 100% da tradução esteja realizada, nós não podemos
> ter certeza de que sua tradução está pronta para ser publicada.
> Só publicaremos a tradução se você abrir um chamado solicitando-a.

<a href="https://hosted.weblate.org/engage/sozi/?utm_source=widget">
<img src="https://hosted.weblate.org/widgets/sozi/-/translations/multi-auto.svg" alt="État de la traduction" />
</a>

Editar diretamente nos arquivos PO
-----------------------------

Crie uma bifurcação (Fork) no [repositório fonte do Sozi no GitHub](https://github.com/senshu/Sozi).
Os arquivos *PO* relativos ao Sozi podem ser encontrados na pasta `locales`.

Arquivos *PO* podem ser editados em qualquer editor de texto ou um editor específico para tradução como
o [Poedit](http://poedit.net/).
Caso queira incluir um novo idioma file, crie uma cópia do arquivo `locales/messages.pot`.
Nomeie o arquivo de seu idioma de modo apropriado, usando [o marcador de idioma IETF](http://www.langtag.net/)
e inserindo `.po` como extensão do arquivo.

Quando finalizar o trabalho, não se esqueça de abrir um chamado solicitando publicação da tradução.
