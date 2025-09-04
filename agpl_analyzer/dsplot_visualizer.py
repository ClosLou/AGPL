from agpl_analyzer.tree_gen import Node, AtomType, Classe
from dsplot import tree

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
