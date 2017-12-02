Title: Traduire l'interface utilisateur de l'éditeur dans votre langue
Slug: translate-editor
Lang: fr
Status: hidden
Author: Guillaume Savaton

Les traductions du texte affiché dans l'éditeur de présentation sont définies dans des
fichiers *PO* compatibles avec [GNU gettext](https://www.gnu.org/software/gettext/).
Vous pouvez participer à la traduction de Sozi de deux manières&nbsp;:

En utilisant l'interface en ligne chez Launchpad.net
----------------------------------------------------

Inscrivez-vous chez [launchpad.net](https://launchpad.net/)
et visitez [la page de traduction de Sozi](https://translations.launchpad.net/sozi).
Vous pouvez commencer à traduire immédiatement.
Quand votre travail est terminé, merci d'[ouvrir un ticket](https://github.com/senshu/Sozi/issues)
pour demander à ce que la nouvelle traduction soit ajoutée à la version suivante de Sozi.

> Même lorsque 100% des chaînes sont marquées comme traduites dans Launchpad, nous
> ne pouvons pas savoir si cette version est prête à être publiée.
> Nous ne publierons votre traduction que si vous en faites la demande.


En éditant les fichiers PO directement
--------------------------------------

Créez un fork du [dépôt de code source chez GitHub](https://github.com/senshu/Sozi).
Les fichiers *PO* de Sozi 15 sont situés dans le dossier `locales`.

Vous pouvez éditer les fichiers *PO* à l'aide d'un éditeur de texte généraliste
ou en utilisant un éditeur spécialisé comme [Poedit](http://poedit.net/).
Si vous voulez ajouter un fichier de traduction pour une nouvelle langue,
créez une copie du fichier `locales/messages.pot`.
Nommez ce fichier en utilisant le [code IETF](http://www.langtag.net/) approprié
et en lui ajoutant l'extension `.po`.

Quand votre travail est terminé, merci de nous envoyer une *pull request*.
