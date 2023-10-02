

class Node:
    def __init__(self, valeur = None, noeud_gauche = None, noeud_droit = None):
        self.valeur = valeur
        self.noeud_gauche = noeud_gauche
        self.noeud_droit = noeud_droit



gen_conc(GenStar(gen_conc(gen_conc(gen_conc(GenAtom(N,0,nonterminal),GenAtom('->',0,terminal)),GenAtom('E'0,nonterminal)),GenAtom(',',0,terminal)),GenAtom(';',0,terminal)))
GenAtom('IDnter',0,terminal)
gen_conc(genAtom('T',0,nonterminal),gen_star(gen_conc(gen_union('.',0,terminal),genAtom('T',0,nonterminal))))
gen_conc(GenAtom(T,0,nonterminal),GenStar(gen_conc(GenAtom('+',0,terminal),GenAtom(T,0,nonterminal))))
gen_union(gen_union(gen_union(gen_union(gen_atom('IDnter',0,terminal),gen_atom('Elter',0,terminal)),gen_conc(gen_atom('(',0,terminal),gen_conc(gen_atom(E,0,nonterminal),gen_atom(')',0,terminal)))),gen_conc(gen_atom('[',0,terminal),gen_conc(gen_atom(E,0,nonterminal),gen_atom(']',0,terminal)))),gen_conc(gen_atom('(/',0,terminal),gen_conc(gen_atom(E,0,nonterminal),gen_atom('/)',0,terminal))))
    