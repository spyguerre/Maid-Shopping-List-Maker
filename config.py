# Path to save the generated shopping list Excel file
SHOPPING_LIST_PATH = 'shopping_list.xlsx'
# Path to the CSV file containing the ingredients (downloaded back from google sheets)
INGREDIENTS_CSV_PATH = 'boissonsv2.csv'

# List of recipes with their corresponding Google Sheets URLs, starting ingredient row number, and a boolean indicating whether or not to dismiss the pieces per batch information.
RECIPES = {
    # Pâtisseries
    "Muffins façon crumble aux framboises": {"url": "https://docs.google.com/spreadsheets/d/1d7yOfv5HC6V-XHgqbaD0BntkUfq9rWcPukA9KngHG3Y/edit", "ing_cell": 3, "is_single-piece_recipe": False},
    "Caramel Slice": {"url": "https://docs.google.com/spreadsheets/d/1Yf9KPXZPazssTbj6oVwD0Ylcwr5wQbEefbdETQUCmtM/edit", "ing_cell": 3, "is_single-piece_recipe": False},
    "Cookies façon brownie aux trois chocolats": {"url": "https://docs.google.com/spreadsheets/d/16LZ6KlqToblxWPRM8en5SaqZ_xdc1iBZ3Wo9xooG58k/edit", "ing_cell": 3, "is_single-piece_recipe": False},
    "Cookies Vegan": {"url": "https://docs.google.com/spreadsheets/d/1aYAx39OHnSASnraYxkhjNhSwU0ECzTeIFtO9LBQYdts/edit", "ing_cell": 3, "is_single-piece_recipe": False},
    "Dorayaki": {"url": "https://docs.google.com/spreadsheets/d/1Pj5oSizHVMnPT0dVFZnMo596VFZ3uWTl6wEuA8YnBMg/edit", "ing_cell": 3, "is_single-piece_recipe": False},
    "Marbré sésame noir": {"url": "https://docs.google.com/spreadsheets/d/10iQPOiOTlXFz5vNjs94ZXcjrD8Aofs4hz1GKJLow22o/edit", "ing_cell": 3, "is_single-piece_recipe": False},
    "Cake à la cannelle vegan": {"url": "https://docs.google.com/spreadsheets/d/16481zQXy1YIIvZY5AFEqNOVPl_DnwHWUDmKR4RR9Uoo/edit", "ing_cell": 3, "is_single-piece_recipe": False},
    "Mushipan au yuzu": {"url": "https://docs.google.com/spreadsheets/d/1oK3LES0A1QPJVCblVR5IWxka5dLYOsSBB4C8NtWO9mY/edit", "ing_cell": 3, "is_single-piece_recipe": False},
    "Pain d'épices": {"url": "https://docs.google.com/spreadsheets/d/1vFbINQ-5Vxz1P1Fd8ebeDAQGDPOVa6s7Ohl57xDRNis/edit", "ing_cell": 3, "is_single-piece_recipe": False},
    "Rose des pommes à la figue et cannelle": {"url": "https://docs.google.com/spreadsheets/d/1hcFzcjYxh4jZikg2c8mcRjyChKmRi6Vy4O8qkcrXrQk/edit", "ing_cell": 3, "is_single-piece_recipe": False},
    "Sablés verveine citron/jasmin/cannelle": {"url": "https://docs.google.com/spreadsheets/d/1uIDs8i9wQuQKls9cu4B6qBouL9eAEJodVC-DUWc7EEA/edit", "ing_cell": 3, "is_single-piece_recipe": False},
    "Trio de mochi aux saveurs sorbets": {"url": "https://docs.google.com/spreadsheets/d/1P9M5OO7WwIvPMZIFzy3Tf-qqzkbKrOar9qLiw16YdBE/edit", "ing_cell": 3, "is_single-piece_recipe": False},
    # Boissons
    "Café simple": {"url": "https://docs.google.com/spreadsheets/d/1xXNuJxmAe7WquyBj7g_SKjtUqaxPkoBvW9LIGCDnl4g/edit?gid=0#gid=0", "ing_cell": 9, "is_single-piece_recipe": True},
    "Cappuccino cookie": {"url": "https://docs.google.com/spreadsheets/d/1-0gqlFrg_0qiK4AeAPb0tkndyNdMYPx_1jaYY717WTU/edit?gid=0#gid=0", "ing_cell": 9, "is_single-piece_recipe": True},
    "Macchiato latte au pain d'épices": {"url": "https://docs.google.com/spreadsheets/d/1L6ntcQwFGUrWMJnmdvrvi70RtjRx8NxPe2YqjdTqU0A/edit?gid=0#gid=0", "ing_cell": 9, "is_single-piece_recipe": True},
    "Mocha au chocolat blanc": {"url": "https://docs.google.com/spreadsheets/d/1fOb0rjeKEWwrLZ_llHeJgBv4_fr3ka9Wda3Oaz8n9sY/edit?gid=0#gid=0", "ing_cell": 9, "is_single-piece_recipe": True},
    "Chocolat guimauve": {"url": "https://docs.google.com/spreadsheets/d/1xuIw9pK0c4Wq5Jl5UcZ7od70FsPPQsz45Xs79pq4Mb4/edit?gid=0#gid=0", "ing_cell": 9, "is_single-piece_recipe": True},
    "Chai latte": {"url": "https://docs.google.com/spreadsheets/d/1DDxpLx9U1p1oKm2SnQWUq0suzQQf7i3D88pKCxF7aeU/edit?gid=0#gid=0", "ing_cell": 9, "is_single-piece_recipe": True},
    "Taro latte": {"url": "https://docs.google.com/spreadsheets/d/1nZHH6b62sW_iptZlywKCZzB9eBztiu0yJcnaTNDIZqc/edit?gid=0#gid=0", "ing_cell": 9, "is_single-piece_recipe": True},
    "Thé matcha": {"url": "https://docs.google.com/spreadsheets/d/1AR6PUlUwFrhRaURi0kh2B-NOz-Gvxmr4hrftl18vB0U/edit?gid=0#gid=0", "ing_cell": 9, "is_single-piece_recipe": True},
    "Lassi litchi rose gingembre": {"url": "https://docs.google.com/spreadsheets/d/1IdMB6C6Zz2gmWme-ly5w5egdBjWhDuF_YlxCOMAAH8Y/edit?gid=0#gid=0", "ing_cell": 9, "is_single-piece_recipe": True},
    "Diabolo": {"url": "https://docs.google.com/spreadsheets/d/1UAtNaav3rMF-B3GfbxRO2D4CzqiKjHKxcLbFVb4Idqs/edit?gid=0#gid=0", "ing_cell": 9, "is_single-piece_recipe": True},
    "Tanu tanu à la myrtille": {"url": "https://docs.google.com/spreadsheets/d/1u7goZqapTH1FBMcSjdhjPsieSUvc2rW_8sh3CXJERHs/edit?gid=0#gid=0", "ing_cell": 9, "is_single-piece_recipe": True},
    "Thé chaud des Vahinés": {"url": "https://docs.google.com/spreadsheets/d/1OSFZpVU5C2rCkflA-sEWyXukjEANdO7zkXnBd-HrZnk/edit?gid=0#gid=0", "ing_cell": 9, "is_single-piece_recipe": True},
    "The froid Guimet": {"url": "https://docs.google.com/spreadsheets/d/1bNsPWO60L1uOoM3AtmbvPEizRqZ5AAVOCxG_F63Pw2s/edit?gid=0#gid=0", "ing_cell": 9, "is_single-piece_recipe": True},
    # Misc
    # "Miscelaneous": {"products": [
    #     "Krema",
    #     "Carambars",
    #     "Sucre",
    #     "Charlottes",
    #     "Gants",
    # ]}
}


