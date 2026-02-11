"""
    Filename: computer.py
    Description: Defines computer class used to store and manage information
        about computers. Provides methods to update the computer's operating system
        and price.
     Author: R. Jordan Crouser (@jcrouser), Yushan He
       Date: 10 February 2026
"""


class Computer:
    '''Computer Class with ability to store information about specific computer, update computer price, and update computer OS'''
    # computer.py : storing information about a specific computer, updating a computer's price, updating a computer's OS

    # attributes gathered from main.py for creating a computer

    description: str = ""
    processor_type: str = ""
    hard_drive_capacity: int = 0
    memory: int = 0
    operating_system: str = ""
    year_made: int = 0
    price: int = 0

    def __init__(self, desc: str, processor: str, harddrive: int, memory: int, OS: str, year: int, amt: int):
        '''initializes a new Computer object with hardware, operating system, year made, and price. 

        args:

        '''
        self.description = desc
        self.processor_type = processor
        self.hard_drive_capacity = harddrive
        self.memory = memory
        self.operating_system = OS
        self.year_made = year
        self.price = amt

    def updateOS(self, str: str):
        '''Changes operating system of computer'''
        self.operating_system = str

    def update_price(self, amt: int):
        '''updates price of computer'''
        self.price = amt


def main():
    inventory = []

    myComputer: Computer = Computer(
        "Mac Pro (Late 2013)", "3.5 GHc 6-core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500)

    myComputer.add_to_inventory(inventory)

    print(myComputer.check_inventory(inventory))

    print(myComputer.check_inventory)

    # print(myComputer.operating_system)
    # print(myComputer.price)

    # myComputer.updateOS("MacOS Monterey")
    # myComputer.update_price(1750)

    # print(myComputer.operating_system)
    # print(myComputer.price)


if __name__ == "__main__":
    main()
