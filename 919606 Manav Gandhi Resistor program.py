"""Resistor quiz program, using the formula (Vs-Vf)/If, program made for year 10/11 students """
import os # imports the os module for Python
import time # imports the time module for Python
import random # imports random module for Pythonn
from termcolor import colored # imports colored module for python


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
        self.resistance_guess = 0  # the R value they guess
        self.resistance_calculate = 0 # the R value the code guesses
        self.question = 0
        self.score = 0
        self.help = 0
        self.grade = None
        self.led_data = led_data # data
        self.vs3_list = ['3','3.0']
        self.vs5_list = ['5','5.0']
        self.green = "green"
        self.yellow = "yellow"
        self.red = "red"



    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # def pause_quick(self):
        # time.sleep(2)

    # def pause_medium(self):
        # time.sleep(4)

    # def pause_slow(self):
        # time.sleep(6)


    def intro(self):
        # Introduction displayed to the user
        print("\n" + "=" * 50)
        print("  🔥 Welcome to Manav's Resistor Quiz Program! 🔥")
        print("=" * 50)

        print("\n📢 This program will test your ability to calculate")
        print("the recommended resistor for various LEDs in a series circuit.\n")

        # Briefly show the equation
        print("💡 Resistor Formula: R = (V_supply - V_forward) / I_forward")
        print("   - V_supply = Voltage from the power source")
        print("   - V_forwardD = Voltage drop across the LED")
        print("   - I_forward = Desired current for the LED\n")

        # Ask if the user wants guidelines
        text = input("📝 Would you like some guidelines before starting? (Yes/No): ").strip().lower()

        if text == "yes":
            print("\n📖 Great choice! Let's go over the guidelines first...\n")
            self.guidelines()
        elif text == "no":
            print("\n🎯 Alright! Let's jump straight into the quiz!\n")
            self.clear()
            self.loop()
        else:
            print("\n🤔 It seems like you're unsure... No worries!")
            print("We'll go ahead and start the quiz anyway. 🚀\n")
            self.clear()
            self.loop()

    def guidelines(self):
        # Provides guidelines to the user on how the quiz works
        index = 0
        self.clear()
        self.select_led(index)

        self.voltage_supply = 3
        if self.voltage_forward >= self.voltage_supply:
            self.voltage_supply = 5
        else:
            pass

        self.calculate_resistance()

        print("\n" + "=" * 50)
        print(" 📖 GUIDELINES: Understanding the Resistor Quiz ")
        print("=" * 50)

        print(f"\n🔧 The key values for this calculation are:")
        print(f"    ⚡ Supply Voltage: {self.voltage_supply}V")
        print(f"   💡 Forward Voltage: {self.voltage_forward}V")
        print(f"   🔌 Forward Current: {self.current}mA\n")

        # self.pause_medium()

        print("📌 These values are used to find the recommended resistor in a series circuit (e.g., for a JackBord).")
        print("💡 The formula required is Ohm’s Law, allowing us to calculate resistance.")

        # self.pause_quick()

        print("\n✨ Quick Tip:")
        print("   🔹 Current (I) is measured in Amps (A), but the data given for forward current is in "
              "milliamps (mA).")
        print("   🔹 To convert mA to A, divide by 1000.")

        # self.pause_medium()

        print("\n📐 Formula Required to Find Resistance:")
        print("   Resistance = (Vs - Vf) ÷ (If ÷ 1000)")

        # self.pause_medium()

        print("\n📊 Step-by-Step Calculation:")
        print(f"   1️⃣ Convert current: {self.current}mA ÷ 1000 = {self.current_amps}A")
        print(f"   2️⃣ Substitute values into the formula:")
        print(f"      Resistance = ({self.voltage_supply} - {self.voltage_forward}) ÷ {self.current_amps}")
        print(f"      Resistance = {self.resistance_calculate} Ω")

        # self.pause_slow()

        print(f"\n📌 Final Resistance Value: {self.resistance_calculate} Ω")


        # self.pause_slow()

        input("\n🎯 Press Enter to continue...")
        self.clear()
        del self.led_data[index]
        self.loop()


    def help_function(self):
        self.clear()

        print("\n" + "=" * 50)
        print(" 🆘 HELP: Step-by-Step Resistance Calculation ")
        print("=" * 50)

        print("\n📌 Step 1: Identify the Key Variables")
        print(f"    ⚡ Supply Voltage (Vs): {self.voltage_supply}V")
        print(f"   💡 Forward Voltage (Vf): {self.voltage_forward}V")
        print(f"   🔌 Forward Current (If): {self.current}mA")

        # self.pause_slow()

        print("\n📌 Step 2: Convert Forward Current to Amps")
        print("   🔹 Since current is given in milliamps, we convert it to amps by dividing by 1000.")
        print(f"   🔢 {self.current}mA ÷ 1000 = {self.current_amps}A")

        # self.pause_medium()

        print("\n📌 Step 3: Apply the Formula")
        print("   Resistance = (Vs - Vf) ÷ If")
        print(f"   ({self.voltage_supply} - {self.voltage_forward}) ÷ {self.current_amps} = "
              f"{self.resistance_calculate} Ω")

        # self.pause_medium()

        print("\n🎯 Final Answer:")
        print(f"   ✅ The calculated resistance is {self.resistance_calculate} Ω")

        # self.pause_slow()

        input("\n🔄 Press Enter to continue...")
        self.clear()
        return


    def select_led(self, index):
        # This function sets the led
        # random.shuffle(self.led_data)
        led = self.led_data[index]
        self.voltage_forward = led["Vf"]
        self.current = led["If"]


    def voltage_input(self):
        # Displaying the LED specifications
        print("\n" + "=" * 50)
        print("💡 LED Specifications 💡")
        print("=" * 50)


        print(f"🔋 Forward Voltage: {self.voltage_forward}V"
              f"\n ⚡ Forward Current: {self.current}mA")
        print("=" * 50 + "\n")
        print(f'Resistance Calculated: {self.resistance_calculate} Ω')


        while True:
            try:
                guess = input(f"🔌 Select a supply voltage for question {self.question} (3V or 5V): ").strip()

                # Allow different valid inputs (e.g., "3", "3.0", "3V", "3.0V")
                valid_3 = self.vs3_list + [x + 'V' for x in self.vs3_list]
                valid_5 = self.vs5_list + [x + 'V' for x in self.vs5_list]

                if guess in valid_3:
                    self.voltage_supply = 3
                    if self.voltage_forward > self.voltage_supply:
                        print(colored(f"\n❌  Oops! {self.voltage_forward}V is greater than {self.voltage_supply}V."
                              f"\n🔄 Try again with a 5V supply instead.\n", self.yellow))

                    elif self.voltage_forward == self.voltage_supply:
                        print(colored(f"\n❌  Oops! {self.voltage_forward}V is equal to {self.voltage_supply}V."
                              f"\n🔄 Try again with a 5V supply instead.\n", self.yellow))
                        continue  # Ask for input again

                    else:

                        print("\n✅ 3V selected. Let's continue.\n")
                        # self.pause_quick()
                        break

                elif guess in valid_5:
                    self.voltage_supply = 5
                    print("\n✅ 5V selected. Let's continue.\n")
                    # self.pause_quick()
                    break

                else:
                    print(colored("\n⚠️ Invalid choice! Please enter either 3V or 5V.\n", self.yellow))
                    # self.pause_quick()

            except ValueError:
                print(colored("\n⚠️ Invalid input. Please enter a valid number (3 or 5).\n", self.yellow))
                # self.pause_quick()
        self.clear()

    def resistance(self):
        # Displaying the calculated values
        print("\n" + "=" * 50)
        print("📏 Resistance Calculation 📏")
        print("=" * 50)
        print(f"🔋 Supply Voltage: {self.voltage_supply}V"
              f"\n ⚡ Forward Voltage: {self.voltage_forward}V"
              f"\n🔌 Forward Current: {self.current}mA")
        print("=" * 50 + "\n")
        # self.pause_quick()


        while True:
            try:
                # Asking user for their resistance guess
                self.resistance_guess = int(input("📝 Enter the resistance: "))
                # Ensuring the number is rounded correctly
                if self.resistance_guess > 0:
                    break

                else:
                    print(colored("⚠️ Invalid input. Please enter a valid number for a resistor.", self.yellow))
                # Valid input, exit loop

            except ValueError:
                print(colored("\n⚠️ That doesn't seem like a valid number!\n", self.yellow))
                # self.pause_quick()


    def calculate_resistance(self):
        # Calculates resistance of the given question
        self.current_amps = self.current / 1000 # Calculates the current in amps, not milliamps
        self.resistance_calculate = round((self.voltage_supply - self.voltage_forward) / self.current_amps)
        print(f'Resistance Calculated: {self.resistance_calculate} Ω')


    def output(self):
        # Provides feedback based on the user's answer
        print("\n" + "=" * 50)
        print("📊 QUIZ PROGRESS 📊")
        print("=" * 50)

        if self.resistance_guess == self.resistance_calculate:
            self.score += 1
            print(colored(
                  f"✅ Correct! The resistance for question {self.question} is {self.resistance_calculate} Ω.",
                  f"{self.green}"))
        else:
            print(colored(
                f"❌ Incorrect! The correct resistance for question {self.question} is {self.resistance_calculate} Ω.",
                f"{self.red}"))

        print(f"\n📈 You have answered {self.score} out of {self.question} questions correctly so far.")
        print("=" * 50 + "\n")

        # self.pause_medium()

        self.help = input("💡 Need a worked answer? Type 'help' or press Enter to continue: ").strip().lower()
        self.clear()

        if self.help == "help":
            self.help_function()
        else:
            return


    def grade_boundaries(self):
        if self.score < (self.question / 2):
            self.grade = colored("Not Achieved", self.red)
        else:
            if (self.question / 2) <= self.score < (self.question / 1.5):
                self.grade = colored("Achieved", self.yellow)

            else:
                if (self.question / 1.5) <= self.score < (self.question / 1.1):
                    self.grade = colored("Merit", self.green)

                else:
                    if (self.question / 1.1) <= self.score == self.question :
                        self.grade = colored("Excellence", self.green)

                    else:
                        pass



    def end(self):
        print("\n" + "=" * 50)
        print(f"🏆 QUIZ COMPLETE! 🏆")
        print("=" * 50)
        print(f"📊 You answered {self.score} out of {self.question} correctly.")
        print(f"🎓 Your final grade: {self.grade}")
        print("\nThank you for using the Resistor Quiz Program! 🎉")
        print("🚀 Hopefully, you now have the skills to ace your test! 🏆")

    def start(self):
    # start function
        self.intro()

    def loop(self):
        # loops the function
        for index in range(len(self.led_data)):
            self.select_led(index)
            self.question += 1
            self.voltage_input()
            self.calculate_resistance()
            self.resistance()
            self.output()
        self.grade_boundaries()
        self.end()




        # self.pause_medium()

# Load LED Data
led_data = LED("data.txt").led_list

# Start the Quiz
quiz = Quiz(led_data)
quiz.start()