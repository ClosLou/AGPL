from enum import Enum

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
