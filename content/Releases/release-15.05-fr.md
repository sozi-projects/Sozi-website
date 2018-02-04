Title: Sozi 15.05 est disponible pour les testeurs et traducteurs
Date: 2015-05-15
Slug: release-15.05
Lang: fr
Author: Guillaume Savaton
Summary:
    Voici la première sortie officielle de Sozi 15.
    Bien qu'il ne s'agisse plus d'un prototype, cette version est
    cependant destinée principalement aux testeurs.

Un nouvel éditeur de présentation était en développement depuis le début de l'année 2014.
Le développement a été relativement lent et [un premier prototype a été officiellement
annoncé en octobre 2014](|filename|release-14.10.md).
En 2015, il a été suivi par une longue série de corrections et d'améliorations.
Plusieurs utilisateurs ont commencé à l'utiliser quotidiennement, ont rencontré des problèmes
et m'ont aidé à les corriger.

Sozi 15.05 est la version la plus récente de cette série.
Je pense que c'est le bon moment pour la publier officiellement afin qu'un plus grand nombre
de personnes puissent l'essayer, la traduire, l'empaqueter, et signalent les éventuels problèmes
non détectés jusqu'à présent.

Quelles sont les nouveautés dans Sozi 15&nbsp;?
-----------------------------------------------

Jusqu'à la version 13.11, l'éditeur de Sozi se présentait sous la forme d'une extension pour Inkscape.
Le système d'extensions d'Inkscape n'était pas conçu pour ce type d'usage, si bien que Sozi était
mal intégré dans Inkscape et l'expérience utilisateur était plutôt pauvre.
De plus, l'éditeur dépendait de plusieurs autres frameworks et bibliothèques
(Python 2.7, GTK2, PyGTK) qui devaient être installés manuellement sous Windows et OS X.
Certains sont à présent obsolètes.
Pour toutes ces raisons, Sozi a été presqu'entièrement récrit avec les préoccupations suivantes&nbsp;:

* L'éditeur n'est plus une extension pour Inkscape. C'est une application autonome qui peut être utilisée avec n'importe quel éditeur SVG.
* Son interface utilisateur permet d'éditer les vues et de gérer les calques visuellement.
* Il ne modifie pas le document SVG original mais enregistre la présentation dans un fichier HTML séparé.
* Il est plus facile à installer sous Windows et OS X.
* Il repose sur les technologies du web (HTML, JavaScript, SVG).

Une nouvelle interface utilisateur
----------------------------------

Trois panneaux de l'éditeur permettent la création et la modification des vues&nbsp;:

* Le panneau de chronologie (en bas) est organisée comme un tableau dans lequel chaque ligne représente
  un calque et chaque colonne représente une vue.
  Sélectionnez les vues et calques avec la souris.
  Utilisez les touches `Shift` et `Ctrl` pour effectuer des sélections multiples.
* Le panneau de prévisualisation (en haut à gauche) représente la vue courante.
  Utilisez la souris pour déplacer, zoomer ou faire tourner la caméra dans les calques sélectionnés,
  ou pour rogner le contenu de la vue courante.
* Le panneau des propriétés (en haut à droite) permet de modifier différentes propriétés des
  vues et transitions.

Il n'est plus nécessaire de dessiner des rectangles pour délimiter les vues, mêmes si cela peut
faciliter les choses dans certains cas.
Une documentation sur ce sujet sera bientôt disponible.

L'éditeur enregistre la présentation automatiquement à chaque fois que la fenêtre perd le focus
et en quittant.
Si vous modifiez le document SVG pendant que Sozi est ouvert, le document sera automatiquement
rechargé lorsque Sozi recevra à nouveau le focus.
Si l'enregistrement et le rechargement ne sont pas déclenchés automatiquement, vous pouvez
toujours utiliser les boutons *Enregistrer* et *Recharger*.

Un nouveau format de fichier
----------------------------

Si vous avez déjà utilisé des versions précédentes de Sozi, vous remarquerez que le nouvel
éditeur enregistre votre présentation dans des fichiers séparés à côté de votre document SVG.
Par exemple, si votre document SVG original se nomme `ma_presentation.svg`, Sozi 15 créera
deux nouveaux fichiers&nbsp;:

* `ma_presentation.sozi.json` contient les données de la présentation. Il est utilisé en interne par l'éditeur.
* `ma_presentation.sozi.html` est la présentation Sozi complète. Ouvrez-la dans un navigateur web pour l'afficher.

Techniquement, le fichier HTML contient une copie de votre document SVG, une copie des données de
la présentation et le logiciel de visionnage.
Il s'agit d'un document autonome&nbsp;: si vous voulez partager une présentation, vous n'avez pas
besoin de fournir les fichiers SVG et JSON.

Sozi 15 peut importer les présentations créées avec Sozi 13.

Problèmes connus
----------------

La version courante du nouvel éditeur n'affiche pas les images liées à votre document.
Les documents SVG dans lesquels des images ont été incorporées sont affichés correctement
mais ils peuvent être long à charger s'ils contiennent un grand nombre d'images volumineuses.

Essayez Sozi 15 dès maintenant&nbsp;!
-------------------------------------

Sozi 15 peut se présente sous deux formes&nbsp;:

* [Une application native que vous pouvez installer sur votre ordinateur](https://github.com/senshu/Sozi/releases/tag/15.05-preview).
  Choisissez le fichier zip correspondant à votre plate-forme, décompressez-le et lancez l'exécutable `Sozi`.
* [Une application web que vous pouvez exécuter dans votre navigateur](/demo)
  (nécessite un compte Google Drive pour enregistrer vos présentations).

Contribuez
----------

[Signalez les problèmes](https://github.com/senshu/Sozi/issues) que vous rencontrez
ou proposez des améliorations.
Merci d'indiquer clairement que vous utilisez Sozi 15.

[Traduisez Sozi](|filename|/pages/fr/translate-editor.md) dans votre langue maternelle.
