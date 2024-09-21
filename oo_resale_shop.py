from typing import Optional
from computer import Computer

class ResaleShop:

    # What attributes will it need?
    inventory : list
    
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, invent):
       self.inventory = invent
       invent = []

    # What methods will you need?

        # buying a computer (add to inventory)
    """
    Takes in a Dict containing all the information about a computer,
    adds it to the inventory, returns the assigned item_id
    """
    def buy(self, computer: Computer):
        self.inventory.append(computer)
    
    """
    prints all the items in the inventory (if it isn't empty), prints error otherwise
    """
    def print_inventory(self):
        # If the inventory is not empty
        if self.inventory:
            # For each item
            for item in self.inventory:
                # Print its details
                print(item.description)
        else:
            print("No inventory to display.")

        # selling a computer (remove from inventory)
    """
    Takes in an item_id, removes the associated computer if it is the inventory, 
    prints error message otherwise
    """
    def sell(self, item: Computer):
        if item in self.inventory:
            self.inventory.remove(item)
            print("Item", item, "sold!")
        else: 
            print("Item", item, "not found. Please select another item to sell.")

        # refurbishing a computer
    def refurbish(self, computer: Computer, new_os: Optional[str] = None):
        if computer in self.inventory:
            if computer.year_made < 2000:
                computer.price = 0 # too old to sell, donation only
            elif computer.year_made < 2012:
                computer = 250 # heavily-discounted price on machines 10+ years old
            elif computer.year_made < 2018:
                computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer.price = 1000 # recent stuff

            if new_os is not None:
                computer.operating_system = new_os # update details after installing new OS
        else:
            print("Item", computer, "not found. Please select another item to refurbish.")

    def main():
        my_computer = Computer("2019 MackBook Pro", "Intel", 256, 16, "High Sierra", 2019, 1000)
        my_resale = ResaleShop()
        my_resale.buy(my_computer)
        my_resale.print_inventory()
    main()


