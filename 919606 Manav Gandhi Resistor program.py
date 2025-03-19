"""Resistor quiz program, using the formula (Vs-Vf)/If, program made for year 10/11 students """

class LED:
# LED class, gathers/stores LED data
    def __init__(self, filename):
        self.led_list = self.load_led_data(filename)
        print(f'{self.led_list}')

    def load_led_data(self, filename):
        with open(filename, "r") as file:
            data = file.read().splitlines()
        return [{"Vf": float(data[i]), "If": int(data[i+1])} for i in range(0, len(data), 2)]



class Quiz:

# Stored data about each single LED

    def __init__(self, led_data):
        self.voltage_forward = 0 # Forward voltage
        self.current = 0 # Forward Current
        self.voltage_supply = 0 # Supply voltage
        self.resistance_guess = 0 # the R value they guess
        self.resistance_calculate = 0 # the R value the code guesses
        self.led_data = led_data # data

    def intro(self):
        # Introduction outputed to user
        print("Welcome to Manav's resistor quiz program, this program will require you to"
              "\ncalculate the recommended resistor for a variety of LED's in a series circuit")

    def select_led(self):
        led = self.led_data[0]
        self.voltage_forward = led["Vf"]
        self.current = led["If"]
        print(f'voltage forward: {self.voltage_forward}, forward current: {self.current}')


    def inputs(self):
        # Gathers the inputs from the user
        self.voltage_supply = int(input("What voltage out of 3V or 5V would you like to pick?"))
        if self.voltage_supply == 3 or 5:
            self.resistance_guess = int(input("What is the resistance "))
        else:
            print("That is not 3V or 5V, please lock in")
            self.voltage_supply = int(input("What voltage out of 3V or 5V would you like to pick? "))


    def calculate_resistance(self):
        # Calculates resistance of the given question
        self.current = self.current / 1000 # Calculates the current in amps, not milliamps
        self.resistance_calculate = (self.voltage_supply - self.voltage_forward) / self.current
        print(f'Resistance Calculated: {self.resistance_calculate}')

    def output(self):
        # provides the basic outputs
        if self.resistance_guess == self.resistance_calculate:
            print(f'You are correct, the resistance is in fact {self.resistance_calculate}')
        else:
            print(f'You are incorrect, the resistance is in fact {self.resistance_calculate}')

    def start(self):
    # start function
        self.intro()
        self.select_led()
        self.inputs()
        self.calculate_resistance()
        self.output()

# Load LED Data
led_data = LED("data.txt").led_list

# Start the Quiz
quiz = Quiz(led_data)
quiz.start()
