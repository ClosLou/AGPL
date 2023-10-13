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
        while grammar[index] != "'" :
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
    if node.classe == Classe.Conc :
        if analyse_aux(node.left, grammar) :
            return analyse_aux(node.right, grammar)
        else:
            return False
        
    elif node.classe == Classe.Union :
        if analyse_aux(node.left, grammar) :
            return True
        else:
            return analyse_aux(node.right, grammar)
        
    elif node.classe == Classe.Star :
        while analyse_aux(node.left, grammar) :
            pass
        return True
    
    elif node.classe == Classe.Un :
        if analyse_aux(node.left, grammar) :
            pass
        return True
    
    elif node.classe == Classe.Atom :
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
            if node.value == 'S':
                next_node = A[0]
            elif node.value == 'N':
                next_node = A[1]
            elif node.value == 'E':
                next_node = A[2]
            elif node.value == 'T':
                next_node = A[3]
            elif node.value == 'F':
                next_node = A[4]
            else:
                return False
            return analyse_aux(next_node, grammar)
    
                    
                
            
        