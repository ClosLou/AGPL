# Projet AGPL
Programme d'analyse de grammaire de petit langage. Il est découpé
en cinq scripts écrit en langage python :
- **main.py** : mise en commun des différents modules et exécution de l'ensemble du code. 
Un menu a également été ajouté pour améliorer l'expérience de l'utilisateur.
- **analyse_modules.py** : comprend les fonctions d'analyse de grammaire à partir des règles de la métagrammaire
- **constantes.py** : création et stockage des règles de la métagrammaire
- **graphic_modules.py** : fonctions qui permettent d'afficher les arbres de la metagrammaire 
- **tree_gen.py** : définition d'une classe Node et des fonctions permettant d'implémenter chaque opérateur (concaténation, un, union, star, atom)

## Getting started
L'utilisation de la fonction `create_tree_dsplot` du module **graphic_modules.py** nécessite l'installation
du package dsplot et graphviz. <br>
`apt-get install graphviz libgraphviz-dev` <br>

