from abc import ABC, abstractmethod
from pprint import pprint 
import csv


def read_csv(file):
    with open("sample.csv") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)

read_csv("sample.csv")

#######

class Cupcake (ABC):
  
    def __init__(self, size, name, price, flavor, filling, frosting):
        self.size = size
        self.name = name 
        self.price = price
        self.flavor = flavor
        self.filling = filling
        self.frosting = frosting
        self.sprinkles = []

    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)
    @abstractmethod
    def calculate_price(self, quantity):
        return self.price * quantity

class Large(Cupcake):
    size = "large"

    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []

    def calculate_price(self, quantity):
        return self.price * quantity

class Regular(Cupcake):
    size = "regular"
    def __init__(self, name, price, flavor, filling, frosting):
        self.name = name 
        self.price = price
        self.flavor = flavor
        self.filling = filling
        self.frosting = frosting
        self.sprinkles = []

    def calculate_price(self, quantity):
        return self.price * quantity

class Mini(Cupcake):
    size = "mini"

    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []

    def calculate_price(self, quantity):
        return self.price * quantity


mini_cupcake = Mini("Chocolate", 1.59, "Chocolate", "Red")
regular_cupcake = Regular("Vanilla Love", 1.99, "vanilla", "strawberry", "vanilla")
large_cupcake = Large("Chocolate Love", 2.99, "chocolate", "strawberry", "chocolate")


mini_cupcake.frosting = "Chocolate"
regular_cupcake.filling = "Chocolate"

print(mini_cupcake.name)
print(mini_cupcake.price)
print(mini_cupcake.size)

mini_cupcake.is_mini = True
regular_cupcake.is_mini = False
large_cupcake.is_mini = False
print(mini_cupcake.is_mini)


print(mini_cupcake.frosting)
print(regular_cupcake.filling)

regular_cupcake.add_sprinkles("Oreo crumbs", "Chocolate", "Vanilla")

print(large_cupcake.sprinkles)



cupcakeA = Regular("Stars and Stripes", 1.99, "Vanilla", "Vanilla", "Chocolate")
cupcakeA.add_sprinkles("Red", "White", "Blue")
cupcakeC = Mini("Oreo", 1.59, "Chocolate", "Cookies and Cream")
cupcakeC.add_sprinkles("Oreo pieces")
cupcakeB = Large("Red Velvet", 2.99, "Red Velvet", "Cream Cheese", None)

cupcake_list = [
    cupcakeA,
    cupcakeB,
    cupcakeC
]
def write_new_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ['size', 'name', 'price', 'flavor', 'frosting', 'filling', 'sprinkles']
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
       
        writer.writeheader()

        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
            else:
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})


write_new_csv("sample.csv", cupcake_list)
    
def new_cupcake(file, cupcake):
    with open(file, 'a', newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if hasattr(cupcake, "filling"):
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
        else:
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})

    
# new_cupcake()
def get_cupcakes(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader

def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake ["name"] == name:
            return cupcake
        return None 

def add_cupcake_dictionary(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "sprinkles", "filing"]
        writer = csv.DictReader(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)
    if cupcake:
        add_cupcake_dictionary("orders.csv", cupcake)
        return redirect(url_for("home"))
    else:
        return "Sorry cupcake not found."