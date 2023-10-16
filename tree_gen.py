# 1) création classe operations
from enum import Enum # traducteur pour ordinateur des choix quali

class Atom_type(Enum):
    NonTerminal = 1 # nonterminal traduit pour ordi en 1
    Terminal = 2

Atom_type = Enum('Atom_type', ['NonTerminal','Terminal']) # défini un type

class Classe(Enum):
    conc  = 1
    star  = 2
    union = 3
    un    = 4
    atom  = 5 


class Node:
    def __init__(self, left = 'None', right = 'None', classe = 'None', action = 'None',
                Atype = 'None', value = 'None'): # constructeur, Atype : stock du type 
        self.action = action
        self.left = left
        self.right = right
        self.value = value
        self.Atype = Atype
        self.classe = classe

# 2) ecriture de chaque fonction operation

def GenConc(left : Node, right : Node) -> Node: # '->' ce que la fonction doit retournée
    '''
    Fonction qui permet de générer un noeud de type concaténation
    '''
    new_node = Node(left, right, Classe.conc,  value= '.')
    return new_node

def GenUn(left : Node) -> Node:
    '''
    Fonction qui permet de générer un noeud de type Un où une seule branche gauche est présente
    '''
    new_node = Node(left, None, Classe.un, value = '////')
    return new_node

def GenUnion(left: Node, right: Node) -> Node:
    '''
    Fonction qui permet de générer un noeud de type Union
    '''
    new_node = Node(left,right, Classe.union,value = '+')
    return new_node

def GenStar(left : Node) -> Node:
    '''
    Fonction qui permet de générer un noeud de type Star
    '''
    new_node = Node(left, None, Classe.star, value = '*')
    return new_node

def GenAtom(value : str, action : int, Atype : Atom_type ) -> Node:
    '''
    Fonction qui permet de générer un noeud de type Atom
    '''
    new_node = Node(None, None, Classe.atom, action, value, Atom_type)
    return new_node