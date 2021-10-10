class Spaceship:
    fuel = 400
    passengers = ["John", "Steve", "Sam", "Danielle"]
    Shields = True
    Speedometer = 0

    def listPassengers(self):
        for passenger in self.passengers:
            print(f'Passenger: {passenger}')

    def add_passenger(self, new_passenger):
        self.passengers.append(new_passenger)
        print(f'{new_passenger} was added to the ship.')

    def travel(self, distance):
        print(f'Trying to travel {distance}.')
        if self.fuel <= 0:
            print("Can't go further, tank is empty.")
        else:
            self.fuel = self.fuel - (distance / 2)
            if self.fuel < 0:
                distance = (distance - (self.fuel * -2))
                print(f"Can only travel {distance}.")
                self.fuel = 0
            self.Speedometer += distance
            if self.fuel < 30 and self.Shields:
                self.Shields = False
                print("Fuel is low, turning off shields!")
            print(f"The spaceship is at {self.Speedometer}.")
            print(f"The spaceship has {self.fuel} fuel.")


mySpaceship = Spaceship()

mySpaceship.listPassengers()
mySpaceship.add_passenger('Lindsay')
mySpaceship.listPassengers()
mySpaceship.travel(750)
mySpaceship.travel(200)
mySpaceship.travel(100)