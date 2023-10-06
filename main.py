from tree_gen import Node, AtomType, gen_conc, gen_star, gen_atom, gen_union
from graphic_modules import tree_print, draw_tree, create_tree_dsplot
from constantes import A1, A2, A3, A4, A5


if __name__ == '__main__':
    tree_print(A1)
    draw_tree(A1)
    create_tree_dsplot(A1, 'A1.png')
    create_tree_dsplot(A2, 'A2.png')
    create_tree_dsplot(A3, 'A3.png')
    create_tree_dsplot(A4, 'A4.png')
    create_tree_dsplot(A5, 'A5.png')