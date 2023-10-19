from constantes import A
from tree_gen import *


def isArrow(grammar : str) -> bool:
    global index
    if grammar[index:index+2] == '->':
        index += 2
        return True
    else:
        return False
    
def isElter(grammar : str) -> bool:
    global index
    if grammar[index] == "'":
        if index >= len(grammar) :
            return False
        else :
            index += 1
        while grammar[index] != "'" and not grammar[index-1] == '\\' : 
            # On ne prend pas en compte les ' qui sont précédés d'un \
            # car ils ne sont pas des délimiteurs
            if index >= len(grammar) :
                return False
            index += 1
        index += 1
        return True
    else:
        return False
    
def isIDnter(grammar : str) -> bool:
    global index
    if grammar[index] in 'SNETF' :
        index += 1
        return True
    else :
        return False


def analyse(node : Node, grammar : str)-> bool :
    global index
    index = 0
    if analyse_aux(node, grammar) and index == len(grammar):
        return True
    else:
        return False

def analyse_aux(node : Node, grammar : str)-> bool :
    global index
    if index == len(grammar) :
        return False
    match node.classe :
        case Classe.Conc :
            if analyse_aux(node.left, grammar) :
                return analyse_aux(node.right, grammar)
            else:
                return False
            
        case Classe.Union :
            if analyse_aux(node.left, grammar) :
                return True
            else:
                return analyse_aux(node.right, grammar)
            
        case Classe.Star :
            while analyse_aux(node.left, grammar) :
                pass
            return True
        
        case Classe.Un :
            if analyse_aux(node.left, grammar) :
                pass
            return True
        
        case Classe.Atom :
            if node.AType == AtomType.Terminal :
                if node.value == '->'  :
                    return isArrow(grammar)
                elif node.value == 'IDnter' :
                    return isIDnter(grammar)
                elif node.value == 'Elter' :
                    return isElter(grammar)
                elif node.value == grammar[index] :
                    index += 1
                    return True
                else :
                    return False
                
            else : #NonTerminal
                match node.value :
                    case 'S':
                        next_node = A[0]
                    case 'N':
                        next_node = A[1]
                    case 'E':
                        next_node = A[2]
                    case 'T':
                        next_node = A[3]
                    case 'F':
                        next_node = A[4]
                    case other :
                        return False
                return analyse_aux(next_node, grammar)
    
                    
                
            
        