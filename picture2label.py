"""
Match pictures to their respective labels by looking it up in the Excel sheet

Usage:
  picture2label.py <excel_file>
"""

import pandas as pd
import os, shutil, sys

from docopt import docopt

def main(args):
    excel_file = args["<excel_file>"]

    pd.set_option('display.max_columns', 500)
    df = pd.read_excel(excel_file)

    category = df['Category ']

    # Making sure that we only have the expected six unique values - buildings & architecture, etc
    category = df['Category '].str.lower()
    category = category.str.strip(to_strip=None)

    cats = []
    for c in df['Category ']:
        c = c.lower().strip()

        if c == "professions & industries":
            pass
        else:
            cats.append(c)

    cats = list(set(cats))

    cats_idx = zip(cats, range(len(cats)))   # [("a", 0), ("b", 1), ...]
    cats_idx = map(lambda x: '"' + x[0] + '": ' + str(x[1]), cats_idx)
    
    # Print categories as a Python dict
    print("cats = {" + ", ".join(cats_idx) + "}")
    print()

    for c, n in zip(df['Category '], df['File Name ']):
        c = c.lower().strip()

        if c == "professions & industries":
            c = 'industries & professions'

        c = c.replace("&", "and")

        print(n + "\t" + c)

if __name__ == "__main__":
    args = docopt(__doc__, argv=None, help=True, version=None, options_first=False)
    main(args)
