from constantes import A
from tree_gen import *

def scan(grammar)-> list:
    grammar_list = []
    while grammar:
        if grammar[0:2] == '->':
            grammar_list.append(('->',AtomType.Terminal))
            grammar = grammar[2:]
        elif grammar[0:2] == '(/':
            grammar_list.append(('(/',AtomType.Terminal))
            grammar = grammar[2:]
        elif grammar[0:2] == '/)':
            grammar_list.append(('/)',AtomType.Terminal))
            grammar = grammar[2:]
        elif grammar[0] == "'":
            if len(grammar) <= 1 :
                print('Erreur lors du scan de la grammaire : guillemet fermant manquant')
                return [] #TODO : gérer les erreurs
            index = 1
            while grammar[index] != "'" and not grammar[index-1] == '\\' : 
                # On ne prend pas en compte les ' qui sont précédés d'un \
                # car ils ne sont pas des délimiteurs
                if  len(grammar) <= index :
                    print('Erreur lors du scan de la grammaire : guillemet fermant manquant')
                    return [] #TODO : gérer les erreurs
                index += 1
            index += 1
            grammar_list.append((grammar[0:index], AtomType.Terminal))
            grammar = grammar[index:]
        elif grammar[0] == ',' or grammar[0] == ';' or grammar[0] == '+' or grammar[0] == '.' or grammar[0] == '[' or grammar[0] == ']' or grammar[0] == '(' or grammar[0] == ')':
            grammar_list.append((grammar[0], None))
            grammar = grammar[1:]
        else:
            grammar_list.append((grammar[0], AtomType.NonTerminal))
            grammar = grammar[1:]
    return grammar_list
        
        
def analyse(node : Node, grammar_list : str)-> bool :
    """Fonction qui permet d'analyser une grammaire

    Args:
        node (Node): noeud de l'arbre
        grammar_list (str): grammaire à analyser

    Returns:
        bool: True si la grammaire est correcte, False sinon
    """
    global index
    index = 0
    if analyse_aux(node, grammar_list) and index == len(grammar_list):
        return True
    else:
        return False




def analyse_aux(node : Node, grammar_list : list)-> bool :
    """Fonction auxiliaire qui permet d'analyser une grammaire

    Args:
        node (Node): noeud de l'arbre
        grammar_list (str): grammaire à analyser

    Returns:
        bool: True si la grammaire est correcte, False sinon
    """
    global index
    if index >= len(grammar_list) :
        return False
    match node.classe :
        case Classe.Conc :
            if analyse_aux(node.left, grammar_list) :
                return analyse_aux(node.right, grammar_list)
            else:
                return False
            
        case Classe.Union :
            index_tmp = index # On sauvegarde l'index de la dernière réussite
            if analyse_aux(node.left, grammar_list) :
                return True
            else:
                index = index_tmp # On restaure l'index de la dernière réussite
                return analyse_aux(node.right, grammar_list)
            
        case Classe.Star :
            index_tmp = index # On sauvegarde l'index de la dernière réussite
            while analyse_aux(node.left, grammar_list) :
                index_tmp = index # On sauvegarde l'index de la dernière réussite
            index = index_tmp # On restaure l'index de la dernière réussite
            return True
        
        case Classe.Un :
            index_tmp = index
            if analyse_aux(node.left, grammar_list) :
                index_tmp = index # On sauvegarde l'index de la dernière réussite
            index = index_tmp # On restaure l'index de la dernière réussite
            return True
        
        case Classe.Atom :
            if node.AType == AtomType.Terminal :
                result = False
                if node.value == '->'  :
                    result = grammar_list[index][0] == '->'
                    
                elif node.value == 'IDnter' :
                    result = grammar_list[index][1] == AtomType.NonTerminal
                    
                elif node.value == 'Elter' :
                    result = grammar_list[index][1] == AtomType.Terminal
                elif node.value == grammar_list[index][0] and grammar_list[index][1] == None :
                    result = True
                if result :
                    index += 1
                return result
                
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
                return analyse_aux(next_node, grammar_list)
