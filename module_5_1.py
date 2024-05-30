
class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def go_to(self, n_f):
        self.new_floor = n_f
        if self.new_floor < 1 or self.new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            print(n_f)




h1 = House('ЖК Созвездие', 15)
h2 = House('ЖК Авиатор', 20)
print(h1.name, h1.floors)
print(h2.name, h2.floors)
h1.go_to(5)
h2.go_to(20)