class Rectangle:
    def __init__(self,height,width):
        self.height=height
        self.width=width

    def calculate_area(height,width):
        return height*width

    @classmethod
    def _new_square(cls,side_length):
        return side_length*side_length

print(Rectangle._new_square(5))

#or

square=Rectangle._new_square
print(square(5))


class Pizza:
    def __init__(self,toppings):
        self.toppings=toppings
    
    @staticmethod
    def validate_topping(topping):
        if topping=="pineapple":
            raise ValueError("No pineapples!")
        else:
            return True
ingredients=["cheese","onions","spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza =Pizza(ingredients)

v=0
for i in (pizza.toppings):
    print(pizza.toppings[v])
    v+=1
print("---Done---")

class Pizzas:
    def __init__(self,toppingss):
        self.toppingss=toppingss
    
    @property
    def pineapple_allowed(self):
        return False

pizzas=Pizzas(["cheese","tomato"])
print(pizzas.pineapple_allowed)

class Pizzars:
    def __init__(self,toppin):
        self.toppin=toppin
        self._pineapple_alloweds = False
    
    @property
    def pineapple_alloweds(self):
        return self._pineapple_alloweds

    @pineapple_alloweds.setter
    def pineapple_alloweds(self,value):
        if value:
            password = input("Enter the password: ")
            if password == "Sw0rdfish!":
                self._pineapple_alloweds = value
                #print(value)
            else:
                raise ValueError("Alert! Intruder")

pizzars=Pizzars(["cheese","tomato"])
print(pizzars.pineapple_alloweds)
pizzars.pineapple_alloweds =True
print(pizzars.pineapple_alloweds)