Title: Traduzindo o web site para sua língua nativa
Slug: translate-web-site
Lang: pt_br
Status: hidden
Authors: Guillaume Savaton, Vincent Garibal, Marcelo Vaz Pupo

O website do Sozi é um site estático gerado com o [Pelican](http://blog.getpelican.com/).
Ele não oferece um editor online para fazermos a tradução.

Os arquivos fonte do site são arquivos texto que usam a sintaxe [Markdown](http://daringfireball.net/projects/markdown/syntax).
Estes arquivos estão hospedados no [repositório do site do Sozi no GitHub](https://github.com/senshu/Sozi-website), na pasta
[content/](https://github.com/senshu/Sozi-website/tree/master/content) folder.
A pasta [content/pages/](https://github.com/senshu/Sozi-website/tree/master/content/pages) contém
a documentação do Sozi.
Ela está dividida em subpastas por idioma (`en` para inglês, `fr` para francês, etc)
contendo arquivos Markdown.

Para iniciar a tradução, sugerimos que siga os seguintes passos:

1. [Bifurque (Fork) o repositório](https://github.com/senshu/Sozi-website/fork).
2. Crie uma subpasta para seu idioma em `content/pages/`, caso ela ainda não exista.
3. Se quiser traduzir uma pagina, encontre a versão original em inglês na pasta `en` e crie um novo arquivo com o mesmo nome na subpasta de seu idioma.
4. Edit the new file.
5. Optionally, you can use Pelican to generate your own copy of the site and preview your modifications.
6. When you are satisfied with the result, commit and push your changes to your GitHub repository and send a pull request to the official Sozi repository.

The header of a translated Markdown file should contain the following fields:

* `Title`: the title of the original page, translated to your language.
* `Author`: comma-separated list of original authors and translators.
* `Slug`: same as the original file.
* `Lang`: the language code of the translation.
* `Translation`: must be set to `true`.
