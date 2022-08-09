


class Student():
    def __init__(self,name,house):
        #constructor calling itself with name ,house 
        if not name:
            raise ValueError("Missing Value")
        if house not in ["gryffindor","Slyterin","RavenClaw","Hufflepuff"]:
            raise ValueError("Invalid house")
        self.name=name
        self.house= house 

    @classmethod
    def get(cls):
        name=input("Name:") 
        house=input("House:")
        return Student(name,house)    

    def __str__(self):
        return " a student "
    # def charm(self):
    #     print(f"{self.name} charmes others")
    @property #getters by convention is like this
    def home(self):
        return self.house
    # @_house.setter  # setters by convention are like this and also called when student.house
    # def home(self,house):
    #     house = self.house
        

def main():
    student = rename()
#tuples are immutabale(changeable) lists are not
    print(f"{student.name} is in {student.house}")  
    # student.charm()
    # print(student)  

# tuples like return a ,b is single entity
def rename():
    student =Student.get()
    return student
    

if __name__ == "__main__":
    main()