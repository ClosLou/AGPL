# script_visualisation.py
import os
from agpl_analyzer.grammar_builder import A
from agpl_analyzer.dsplot_visualizer import create_tree_dsplot

# S'assurer que le dossier de sortie existe
if not os.path.exists('output'):
    os.makedirs('output')

# Générer l'image pour chaque règle
for i, rule_tree in enumerate(A):
    output_file = f"output/A{i+1}.png"
    print(f"Génération de l'image pour la règle {i+1} dans {output_file}...")
    create_tree_dsplot(rule_tree, output_file)

print("Toutes les images ont été générées.")
