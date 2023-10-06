from tree_gen import *

A1 = gen_conc(gen_star(gen_conc(gen_conc(gen_conc(gen_atom('N',0,AtomType.NonTerminal),gen_atom("'->'",0,AtomType.Terminal)),gen_atom('E',0,AtomType.NonTerminal)),gen_atom("','",0,AtomType.Terminal))),gen_atom("';'",0,AtomType.Terminal))
A2 = gen_atom("'IDnter'",0,AtomType.Terminal)
A3 = gen_conc(gen_atom('T',0,AtomType.NonTerminal),gen_star(gen_conc(gen_atom("'.'",0,AtomType.Terminal),gen_atom('T',0,AtomType.NonTerminal))))
A4 = gen_conc(gen_atom('T',0,AtomType.NonTerminal),gen_star(gen_conc(gen_atom("'+'",0,AtomType.Terminal),gen_atom('T',0,AtomType.NonTerminal))))
A5 = gen_union(gen_union(gen_union(gen_union(gen_atom("'IDnter'",0,AtomType.Terminal),gen_atom("'Elter'",0,AtomType.Terminal)),gen_conc(gen_atom("'('",0,AtomType.Terminal),gen_conc(gen_atom('E',0,AtomType.NonTerminal),gen_atom("')'",0,AtomType.Terminal)))),gen_conc(gen_atom("'['",0,AtomType.Terminal),gen_conc(gen_atom('E',0,AtomType.NonTerminal),gen_atom("']'",0,AtomType.Terminal)))),gen_conc(gen_atom("'(/'",0,AtomType.Terminal),gen_conc(gen_atom('E',0,AtomType.NonTerminal),gen_atom("'/)'",0,AtomType.Terminal))))