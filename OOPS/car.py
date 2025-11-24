class Car:
    def __init__(self,model,year, color,for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
    def drive(self):
        print(f"Driving Car {self.model}")
    def stop(self):
        print(f"Stopping Car {self.model}")
    def describe(self):
        print(f"The car model is {self.model} and its color is {self.color} being made in {self.year}. Sale Status = {self.for_sale}")
