# Вы приехали помогать на ферму Дядюшки Джо и видите вокруг себя множество разных животных:
# гусей "Серый" и "Белый"
# корову "Маньку"
# овец "Барашек" и "Кудрявый"
# кур "Ко-Ко" и "Кукареку"
# коз "Рога" и "Копыта"
# и утку "Кряква"
# Со всеми животными вам необходимо как-то взаимодействовать:
# кормить
# корову и коз доить
# овец стричь
# собирать яйца у кур, утки и гусей
# различать по голосам(коровы мычат, утки крякают и т.д.)

# Задача №1
# Нужно реализовать классы животных, не забывая использовать наследование, определить общие методы взаимодействия с животными и дополнить их в дочерних классах, если потребуется.
#
# Задача №2
# Для каждого животного из списка должен существовать экземпляр класса. Каждое животное требуется накормить и подоить/постричь/собрать яйца, если надо.
#
# Задача №3
# У каждого животного должно быть определено имя(self.name) и вес(self.weight).
#
# Необходимо посчитать общий вес всех животных(экземпляров класса);
# Вывести название самого тяжелого животного.

class Goose():
    weight = 0
    eggs = 0
    feed = 0
    voice = 'Гагочут'
    name = ''
    type_animal = 'Гусь'
    def pick_eggs(self, eggs = 0):
        self.eggs += eggs
    def weight_animal(self, weight):
        self.weight += weight
    def give_feed(self, feed):
        self.feed += feed
    def name_animal(self, name):
        self.name += name

class Cow():
    weight = 0
    milk = 0
    feed = 0
    voice = 'Мычат'
    name = ''
    type_animal = 'Корова'
    def pick_milk(self, milk = 0):
        self.milk += milk
    def weight_animal(self, weight):
        self.weight += weight
    def give_feed(self, feed):
        self.feed += feed
    def name_animal(self, name):
        self.name += name

class Sheep():
    wool = 0
    weight = 0
    feed = 0
    voice = 'Блеют'
    name = ''
    type_animal = 'Овечка'
    def pick_wool(self, wool = 0):
        self.wool += wool
    def weight_animal(self, weight):
        self.weight += weight
    def give_feed(self, feed):
        self.feed += feed
    def name_animal(self, name):
        self.name += name

class Chicken(Goose):
    voice = 'Кудахчут'
    type_animal = 'Курица'

class Goat(Cow):
    voice = 'Мекают'
    type_animal = 'Коза'

class Duck(Goose):
    voice = 'Крякают'
    type_animal = 'Утка'

goose = Goose()
goose1 = Goose()
cow = Cow()
sheep = Sheep()
sheep1 = Sheep()
chicken = Chicken()
chicken1 = Chicken()
goat = Goat()
goat1 = Goat()
duck = Duck()
goose.name_animal('Белый')
goose1.name_animal('Серый')
cow.name_animal('Манька')
sheep.name_animal('Барашек')
sheep1.name_animal('Кудрявый')
chicken.name_animal('Ко-Ко')
chicken1.name_animal('Кукареку')
goat.name_animal('Рога')
goat1.name_animal('Копыта')
duck.name_animal('Кряква')
goose.weight_animal(10)
goose1.weight_animal(9)
cow.weight_animal(250)
sheep.weight_animal(20)
sheep1.weight_animal(25)
chicken.weight_animal(10)
chicken1.weight_animal(9)
goat.weight_animal(30)
goat1.weight_animal(35)
duck.weight_animal(12)

farm_animals = [goose, goose1, cow, chicken, chicken1, sheep, sheep1, goat, goat1, duck]

def weight_animals(farm_animals):
    a = 0
    for i in farm_animals:
        a += i.weight
    print('Общий вес животных на ферме %s кг.' % a)
    i = 0
    h = ''
    g = 0
    for i in range(len(farm_animals)):
        if g < farm_animals[i].weight:
            g = farm_animals[i].weight
            h = farm_animals[i].type_animal
        i += 1
    print('Самое тяжёлое животное на ферме - %s.' %h)

def weight_type(farm_animals):
    list_a = []
    for i in farm_animals:
        list_a += [i.type_animal]
    type_list = list(set(list_a))
    for i in type_list:
        a = 0
        for y in farm_animals:
            if y.type_animal == i:
                a += y.weight
        print('Вес животного/ых типа %s равен %s кг.' % (i, a))


weight_animals(farm_animals)
weight_type(farm_animals)