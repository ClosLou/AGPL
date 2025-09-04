# Projet AGPL

## Contexte du Projet

Ce projet a été réalisé dans le cadre du Master Bioinformatique de Nantes Université durant l'année universitaire 2023-2024. Il s'agit d'un analyseur de grammaire développé pour un petit langage, sous la supervision du Professeur Mourad Oussalah.

### Auteurs

*   **Louis Closson** - [clossonlouis@gmail.com](mailto:clossonlouis@gmail.com)
*   **Louise Helary**
*   **Louis Troussé**

### Encadrant

*   **Mourad Oussalah** - [mourad.oussalah@univ-nantes.fr](mailto:mourad.oussalah@univ-nantes.fr)

---

Programme d'analyse de grammaire pour un petit langage. Le projet est structuré en plusieurs modules Python pour une meilleure organisation du code.

-   `main.py`: Le point d'entrée du programme. Il fournit un menu interactif pour tester différentes fonctionnalités de l'analyseur.
-   `agpl_analyzer/`: Un package Python contenant toute la logique de l'analyseur.
    -   `analyse_modules.py`: Contient les fonctions principales pour l'analyse syntaxique de la grammaire.
    -   `grammar_builder.py`: Définit et construit les arbres de la métagrammaire utilisée pour l'analyse.
    -   `tree_visualizer.py`: Fournit des fonctions pour un affichage textuel des arbres dans la console (`tree_print`, `draw_tree`).
    -   `dsplot_visualizer.py`: (Optionnel) Module séparé pour la génération d'images des arbres. Il dépend de `dsplot` et `Graphviz`.
    -   `tree_gen.py`: Contient la définition de la classe `Node` pour les arbres et les fonctions permettant de générer les différents types de nœuds.
-   `output/`: Dossier où sont sauvegardées les images des arbres générés.

## Getting Started

L'analyseur de grammaire principal ne nécessite aucune dépendance externe pour fonctionner. 

Cependant, le projet inclut un module optionnel (`dsplot_visualizer.py`) pour visualiser les arbres de grammaire sous forme d'images (`.png`). Si vous souhaitez utiliser cette fonctionnalité, vous devrez installer les dépendances décrites ci-dessous.

### Prérequis

-   Python 3.x
-   Graphviz

### Installation

1.  **Clonez le dépôt :**
    ```bash
    git clone ""
    cd agpl_project
    ```

2.  **Installez les dépendances optionnelles (pour la visualisation graphique) :**
    Le fichier `requirement.txt` contient le package `dsplot`.
    ```bash
    pip install -r requirement.txt
    ```

3.  **Installez Graphviz (pour la visualisation graphique) :**
    Graphviz est utilisé par `dsplot` pour générer les images des arbres.

    -   **Sur Windows :**
        Vous pouvez l'installer avec Chocolatey :
        ```bash
        choco install graphviz
        ```
        Ou téléchargez-le depuis le [site officiel de Graphviz](https://graphviz.org/download/) et assurez-vous d'ajouter le répertoire `bin` de Graphviz à votre `PATH`.

    -   **Sur macOS :**
        Avec Homebrew :
        ```bash
        brew install graphviz
        ```

    -   **Sur Linux (Debian/Ubuntu) :**
        ```bash
        sudo apt-get update
        sudo apt-get install graphviz libgraphviz-dev
        ```

## Utilisation

Pour lancer le programme, exécutez le script `main.py` :
```bash
python main.py
```
Un menu vous guidera pour choisir entre l'analyse de grammaires et l'affichage textuel des arbres de la métagrammaire.

### Visualisation Graphique (Optionnel)

La génération d'images des arbres n'est pas intégrée au menu principal pour ne pas imposer l'installation de dépendances supplémentaires.

Si vous avez installé `dsplot` et `Graphviz` (voir la section `Installation`), vous pouvez facilement générer les images des arbres en utilisant le script fourni.

Exécutez simplement le script `script_visualisation.py` :
```bash
python script_visualisation.py
```
Les images (`.png`) de chaque règle de la grammaire seront sauvegardées dans le dossier `output/`.
