class AutoMobile:

    def __init__(self, name, model):
        self.name = name
        self.model = model

    def start(self):
        print(f"{self.name} {self.model} is starting.")

    def brake(self):
        print(f"{self.name} {self.model} is braking.")


class Car(AutoMobile):
    def __init__(self, name, model, num_doors):
        super().__init__(name, model)
        self.num_doors = num_doors

class Bike(AutoMobile):
    def __init__(self, name, model, has_sidecar):
        super().__init__(name, model)
        self.has_sidecar = has_sidecar


car = Car("Toyota", "Camry", 4)
bike = Bike("Harley-Davidson", "Street 750", False)

bike.start()
car.start()