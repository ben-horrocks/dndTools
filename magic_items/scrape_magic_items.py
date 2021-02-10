import json
import math
from PyPDF2 import PdfFileReader
from enum import Enum
import editdistance

editdistance_tolerance = 3

magic_items_books = {
    "./books/Dungeon Master's Guide.pdf": {
        "first": 149,
        "last": 226
    }
}

item_type = ["armor", "potion", "ring", "rod", "staff", "scroll", "wand", "weapon", "wondrous"]
rarity = ["common", "uncommon", "rare", "very rare", "legendary", "artifact"]
attunement = ["requires", "attunement"]



for book in magic_items_books:
    pdf = PdfFileReader(book)
    for page in range(magic_items_books[book]["first"], magic_items_books[book]["last"]):
        page_text = pdf.getPage(page).extractText().split(" ")
        capital_words = []
        item_name = ""

        for word in page_text:
            # start by looking for capital words: if a word is more than 75% capital, it's probably an item name
            percentage_capital = sum(1.0 for c in word if c.isupper())/len(word)
            # at this point, we should also probably get
            # From there, we need to look for the type. It should be one of the item_type above
            # If it is armor or weapon, we need to check for type of armor or weapon as well (shield, sword, etc)
            # From there, we need to get the rarity. It should be one of the values above.
            # We should then check for attunement, it will probably also have parentheses around it
            # At this point, we should just extract all the text as description until we hit another capital,
            # in the which case, we would create the object and then start from the top again.



