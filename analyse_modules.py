from constantes import A
from tree_gen import *


def isArrow(grammar : str, local_index : int) -> bool:
    if grammar[local_index:local_index+2] == '->':
        return True
    else:
        return False
    

index = 0
    
def analyse(node : Node, grammar)-> bool :
    global index
    if node.classe == Classe.Conc :
        if analyse(node.left, grammar) :
            return analyse(node.right, grammar)
        else:
            return False
    elif node.classe == Classe.Union :
        if analyse(node.left, grammar) :
            return True
        else:
            return analyse(node.right, grammar)
    elif node.classe == Classe.Star :
        while analyse(node.left, grammar) :
            pass
    elif node.classe == Classe.Un :
        if analyse(node.left, grammar) :
            pass
    elif node.classe == Classe.Atom :
        if node.AType == AtomType.Terminal :
            if node.value == '->'  :
                index += 2
                return isArrow(grammar, index-2)
            elif node.value == 'IDnter' :
                index += 1
                return grammar[index-1] in 'SNTEF'
            elif node.value == 'Elter' :
                if grammar[index] == "'" :
                    while grammar[index] != "'" :
                        index += 1
                    return True
            elif node.value == grammar[index] :
                index += 1
                return True
            else :
                return False
        else : #NonTerminal
            if node.value == 'S':
                next_node = A[0]
            elif node.value == 'N':
                next_node = A[1]
            elif node.value == 'T':
                next_node = A[2]
            elif node.value == 'E':
                next_node = A[3]
            elif node.value == 'F':
                next_node = A[4]
            else:
                return False
            return analyse(next_node, grammar)
    
                    
                
            
        