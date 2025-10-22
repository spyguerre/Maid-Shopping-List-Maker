# Path to save the generated shopping list Excel file
SHOPPING_LIST_PATH = 'shopping_list.xlsx'
# Path to the CSV file containing the ingredients (downloaded back from google sheets)
INGREDIENTS_CSV_PATH = 'unitrecipes/MushipanYuzu.csv'

# List of recipes with their corresponding Google Sheets URLs
RECIPES = {
    "Muffins façon crumble aux framboises": "https://docs.google.com/spreadsheets/d/1d7yOfv5HC6V-XHgqbaD0BntkUfq9rWcPukA9KngHG3Y/edit",
    "Caramel Slice": "https://docs.google.com/spreadsheets/d/1Yf9KPXZPazssTbj6oVwD0Ylcwr5wQbEefbdETQUCmtM/edit",
    "Cookies façon brownie aux trois chocolats": "https://docs.google.com/spreadsheets/d/16LZ6KlqToblxWPRM8en5SaqZ_xdc1iBZ3Wo9xooG58k/edit",
    "Cookies Vegan": "https://docs.google.com/spreadsheets/d/1aYAx39OHnSASnraYxkhjNhSwU0ECzTeIFtO9LBQYdts/edit",
    "Dorayaki": "https://docs.google.com/spreadsheets/d/1Pj5oSizHVMnPT0dVFZnMo596VFZ3uWTl6wEuA8YnBMg/edit",
    "Marbré sésame noir": "https://docs.google.com/spreadsheets/d/10iQPOiOTlXFz5vNjs94ZXcjrD8Aofs4hz1GKJLow22o/edit",
    "Muffins à la cannelle vegan": "https://docs.google.com/spreadsheets/d/16481zQXy1YIIvZY5AFEqNOVPl_DnwHWUDmKR4RR9Uoo/edit",
    "Mushipan au yuzu": "https://docs.google.com/spreadsheets/d/1oK3LES0A1QPJVCblVR5IWxka5dLYOsSBB4C8NtWO9mY/edit",
    "Pain d'épices": "https://docs.google.com/spreadsheets/d/1vFbINQ-5Vxz1P1Fd8ebeDAQGDPOVa6s7Ohl57xDRNis/edit",
    "Rose des pommes à la figue et cannelle": "https://docs.google.com/spreadsheets/d/1hcFzcjYxh4jZikg2c8mcRjyChKmRi6Vy4O8qkcrXrQk/edit",
    "Sablés verveine citron/jasmin/cannelle": "https://docs.google.com/spreadsheets/d/1uIDs8i9wQuQKls9cu4B6qBouL9eAEJodVC-DUWc7EEA/edit",
    "Trio de mochi aux saveurs sorbets": "https://docs.google.com/spreadsheets/d/1P9M5OO7WwIvPMZIFzy3Tf-qqzkbKrOar9qLiw16YdBE/edit"
}