PRICE_DATA = {
    "4 épices": {"price": 3., "unit_qty": 30, "store": "Gde Srf"},
    "beurre": {"price": 1.95, "unit_qty": 250, "store": "https://www.promocash.com/ecommerce/product/250g-beur-dx-montfleuri-60/01t7R00000A50qEQAR"},
    "beurre salé": {"price": 2.55, "unit_qty": 250, "store": "https://www.promocash.com/ecommerce/product/250g-plqbeur1-2sel-gastro-cr/01t7R000008L5gxQAC"},
    "café moulu": {"price": 20., "unit_qty": 1000, "store": "Le comptoir des cafés 2 rue des poissonniers 51000 Ch-en-Ch"},
    "cannelle": {"price": 3., "unit_qty": 15, "store": "Gde Srf"},
    "cassonade": {"price": 2.69, "unit_qty": 1000, "store": "https://www.promocash.com/ecommerce/product/1kg-cassonade-bv-equi-st-louis/01t7R00000EHddyQAD"},
    "caissettes": {"price": .79, "unit_qty": 80, "store": "Stockomani"},
    "carambars": {"price": 12.72, "unit_qty": 1000, "store": "https://www.promocash.com/ecommerce/product/1kg-carambar-mini-mix/01t7R000007xno2QAA"},
    "chantilly": {"price": 5.96, "unit_qty": 500, "store": "https://www.promocash.com/ecommerce/product/500ml-creme-fouettee-en-cuisin/01t7R000008LHxoQAG"},
    "chocolat": {"price": 4.33, "unit_qty": 600, "store": "https://www.promocash.com/ecommerce/product/5x100g-tablet-choc-noir-simpl/01t7R00000A50B8QAJ"},
    "chocolat en poudre": {"price": 6.79, "unit_qty": 800, "store": "https://www.promocash.com/ecommerce/product/800g-grand-arome-poulain/01t7R000008LGqJQAW"},
    "chocolat vegan": {"price": 4.52, "unit_qty": 100, "store": "https://www.greenweez.com/recherche/tablette%20chocolat%20noir%2075%25%20cacao%20nicaragua%20bio%20100g"},
    "coulis caramel": {"price": 7.67, "unit_qty": 1000, "store": "https://www.promocash.com/ecommerce/product/1kg-topp-caramel-bs-exquizito/01t7R000008LCFxQAO"},
    "coulis chocolat": {"price": 8.93, "unit_qty": 1000, "store": "https://www.promocash.com/ecommerce/product/1kg-sweeties-chocolat-vahine/01t7R000008L8APQA0"},
    "confiture de figue": {"price": 2.02, "unit_qty": 360, "store": "https://www.promocash.com/ecommerce/product/370g-confiture-figues-bmaman/01t7R000008KysRQAS"},
    "extrait de yuzu": {"price": 7.5, "unit_qty": 100, "store": "Exo Est"},
    "farine": {"price": .95, "unit_qty": 1000, "store": "https://www.promocash.com/ecommerce/product/1kg-farine-ble-t45-/01t7R000008LAb8QAG"},
    "farine de riz": {"price": 3., "unit_qty": 400, "store": "Exo Est"},
    "farine de riz gluant": {"price": 2.5, "unit_qty": 400, "store": "Exo Est"},
    "fécule de pomme de terre": {"price": 1.08, "unit_qty": 250, "store": "https://www.promocash.com/ecommerce/product/bte-250g-fecule-pdt-tipiak/01t7R000008LEx1QAG"},
    "framboises": {"price": 7.37, "unit_qty": 1000, "store": "https://www.promocash.com/ecommerce/product/1kg-framboises-ent-en-cuisine/01t7R000008LFUKQA4"},
    "fécule de maïs": {"price": 1.99, "unit_qty": 400, "store": "https://www.promocash.com/ecommerce/product/400g-maizena-fleur-de-mais/01t7R000008L2FmQAK"},
    "gingembre": {"price": 2.5, "unit_qty": 29, "store": "Gde Srf"},
    "graines de lin": {"price": 4., "unit_qty": 400, "store": "Norma/Stock Alex"},
    "graines de sésame noir": {"price": 4., "unit_qty": 400, "store": "Saigon Store"},
    "huile de tournesol": {"price": 2.06, "unit_qty": 1000, "store": "https://www.promocash.com/ecommerce/product/1l-huile-tournesol-clairor/01t7R000008L6XUQA0"},
    "jus de citron": {"price": 4.03, "unit_qty": 1000, "store": "https://www.promocash.com/ecommerce/product/1l-jus-de-citron-concentre-ec/01t7R000008L3K3QAK"},
    "krema": {"price": 15.1, "unit_qty": 2000, "store": "https://www.promocash.com/ecommerce/product/2kg-krema-regalad/01t7R000008LGCgQAO"},
    "lait": {"price": 5.82, "unit_qty": 6000, "store": "https://www.promocash.com/ecommerce/product/1l-lait-1-2-ecreme-simpl/01t7R000008LAI5QAO"},
    "lait concentré sucré": {"price": 1.9, "unit_qty": 397, "store": "https://www.promocash.com/ecommerce/product/397g-bt-lt-concsucre-nestle/01t7R000008L3VcQAK"},
    "lait d'avoine": {"price": 1.8, "unit_qty": 1000, "store": "Gde Srf"},
    "lait d'amande": {"price": 1.8, "unit_qty": 1000, "store": "Gde Srf"},
    "levure chimique": {"price": 0.3, "unit_qty": 6, "store": "https://www.auchan.fr/auchan-levure-chimique-les-patissiers/pr-C1817544"},
    "limonade": {"price": 5.95, "unit_qty": 9000, "store": "https://www.promocash.com/ecommerce/product/limonade-saxo-15l/01t7R000008LJOgQAO"},
    "litchi": {"price": 2.58, "unit_qty": 230, "store": "Exo Est"},
    "marshmallow": {"price": 21.7, "unit_qty": 1000, "store": "https://www.delidrinks.com/topping-et-decorations/15511v5091-tooping-mini-marshmallow-blanc-sachet-1kg.html#/3-conditionnement-a_la_piece"},
    "miel": {"price": 6.59, "unit_qty": 1000, "store": "https://www.promocash.com/ecommerce/product/1kg-miel-liquide-pp/01t7R000008LGaNQAW"},
    "nate de coco": {"price": 5., "unit_qty": 600, "store": "Exo Est"},  # Full pif ici
    "oeuf": {"price": 25.62, "unit_qty": 90, "store": "https://www.promocash.com/ecommerce/product/90-oeufs-sol-moyen-vrac/01t7R000008LGffQAG"},
    "orange": {"price": 3., "unit_qty": 6, "store": "Gde Srf"},
    "pâte de haricots azuki": {"price": 2.99, "unit_qty": 500, "store": "Exo Est"},
    "pâte feuilletée": {"price": 0.79, "unit_qty": 1, "store": "https://www.promocash.com/ecommerce/product/230g-pate-feuillete-roucrf-cl/01t7R000008L0IhQAK"},
    "pépites chocolat au lait": {"price": 23.77, "unit_qty": 1000, "store": "https://www.promocash.com/ecommerce/product/1kg-pepites-chocolat-lait-lp/01t7R000008KxWzQAK"},
    "pépites trois choco": {"price": 10.6, "unit_qty": 400, "store": "https://www.promocash.com/ecommerce/product/400g-croc-gout-3-choco-vahine/01t7R000008LBKiQAO"},
    "pomme": {"price": 3., "unit_qty": 10, "store": "Gde Srf"},
    "poudre de taro": {"price": 17.36, "unit_qty": 1000, "store": "https://www.delidrinks.com/aromatisation/15955v5493-bubble-tea-poudre-taro-vegan-poche-1kg.html#/3-conditionnement-a_la_piece"},
    "sel": {"price": 0., "unit_qty": 1., "store": "Maison"},
    "sirop chocolat blanc": {"price": 8.55, "unit_qty": 1000, "store": "https://www.delidrinks.com/sirops-boissons-chaudes/13993v1529-sirop-chocolat-blanc-bouteille-verre-1l.html#/3-conditionnement-a_la_piece"},
    "sirop cookie": {"price": 7.9, "unit_qty": 1000, "store": "https://www.promocash.com/ecommerce/product/70cl-sirop-choco-cookies-monin/01t7R000008L6KjQAK"},
    "sirop diabolo average": {"price": 3., "unit_qty": 1000, "store": "Placeholder"},
    "sirop de rose": {"price": 6.39, "unit_qty": 1000, "store": "https://www.promocash.com/ecommerce/product/70cl-sir-rose-monin/01t7R000008L3BwQAK"},
    "sirop grenadine": {"price": 2.51, "unit_qty": 1000, "store": "https://www.promocash.com/ecommerce/product/pet-1l-sirop-grenadine-saxo/01t7R000008L5OPQA0"},
    "sirop menthe": {"price": 2.38, "unit_qty": 1000, "store": "https://www.promocash.com/ecommerce/product/pet-1l-sirop-menthe-saxo/01t7R000008L5e3QAC"},
    "sirop myrtille": {"price": 18.53, "unit_qty": 2500, "store": "https://www.delidrinks.com/aromatisation/15078v4421-bubble-tea-sirop-myrtille-bidon-25kg.html#/3-conditionnement-a_la_piece"},
    "sirop pain d'épices": {"price": 8.1, "unit_qty": 1000, "store": "https://www.promocash.com/ecommerce/product/70cl-sirop-pain-epice-monin/01t7R000008LG9eQAG"},
    "sirop pêche": {"price": 3.56, "unit_qty": 1000, "store": "https://www.promocash.com/ecommerce/product/pet-1l-sirop-peche-saxo/01t7R000008L44IQAS"},
    "sirop pumpkin spice": {"price": 10., "unit_qty": 1000, "store": "https://www.delidrinks.com/sirops-boissons-chaudes/14430v1571-sirop-pumpkin-spice-bouteille-verre-1l.html#/3-conditionnement-a_la_piece"},
    "sirop raisin": {"price": 17.47, "unit_qty": 2500, "store": "https://www.delidrinks.com/aromatisation/15404v4904-bubble-tea-sirop-raisin-grape-bidon-25kg.html#/3-conditionnement-a_la_piece"},
    "sorbet framboise": {"price": 9.22, "unit_qty": 1400, "store": "https://www.promocash.com/ecommerce/product/25l-sorbet-en-cuis-frambois/01t7R000008KyYzQAK"},
    "sorbet poire": {"price": 9.82, "unit_qty": 1350, "store": "https://www.promocash.com/ecommerce/product/25l-sorbet-en-cuis-poire/01t7R000008LGunQAG"},
    "sorbet mangue": {"price": 9.05, "unit_qty": 1350, "store": "https://www.promocash.com/ecommerce/product/25l-sorbet-en-cuis-mangue/01t7R000008LFw8QAG"},
    "sorbet average": {"price": 9.5, "unit_qty": 1350, "store": "Placeholder"},
    "sucre": {"price": 1.32, "unit_qty": 1000, "store": "https://www.promocash.com/ecommerce/product/1kg-sac-sucre-cristal-pp/01t7R000008LDzjQAG"},
    "sucre vanillé": {"price": 0.85, "unit_qty": 10, "store": "https://www.auchan.fr/auchan-sucre-vanille-a-l-extrait-de-vanille/pr-C1273910"},
    "sucre vanillé vegan": {"price": 0.85, "unit_qty": 10, "store": "https://www.auchan.fr/auchan-sucre-vanille-a-l-extrait-de-vanille/pr-C1273910"},
    "thé chai impérial": {"price": 22.41, "unit_qty": 100, "store": "Palais des thés"},
    "thé des vahinés": {"price": 12., "unit_qty": 100, "store": "Palais des thés"},
    "thé guimet": {"price": 12., "unit_qty": 100, "store": "Palais des thés"},
    "thé jasmin": {"price": 13.78, "unit_qty": 100, "store": "Palais des thés"},
    "thé matcha": {"price": 5., "unit_qty": 80, "store": "Exo Est"},
    "thé verveine": {"price": 11.2, "unit_qty": 50, "store": "Palais des thés"},
    "eau": {"price": 0., "unit_qty": 1., "store": "Maison"},
    "margarine": {"price": 3.27, "unit_qty": 500, "store": "https://www.auchan.fr/primevere-margarine-doux-pour-tartine/pr-C1169616"},
}

