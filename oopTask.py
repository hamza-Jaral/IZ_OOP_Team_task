class Bike:
    def __init__(self, color, engine, speed):
        self.color = color
        self.engine = engine
        self.speed = speed
    
    def __str__(self):
        return f'this is a bike of {self.color} color with engine {self.engine}'
    
    ## hassan has to write his code between these two commented lines##
    ##hasan code start
    def set_engine(self, engine):
        self.engine = engine
        print("Engine Updated")
    def get_engine(self):
        return self.engine
    def set_speed (self, speed):
        self.speed = speed
        print("Speed updated!")

    def get_speed (self):
        return self.speed
    # hasan code end


    #arslan has to write his code between these two commented lines
    # arslan code start
    # arslan code end


b = Bike('white', '2cyl', 80)
b.set_engine('3cyl')
print(b.get_engine())
b.set_speed(90)
print(b.get_speed())

