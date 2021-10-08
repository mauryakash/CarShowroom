from display import CarInventory
print("________Car Showroom_______")

# object creation of CarInventory
showroom = CarInventory()


while True:
    # User Choice Selection
    print('Choice 1: Add Car to showroom')
    print('Choice 2: Delete car from showroom')
    print('Choice 3: Search car')
    print('Choice 4: View all available Cars')
    print('Choice 5: exit')
    # Input taken by user based on above selection
    User_Choice = input('Please Enter your Choice from one of the above options: ')
    if User_Choice == "1":
        # add a car
        showroom.add_car()
    elif User_Choice == '2':
        # delete a car
        # check if any car is present or not
        if len(showroom.cars) < 1:
            print('Sorry there are no Cars currently in Inventory')
            continue
        # display the available cars in the Inventory
        showroom.display_all()
        # taking user input to delete the car
        Products = int(input('Please enter the number associated with the vehicle to be removed: '))
        # check if input provided is valid or not for deletion
        # checking by index
        if Products - 1 > len(showroom.cars):
            print('This is an invalid number')
            print()
        else:
            # remove the car by index no
            showroom.cars.remove(showroom.cars[Products - 1])
            # print a blank line
            print()
            print('This car has been removed')
            print()
    elif User_Choice == '3':
        # check if any car is present or not
        if len(showroom.cars) < 1:
            print('Sorry there are no vehicles currently in inventory')
            print()
            continue
        # display the available car after one print statement of available
        # print("Available")
        name = input("enter the name of car you want : ")
        color = input("enter the color of car you want : ")
        price = int(input("Enter the price : "))

        showroom.display(name=name, color=color, price=price)

    elif User_Choice == '4':
        # check if any car is present or not
        if len(showroom.cars) < 1:
            print('Sorry there are no vehicles currently in inventory')
            print()
            continue
        else:
            print("All available Cars")
            showroom.display_all()

    elif User_Choice == '5':
        print('Goodbye')
        print()
        # terminate the loop and exit out
        break
    else:
        # invalid user input
        print('This is an invalid input. Please try again.')
        print()

