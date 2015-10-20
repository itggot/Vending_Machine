class VendingMachine(object):

    #Constructor
    def __init__(self, address, change):
        self.__address = address
        self.__change = change

    #Getter - gets attribute
    @property
    def address(self):
        return self.__address

    @property
    def change(self):
        return self.__change


v1 = VendingMachine(address='Gibraltargatan 12', change=50)
v2 = VendingMachine(address='Eklandagatan 23', change=25)

print(v1.change)
print(v2.change)