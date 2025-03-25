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
        self.current = 0 # Forward Current mA
        self.current_amps = 0
        self.voltage_supply = 0 # Supply voltage
        self.resistance_guess = 0 # the R value they guess
        self.resistance_calculate = 0 # the R value the code guesses
        self.led_data = led_data # data

    def intro(self):
        # Introduction outputed to user
        print("Welcome to Manav's resistor quiz program, this program will require you to"
              "\ncalculate the recommended resistor for a variety of LED's in a series circuit")
        text = input("Would you like some guidelines?(Yes/No)")
        if text.lower() == "yes":
            self.guidelines()
        elif text.lower() == "no":
            print("Here comes the quiz!")
            self.loop()
        else:
            print(f"If you are indecisive you won't get the guidelines")
            self.loop()

    def guidelines(self):
        # Provides guidelines to the user on how the quiz works\
        index = 0
        self.select_led(index)
        self.voltage_input()
        print(f"The Supply voltage is {self.voltage_supply}V \nThe forward voltage is {self.voltage_forward}V"
              f"\nThe forward current is {self.current}mA")

        print("These peices of data are used to find the reccommend resistor in a series circuit(ie; for a jackbord)"
              "\nThe formula required for this calculation is Ohm's Law, allowing you to calculate the resistance."
              "\nA quick tip is that current(I) is measured in amps, the data you recieve for forward current"
              "\nis in milliamps. To find the current in amps divide the current given by 1000."
              "\n\nSo the formula requried to find the resistance is""\n Resistance = (Vs - Vf) ÷ (If ÷ 1000)")

        print(f'First of all we should divide the current by 1000 in order to find the current in amps'
              f'\n{self.current} / 1000 = {self.current_amps}'
              f'\n\nNext wee need to add the supply voltage, forward voltage, and current into our previous equation'
              f'\nResistance = {self.voltage_supply} - {self.voltage_forward} / {self.current_amps}'
              f'\nResitance = {self.resistance_calculate}'
              f'\n\nWe will want the resistance to be rounded to 2 decimal places, altough values with >(2d.p.)'
              f'\ndo not need to be rounded'
              f'\n\nThus the resistance found is {self.resistance_calculate}ohms')
        enter = input("Press enter to continue")
        if enter == enter:
            self.loop()



    def select_led(self, index):
        # This function sets the led
        led = self.led_data[index]
        self.voltage_forward = led["Vf"]
        self.current = led["If"]
        print(f'voltage forward: {self.voltage_forward}, forward current: {self.current}')


    def voltage_input(self):
        # Gathers the inputs from the user
        self.voltage_supply = int(input("What supply voltage out of 3V or 5V would you like to pick?"))
        if self.voltage_supply == 3 or self.voltage_supply == 5:
            self.resistance_guess = int(input("What is the resistance "))
        else:
            print("That is not 3V or 5V, please lock in")
            self.voltage_input()


    def calculate_resistance(self):
        # Calculates resistance of the given question
        self.current_amps = self.current / 1000 # Calculates the current in amps, not milliamps
        self.resistance_calculate = (self.voltage_supply - self.voltage_forward) / self.current_amps
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

    def loop(self):
        # loops the function
        for index in range(len(self.led_data)):
            self.select_led(index)
            self.voltage_input()
            self.calculate_resistance()
            self.output()
        print("Thank you for running my resistor program, I hope you are now skilled enough to ace your test")

# Load LED Data
led_data = LED("data.txt").led_list

# Start the Quiz
quiz = Quiz(led_data)
quiz.start()