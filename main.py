# oscar palomares
# main.py
# m03

class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def __str__(self):
        return (
            f"Vehicle type: {self.vehicle_type}\n"
            f"Year: {self.year}\n"
            f"Make: {self.make}\n"
            f"Model: {self.model}\n"
            f"Number of doors: {self.doors}\n"
            f"Type of roof: {self.roof}\n"
        )


car = Automobile(
    input("What type of vehicle: "),
    input("What year is the vehicle: "),
    input("What is the make: "),
    input("What is the model: "),
    input("How many doors: "),
    input("Does it have a solid roof or sun roof: "),
)

print(car)