PRICE_DATA = {
    "4 épices": {"price": 3., "unit_qty": 30, "store": "Gde Srf"},
    "beurre": {"price": 1.95, "unit_qty": 250, "store": "https://www.promocash.com/ecommerce/product/250g-beur-dx-montfleuri-60/01t7R00000A50qEQAR"},
    "beurre salé": {"price": 2.55, "unit_qty": 250, "store": "https://www.promocash.com/ecommerce/product/250g-plqbeur1-2sel-gastro-cr/01t7R000008L5gxQAC"},
    "cannelle": {"price": 3., "unit_qty": 15, "store": "Gde Srf"},
    "cassonade": {"price": 2.69, "unit_qty": 1000, "store": "https://www.promocash.com/ecommerce/product/1kg-cassonade-bv-equi-st-louis/01t7R00000EHddyQAD"},
    "caissettes": {"price": .79, "unit_qty": 80, "store": "Stockomani"},
    "chocolat": {"price": 4.33, "unit_qty": 600, "store": "https://www.promocash.com/ecommerce/product/5x100g-tablet-choc-noir-simpl/01t7R00000A50B8QAJ"},
    "chocolat vegan": {"price": 4.52, "unit_qty": 100, "store": "https://www.greenweez.com/recherche/tablette%20chocolat%20noir%2075%25%20cacao%20nicaragua%20bio%20100g"},
    "jus de citron": {"price": 4.03, "unit_qty": 1000, "store": "https://www.promocash.com/ecommerce/product/1l-jus-de-citron-concentre-ec/01t7R000008L3K3QAK"},
    "confiture de figue": {"price": 2.02, "unit_qty": 360, "store": "https://www.promocash.com/ecommerce/product/370g-confiture-figues-bmaman/01t7R000008KysRQAS"},
    "extrait de yuzu": {"price": 7.5, "unit_qty": 100, "store": "Exo Est"},
    "farine": {"price": .95, "unit_qty": 1000, "store": "https://www.promocash.com/ecommerce/product/1kg-farine-ble-t45-/01t7R000008LAb8QAG"},
    "farine de riz": {"price": 3., "unit_qty": 400, "store": "Exo Est"},
    "farine de riz gluant": {"price": 2.5, "unit_qty": 400, "store": "Exo Est"},
    "fécule de pomme de terre": {"price": 1.08, "unit_qty": 250, "store": "https://www.promocash.com/ecommerce/product/bte-250g-fecule-pdt-tipiak/01t7R000008LEx1QAG"},
    "framboises": {"price": 7.37, "unit_qty": 1000, "store": "https://www.promocash.com/ecommerce/product/1kg-framboises-ent-en-cuisine/01t7R000008LFUKQA4"},
    "fécule de maïs": {"price": 1.99, "unit_qty": 400, "store": "https://www.promocash.com/ecommerce/product/400g-maizena-fleur-de-mais/01t7R000008L2FmQAK"},
    "graines de lin": {"price": 4., "unit_qty": 400, "store": "Norma/Stock Alex"},
    "graines de sésame noir": {"price": 4., "unit_qty": 400, "store": "Saigon Store"},
    "huile de tournesol": {"price": 2.06, "unit_qty": 1000, "store": "https://www.promocash.com/ecommerce/product/1l-huile-tournesol-clairor/01t7R000008L6XUQA0"},
    "lait": {"price": 5.82, "unit_qty": 6000, "store": "https://www.promocash.com/ecommerce/product/1l-lait-1-2-ecreme-simpl/01t7R000008LAI5QAO"},
    "lait concentré sucré": {"price": 1.9, "unit_qty": 397, "store": "https://www.promocash.com/ecommerce/product/397g-bt-lt-concsucre-nestle/01t7R000008L3VcQAK"},
    "lait d'avoine": {"price": 2.39, "unit_qty": 1000, "store": "https://www.promocash.com/ecommerce/product/1l-boisson-avoine-oatly/01t7R00000A4Nx5QAF"},
    "levure chimique": {"price": 0.3, "unit_qty": 6, "store": "https://www.auchan.fr/auchan-levure-chimique-les-patissiers/pr-C1817544"},
    "miel": {"price": 6.59, "unit_qty": 1000, "store": "https://www.promocash.com/ecommerce/product/1kg-miel-liquide-pp/01t7R000008LGaNQAW"},
    "oeuf": {"price": 25.62, "unit_qty": 90, "store": "https://www.promocash.com/ecommerce/product/90-oeufs-sol-moyen-vrac/01t7R000008LGffQAG"},
    "orange": {"price": 3., "unit_qty": 6, "store": "Gde Srf"},
    "pâte de haricots azuki": {"price": 2.99, "unit_qty": 500, "store": "Exo Est"},
    "pâte feuilletée": {"price": 0.79, "unit_qty": 1, "store": "https://www.promocash.com/ecommerce/product/230g-pate-feuillete-roucrf-cl/01t7R000008L0IhQAK"},
    "pépites trois choco": {"price": 10.6, "unit_qty": 400, "store": "https://www.promocash.com/ecommerce/product/400g-croc-gout-3-choco-vahine/01t7R000008LBKiQAO"},
    "pomme": {"price": 3., "unit_qty": 10, "store": "Gde Srf"},
    "sel": {"price": 0., "unit_qty": 1., "store": "Maison"},
    "sorbet framboise": {"price": 9.22, "unit_qty": 1400, "store": "https://www.promocash.com/ecommerce/product/25l-sorbet-en-cuis-frambois/01t7R000008KyYzQAK"},
    "sorbet poire": {"price": 9.82, "unit_qty": 1350, "store": "https://www.promocash.com/ecommerce/product/25l-sorbet-en-cuis-poire/01t7R000008LGunQAG"},
    "sorbet mangue": {"price": 9.05, "unit_qty": 1350, "store": "https://www.promocash.com/ecommerce/product/25l-sorbet-en-cuis-mangue/01t7R000008LFw8QAG"},
    "sorbet average": {"price": 9.5, "unit_qty": 1350, "store": "Placeholder"},
    "sucre": {"price": 1.32, "unit_qty": 1000, "store": "https://www.promocash.com/ecommerce/product/1kg-sac-sucre-cristal-pp/01t7R000008LDzjQAG"},
    "sucre vanillé": {"price": 0.85, "unit_qty": 10, "store": "https://www.auchan.fr/auchan-sucre-vanille-a-l-extrait-de-vanille/pr-C1273910"},
    "sucre vanillé vegan": {"price": 0.85, "unit_qty": 10, "store": "https://www.auchan.fr/auchan-sucre-vanille-a-l-extrait-de-vanille/pr-C1273910"},
    "thé jasmin": {"price": 13.78, "unit_qty": 100, "store": "Palais des thés"},
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
