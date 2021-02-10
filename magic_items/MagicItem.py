


class MagicItem:

    def __init__(self, name, item_type, rarity, reference, description, attunement=False):
        self.name = name
        self.item_type = item_type
        self.rarity = rarity
        self.attunment = attunement
        self.reference = reference
        self.description = description

    def __str__(self):
        return f'{self.name}:' \
               f'  Type: {self.item_type}' \
               f'  Rarity: {self.rarity}' \
               f'  Attunement: {self.attunment}' \
               f'  Reference: {self.reference}' \
               f'  Description: {self.description}'
