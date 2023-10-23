class Human:
    def __init__(self,name = "Human"):
        self.name = name

class Auto:
    def __init__(self,brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, *args):
        for passenger in args:
            self.passengers.append(passenger)

    def print_passengers_names(self):
        if self.passengers != []:
            print(f"Імена пасажирів в авто:{self.brand}")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"в авто{self.brand} пасажири відсутні")

car = Auto("ВАЗ 2101")
for i in range(4):
    p1 = Human(input("Введіть ім'я пасажира"))
    car.add_passenger(p1)

car.print_passengers_names()