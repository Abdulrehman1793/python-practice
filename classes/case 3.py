# Case 3 :- Simple Car Simulation 

class CarSimulation :
    def __init__(self, make, models, years):
         self.make = make
         self.models = models
         self.years = years
         self.is_engine_on = False

    def start_engine(self):
         if self.is_engine_on==False:
            self.is_engine_on = True
         else:
            print("Engkine is aLREADY ON...")

    def stop_engine(self):
         if self.is_engine_on == True:
            self.is_engine_on = False
         else:
             print("engine is off")
    
    def drive(self):
        if self.is_engine_on == True:
            print(f'{self.make}, {self.models},"is driving')
        else:
            print("engine is off  Please start the engine" )
    
#example

car = CarSimulation ("ford","mustang","1999" )
car.stop_engine()
car.drive()


             



          