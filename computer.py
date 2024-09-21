class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int   
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, des: str, p_type: str, hd_capacity: int, memo: int, op_sys: str, yearmade: int, cost: int):
        self.description = des
        self.processor_type = p_type
        self.hard_drive_capacity = hd_capacity
        self.memory = memo
        self.operating_system = op_sys
        self.year_made = yearmade
        self.price = cost

    # What methods will you need?
    
    # updating a computer's price
    def update_price(self, new_price): # should I be using cost instead here?
         self.price = new_price
    # updating a computer's OS
    def update_os(self, os):
        self.operating_system = os
    


