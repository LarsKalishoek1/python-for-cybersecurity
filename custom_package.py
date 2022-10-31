class inventory:
    def __init__(self, name, quantity, description):
        self.name = name
        self.quantity = quantity
        self.description = description
    
    def itemView(self):
        return "{} {} {}".format(self.name, self.quantity, self.description)
    
    def questions(self): 
        for x in range(1,1000):
            listItem = []
            item = input("Which item do you want to add to the inventory?: ").lower()
            quan = input(f"How many {item} do you want to add?: ").lower()
            desc = input(f"Describe {item}: ").lower()
            listItem.append(inventory(item, quan, desc))

            item1 = [inventory(item, 2, "milk")]
            print(inventory.itemView(item1))    

inventory.questions(item1)