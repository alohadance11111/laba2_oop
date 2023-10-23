class Car:
    fuel = 100
    brand = "bugatti"
    model = "veyron"
    year = "2015"
    driver = "ilya"

    def go(self):
        pass

    def turn(self):
        pass

    def stop(self):
        pass

    def show_info(self):
        print(self.fuel,self.brand,self.model,self.year,self.driver)
#
class Driver:
    name="ilya"
    surname="filippov"
    age="18"
    def show_info(self):
        print(self.name,self.surname,self.age)

myCar = Car()
myCar.go()

myCar.show_info()

myDriver = Driver()
myDriver.show_info()