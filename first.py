from random import choice


class Car:
    def __init__(self, engine_capasity, mileage, color, max_speed, fuel_supply, cost):
        self.engine_capasity = engine_capasity
        self.mileage = mileage
        self.color = color
        self.max_speed = max_speed
        self.fuel_supply = fuel_supply
        self.cost = cost

    def __lt__(self, other):
        if self.cost < other.cost:
            return self.cost < other.cost
        elif self.cost == other.cost and self.engine_capasity != other.engine_capasity:
            return self.engine_capasity < other.engine_capasity
        elif self.cost == other.cost and self.engine_capasity == other.engine_capasity:
            return self.fuel_supply < other.fuel_supply

    def __str__(self):
        return f'engine_capasity: {self.engine_capasity} ,mileage: {self.mileage} ,color: {self.color} ,max_speed: {self.max_speed} ,fuel_supply: {self.fuel_supply} ,cost: {self.cost}'


color_list = ['red', 'blue', 'white', 'black', 'pink', 'green', 'grey', 'yellow', 'purple']
mileage_list = ['10000', '20000', '30000', '40000', '50000', '60000', '70000', '80000', '90000', '100000']
engine_capasity_list = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
max_speed_list = ['120', '130', '140', '150', '160', '170', '180', '190', '200', '210', '220', '230', '240', '250']
fuel_supply_list = [30, 40, 50, 60, 70, 80, 90, 100]
cost_list = [3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]
cars_list = []
for i in range(10):
    car = Car(choice(engine_capasity_list),
              choice(mileage_list),
              choice(color_list),
              choice(max_speed_list),
              choice(fuel_supply_list),
              choice(cost_list))
    cars_list.append(car)

[print(i) for i in cars_list]
print('==============================================================================================================')
cars_list = sorted(cars_list)
[print(i) for i in cars_list]