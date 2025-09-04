from agpl_analyzer.tree_gen import Node, AtomType, Classe
# Utilisé pour le dessin de l'arbre
#from dsplot import tree

def tree_print(tree : Node, sep : str = ' ') -> None:
    """Fonction qui permet d'afficher un arbre dans la console


    Args:
        tree (Node): Arbre à afficher
        sep (str, optional): Séparateur entre les noeuds. Par défaut ' '.
    """
    tree_print_aux(tree, sep)
    print()

def tree_print_aux(tree : Node, sep : str) -> None:
    """Fonction auxiliaire qui permet d'afficher un arbre dans la console
    il s'agit d'un parcours préfixe de l'arbre avec des test afin de savoir si on doit 
    afficher un crochet pour les neouds de type star ou une parenthèse et une bare 
    oblique pour les noeuds de type un 

    Args:
        tree (Node): Arbre à afficher
        sep (str, optional): Séparateur entre les noeuds. Par défaut ' '.
    """

    if tree.classe == Classe.Star:
        print('[', end = sep)
    elif tree.classe == Classe.Un:
        print('(/', end = sep)
        
    if tree.left is not None:
        tree_print_aux(tree.left, sep)
    
    if tree.classe == Classe.Star:
        print(']', end = sep)
    elif tree.classe == Classe.Un:
        print('/)', end = sep)
    else :
        if tree.classe == Classe.Atom and tree.AType == AtomType.Terminal:
                print("'",tree.value,"'", sep='', end = sep)
        else:
            print(tree.value, end = sep)
    
    if tree.right is not None:
        tree_print_aux(tree.right, sep)
    return

def draw_tree(tree : Node) -> None:
    """Fonction qui permet de dessiner un arbre dans la console

    Args:
        tree (Node): Arbre à dessiner
    """
    draw_tree_aux(tree, depth=0)
    print() # affichage d'une fin de ligne
    
def draw_tree_aux(tree : Node, depth : int) -> None:
    """Fonction auxiliaire qui permet de dessiner un arbre dans la console

    Args:
        tree (Node): arbre à dessiner
        depth (int): profondeur de l'arbre
    """
    if tree.left is not None:
        draw_tree_aux(tree.left, depth+1)
    if tree.classe == Classe.Atom and tree.AType == AtomType.Terminal:
            print('--- '*depth,"'",tree.value,"'", sep='')
    else:
        print('--- '*depth,tree.value, sep='')
    if tree.right is not None:
        draw_tree_aux(tree.right, depth+1)
    return

 
def read_tree_to_list_for_dsplot(tree : Node) -> list:
    """Fonction qui permet de lire un arbre et de le retourner sous forme de liste 
    dans le format de dsplot.tree.BinaryTree

    Args:
        tree (Node): Arbre à lire
        
    Returns:
        list: Liste des valeurs de l'arbre
    """
    list_value = []
    read_tree_to_list_for_dsplot_aux(tree, list_value, 0)
    if len(list_value[-1]) == list_value[-1].count(None):
        list_value.pop()
    return sum(list_value,[])

def read_tree_to_list_for_dsplot_aux(tree : Node, list_value : list, depth : int):
    """Fonction auxiliaire qui permet de lire un arbre et de le retourner sous forme de liste 
    les valeurs sont stockées en fonction de leur niveau dans l'arbre

    Args:
        tree (Node): Arbre à lire
        list_value (list): Liste des valeurs de l'arbre
        index (int): Niveau de l'arbre
    """
    if tree == None:
        if len(list_value) <= depth:
            list_value.append([None])
        else :
            list_value[depth].append(None)
        return 
    else :
        if len(list_value) <= depth:
            if tree.classe == Classe.Atom:
                if tree.AType == AtomType.Terminal:
                    list_value.append(["'"+tree.value+"'"])
                else:
                    list_value.append([tree.value])
            else:
                list_value.append([tree.value])
        else :
            if tree.classe == Classe.Atom:
                if tree.AType == AtomType.Terminal:
                    list_value[depth].append("'"+tree.value+"'")
                else:
                    list_value[depth].append(tree.value)
            else:
                list_value[depth].append(tree.value)
        read_tree_to_list_for_dsplot_aux(tree.left, list_value, depth+1)
        read_tree_to_list_for_dsplot_aux(tree.right, list_value, depth+1)

def create_tree_dsplot(node_tree : Node, output_path : str):
    """Fonction qui permet de créer un plot de l'arbre tree avec dsplot.tree.BinaryTree
    et de le sauvegarder dans un fichier png à l'adresse output_path

    Args:
        node_tree (Node): Arbre à dessiner
        output_path (str): Chemin du fichier de sortie
    """
    tree_dsplot = tree.BinaryTree(read_tree_to_list_for_dsplot(node_tree))
    tree_dsplot.plot(output_path=output_path)
    return
