import openpyxl

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

HEIGHT = 22 * len(RECIPES) + 1
WIDTH = 15


def get_excel_cell(i, j, lock_row=False, lock_col=False):
    """Convert Python indices (i, j) to Excel cell identifier (e.g., $A$1)."""
    def col_to_excel(col_idx):
        col_str = ""
        while col_idx >= 0:
            col_str = chr(col_idx % 26 + ord('A')) + col_str
            col_idx = col_idx // 26 - 1
        return col_str
    col = col_to_excel(j)
    row = str(i + 1)
    col_prefix = "$" if lock_col else ""
    row_prefix = "$" if lock_row else ""
    return f"{col_prefix}{col}{row_prefix}{row}"


wb = openpyxl.Workbook()

# Tab 2: Ingredients & Pieces
ws2 = wb.active
ws2.title = "Ingredients & Pieces"

cells = [["" for _ in range(WIDTH)] for _ in range(HEIGHT)]

cells[0] = ["Recipe", "Pieces", "Quantity", "Unit", "Ingredient", "", "Mult. Qty", "Unit", "Ingredient"]

recipe_index = 0
for recipe, url in RECIPES.items():
    cells[recipe_index * 22 + 1][0] = f'=HYPERLINK("{url}", "{recipe}")'
    cells[recipe_index * 22 + 1][1] = f'=IMPORTRANGE("{url}", "RECETTE!L2")'

    cells[recipe_index * 22 + 2][0] = "Target pieces:"
    cells[recipe_index * 22 + 2][1] = "0"

    for i in range(3, 23):  # Assuming max 20 ingredients per recipe
        qty_formula = f'=IMPORTRANGE("{url}", "RECETTE!J{i}")'
        cells[recipe_index * 22 + i - 1][2] = qty_formula
        mult_qty_formula = f'=IF({get_excel_cell(recipe_index * 22 + i - 1, 4)}=0; \"\"; {get_excel_cell(recipe_index * 22 + i - 1, 2)}*CEILING({get_excel_cell(recipe_index * 22 + 2, 1, True, True)} / {get_excel_cell(recipe_index * 22 + 1, 1, True, True)}))'
        cells[recipe_index * 22 + i - 1][6] = mult_qty_formula

        unit_formula = f'=IMPORTRANGE("{url}", "RECETTE!K{i}")'
        cells[recipe_index * 22 + i - 1][3] = unit_formula
        cells[recipe_index * 22 + i - 1][7] = unit_formula

        ing_formula = f'=IMPORTRANGE("{url}", "RECETTE!L{i}")'
        cells[recipe_index * 22 + i - 1][4] = ing_formula
        cells[recipe_index * 22 + i - 1][8] = ing_formula



    recipe_index += 1

# Fill tab 2
for row in cells:
    ws2.append(row)

# Tab 1: Shopping List (empty, to be filled in Google Sheets)
ws1 = wb.create_sheet(title="Shopping List")
ws1.append(["Ingredient", "Total Quantity", "Unit"])

wb.save('recipes_with_shopping_list.xlsx')
