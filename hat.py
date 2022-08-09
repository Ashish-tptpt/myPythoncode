import random
class Hat:
    # def __init__(self): , class objects are shared by all the objects of class -->means only 1 
        self.houses=["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]
    # def sort(self,name):

    @classmethod
    def sort(cls,name):
        # hhouse= random.choice(self.houses)
        hhouse= random.choice(cls.houses)# now its not obects method its class method
        print(f"{name} is in {hhouse} house")

hat = Hat()
hat.sort("Sarthak")
#Someties We dont even need more than one class instances so we use @classmethods