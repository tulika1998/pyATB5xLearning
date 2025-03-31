class car:
    def __init__(self, o_name, o_make, o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model

    def start_engine(self):
        print("starting a car with the name" + self.name)
        print("starting a car with the make" + self.make)
        print("starting a car with the model" + self.model)

lambo = car("lambo", "V6", "2023" )
lambo.start_engine()
