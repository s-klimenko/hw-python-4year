class Bird:  # все объекты класса Птица меньше человека, могут двигаться и хорошо поют
    def __init__(self, name):
        self.name = name

    def smallerThanHuman(self):
        return True

    def ability(self):
        return 'move'

    def sing(self):
        return 'nice'

    def canFly(self):
        if self.ability() == 'fly':
            return 'can fly'
        else:
            return 'can not fly, but can {}'.format(self.ability())


class Carinatae(Bird):  # Килевые наследуют класс Птиц, но могут летать
    def __init__(self, name):
        super().__init__(name)

    def ability(self):
        return 'fly'


class Crow(Carinatae):  # Вороны наследуют класс Килевых, но поют "кар"
    def __init__(self, name):
        super().__init__(name)

    def sing(self):
        return 'caw'


class Penguin(Carinatae):  # Пингвины наследуют класс Килевых, но летать не умеют, только плавать
    def __init__(self, name):
        super().__init__(name)

    def ability(self):
        return 'swim'


class PalaeeudyptesKlekowskii(Penguin):  # наследует класс Пингвинов, но больше человека
    def __init__(self, name):
        super().__init__(name)

    def smallerThanHuman(self):
        return False


class Ratite(Bird):  # Бескилевые наследуют класс Птиц, но не летают
    def __init__(self, name):
        super().__init__(name)

    def ability(self):
        return 'walk'

class Ostrish(Ratite):  # Страус наследует класс Бескилевых, но ужасно поет и больше человека
    def __init__(self, name):
        super().__init__(name)

    def smallerThanHuman(self):
        return False

    def sing(self):
        return 'not nice'


class Tinamu(Ratite):  # Тинаму наследует класс Бескилевых, но летает
    def __init__(self, name):
        super().__init__(name)

    def ability(self):
        return 'fly'


birds = [Tinamu('Тинаму'), Penguin('Пингвин'), Crow('Ворона'), Ostrish('Страус')]
for bird in birds:
    print(bird.name, bird.canFly())
