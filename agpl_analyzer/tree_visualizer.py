from agpl_analyzer.tree_gen import Node, AtomType, Classe

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

