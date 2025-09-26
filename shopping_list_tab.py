import openpyxl
import csv
import pandas as pd
import os
import datetime
from config import INGREDIENTS_MAP, UNITS_MAP, PRICE_DATA, SHOPPING_LIST_PATH, INGREDIENTS_CSV_PATH
from util import get_excel_cell


class Ingredient:
    def __init__(self, qty, unit, name):
        self.qty = float(qty)
        self.unit = UNITS_MAP[unit.lower()] if unit.lower() in UNITS_MAP.keys() else unit
        self.name = INGREDIENTS_MAP[name.lower()] if name.lower() in INGREDIENTS_MAP.keys() else name

    def is_similar(self, other):
        return self.name.lower() == other.name.lower() and self.unit.lower() == other.unit.lower()

    def add_qty(self, qty):
        self.qty += qty


def generate_shopping_list():
    df = pd.read_csv(INGREDIENTS_CSV_PATH)
    df = df[['Mult. Qty', 'Unit', 'Ingredient']]
    df = df.dropna()

    ingredient_list = []
    for qty, unit, ingredient in df.itertuples(index=False, name=None):
        current_ingredient = Ingredient(qty, unit, ingredient)

        found = False
        for ing in ingredient_list:
            if ing.is_similar(current_ingredient):
                ing.add_qty(current_ingredient.qty)
                found = True
                break

        if not found:
            ingredient_list.append(current_ingredient)

    ingredient_list.sort(key=lambda ing: ing.name)

    wb = openpyxl.load_workbook(SHOPPING_LIST_PATH)
    ws2 = wb.create_sheet(title=f"List at {datetime.datetime.now().strftime('%Y-%m-%d %Hh%M.%S')}")

    ws2.append(["Quantity", "Unit", "Ingredient", "Unit price", "Unit qty", "Total price", "Store", "Notes"])
    for i, ing in enumerate(ingredient_list):
        ws2.append([
            ing.qty,
            ing.unit,
            ing.name,
            PRICE_DATA[ing.name.lower()]["price"] if ing.name.lower() in PRICE_DATA.keys() else "",
            PRICE_DATA[ing.name.lower()]["unit_qty"] if ing.name.lower() in PRICE_DATA.keys() else "",
            f"=IF(AND({get_excel_cell(i+1, 3)}<>\"\"; {get_excel_cell(i+1, 4)}<>\"\"); {get_excel_cell(i+1, 3)}*CEILING({get_excel_cell(i+1, 0)} / {get_excel_cell(i+1, 4)}); \"\")",
            PRICE_DATA[ing.name.lower()]["store"] if ing.name.lower() in PRICE_DATA.keys() else "",
            ""
        ])

    wb.save(SHOPPING_LIST_PATH)


if __name__ == "__main__":
    generate_shopping_list()
