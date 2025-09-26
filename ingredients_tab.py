import openpyxl
from util import get_excel_cell
from config import RECIPES, SHOPPING_LIST_PATH, HEIGHT, WIDTH


def generate_ingredients_tab():
    wb = openpyxl.Workbook()

    # Tab 1: Ingredients & Pieces
    ws1 = wb.active
    ws1.title = "Ingredients"

    cells1 = [["" for _ in range(WIDTH)] for _ in range(HEIGHT)]

    cells1[0] = ["Recipe", "Pieces", "Quantity", "Unit", "Ingredient", "", "Mult. Qty", "Unit", "Ingredient"]

    recipe_index = 0
    for recipe, url in RECIPES.items():
        cells1[recipe_index * 22 + 1][0] = f'=HYPERLINK("{url}", "{recipe}")'
        cells1[recipe_index * 22 + 1][1] = f'=IMPORTRANGE("{url}", "RECETTE!L2")'

        cells1[recipe_index * 22 + 2][0] = "Target pieces:"
        cells1[recipe_index * 22 + 2][1] = "0"

        for i in range(3, 23):  # Assuming max 20 ingredients per recipe
            qty_formula = f'=IMPORTRANGE("{url}", "RECETTE!J{i}")'
            cells1[recipe_index * 22 + i - 1][2] = qty_formula
            mult_qty_formula = f'=IF({get_excel_cell(recipe_index * 22 + i - 1, 4)}=0; \"\"; {get_excel_cell(recipe_index * 22 + i - 1, 2)}*CEILING({get_excel_cell(recipe_index * 22 + 2, 1, True, True)} / {get_excel_cell(recipe_index * 22 + 1, 1, True, True)}))'
            cells1[recipe_index * 22 + i - 1][6] = mult_qty_formula

            unit_formula = f'=IMPORTRANGE("{url}", "RECETTE!K{i}")'
            cells1[recipe_index * 22 + i - 1][3] = unit_formula
            cells1[recipe_index * 22 + i - 1][7] = unit_formula

            ing_formula = f'=IMPORTRANGE("{url}", "RECETTE!L{i}")'
            cells1[recipe_index * 22 + i - 1][4] = ing_formula
            cells1[recipe_index * 22 + i - 1][8] = ing_formula



        recipe_index += 1

    # Fill tab 2
    for row in cells1:
        ws1.append(row)

    wb.save(SHOPPING_LIST_PATH)


if __name__ == "__main__":
    generate_ingredients_tab()
