# Formation Power BI

## Installer Power BI

* Windows --> Microsoft Store ou Website
* Linux ou Mac --> Microsoft Power BI website

## Cours

### Question à se poser

---

1. **Quoi** : Quelles sont les données que votre utilisateur souhaite visualiser ?  
En fonction de celles-ci, vous ne vous choisirez pas le même type de visualisation.
2. **Pourquoi** : Pourquoi votre utilisateur souhaite visualiser ces données ?  
Cette question a une incidence forte sur le choix de la visualisation et l'interaction que vous devez mettre en place.  
Souhaite-il identifier une tendance ? des corrélations entre des variables ? rechercher une valeur particulière ?
3. **Comment** : Enfin, demandez-vous comment présenter les données à votre utilisateur.  
Souhaite-t-il les afficher triées ? filtrées ?  
Souhaite-t-il afficher tous les points de données, ou les agréger dans des groupes de valeurs ?

### Évitez les erreurs

---

* [Site qui ressence les erreurs de diagramme](https://viz.wtf)

### Astuces

---

* [Librairie de visualisation gratuit](https://appsource.microsoft.com/fr-fr/marketplace/apps?page=1&product=power-bi-visuals&exp=ubp8)
* Visualisations -> Mettre en forme votre visuel (logo avec un pinceau) - [Personalisé les diagrammes]
* Visualisations -> Mettre en forme votre visuel (logo avec un pinceau) -> Étiquettes des données - [Accès dynamique des données par exemple des acceptations ou des refus de demandes]
* Visualisations -> Mettre en forme votre visuel (logo avec un pinceau) -> Éléments de cellule -> Couleur d'arrière plan - [Ajout d'une règle pour surligner un élément important parmi tant d'autre]
* Format -> Modifier les interractions -> filtre / aucun - [Synchroniser ou non les filtres d'un diagramme]

* **Export :**

1. Dans Power BI Desktop, sélectionnez Fichier > Options et paramètres > Options.
2. Dans le volet de navigation gauche de la fenêtre Options, en bas de la section Fichier actuel, sélectionnez Paramètres des rapports.
3. En bas à droite, sous Extraction interrapport, cochez la case "Autoriser les visuels de ce rapport à utiliser des cibles d’extraction d’autres rapports".

### Bonnes pratiques

---

#### Camembert / Graphique en secteurs

* Veillez toujours à ce que les proportions soient respectées.
* Utilisez des légendes claires.
* Affichez les non-réponses pour ne pas laisser supposer que votre échantillon est complet.

#### Graphique en courbes

* Utilisez un axe des ordonnées continu, ou affichez clairement le saut de données sur le graphique.
* Utilisez une légende !

#### Histogramme

* Respectez les proportions sur vos visuels, même si les valeurs sont indiquées.
* Une flèche vers le bas sera interprétée par tous comme une baisse, faites attention à l’utilisation de ce type de formes sur vos graphiques.

### Avantages des diagrammes

---

#### Les graphiques en secteurs

✅ Simples à utiliser pour représenter un tout comme la somme de ses éléments.  
⚠️ Difficiles pour l’œil de comparer la taille des parts de camembert.  
⚠️ Au-delà de 4 parts, ils deviennent illisibles.

#### Les graphiques en courbes

✅ Très pratiques pour représenter l’évolution d’une variable numérique.  
⚠️ Lorsqu’il y a trop de courbes superposées, on risque l’effet "plat de spaghettis".

#### Les graphiques en barres

✅ C’est le graphique le plus efficace pour représenter des valeurs numériques par catégorie.  
⚠️ Les données sont souvent regroupées, ce qui peut influencer l’interprétation de l’utilisateur final.  
⚠️ Si les données ne sont pas triées, ils peuvent être difficiles à lire.

#### Les "treemaps"

✅ L'utilisation optimale de l’espace permet de représenter beaucoup de données simultanément.  
⚠️ S’il n’y a pas de variance dans vos données, cela a peu d’intérêt.

#### Les maps

✅ Elles permettent de projeter l’utilisateur final dans son environnement.  
⚠️ Illisibles s’il y a trop de points.  
⚠️ Les cartes disposent souvent de couleurs de base (la mer, le continent...), attention donc à la gestion de vos couleurs.

### Power Query Editor / Langage M

---

### +

---

Si vous souhaitez aller plus loin :

Le [site d’apprentissage de Microsoft sur Power BI](https://docs.microsoft.com/learn/paths/prepare-data-power-bi/?wt.mc_id=openclassrooms_learncontent_webpage_wwl) dispose de ressources de qualité pour compléter votre formation.

La [documentation en ligne de Microsoft Power BI](https://docs.microsoft.com/fr-fr/power-bi/) doit être votre référence lorsque vous souhaitez utiliser de nouvelles fonctionnalités et formules.

Si vous souhaitez conclure votre apprentissage par [la certification "PL-300 : Power BI Data Analyst" de Microsoft](https://learn.microsoft.com/fr-fr/certifications/power-bi-data-analyst-associate/), vous pouvez suivre les parcours d’apprentissage proposés par Microsoft. Vous y trouverez tous les compléments nécessaires pour vous préparer !

La [chaîne YouTube de Curbal](https://www.youtube.com/channel/UCJ7UhloHSA4wAqPzyi6TOkw) regorge d’astuces très utiles à connaître et d’exemples très sympas à suivre, comme son dashboard de suivi de la Coupe du monde de football en 2018.

Le [blog de Carl](https://carldesouza.com/power-bi/) de Souza contient également de nombreux tutoriels pour les fonctions de Power BI, des plus simples aux plus avancées.
