from Userinput import Car


class CarInventory:
    def __init__(self):
        self.cars = []   # Empty list initialization for storing the objects

    # method to add a car
    def add_car(self):
        vehicle = Car()    # variable (Vehicle) created to store the User input data from Car Class
        if vehicle.add_car():   # if True value is returned from add_car()
            self.cars.append(vehicle)   # add it to list self.Car
            print("Car has been added to list")
            print()

    # method to display a car that is requested by customer
    def display(self, name, color, price):  # parameters name, color, price will be taken by user
        count = 0
        for i in self.cars:     # iterating over the list
            # check if value present in stock == value given by customer
            if i.name == name and i.color == color and i.price == price:
                count = count + 1  # checking the no. of available stock which asked by customer

        if count > 0:    # check for availability
            print("Available", count)
            print()

        else:       # if no stock exist as asked by customer
            print("Not available")
            print()

    # method to display the whole stock of the showroom
    def display_all(self):
        for i in self.cars:   # to iterate through the list
            print(i.name, i.color, i.price)  # print the objects value
            print()   # print blank line

