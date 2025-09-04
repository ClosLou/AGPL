from agpl_analyzer.tree_gen import *

# Règle "S->[N.'->'.E.','].';'"
A1 = gen_conc(
    gen_star(
        gen_conc(
            gen_conc(
                gen_conc(
                    gen_atom('N',0,AtomType.NonTerminal),
                    gen_atom('->',0,AtomType.Terminal)
                    ),
                gen_atom('E',0,AtomType.NonTerminal)
                ),
            gen_atom(',',0,AtomType.Terminal)
            )
        ),
    gen_atom(';',0,AtomType.Terminal)
    )

# Règle "N->'IDnter',;"
A2 = gen_atom('IDnter',0,AtomType.Terminal)

# Règle "E->T.['+'.T],;"
A3 = gen_conc(
    gen_atom('T',0,AtomType.NonTerminal),
    gen_star(
        gen_conc(
            gen_atom('+',0,AtomType.Terminal),
            gen_atom('T',0,AtomType.NonTerminal)
            )
        )
    )

# Règle "T->F.['.'.F],;"
A4 = gen_conc(
    gen_atom('F',0,AtomType.NonTerminal),
    gen_star(
        gen_conc(
            gen_atom('.',0,AtomType.Terminal),
            gen_atom('F',0,AtomType.NonTerminal)
            )
        )
    )

# Règle "F->['IDnter'.'Elter'.('('.E.')')+('['.E.']').('(/'.E.'/)')],;"
A5 = gen_union(
    gen_union(
        gen_union(
            gen_union(
                gen_atom('IDnter',0,AtomType.Terminal),
                gen_atom('Elter',0,AtomType.Terminal)
                ),
            gen_conc(
                gen_atom('(',0,AtomType.Terminal),
                gen_conc(
                    gen_atom('E',0,AtomType.NonTerminal),
                    gen_atom(')',0,AtomType.Terminal)
                    )
                )
            ),
        gen_conc(
            gen_atom('[',0,AtomType.Terminal),
            gen_conc(
                gen_atom('E',0,AtomType.NonTerminal),
                gen_atom(']',0,AtomType.Terminal)
                )
            )
        ),
    gen_conc(
        gen_atom('(/',0,AtomType.Terminal),
        gen_conc(
            gen_atom('E',0,AtomType.NonTerminal),
            gen_atom('/)',0,AtomType.Terminal)
            )
        )
    )

A = [A1,A2,A3,A4,A5] # Liste des arbres de la grammaire G0