# Mappings to standardize ingredient names
INGREDIENTS_MAP = {
    "oeuf entier": "oeuf",
    "blanc d'oeuf": "oeuf",
    "jaune d'oeuf": "oeuf",
    "oeufs": "oeuf",
    "beurre demi-sel": "beurre salé",
    "beurre doux": "beurre",
    "chocolat noir": "chocolat",
    "chocolat noir corsé": "chocolat",
    "chocolat noir vegan": "chocolat vegan",
    "graines de lin moulues": "graines de lin",
    "lait de soja": "lait végétal",
    "maïzena": "fécule de maïs",
    "mélange 4 épices": "4 épices",
    "jus d'orange": "orange",
    "sucre blanc": "sucre",
    "huile neutre": "huile de tournesol",
    "lait végétal": "lait d'avoine",
    "caissettes/papier muffin": "caissettes",
    "sorbet": "sorbet average",
    "café": [{"name": "café moulu", "unit": "g", "coef": 0.05 * 10}],  # cL de café chaud -> g de café moulu acheté
    "(chantilly)": [{"name": "chantilly", "unit": "g", "coef": 0.5}],  # Option -> prise une fois sur deux
    "(sirop pumpkin spice)": [{"name": "sirop pumpkin spice", "unit": "g", "coef": 0.5}],  # Option -> prise une fois sur deux
    "thé chai infusé": [{"name": "thé chai impérial", "unit": "g", "coef": 0.01}],  # cL de thé infusé -> g de thé acheté
    "thé des vahinés infusé": [{"name": "thé des vahinés", "unit": "g", "coef": 0.01 * 10}],  # cL de thé infusé -> g de thé acheté
    "thé guimet infusé": [{"name": "thé guimet", "unit": "g", "coef": 0.01 * 10}],  # cL de thé infusé -> g de thé acheté
    "lait chaud": [{"name": "lait", "unit": "g", "coef": 10}],  # cL -> g
    "lait moussé chaud": [{"name": "lait", "unit": "g", "coef": 10}],  # cL -> g
    "pépites chocolat blanc": "pépites chocolat au lait",
    "eau bouillante": "eau",
    "eau froide": "eau",
    "mélange lait froid + litchi": [
        {"name": "lait", "unit": "g", "coef": 0.813},  # cL de mélange -> g de lait acheté
        {"name": "litchi", "unit": "g", "coef": 0.187}  # cL de mélange -> g de litchi acheté
    ],
    "sirop de menthe/grenadine/pêche": "sirop diabolo average",
    "mélange eau de coco + nata": "nate de coco"
}

# Mappings to standardize unit names
UNITS_MAP = {
    "blanc d'oeuf": "oeuf",
    "jaune d'oeuf": "oeuf",
    "oeufs": "oeuf",
    "sachets": "sachet",
    "(petite) càc": "càc",
}

# The width and height of the ingredients tab
HEIGHT = 22 * len(RECIPES) + 1
WIDTH = 15
