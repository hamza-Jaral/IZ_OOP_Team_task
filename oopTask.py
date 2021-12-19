class Bike:
    def __init__(self, color, engine, speed):
        self.color = color
        self.engine = engine
        self.speed = speed
    
    def __str__(self):
        return f'this is a bike of {self.color} color with engine {self.engine}'
    
    ## hassan has to write his code between these two commented lines##
    ##hasan code start
    # hasan code end


    #arslan has to write his code between these two commented lines
    # arslan code start
    # arslan code end


b = Bike('white', '2cyl', '80')
b.set_color('black')
print(b.get_color())
print(b.time_to_complete_distance(30))

