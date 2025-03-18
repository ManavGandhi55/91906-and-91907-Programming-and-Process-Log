"""Resistor quiz program, using the formula (Vs-Vf)/If, program made for year 10/11 students """

class Quiz:
    # Stored data about each single LED

    def __init__(self):
        self.voltage_forward = 0 # Forward voltage
        self.current = 0 # Forward Current
        self.voltage_supply = 0 # Supply voltage
        self.resistance = 0
        self.data = [] # data

    def intro(self):
        # Introduction outputed to user
        print("Welcome to Manav's resistor quiz program, this program will require you to"
              "\ncalculate the recommended resistor for a variety of LED's in a series circuit")

    def get_data(self):
        # Opens the file
        self.data = open(r"data.txt").split()


    def inputs(self):
        # Gathers the inputs from the user
        self.voltage_supply = int(input("What voltage out of 3V or 5V would you like to pick?"))
        if self.voltage_supply is 3 or 5:
            self.resistance = int(input("What is the resistance"))
        else:
            print("That is not 3V or 5V, please lock in")
            self.voltage_supply = int(input("What voltage out of 3V or 5V would you like to pick?"))



    def calculate_resistance(self):
        # Calculates resistance of the given question
        self.current = self.current / 1000 # Calculates the current in amps, not milliamps
        self.resistance = (self.voltage_supply - self.voltage_forward) / self.current






intro()