class Student:
    def __init__(self, name, id, address):
        self.name = name
        self.id = id
        self.address = address 
   
    def displayInfo(self):
        print("Name:", self.name)
        print("ID:", self.id)
        print("Address", self.address)

student = Student("Maxwell S.", "909102", "123 Fake St")

student.displayInfo()