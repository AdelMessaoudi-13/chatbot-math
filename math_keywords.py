# math_keywords.py

# Mots-clés généraux en mathématiques
math_general = [
    "mathématiques", "calcul", "équation", "formule", "variable",
    "résoudre", "résolution", "preuve", "notation", "expression",
    "système", "développement", "simplification"
]

# Algèbre
algebra = [
    "algèbre", "polynôme", "facteur", "développement", "identité remarquable",
    "équation", "système d’équations", "racine", "factorisation", "binôme",
    "quadratique", "fonction affine", "fonction quadratique", "parabole"
]

# Analyse
analysis = [
    "analyse", "limite", "dérivée", "intégrale", "primitif",
    "fonction continue", "tangente", "courbe", "asymptote", "logarithme",
    "exponentielle", "série", "somme infinie", "convexité", "croissance",
    "décroissance", "point critique", "point d'inflexion"
]

# Géométrie
geometry = [
    "géométrie", "triangle", "cercle", "aire", "périmètre",
    "volume", "angle", "cosinus", "sinus", "tangente",
    "distance", "théorème", "Pythagore", "Thalès",
    "projection", "symétrie", "transformation", "homothétie", "vecteur",
    "droite", "segment", "milieu", "bissectrice", "orthogonal"
]

# Probabilités et statistiques
probability_stats = [
    "probabilité", "statistiques", "moyenne", "variance", "écart-type",
    "médiane", "loi normale", "loi binomiale", "espérance",
    "indépendance", "corrélation", "régression", "distribution",
    "probabilité conditionnelle", "événement", "expérience aléatoire"
]

# Arithmétique et nombres
arithmetic = [
    "arithmétique", "nombre", "entier", "rationnel", "irrationnel",
    "décimal", "premier", "divisibilité", "facteur",
    "multiplication", "addition", "division", "soustraction",
    "modulo", "congruence", "théorème des nombres premiers"
]

# Vecteurs et matrices
vectors_matrices = [
    "vecteur", "matrice", "déterminant", "trace", "diagonalisation",
    "produit scalaire", "produit vectoriel", "base", "dimension",
    "système linéaire", "valeur propre", "vecteur propre", "transformation linéaire"
]

# Théorie des ensembles et logique
sets_logic = [
    "ensemble", "appartenance", "union", "intersection", "différence",
    "inclusion", "cardinal", "logique", "implication", "équivalence",
    "quantificateur", "prédicat", "proposition", "contraposée",
    "négation", "binaire", "vrai", "faux"
]

# Informatique et mathématiques discrètes
discrete_math = [
    "graphes", "combinatoire", "permutation", "combinaison", "récurrence",
    "relation d’ordre", "arbre", "chemin", "circuit",
    "automate", "logique booléenne", "table de vérité", "complexité"
]

# Fusionner toutes les listes en une seule liste de mots-clés mathématiques
math_keywords = set(
    math_general + algebra + analysis + geometry + probability_stats +
    arithmetic + vectors_matrices + sets_logic + discrete_math
)
