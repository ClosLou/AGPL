from enum import Enum

class AtomType(Enum):
    Terminal = 1
    NonTerminal = 2

AtomType = Enum('AtomType', ['Terminal', 'NonTerminal'])

class Node:
    def __init__(self, left = None, right = None, classe = None, action = None, value = None, AType = None):
        self.left = left
        self.right = right
        self.classe = classe
        self.action = action
        self.value = value
        self.AType = AType
        

def gen_conc(left, right):
    new_node = Node(left, right, 'conc',  value= '.')
    return new_node

def gen_union(left, right):
    new_node = Node(left, right, 'union',  value= '+')
    return new_node

def gen_star(left):
    new_node = Node(left, None, 'star',  value= '*')
    return new_node

def gen_un(left):
    new_node = Node(left, None, 'un', value= '(\\\\)')
    return new_node

def gen_atom(value, action, AtomType):
    new_node = Node(None, None, 'atom', action, value, AtomType)
    return new_node 

def tree_print(tree):
    tree_print_aux(tree)
    print()

def tree_print_aux(tree):
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

draw_tree(A5)