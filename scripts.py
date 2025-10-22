import os
from shopping_list_tab import generate_shopping_list


def gen_unit_prices():
    for file in os.listdir("./unitrecipes"):
        generate_shopping_list(ingredients_csv_path_override="./unitrecipes/" + file, tab_name=file.split(".csv")[0])
        print(f"{file} done!")


if __name__ == "__main__":
    gen_unit_prices()
