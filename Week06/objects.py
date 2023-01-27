class Student():
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def changeID(self, id):
        self.id = id

    def print(self):
        print("{} - {}".format(self.name, self.id))

dudu = Student("Eduardo", 24)
dudu.print() # Eduardo - 24
dudu.changeID(25)
dudu.print() # Eduardo - 25