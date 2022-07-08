class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []
        self.first_letter_list = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        for el in self.products:
            if el[0] == first_letter.lower():
                self.first_letter_list.append(el)

            elif el[0] == first_letter.upper():
                self.first_letter_list.append(el)

        return self.first_letter_list

    def __repr__(self):
        self.products.sort()

        output = f"Items in the {self.name} catalogue:\n"

        output += '\n'.join(self.products)

        return output


# code to test the class
#
# catalogue = Catalogue("Furniture")
# catalogue.add_product("Sofa")
# catalogue.add_product("Mirror")
# catalogue.add_product("Desk")
# catalogue.add_product("Chair")
# catalogue.add_product("Carpet")
# print(catalogue.get_by_letter("C"))
# print(catalogue)
