class Pet:
    def __init__(self):
        self.name = ""
        self.type = ""
        self.age = 0

    # Mutator methods (setters)
    def setName(self, name):
        self.name = name

    def setType(self, pet_type):
        self.type = pet_type

    def setAge(self, age):
        self.age = age

    # Accessor methods (getters)
    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getAge(self):
        return self.age


# Main program
def main():
    # Create a Pet object
    my_pet = Pet()

    # Get user input
    name = input("Enter the name of your pet: ")
    pet_type = input("Enter the type of animal (e.g., Dog, Cat, Bird): ")
    age = input("Enter the age of your pet: ")

    # Set data in the object
    my_pet.setName(name)
    my_pet.setType(pet_type)
    my_pet.setAge(age)

    # Display pet information using accessor methods
    print("\nYour Pet's Information")
    print("----------------------")
    print(f"Name: {my_pet.getName()}")
    print(f"Type: {my_pet.getType()}")
    print(f"Age : {my_pet.getAge()}")


# Run the program
if __name__ == "__main__":
    main()