class Drink:
    def __init__(self, name, volume):
        self.name = name 
        self.volume = volume
    def info_display(self):
        print(f"Напиток: {self.name}, объем: {self.volume} мл.")

class HotDrink(Drink):
    def __init__(self, name, volume, temperature=75):
        super().__init__(name, volume)
        self.temperature = temperature
    def info_display(self):
        print(f"Горячий напиток: {self.name}, объем: {self.volume} мл, температура: {self.temperature} градусов.")

class ColdDrink(Drink):
    def __init__(self, name, volume, ice_cubes=3):
        super().__init__(name, volume)
        self.ice_cubes = ice_cubes
    def info_display(self):
        print(f"Холодный напиток: {self.name}, объем: {self.volume} мл, кубики льда: {self.ice_cubes}")

class Customer:
    def __init__(self,name):
        self.name = name
        self.orders = []
    def order_drink(self, drink):
        self.orders.append(drink)
        print(f"{self.name} заказал: {drink.name}")
    def show_orders(self):
        print(f"Заказы клиента {self.name}:")
        if not self.orders:
            print("Нет заказов.")
        else:
            for drink in self.orders:
                drink.info_display()

class DrinkMenu:
    def __init__(self):
        self.drinks = []
    def add_drink(self, drink):
        self.drinks.append(drink)
        print(f"Добавлен напиток в меню: {drink.name}")
    def show_all_drinks(self):
        print("Меню кафе:")
        for drink in self.drinks:
            drink.info_display()

tea = HotDrink("Чай", 300)
coffee = HotDrink("Кофе", 250, temperature=80)
cola = ColdDrink("Кола", 330)
lemonade = ColdDrink("Лимонад", 500, ice_cubes=5)

menu = DrinkMenu()
menu.add_drink(tea)
menu.add_drink(coffee)
menu.add_drink(cola)
menu.add_drink(lemonade)

menu.show_all_drinks()

customer1 = Customer("Алексей")

customer1.order_drink(tea)
customer1.order_drink(cola)
customer1.show_orders()

print("\n")
#Bus 
import random

class Passenger:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

class BusStop:
    def __init__(self, name):
        self.name = name 
        self.waiting_passengers = [] #Люди ожидают автобус
    def arrive_passengers(self):
        count = random.randint(0, 5)
        for i in range(count):
            passenger = Passenger(f"Пассажир_{self.name}_{i+1}")
            self.waiting_passengers.append(passenger)
        print(f"На остановке {self.name} ждут {len(self.waiting_passengers)} человек.")
    def board_bus(self, bus):
        if self.waiting_passengers:
            bus.passengers.extend(self.waiting_passengers)
            print(f"{len(self.waiting_passengers)} человек сели в автобус.")
            self.waiting_passengers = []
        else:
            print("На этой остановке никто не садится.")

class Bus:
    def __init__(self, route_name, capacity=10):
        self.route_name = route_name
        self.capacity = capacity
        self.passengers = []
    def arrive_stop(self, stop):
        print(f"\n Автобус '{self.route_name}' прибыл на остановку: {stop.name}")
        self.drop_off()
        stop.arrive_passengers()
        stop.board_bus(self)
        print(f"Сейчас в автобусе {len(self.passengers)} пассажиров.")
    def drop_off(self):
        if self.passengers:
            count = random.randint(0, len(self.passengers))
            leaving = self.passengers[:count]
            self.passengers = self.passengers[count:]
            print(f"{len(leaving)} человек(а) вышли из автобуса.")
        else:
            print("Автобус пуст, никто не выходит.")
    def finish_route(self):
        print(f"Автобус '{self.route_name}' закончил маршрут.")
        print(f"Всего пассажиров осталось в автобусе: {len(self.passengers)}.")

stops = [BusStop("Центр"),BusStop("Школа"),BusStop("Парк"),BusStop("Вокзал")]
bus = Bus("Маршрут 46")
for stop in stops:
    bus.arrive_stop(stop)
bus.finish_route()