from agpl_analyzer.grammar_builder import A
from agpl_analyzer.tree_gen import *

def scan(grammar : str)-> list:
    """Cette fonction analyse la chaîne de caractères `grammar` qui représente une grammaire
    et catégorise chaque partie de la grammaire en un tuple de la forme `(part, AtomType)`,
    où `part` est une chaîne de caractères représentant une partie de la grammaire
    et `AtomType` est une énumération représentant si la partie est un Terminal ou un NonTerminal.
    La fonction renvoie une liste de ces tuples.

    Args:
        grammar (str): chaîne de caractères représentant une grammaire

    Returns:
        list: liste de tuples de la forme `(part, AtomType)`
    """
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
                return []
            index = 1
            
            while grammar[index] != "'" or (grammar[index-1] == '\\' and grammar[index] == "'"): 
                # On ne prend pas en compte les ' qui sont précédés d'un \
                # car ils ne sont pas des délimiteurs
                if  len(grammar) == index+1 :
                    print('Erreur lors du scan de la grammaire : guillemet fermant manquant')
                    return []
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


def analyse(node : Node, grammar_list : list)-> bool :
    """Cette fonction analyse une grammaire représentée par une liste de tuples (`grammar_list`)
    en utilisant une structure d'arbre (`node`). Elle utilise une liste `index_list` pour suivre l'index actuel
    dans la grammaire. Si la fonction auxiliaire `analyse_aux` renvoie `True`
    et que l'index a atteint la fin de la grammaire, la fonction renvoie `True`, indiquant que la grammaire est correcte.
    Sinon, elle renvoie `False`.
    
    On utilise une liste `index_list` pour pouvoir modifier la valeur de l'index 
    dans la fonction auxiliaire analyse_aux tout en gardant la même référence
    dans la fonction analyse. 
    Ce qui aurait été impossible avec un int car il est passé par valeur
    et non par référence (il est immutable contrairement à une liste).

    Args:
        node (Node): noeud de l'arbre de la metagrammaire
        grammar_list (list): grammaire à analyser sous forme de liste de tuples de la forme `(part, AtomType)`

    Returns:
        bool: True si la grammaire est correcte, False sinon
    """
    if not grammar_list:
        return False
    index_list = [0]
    if analyse_aux(node, grammar_list, index_list) and index_list[0] == len(grammar_list):
        return True
    else:
        return False



def analyse_aux(node : Node, grammar_list : list, index_list : list[int])-> bool :
    """Cette fonction auxiliaire parcourt la structure d'arbre (`node`) 
    et compare les éléments de la grammaire position par position. 
    L'index de la position testée est stocké dans `index_list[0]`. 
    La fonction gère différents cas en fonction de la classe du noeud actuel (`node.classe`),
    qui peut être `Conc`, `Union`, `Star`, `Un` ou `Atom`. 
    Pour chaque cas, elle effectue une analyse spécifique et renvoie `True` si
    la grammaire est correcte jusqu'à présent, et `False` sinon.

    Args:
        node (Node): noeud de l'arbre de la metagrammaire
        grammar_list (list): grammaire à analyser sous forme de liste de tuples de la forme `(part, AtomType)`
        index_list (list[int]): index de la grammaire, seul le premier élément est utilisé

    Returns:
        bool: True si la grammaire est correcte, False sinon
    """
    if index_list[0] >= len(grammar_list) :
        return False
    match node.classe :
        case Classe.Conc :
            if analyse_aux(node.left, grammar_list, index_list) :
                return analyse_aux(node.right, grammar_list, index_list)
            else:
                return False
            
        case Classe.Union :
            index_tmp = index_list[0] # On sauvegarde l'index_list[0] de la dernière réussite
            if analyse_aux(node.left, grammar_list, index_list) :
                return True
            else:
                index_list[0] = index_tmp # On restaure l'index_list[0] de la dernière réussite
                return analyse_aux(node.right, grammar_list, index_list)
            
        case Classe.Star :
            index_tmp = index_list[0] # On sauvegarde l'index_list[0] de la dernière réussite
            while analyse_aux(node.left, grammar_list, index_list) :
                index_tmp = index_list[0] # On sauvegarde l'index_list[0] de la dernière réussite
            index_list[0] = index_tmp # On restaure l'index_list[0] de la dernière réussite
            return True
        
        case Classe.Un :
            index_tmp = index_list[0]
            if analyse_aux(node.left, grammar_list, index_list) :
                index_tmp = index_list[0] # On sauvegarde l'index_list[0] de la dernière réussite
            index_list[0] = index_tmp # On restaure l'index_list[0] de la dernière réussite
            return True
        
        case Classe.Atom :
            if node.AType == AtomType.Terminal : 
                result = False # On initialise result à False
                if node.value == '->'  : # On vérifie si le noeud est une flèche
                    # On vérifie si la partie de la grammaire stoquée grammar_list[indice][0] est une flèche
                    result = grammar_list[index_list[0]][0] == '->' 
                    
                elif node.value == 'IDnter' : # On vérifie si le noeud est un IDnter
                    # On vérifie si la partie de la grammaire stoquée grammar_list[indice][0] est un IDnter
                    result = grammar_list[index_list[0]][1] == AtomType.NonTerminal
                    
                elif node.value == 'Elter' : # On vérifie si le noeud est un Elter
                    # On vérifie si la partie de la grammaire stoquée grammar_list[indice][0] est un Elter
                    result = grammar_list[index_list[0]][1] == AtomType.Terminal
                
                # Sinon, on vérifie si la valeur du noeud est égale à la partie de la grammaire stoquée grammar_list[indice][0]
                # et que le AtomType de la partie de la grammaire stoquée grammar_list[indice][1] est None
                elif node.value == grammar_list[index_list[0]][0] and grammar_list[index_list[0]][1] == None :
                    result = True
                    
                if result : # Si le résultat est True, on incrémente l'index_list[0]
                    index_list[0] += 1
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
                return analyse_aux(next_node, grammar_list, index_list)
