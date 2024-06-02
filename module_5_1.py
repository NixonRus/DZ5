
class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def go_to(self, n_f):
        self.new_floor = n_f
        for i in range(1, n_f):
            print(i, end='\n')
        if self.new_floor < 1 or self.new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            print(n_f)




h1 = House('ЖК Созвездие', 5)
h2 = House('ЖК Авиатор', 10)
print(h1.name, h1.number_of_floors)
print(h2.name, h2.number_of_floors)
h1.go_to(6)
print('\n')
h2.go_to(10)