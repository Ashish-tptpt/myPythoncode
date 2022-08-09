class Vault():
    def __init__(self,money,time,will):
        self.money= money
        self.time= time
        self.will= will
    def __str__(self):
        return f"{self.time} and {self.will} and {self.money} are must"

    def __add__(self,other):
        money = self.money+other.money
        time = self.time+other.time
        will = self.will+other.will
        return Vault(money,time,will)

my =Vault(50,100,80)
print(my)
Anna =Vault(100,60,75)
print(Anna)
total=my + Anna
print(total)