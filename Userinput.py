
class Car:
    def __init__(self):   # constructor initialization
        # Variable initialization
        self.name = ''
        self.color = ''
        self.price = 0

    # method to add car by taking input from user
    def add_car(self):
        try:      # Exceptions
            self.name = input("Enter the name of the car : ")
            self.color = input("Enter the color of car : ")
            self.price = int(input("Enter the price of car : "))
            return True   # if no exception then it will return true.
        except ValueError:      # Handle Exception
            print("Please enter the correct values !")
            return False   # if exception then it will return false to method.
