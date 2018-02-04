Title: Sozi 17.02 est disponible
Date: 2017-03-25
Slug: release-17.02
Lang: fr
Author: Guillaume Savaton
Summary:
    Sozi 17.02 est considérée comme la nouvelle version stable après Sozi 16.02.
    Elle apporte quelques nouvelles fonctionnalités, corriges plusieurs bugs et a été traduite dans deux nouvelles langues.

L'essentiel des nouveautés consiste en corrections de bugs.
Cette nouvelle version n'apporte en réalité qu'une nouvelle fonction&nbsp;:
en jouant une présentation, une pression sur la touche "." (point) bascule
vers un écran noir.

La notion d'*élément de référence* d'une vue était source de confusion.
Elle est toujours utilisée en interne mais n'est désormais plus visible dans l'interface utilisateur.
En complément, l'utilisateur peut à présent définir un *élément de contour*
qui permet d'ajuster les calques sélectionnés à un élément SVG de votre choix
(un rectangle, par exemple).
L'interface utilisateur est très similaire à la version précédente mais son
comportement est légèrement différent et devrait être plus intuitif.

En interne, Sozi repose désormais sur [electron](http://electron.atom.io/),
ce qui a permis de corriger plusieurs problèmes.

Sozi 17.02 est disponible dans 14 langues, y compris le russe et l'italien.
Malheureusement, la plupart des traductions ne sont pas à jour, alors si vous
ne parlez ni anglais, français ou espéranto, vous verrez du texte en anglais,
non traduit, dans l'interface de l'éditeur.

Si vous voulez aider à traduire Sozi dans votre langue, vous trouverez [des instructions](|filename|/pages/fr/translate-editor.md) sur ce site.
N'oubliez pas [d'ouvrir un ticket](https://github.com/senshu/Sozi/issues) si vous voulez ajouter
un nouveau fichier de traduction ou si vous avez modifié un fichier existant.


Utilisez Sozi 17.02 dès maintenant&nbsp;!
-----------------------------------------

Sozi 17 est utilisable sous deux formes&nbsp;:

* [Une application native que vous pouvez installer sur votre ordinateur](https://github.com/senshu/Sozi/releases/tag/17.02).
  Choisissez le fichier zip correspondant à votre plate-forme, décompressez-le et lancez l'exécutable `Sozi`.
* [Une application web que vous pouvez exécuter dans votre navigateur](/demo)
  (nécessite un compte Google Drive pour enregistrer vos présentations).

Contribuez
----------

[Signalez les problèmes](https://github.com/senshu/Sozi/issues) que vous rencontrez
ou proposez des améliorations.
