from enum import Enum

# Utilisé pour le dessin de l'arbre
from dsplot import tree
class AtomType(Enum):
    Terminal = 1
    NonTerminal = 2

AtomType = Enum('AtomType', ['Terminal', 'NonTerminal'])

class Node:
    '''
    Classe qui permet de représenter un noeud d'un arbre
    '''
    def __init__(self, left = None, right = None, classe = None, action = None, value = None, AType = None):
        self.left = left
        self.right = right
        self.classe = classe
        self.action = action
        self.value = value
        self.AType = AType
        

def gen_conc(left : Node, right : Node) -> Node:
    '''
    Fonction qui permet de générer un noeud de type concaténation
    '''
    new_node = Node(left, right, 'conc',  value= '.')
    return new_node

def gen_union(left : Node, right : Node) -> Node:
    new_node = Node(left, right, 'union',  value= '+')
    return new_node

def gen_star(left : Node) -> Node:
    new_node = Node(left, None, 'star',  value= '*')
    return new_node

def gen_un(left : Node) -> Node:
    new_node = Node(left, None, 'un', value= '(\\\\)')
    return new_node

def gen_atom(value : str, action : int, AtomType : AtomType) -> Node:
    new_node = Node(None, None, 'atom', action, value, AtomType)
    return new_node 

def tree_print(tree : Node):
    '''
    Fonction qui permet d'afficher un arbre dans la console
    '''
    tree_print_aux(tree)
    print()

def tree_print_aux(tree : Node):
    if tree.classe=='star':
        print('[', end = ' ')
    elif tree.classe=='un':
        print('(\\', end = ' ')
    if tree.left != None:
        tree_print_aux(tree.left)
    
    if tree.classe=='star':
        print(']', end = ' ')
    elif tree.classe=='un':
        print('\\)', end = ' ')
    else :
        print(tree.value, end = ' ')
    
    if tree.right != None:
        tree_print_aux(tree.right)
    return

def draw_tree(tree):
    draw_tree_aux(tree,0)
    print()
    
def draw_tree_aux(tree, level):
    if tree.left != None:
        draw_tree_aux(tree.left, level+1)
    print('   '*level, end = ' ')
    print(tree.value)
    if tree.right != None:
        draw_tree_aux(tree.right, level+1)
    return


    
    

A1 = gen_conc(gen_star(gen_conc(gen_conc(gen_conc(gen_atom('N',0,AtomType.NonTerminal),gen_atom("'->'",0,AtomType.Terminal)),gen_atom('E',0,AtomType.NonTerminal)),gen_atom("','",0,AtomType.Terminal))),gen_atom("';'",0,AtomType.Terminal))
A2 = gen_atom("'IDnter'",0,AtomType.Terminal)
A3 = gen_conc(gen_atom('T',0,AtomType.NonTerminal),gen_star(gen_conc(gen_atom("'.'",0,AtomType.Terminal),gen_atom('T',0,AtomType.NonTerminal))))
A4 = gen_conc(gen_atom('T',0,AtomType.NonTerminal),gen_star(gen_conc(gen_atom("'+'",0,AtomType.Terminal),gen_atom('T',0,AtomType.NonTerminal))))
A5 = gen_union(gen_union(gen_union(gen_union(gen_atom("'IDnter'",0,AtomType.Terminal),gen_atom("'Elter'",0,AtomType.Terminal)),gen_conc(gen_atom("'('",0,AtomType.Terminal),gen_conc(gen_atom('E',0,AtomType.NonTerminal),gen_atom("')'",0,AtomType.Terminal)))),gen_conc(gen_atom("'['",0,AtomType.Terminal),gen_conc(gen_atom('E',0,AtomType.NonTerminal),gen_atom("']'",0,AtomType.Terminal)))),gen_conc(gen_atom("'(/'",0,AtomType.Terminal),gen_conc(gen_atom('E',0,AtomType.NonTerminal),gen_atom("'/)'",0,AtomType.Terminal))))

#draw_tree(A5)


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
            list_value.append([tree.value])
        else :
            list_value[index].append(tree.value)
        read_tree_to_list_for_dsplot_aux(tree.left, list_value, index+1)
        read_tree_to_list_for_dsplot_aux(tree.right, list_value, index+1)
    
tree_A1 = tree.BinaryTree(read_tree_to_list_for_dsplot(A1))
tree_A1.plot(output_path="A1.png")

tree_A2 = tree.BinaryTree(read_tree_to_list_for_dsplot(A2))
tree_A2.plot(output_path="A2.png")

tree_A3 = tree.BinaryTree(read_tree_to_list_for_dsplot(A3))
tree_A3.plot(output_path="A3.png")

tree_A4 = tree.BinaryTree(read_tree_to_list_for_dsplot(A4))
tree_A4.plot(output_path="A4.png")

tree_A5 = tree.BinaryTree(read_tree_to_list_for_dsplot(A5))
tree_A5.plot(output_path="A5.png")





