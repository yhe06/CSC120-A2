"""
    Filename: oo_resale_shop.py
    Description: Defines shop class used to buy, sell, refurbish, and check inventory of computers. Provides methods to store inventory of computer.
     Author: R. Jordan Crouser (@jcrouser), Yushan He
       Date: 10 February 2026
"""

from computer import *
from typing import Dict, Union, Optional


class ResaleShop:
    """Class representing a resale shop that buys, sells, and refurbishes computers."""
    inventory = []

    def __init__(self, inventory: list):
        '''initializes a new ResaleShop object.'''
        self.inventory = inventory  # shop will start with an inventory

    def buy(self, desc: str, processor: str, harddrive: int, memory: int, os: str, year: int, price: int):
        '''Takes in information about new computer and adds it to inventory'''

        new_computer = Computer(
            desc, processor, harddrive, memory, os, year, price)
        self.inventory.append(new_computer)

    def sell(self, computer: Computer, description: str):
        '''Checks whether computer is in inventory and removes it to mimic selling'''

        if computer in self.inventory:
            if computer.description == description:
                self.inventory.remove(computer)
        else:
            print("Computer not found. Please select another item to sell.")

    def updatePrice(self, amt: int, computer: Computer):
        '''Updates price of a computer'''

        if computer in self.inventory:
            computer.price = amt
        else:
            print("Computer not found. Cannot update price.")

    def print_inventory(self, inventory: list):
        '''prints a list of all computer with just the desc., not all the OS and hardware information'''
        for item in self.inventory:
            print(item.description)

    def refurbish(self, computer: Computer, new_os: Optional[str] = None):
        '''updates price of computer depending on year the computer was made, and option to update OS'''
        if computer in self.inventory:
            if int(computer.year_made) < 2000:
                computer.price = 0  # too old to sell, donation only
            elif int(computer.year_made) < 2012:
                # heavily-discounted price on machines 10+ years old
                computer.price = 250
            elif int(computer.year_made) < 2018:
                # discounted price on machines 4-to-10 year old machines
                computer.price = 550
            else:
                computer.price = 1000  # recent stuff

            if new_os is not None:
                # update details after installing new OS
                computer.operating_system = new_os
        else:
            print("Computer not found. Please select another item to refurbish.")


def main():
    inventory = []

    shop: ResaleShop = ResaleShop(inventory)

    shop.buy("Mac Pro (Late 2013)", "3.5 GHc 6-core Intel Xeon E5",
             1024, 64, "macOS Big Sur", 2013, 1500)

    shop.buy("Mac Pro (Late 2020)", "3.5 GHc 6-core Intel Xeon E5",
             1024, 64, "macOS Big Sur", 2020, 1500)

    print(inventory[0].price)

    shop.updatePrice(1750, inventory[2])

    print(inventory[0].price)
    shop.refurbish(inventory[0])

    shop.print_inventory(inventory)
    print(inventory[0].price)

    shop.sell(inventory[0])

    shop.print_inventory(inventory)


if __name__ == "__main__":
    main()
