from agpl_analyzer.analyse_modules import analyse, scan
from agpl_analyzer.grammar_builder import A
from agpl_analyzer.tree_visualizer import tree_print, draw_tree


if __name__ == '__main__':
    g0 = "S->[N.'->'.E.','].';',N->'IDnter',E->T.['+'.T],T->F.['.'.F],F->['IDnter'+'Elter'+'('.E.')'+'['.E.']'+'(/'.E.'/)'],;"
    regles = ["S->[N.'->'.E.','].';',;",
        "N->'IDnter',;",
        "E->T.['+'.T],;",
        "T->F.['.'.F],;",
        "F->['IDnter'+'Elter'+'('.E.')'+'['.E.']'+'(/'.E.'/)'],;",]
    grammars = [
        "F->'IDnter'+'Elter',;", # Bonne grammaire
        "F->'IDnter'+'Elter';", # Erreur : ',' manquant
        "N->'Elter',.", # Erreur : '.' faux -> ';' attendu
        ]

    list_grammar = []

    print("\n\nBienvenue dans le programme de test des grammaires !")
    print("-"*50, end = '\n\n')
    choix = 0
    while choix != 1 or choix != 2 :
        print("Voulez-vous afficher les arbres ou afficher les résultats des analyses ?")
        print("1 - Afficher le test des grammaires")
        print("2 - Afficher les arbres de la metagrammaire")
        try :
            choix = int(input("Votre choix : "))
        except ValueError :
            print("Erreur : Veuillez choisir 1 ou 2")
            print()
            continue
        print()
        if choix == 1 :
            choix2 = 0
            print("Que voulez-vous faire ?")
            print("1 - Démontrer que G0 appartient à G0 en une analyse")
            print("2 - Démontrer que G0 appartient à G0 avec l'analyse de chaque règle de la grammaire")
            print("3 - Analyser d'autre grammaires avec G0")
            print("4 - Analyser votre propre grammaire")
            try:
                choix2 = int(input("Votre choix : "))
            except ValueError:
                print("Erreur : Veuillez choisir un nombre entre 1 et 4")
                print()
                continue
            print()
            if choix2 == 1 :
                list_grammar = scan(g0)
                print("Analyse de la grammaire G0 avec les règles de la grammaire G0")
                print("G0 : ", g0)
                if analyse(A[0], list_grammar) :
                    print("G0 appartient à G0 avec les règles de la grammaire".upper())
                else:
                    print("G0 n'appartient pas à G0 avec les règles de la grammaire")
                print()
            elif choix2 == 2 :
                for regle in regles :
                    list_grammar = scan(regle)
                    if analyse(A[0], list_grammar) :
                        print(f'La règle : "{regle}" est correcte', end = '\n\n')
                    else:
                        print(f'La règle "{regle}" n\'est pas correcte', end = '\n\n')
                    print()
            elif choix2 == 3 :
                for grammar in grammars:
                    list_grammar = scan(grammar)
                    if analyse(A[0], list_grammar) :
                        print(f'La grammaire : "{grammar}" est correcte', end = '\n\n')
                    else:
                        print(f'La grammaire "{grammar}" n\'est pas correcte', end = '\n\n')
                    print()
            elif choix2 == 4 :
                grammar = input('Entrez votre grammaire :')
                print()
                list_grammar = scan(grammar)
                print(f"Analyse de la grammaire {grammar} avec les règles de la grammaire G0")
                if analyse(A[0], list_grammar) :
                    print(f'La grammaire : "{grammar}" est correcte', end = '\n\n')
                else:
                    print(f'La grammaire "{grammar}" n\'est pas correcte', end = '\n\n')
                print()
        elif choix == 2 :
            choix2 = 0
            print("Voulez-vous afficher les arbres de la metagrammaire avec la profondeur ou sans la profondeur ?")
            print("1 - Afficher les arbres de la metagrammaire sans la profondeur")
            print("2 - Afficher les arbres de la metagrammaire avec la profondeur")
            try:
                choix2 = int(input("Votre choix : "))
            except ValueError:
                print("Erreur : Veuillez choisir un nombre entre 1 et 2")
                print()
                continue
            print()
            if choix2 == 1 :
                for i, noeud_regle in enumerate(A) :
                    print(f"Règle {i+1} :")
                    tree_print(noeud_regle)
                    print()

            elif choix2 == 2 :
                for i, noeud_regle in enumerate(A) :
                    print(f"Règle {i+1} :")
                    draw_tree(noeud_regle)
                    print()
            else :
                print("Erreur : Veuillez choisir 1 ou 2")
            print()
        else :
            print("Erreur : Veuillez choisir 1 ou 2")
        print()
    
    
    


    
    
    
    