Title: Inclure une vidéo ou un extrait audio dans une présentation
Slug: tutorial-media
Lang: fr
Authors: Guillaume Savaton
Status: hidden

Vous pouvez insérer de la vidéo et de l'audio dans un présentation Sozi,
voire même dans n'importe quel document SVG, en utilisant l'extension
*Add video or audio* pour Inkscape.

Installation
------------

1. Téléchargez le fichier `Sozi-extras-media-[...].zip`
   de la [version la plus récente de Sozi](https://github.com/senshu/Sozi/releases/).
2. L'archive zip contient deux fichiers&nbsp;: `sozi_extras_media.inx` et `sozi_extras_media.py`.
   Décompressez-les dans le dossier d'extensions d'Inkscape&nbsp;:
    * pour Linux et OS X&nbsp;: `~/.config/inkscape/extensions`,
    * pour Windows&nbsp;: `C:\Program Files\Inkscape\share\extensions`,
3. Ouvrez Inkscape. Dans le menu *Extensions*, vous devez trouver un sous-menu *Sozi extras* proposant l'action *Add video or audio*.

Utilisation
-----------

Lorsque vous ajoutez un nouvel élément video ou audio à un document SVG, l'interface vous demande
de fournir les informations suivantes&nbsp;:

* *Media element*&nbsp;: *video* ou *audio*.
* *Width*&nbsp;: la largeur de l'élément, en pixels.
* *Height*&nbsp;: la hauteur de l'élément, en pixels.
* *MIME type*&nbsp;: le type du media (par exemple, `video/mp4` ou `audio/ogg`).
* *File name or URL*&nbsp;: l'emplacement du fichier contenant le media.
* *Play automatically in Sozi frame*&nbsp;: cochez la case pour démarrer automatiquement le media en entrant
  dans une certaine vue d'une présentation Sozi.
* *Start playing when entering frame (id)*&nbsp;: l'identifiant de la vue où le media doit démarrer automatiquement.
* *Stop playing when entering frame (id)*&nbsp;: l'identifiant de la vue où le media doit s'arrêter automatiquement.

Exemple
-------

La présentation ci-dessous joue une vidéo dans la deuxième vue et un extrait audio
dans la troisième.
[Télécharger les fichiers de la présentation]({static}/presentations/tutorial-media.zip).

<iframe class="sozi" src="{static}/presentations/tutorial-media/tutorial-media.sozi.html">
    Your browser cannot display this content.
</iframe>

Prise en charge par les navigateurs
-----------------------------------

Techniquement, cette fonctionnalité repose sur les éléments HTML5 `<video>` et `<audio>`
qui peuvent être insérés dans un document SVG.
Les navigateurs web n'acceptent pas les mêmes formats de media.
Consultez la page suivante pour plus d'informations&nbsp;:
[Formats Media supportés par les éléments HTML audio et vidéo (Mozilla Developer Network)](https://developer.mozilla.org/fr/docs/Web/HTML/formats_media_support).

> Actuellement, Chrome (version 33) n'applique pas les transformations géométriques
> (rotation, échelle, translation) aux éléments vidéo et audio présents dans un document SVG.
> Ils apparaîtront toujours dans le coin supérieur gauche de la fenêtre du navigateur.
> Il semple que seul Firefox les affiche correctement.
