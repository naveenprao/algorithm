__author__ = 'nrao'
class Fruit:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    # def __eq__(self, other):
    #     return (self.weight, self.name) == (other.weight, other.name)
    # def __ne__(self, other):
    #     return not self == other

    # def __gt__(self, other):
    #     return (self.weight, other.name) > (other.weight, self.name)
    def __lt__(self, other):
        return (self.weight, other.name) < (other.weight, self.name)

    # def __le__(self, other):
    #     return self < other or self == other
    # def __gt__(self, other):
    #     return self > other or self == other

    def __repr__(self):
        return str(self.name) + ' ' + str(self.weight)

fruit_basket = list()
fruit_basket.append(Fruit('apple', 10))
fruit_basket.append(Fruit('pineapple', 10))
fruit_basket.append(Fruit('apple', 100))
fruit_basket.append(Fruit('apple', 10))

print fruit_basket
fruit_basket = sorted(fruit_basket, reverse=True)
print fruit_basket