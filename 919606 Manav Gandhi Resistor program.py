"""Resistor quiz program, using the formula (Vs-Vf)/If, program made for year 10/11 students """
import os # imports the os module for Python
import time # imports the time module for Python
import random # imports random module for Python


class LED:
# LED class, gathers/stores LED data
    def __init__(self, filename):
        self.led_list = self.load_led_data(filename)
        random.shuffle(self.led_list)
        # print(f'{self.led_list}')

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
        self.question = 0
        self.score = 0
        self.help = 0
        self.led_data = led_data # data
        self.vs3_list = ['3', '3V']
        self.vs5_list = ['5', '5V']


    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def pause_quick(self):
        time.sleep(2)

    def pause_medium(self):
        time.sleep(4)

    def pause_slow(self):
        time.sleep(6)

    def intro(self):
        # Introduction outputed to user
        print("Welcome to Manav's resistor quiz program, this program will require you to"
              "\ncalculate the recommended resistor for a variety of LED's in a series circuit")
        self.pause_quick()
        text = input("Would you like some guidelines?(Yes/No)")
        if text.lower() == "yes":
            self.guidelines()
        elif text.lower() == "no":
            print("Here comes the quiz!")
            self.pause_quick()
            self.clear()
            self.loop()
        else:
            print(f"If you are indecisive you won't get the guidelines")
            self.pause_quick()
            self.clear()
            self.loop()

    def guidelines(self):
        # Provides guidelines to the user on how the quiz works\

        index = 0
        self.clear()
        self.select_led(index)
        self.voltage_input()
        self.calculate_resistance()
        print(f"\nThe Supply voltage is {self.voltage_supply}V \nThe forward voltage is {self.voltage_forward}V"
              f"\nThe forward current is {self.current}mA")

        self.pause_quick()

        print(
            "These peices of data are used to find the reccommend resistor in a series circuit(ie; for a jackbord)"
            "\nThe formula required for this calculation is Ohm's Law, allowing you to calculate the resistance."
            "\nA quick tip is that current(I) is measured in amps, the data you recieve for forward current"
            "\nis in milliamps. To find the current in amps divide the current given by 1000."
            "\n\nSo the formula requried to find the resistance is""\nResistance = (Vs - Vf) ÷ (If ÷ 1000)"
        )
        self.pause_slow()


        print(f'First of all we should divide the current by 1000 in order to find the current in amps'
              f'\n{self.current} / 1000 = {self.current_amps}A'
              f'\n\nNext wee need to add the supply voltage, forward voltage, and current into our previous equation'
              f'\nResistance = {self.voltage_supply} - {self.voltage_forward} / {self.current_amps}'
              f'\nResitance = {self.resistance_calculate}Ω'
              f'\n\nWe will want the resistance to be rounded to 1 decimal point, if its a whole number'
              f'\nyou do not need a decimal point'
              f'\n\nThus the resistance found is {self.resistance_calculate}Ω')
        self.pause_slow()

        enter = input("Press enter to continue")
        if enter == enter:
            self.clear()
            del self.led_data[index]
            self.loop()

    def help_function(self):

        print(f"Step 1: First of all we need to recognize the variables"
              f"\n\nThe Supply Voltage is: {self.voltage_supply}V"
              f"\nThe Forward Voltage is: {self.voltage_forward}V"
              f"\nThe Forward Current is: {self.current}mA")
        self.pause_medium()

        print(f"\nStep 2: We will need to convert the forward current into standard form(mA to A)"
              f"\nThis is possible by dividing the milliamps value by 1000"
              f"\n\n{self.current} / 1000 = {self.current_amps}A.")
        self.pause_medium()

        print(f"\nStep 3: Now all we got to do is substitue the values into the equation given"
              f"\n\n({self.voltage_supply} - {self.voltage_forward}) / {self.current_amps} = "
              f"{self.resistance_calculate}\nThus the resistance is {self.resistance_calculate}Ω")
        self.pause_medium()
        enter = input("Press enter to continue")
        if enter == enter:
            self.clear()
            return

    def select_led(self, index):
        # This function sets the led
        # random.shuffle(self.led_data)
        led = self.led_data[index]
        self.voltage_forward = led["Vf"]
        self.current = led["If"]


    def voltage_input(self):
        # Gathers the inputs from the user
        print(f'\nThe Forward Voltage is: {self.voltage_forward}V'
              f'\nThe Forward Current is : {self.current}mA\n')
        while True:
            try:
                guess = input("What supply voltage out of 3V or 5V would you like to pick?").strip()

                if guess in self.vs3_list:
                    self.voltage_supply = 3

                    if self.voltage_forward >= self.voltage_supply:
                        print(f"That wouldn't work, as {self.voltage_forward}V is larger than {self.voltage_supply}V ,"
                              f"So you should instead use a supply voltage of {self.vs5_list[1]}: ")
                        continue
                    else:
                        break

                elif guess in self.vs5_list:
                    self.voltage_supply = 5
                    break

                else:
                    print("That is not 3V or 5V, please lock in")

            except ValueError:
                print("Invailid input, please lock in")
                self.pause_quick()



    def resistance(self):
        print(f'\nVoltage Supply: {self.voltage_supply}V'
              f'\nVoltage Forward: {self.voltage_forward}V'
              f'\nForward Current: {self.current}mA\n')
        self.pause_quick()
        while True:  # Keep looping until valid input is given
            try:
                self.resistance_guess = input("What is the resistance? (Make sure you round to 1 d.p.) ")

                # Convert input to float and check if it has at most 1 decimal place
                if "." in self.resistance_guess and len(self.resistance_guess.split(".")[1]) > 1:
                    print("Invalid input. Please round to 1 decimal place.")
                    self.pause_quick()
                    continue  # Ask again

                # Convert to float (or int if no decimal point)
                self.resistance_guess = float(self.resistance_guess)

                break  # Valid input, exit loop
            except ValueError:
                print("Invalid input. Please enter a number, rounded to 1 decimal place.")
                self.pause_quick()

    def calculate_resistance(self):
        # Calculates resistance of the given question
        self.current_amps = self.current / 1000 # Calculates the current in amps, not milliamps
        self.resistance_calculate = round((float(self.voltage_supply) - float(self.voltage_forward))
                                          / self.current_amps, 1)
        # print(self.voltage_supply)
        # print(self.voltage_forward)
        # print(f'Resistance Calculated: {self.resistance_calculate}Ω')

    def output(self):
        # provides the basic outputs
        if self.resistance_guess == self.resistance_calculate:
            self.score += 1
            print(f'You are correct, the resistance for question {self.question} is {self.resistance_calculate}Ω'
                  f'\nYou have got {self.score} questions out of {self.question} correct so far.')

        else:
            print(f'You are incorrect, the resistance for question {self.question} is {self.resistance_calculate}Ω'
                  f'\nYou have got {self.score} questions out of {self.question} correct so far.')
        self.pause_medium()
        self.help = input("Type help for the worked answer: ")
        self.clear()
        if self.help.lower() == "help":
            self.help_function()
        else:
            return



    def start(self):
    # start function
        self.intro()

    def loop(self):
        # loops the function

        for index in range(len(self.led_data)):
            self.select_led(index)
            self.question += 1
            self.voltage_input()
            self.resistance()
            self.calculate_resistance()
            self.output()
        print("Thank you for running my resistor program, I hope you are now skilled enough to ace your test")
        self.pause_medium()

# Load LED Data
led_data = LED("data.txt").led_list

# Start the Quiz
quiz = Quiz(led_data)
quiz.start()