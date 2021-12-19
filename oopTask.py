class Bike:
    '''
    Bike class creates bike object. It has three attributes (color, engine and speed).
    '''
    def __init__(self, color, engine, speed):
        self.color = color
        self.engine = engine
        self.speed = speed
    
    def __str__(self):
        return f'this is a bike of {self.color} color with engine {self.engine}'
    
    ## hassan has to write his code between these two commented lines##
    ##hasan code start
    def set_engine(self, engine):
        '''
        this is set engine function and will take engine type as in input which is string
        this function will also print Engine Updated

        '''
        self.engine = engine
        print("Engine Updated")
    def get_engine(self):
        '''
        this function will return engine type
        '''
        return self.engine
    def set_speed (self, speed):
        '''
        this function will set bike speed and will print speed updated
        '''
        self.speed = speed
        print("Speed updated!")

    def get_speed (self):
        '''
        this function will return speed
        '''
        return self.speed
    # hasan code end


    #arslan has to write his code between these two commented lines
    # arslan code start
    def set_color(self, color):
        '''
        This is funtion is use for change the color of bike
    '''
        self.color = color
        print("Color updated")
    '''
        This is funtion is use for get the color of bike
    '''
    def get_color(self):
        return self.color
    '''
        This is funtion is use for Distan cover of bike
    '''
    def time_to_complete_distance(self, distance):
        time = distance / self.speed
        return time  
    # arslan code end


b = Bike('white', '2cyl', 80)
b.set_engine('3cyl')
print(b.get_engine())
b.set_speed(90)
print(b.get_speed())


#this is a commmnt

