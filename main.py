from tree_gen import Node, AtomType, gen_conc, gen_star, gen_atom, gen_union
from graphic_modules import tree_print, draw_tree, create_tree_dsplot
from constantes import A1, A2, A3, A4, A5, A
from analyse_modules import analyse


if __name__ == '__main__':
    grammars = [
        "S->[N.'->'.E.','].';',;",
        "N->'IDnter',;",
        "E->T.['+'.T],;",
        "T->F.['.'.F],;",
        "F->'IDnter'+'Elter'+'('.E.')'+'['.E.']'+'(/'.E.'/)',;"
        ]
    for grammar in grammars:
        if analyse(A[0], grammar) :
            print(f'La grammaire : "{grammar}" est correcte', end = '\n\n')
        else:
            print(f'La grammaire "{grammar}" n\'est pas correcte', end = '\n\n')
    
    # create_tree_dsplot(A1, 'A1.png')
    # create_tree_dsplot(A2, 'A2.png')
    # create_tree_dsplot(A3, 'A3.png')
    # create_tree_dsplot(A4, 'A4.png')
    # create_tree_dsplot(A5, 'A5.png')