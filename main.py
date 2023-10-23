from tree_gen import Node, AtomType, gen_conc, gen_star, gen_atom, gen_union, Classe
from graphic_modules import tree_print, draw_tree, create_tree_dsplot
from constantes import A1, A2, A3, A4, A5, A
from analyse_modules import analyse, scan


if __name__ == '__main__':
    grammars = [
        "S->[N.'->'.E.','].';',N->'IDnter',E->T.['+'.T],T->F.['.'.F],F->['IDnter'.'Elter'.('('.E.')')+('['.E.']').('(/'.E.'/)')],;",
        "S->[N.'->'.E.','].';',;",
        "N->'IDnter',;",
        "E->T.['+'.T],;",
        "T->F.['.'.F],;",
        "F->['IDnter'.'Elter'.('('.E.')')+('['.E.']').('(/'.E.'/)')],;",
        ]

    list_grammar = []
    for grammar in grammars:
        list_grammar = scan(grammar)
        if analyse(A[0], list_grammar) :
            print(f'La grammaire : "{grammar}" est correcte', end = '\n\n')
        else:
            print(f'La grammaire "{grammar}" n\'est pas correcte', end = '\n\n')
        

    
    
    
    