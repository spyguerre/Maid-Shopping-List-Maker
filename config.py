# Path to save the generated shopping list Excel file
SHOPPING_LIST_PATH = 'shopping_list.xlsx'
# Path to the CSV file containing the ingredients (downloaded back from google sheets)
INGREDIENTS_CSV_PATH = 'shopping_list.xlsx - Ingredients.csv'

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
    "beurre": {"price": 2.7, "unit_qty": 250, "store": "Gde Srf"},
    "beurre salé": {"price": 2.7, "unit_qty": 250, "store": "Gde Srf"},
    "cannelle": {"price": 3., "unit_qty": 15, "store": "Gde Srf"},
    "cassonade": {"price": 2.5, "unit_qty": 500, "store": "Gde Srf"},
    "caissettes": {"price": 3, "unit_qty": 30, "store": "Stockomani"},
    "chocolat": {"price": 6., "unit_qty": 500, "store": "Super U"},
    "chocolat vegan": {"price": 2.5, "unit_qty": 100, "store": "Site Vegan"},
    "citron": {"price": 2., "unit_qty": 4, "store": "Gde Srf"},
    "confiture de figue": {"price": 2., "unit_qty": 370, "store": "Gde Srf"},
    "extrait de yuzu": {"price": 7.5, "unit_qty": 30, "store": "Exo Est"},
    "farine": {"price": 1., "unit_qty": 1000, "store": "Gde Srf"},
    "farine de riz gluant": {"price": 2.5, "unit_qty": 400, "store": "Saigon Store"},
    "framboises": {"price": 4., "unit_qty": 600, "store": "Gde Srf"},
    "fécule de maïs": {"price": 1.7, "unit_qty": 500, "store": "Gde Srf"},
    "graines de lin": {"price": 4., "unit_qty": 400, "store": "Norma"},
    "graines de sésame noir": {"price": 4., "unit_qty": 400, "store": "Saigon Store"},
    "huile neutre": {"price": 3., "unit_qty": 1000, "store": "Gde Srf"},
    "lait": {"price": 1.2, "unit_qty": 1000, "store": "Gde Srf"},
    "lait concentré sucré": {"price": 2.5, "unit_qty": 397, "store": "Gde Srf"},
    "lait végétal": {"price": 1.5, "unit_qty": 1000, "store": "Gde Srf"},
    "levure chimique": {"price": 0.5, "unit_qty": 6, "store": "Gde Srf"},
    "miel": {"price": 7., "unit_qty": 1000, "store": "Match"},
    "oeuf": {"price": 0.25, "unit_qty": 1, "store": "Gde Srf"},
    "orange": {"price": 3., "unit_qty": 4, "store": "Gde Srf"},
    "pâte feuilletée": {"price": 1.2, "unit_qty": 1, "store": "Gde Srf"},
    "pépites trois choco": {"price": 12., "unit_qty": 400, "store": "Promocash"},
    "pomme": {"price": 3., "unit_qty": 10, "store": "Gde Srf"},
    "sel": {"price": 0., "unit_qty": 1., "store": "Maison"},
    "sorbet": {"price": 5., "unit_qty": 500, "store": "Gde Srf"},
    "sucre": {"price": 1.3, "unit_qty": 1000, "store": "Gde Srf"},
    "sucre vanillé": {"price": 1.7, "unit_qty": 10, "store": "Gde Srf"},
    "sucre vanillé vegan": {"price": 2., "unit_qty": 10, "store": "Site Vegan ?"},
    "thé jasmin": {"price": 4., "unit_qty": 15, "store": "Super U"},
    "thé verveine citron": {"price": 4., "unit_qty": 15, "store": "Super U"},
    "eau": {"price": 0., "unit_qty": 1., "store": "Maison"},
    "margarine": {"price": 2.5, "unit_qty": 500, "store": "Gde Srf"},
}

# Mappings to standardize ingredient names
INGREDIENTS_MAP = {
    "oeuf entier": "Oeuf",
    "blanc d'oeuf": "Oeuf",
    "jaune d'oeuf": "Oeuf",
    "oeufs": "Oeuf",
    "beurre demi-sel": "Beurre salé",
    "beurre doux": "Beurre",
    "chocolat noir": "Chocolat",
    "chocolat noir corsé": "Chocolat",
    "graines de lin moulues": "Graines de lin",
    "lait de soja": "Lait végétal",
    "maïzena": "Fécule de maïs",
    "mélange 4 épices": "4 épices",
    "jus d'orange": "Orange",
    "sucre blanc": "Sucre",
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
