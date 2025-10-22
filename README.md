# Automated shopping list generator

This python project can be used to generate
a shopping list in an Excel/Google Docs format,
based on a list of recipes and their ingredients.
This app was originally built for Anim'Est :)

## Installation

- Clone the repository:

```
git clone https://github.com/spyguerre/Maid-Shopping-List-Maker.git
cd Maid-Shopping-List-Maker
```

- Create a virtual environment and activate it:

```
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate` instead
```

- Install the required packages:

```
pip install -r requirements.txt
```

## Setup

- Your recipes should be uploaded Google Sheets, following
the format (ingredients and pieces counts location)
described in `ExampleRecipe.xlsx`.

- Edit the `config.py` file:
  - Update `RECIPES` with your recipes' names
  and Drive links.
  - Optional: Update `PRICE_DATA` with your ingredients' names,
  prices and store.
  - Optional: Update `INGREDIENTS_MAP` and `UNITS_MAP` to standardize
  and map ingredient and unit names to your preferred names.


## Usage

- First, run the script to generate the ingredients tab:

```
python ingredients_tab.py
```

Your shopping_list.xlsx file will be created with its first tab,
that fetches ingredients data when uploaded to Google Drive.
You will need to manually allow access to each recipe sheet
in Google Sheets.

- After uploading the file to Google Drive and allowing access
to recipe sheets, set your desired amount of pieces for each recipe
next to `target pieces:`, and download this tab as CSV file.
Change the `INGREDIENTS_CSV_PATH` inside `config.py` if necessary.

- Finally, run the script to generate the shopping list tab:

```
python shopping_list.py
```

Your shopping_list.xlsx file will be updated with its second tab
that contains the generated shopping list. You can now upload it
to Google Drive again (replace the previous version instead of removing it;
this makes you skip the access authorization step); and possibly filter
out the zeros in the list!

**WARNING**: You will have to **manually update** the
shopping list with this program each time you want to change
the target amount of pieces for each recipe.
