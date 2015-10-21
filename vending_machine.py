class VendingMachine(object):

    #Constructor
    def __init__(self, address, change):
        self.__address = address
        self.__change = change #"private" instance variable
        self.__items = [{'name': 'Fanta', 'price': 20, 'stock': 10},
                        {'name': 'Cola', 'price': 20, 'stock': 10},
                        {'name': 'Julmust', 'price': 22, 'stock': 20}]

    #Getter - gets attribute
    @property
    def address(self):
        return self.__address

    #Getter - gets attribute
    @property
    def change(self):
        return self.__change


    #Getter - gets and formats
    @property
    def items(self):
        output = ""
        for i, item in enumerate(self.__items):
            output += "{2}: {0} ({1}kr)\n".format(item['name'], item['price'], i + 1)
        return output

    def purchase(self, item_number, amount_paid):
        item_number = item_number - 1
        self.__change += amount_paid
        output = ''
        if len(self.__items) - 1 >= item_number:
            item = self.__items[item_number]
            if item['stock'] > 0:
                if item['price'] <= amount_paid:
                    output = item['name']
                    item['stock'] -= 1
                    if amount_paid > item['price']:
                        change = amount_paid - item['price']
                else:
                    output = "Sorry, {0}kr is not enough, ({1}kr more required)".format(amount_paid, item['price'] - amount_paid)
                    change = amount_paid
            else:
                output = "Sorry, item {0} is out of stock".format(item_number + 1)
                change = amount_paid
        else:
            output = "Sorry, item {0} does not exist".format(item_number + 1)
            change = amount_paid

        output += ", ({0}kr back)".format(change)
        self.__change -= change
        return output

v1 = VendingMachine(address='Gibraltargatan 12', change=50)
v2 = VendingMachine(address='Eklandagatan 23', change=25)
print(v1.items)
print(v1.purchase(item_number=2, amount_paid=12))
print(v1.change)