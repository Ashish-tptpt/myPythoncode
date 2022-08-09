class Wizard:
    def __init__(self,name):
        if not name:
            raise ValueError("Missing Value")
        self.name=name

class Student(Wizard):
    def __init__(self,name,branch):
        super().__init__(name)
        self.branch=branch

    ...

class Proffesor(Wizard):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject=subject

    ...
        
    