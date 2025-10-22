import openpyxl
import csv
import pandas as pd
import os
import datetime
import math
from config import INGREDIENTS_MAP, UNITS_MAP, PRICE_DATA, SHOPPING_LIST_PATH, INGREDIENTS_CSV_PATH
from util import get_excel_cell


class Ingredient:
    def __init__(self, qty, unit, name):
        if type(qty) is str:
            qty = qty.replace(",", ".")
        self.qty = float(qty)
        self.unit = UNITS_MAP[unit.lower()] if unit.lower() in UNITS_MAP.keys() else unit
        self.name = INGREDIENTS_MAP[name.lower()] if name.lower() in INGREDIENTS_MAP.keys() else name

    def is_similar(self, other):
        return self.name.lower() == other.name.lower() and self.unit.lower() == other.unit.lower()

    def add_qty(self, qty):
        self.qty += qty


def add_ingredient(current_ingredient, ingredient_list):
    found = False
    for ing in ingredient_list:
        if ing.is_similar(current_ingredient):
            ing.add_qty(current_ingredient.qty)
            found = True
            break

    # Add the ingredient anyway, even if no price was found in the dictionary from config.py
    if not found:
        ingredient_list.append(current_ingredient)


def generate_shopping_list(ingredients_csv_path_override=None, tab_name=None):
    df = pd.read_csv(INGREDIENTS_CSV_PATH if not ingredients_csv_path_override else ingredients_csv_path_override)
    df = df[['Mult. Qty', 'Unit', 'Ingredient']]
    df = df.dropna()

    # Build the string to count each recipe's count
    df2 = pd.read_csv(INGREDIENTS_CSV_PATH if not ingredients_csv_path_override else ingredients_csv_path_override)
    df2 = df2[['Recipe', 'Pieces']]
    df2 = df2.dropna()
    i = 0  # line count
    current_pastry_name = ""
    pieces_per_batch = -1
    pastry_count_str = ""
    for name, count in df2.itertuples(index=False, name=None):
        if i % 2 == 0:
            current_pastry_name = name
            pieces_per_batch = float(count.replace(",", ".")) if count != "/" else 1
        else:
            target_pieces = float(count.replace(",", "."))
            total_pieces = int(pieces_per_batch * math.ceil(target_pieces / pieces_per_batch))
            if total_pieces:  # Don't add if 0 pieces
                pastry_count_str = f"Ingrédients pour {current_pastry_name} x {total_pieces}" if not pastry_count_str else f"{pastry_count_str} + {current_pastry_name} x {total_pieces}"
        i += 1

    ingredient_list = []
    for qty, unit, ingredient in df.itertuples(index=False, name=None):
        qty = float(qty.replace(",", "."))
        if ingredient.lower() in INGREDIENTS_MAP.keys() and type(INGREDIENTS_MAP[ingredient.lower()]) is list:  # Handle lists of ing mapping
            for ing_mapped in INGREDIENTS_MAP[ingredient.lower()]:
                cur_ing_mapped = Ingredient(ing_mapped["coef"]*qty, ing_mapped["unit"], ing_mapped["name"])
                add_ingredient(cur_ing_mapped, ingredient_list)
            continue

        current_ingredient = Ingredient(qty, unit, ingredient)
        add_ingredient(current_ingredient, ingredient_list)

    ingredient_list.sort(key=lambda ing: ing.name)

    # Write computed data to a new tab in the workbook
    wb = openpyxl.load_workbook(SHOPPING_LIST_PATH)
    ws2 = wb.create_sheet(title=f"List at {datetime.datetime.now().strftime('%Y-%m-%d %Hh%M.%S')}" if not tab_name else tab_name)

    ws2.append(["Quantity", "Unit", "Ingredient", "Unit price", "Unit qty", "Total price", "Store", "Notes", "", pastry_count_str])
    for i, ing in enumerate(ingredient_list):
        ws2.append([
            ing.qty,
            ing.unit,
            ing.name,
            PRICE_DATA[ing.name.lower()]["price"] if ing.name.lower() in PRICE_DATA.keys() else "",
            PRICE_DATA[ing.name.lower()]["unit_qty"] if ing.name.lower() in PRICE_DATA.keys() else "",
            f"=IF(AND({get_excel_cell(i + 1, 3)}<>\"\"; {get_excel_cell(i + 1, 4)}<>\"\"); {get_excel_cell(i + 1, 3)}*CEILING({get_excel_cell(i + 1, 0)} / {get_excel_cell(i + 1, 4)}); \"\")",
            PRICE_DATA[ing.name.lower()]["store"] if ing.name.lower() in PRICE_DATA.keys() else "",
            ""
        ])
    ws2.append(["", "", "", "", "TOTAL :", f"=SUM({get_excel_cell(1, 5)}:{get_excel_cell(len(ingredient_list), 5)})"])

    wb.save(SHOPPING_LIST_PATH)


if __name__ == "__main__":
    generate_shopping_list()
