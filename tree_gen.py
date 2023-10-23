from enum import Enum

class AtomType(Enum):
    """Classe qui permet de représenter le type de noeud atom
    soit un terminal, soit un non terminal

    Args:
        Enum (class): Classe de base d'énumération
    """
    Terminal = 1
    NonTerminal = 2
    

class Classe(Enum):
    """Classe qui permet de représenter le type d'un noeud d'un arbre

    Args:
        Enum (class): Classe de base d'énumération
    """
    Conc = 1
    Union = 2
    Star = 3
    Un = 4
    Atom = 5
    

class Node:
    """Classe qui permet de représenter un noeud d'un arbre
    """
    def __init__(self, left = None, right = None, classe = None, action = None, value = None, AType = None):
        self.left = left
        self.right = right
        self.classe = classe
        self.action = action
        self.value = value
        self.AType = AType
        

def gen_conc(left : Node, right : Node) -> Node:
    """Fonction qui permet de générer un noeud de type concaténation

    Args:
        left (Node): Noeud gauche
        right (Node): Noeud droit

    Returns:
        Node: Noeud concaténation
    """
    new_node = Node(left, right, Classe.Conc,  value= '.')
    return new_node

def gen_union(left : Node, right : Node) -> Node:
    """Fonction qui permet de générer un noeud de type union
    
    Args:
        left (Node): Noeud gauche
        right (Node): Noeud droit

    Returns:
        Node: Noeud union
    """
    new_node = Node(left, right, Classe.Union,  value= '+')
    return new_node

def gen_star(left : Node) -> Node:
    """Fonction qui permet de générer un noeud de type star

    Args:
        left (Node): Noeud gauche

    Returns:
        Node: Noeud star
    """
    new_node = Node(left, classe = Classe.Star,  value= '*')
    return new_node

def gen_un(left : Node) -> Node:
    """Fonction qui permet de générer un noeud de type un

    Args:
        left (Node): Noeud gauche

    Returns:
        Node: Noeud un
    """
    new_node = Node(left, classe = Classe.Un, value= '(//)')
    return new_node

def gen_atom(value : str, action : int, AtomType : AtomType) -> Node:
    """Fonction qui permet de générer un noeud de type atom

    Args:
        value (str): Valeur du noeud
        action (int): Action du noeud
        AtomType (AtomType): Type du noeud

    Returns:
        Node: Noeud atom
    """
    new_node = Node(classe = Classe.Atom, action = action, value = value, AType = AtomType)
    return new_node 
