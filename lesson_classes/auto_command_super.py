class Auto:
    def __init__(self, name, brand, year):
        self.name = name
        self.brand = brand
        self.year = year

    def start(self):
        print('wroom wroom')
    def stop(self):
        print('...')

class ElectricCar(Auto):
    def __init__(self, name, model, year):
        super().__init__(name, model, year)
        self.battery = ElectricCar.Battery()
    class Battery:
        def __init__(self, battery_size=75):
            self.battery_size = battery_size
        def describe_battery(self):
            return f'This car has a {self.battery_size}-kwh battery'
        def get_range(self):
            if self.battery_size == 75:
                range = 260
            elif self.battery_size == 100:
                range = 315
            return f'This car can go about {range} miles on a full charge'


car = ElectricCar('xiaomi', 'galaxy2.3', 2022)
print(car.battery.describe_battery())
print(car.battery.get_range())
