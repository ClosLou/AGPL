from tree_gen import Node, AtomType, Classe
# Utilisé pour le dessin de l'arbre
from dsplot import tree

def tree_print(tree : Node, sep : str = ' '):
    '''
    Fonction qui permet d'afficher un arbre dans la console
    '''
    tree_print_aux(tree, sep)
    print()

def tree_print_aux(tree : Node, sep : str = ' '):
    '''
    Fonction auxiliaire qui permet d'afficher un arbre dans la console
    il s'agit d'un parcours préfixe de l'arbre avec des test afin de savoir si on doit 
    afficher un crochet pour les neouds de type star ou une parenthèse et une bare 
    oblique pour les noeuds de type un 
    
    '''
    if tree.classe==Classe.Star:
        print('[', end = sep)
    elif tree.classe==Classe.Un:
        print('(\\', end = sep)
    if tree.left != None:
        tree_print_aux(tree.left, sep)
    
    if tree.classe==Classe.Star:
        print(']', end = sep)
    elif tree.classe==Classe.Un:
        print('\\)', end = sep)
    else :
        if tree.classe==Classe.Atom:
            if tree.AType == AtomType.Terminal:
                print("'",tree.value,"'", sep='', end = sep)
            else:
                print(tree.value, end = sep)
        else:
            print(tree.value, end = sep)
    
    if tree.right != None:
        tree_print_aux(tree.right, sep)
    return

def draw_tree(tree):
    draw_tree_aux(tree,0)
    print() # affichage d'une fin de ligne
    
def draw_tree_aux(tree, level):
    if tree.classe==Classe.Atom:
        if tree.AType == AtomType.Terminal:
            print('---'*level,"'",tree.value,"'", sep='')
        else:
            print('---'*level,tree.value, sep='')
    else:
        print('---'*level,tree.value, sep='')
    if tree.left != None:
        draw_tree_aux(tree.left, level+1)
    if tree.right != None:
        draw_tree_aux(tree.right, level+1)
    return

 
def read_tree_to_list_for_dsplot(tree):
    '''
    Fonction qui permet de lire un arbre et de le retourner sous forme de liste 
    dans le format de dsplot.tree.BinaryTree
    '''
    list_value = []
    read_tree_to_list_for_dsplot_aux(tree, list_value, 0)
    if len(list_value[-1]) == list_value[-1].count(None):
        list_value.pop()
    return sum(list_value,[])

def read_tree_to_list_for_dsplot_aux(tree, list_value, index):
    '''
    Fonction auxiliaire qui permet de lire un arbre et de le retourner sous forme de liste 
    les valeurs sont stockées en fonction de leur niveau dans l'arbre
    '''
    if tree == None:
        if len(list_value) <= index:
            list_value.append([None])
        else :
            list_value[index].append(None)
        return 
    else :
        if len(list_value) <= index:
            if tree.classe==Classe.Atom:
                if tree.AType == AtomType.Terminal:
                    list_value.append(["'"+tree.value+"'"])
                else:
                    list_value.append([tree.value])
            else:
                list_value.append([tree.value])
        else :
            if tree.classe==Classe.Atom:
                if tree.AType == AtomType.Terminal:
                    list_value[index].append("'"+tree.value+"'")
                else:
                    list_value[index].append(tree.value)
            else:
                list_value[index].append(tree.value)
        read_tree_to_list_for_dsplot_aux(tree.left, list_value, index+1)
        read_tree_to_list_for_dsplot_aux(tree.right, list_value, index+1)

def create_tree_dsplot(node_tree, output_path):
    '''
    Fonction qui permet de créer un plot de l'arbre tree avec dsplot.tree.BinaryTree
    et de le sauvegarder dans un fichier png à l'adresse output_path
    '''
    tree_dsplot = tree.BinaryTree(read_tree_to_list_for_dsplot(node_tree))
    tree_dsplot.plot(output_path=output_path)
    return





