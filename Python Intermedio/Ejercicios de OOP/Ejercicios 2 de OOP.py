class Bus:
    max_passengers = 50
    def __init__(self):
        self.passengers = []
        
    def add_passenger(self, passenger):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(passenger)
    
    def remove_passenger(self, passengers):
        if passengers in self.passengers:
            self.passengers.remove(passengers)
            
class Person:
    pass

my_bus = Bus()

def bus_route(my_bus,passenger):
    while True:
        print("\nBUS MENU")
        print("1. Add passengers")
        print("2. Remove passengers")
        print("3. Exit")
        print(f"Passengers onboard: {len(my_bus.passengers)}")

        option = input("Choose an option: ")

        if option == "1":
            if len(my_bus.passengers) < my_bus.max_passengers:
                amount = int(input("How many passengers are boarding? "))
                for i in range(amount):
                    my_bus.add_passenger(Person())
            else:
                print("Bus is full. You cannot add more passengers.")

        elif option == "2":
            amount = int(input("How many passengers are getting off? "))
            for i in range(amount):
                if my_bus.passengers:
                    passenger = my_bus.passengers[0]
                    my_bus.remove_passenger(passenger)
                else:
                    print("There are no passengers on the bus.")
                    break
                
        elif option == "3":
            print("Exiting bus system.")
            break

        else:
            print("Invalid option. Try again.")
    

bus_route(my_bus,Person())

# If the number of passengers requested exceeds the available capacity,
# only the passengers who fit on the bus will be added.
# The system should notify the user if some passengers cannot board.
# This improvement is left for later becadye due to the current implementation
# meets the assignment requirements.
