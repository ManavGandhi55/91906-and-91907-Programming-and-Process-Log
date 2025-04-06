# Resistor quiz program, using the formula (Vs-Vf)/If, program made for year 10/11 students.  # noqa

# Imports the modules required for functions like os clear, time.delay, and randomization.  # noqa
import os
import time
import random


class LED:
    """LED Class, loads, formats, and shuffles all the LED data."""

    def __init__(self, filename):
        """Initialize the LED object by loading data from a
        file and shuffling the list.
        """
        self.led_list = self.load_led_data(filename)
        random.shuffle(self.led_list)
        # print(f'{self.led_list}')  # Debug: Prints the LED list for testing.

    def load_led_data(self, filename):
        """Load and format all LED data into a list of dictionaries."""
        with open(filename, "r") as file:
            data = file.read().splitlines()
        # Data is grouped in pairs of Vf and If
        return [{"Vf": float(data[i]), "If": int(data[i + 1])}
                for i in range(0, len(data), 2)]


class Quiz:
    """Quiz Class, Bulk of the code that utilizes the LED data."""

    def __init__(self, led_data):
        """Initialize the Quiz data from the LED data."""
        # Electrical circuit properties
        self.voltage_forward = 0  # Forward voltage of the LED (V)
        self.current = 0  # Forward current through the LED (mA)
        self.current_amps = 0  # Forward current in amperes (A)
        self.voltage_supply = 0  # Supply voltage (V)

        # Resistance values
        self.resistance_guess = 0  # Resistance guessed by the user (Ω)
        self.resistance_calculate = 0  # Correct resistance calculated by the program (Ω)  # noqa

        # Quiz tracking
        self.question = 0  # Current question number
        self.score = 0  # User's score
        self.help = 0  # Tracks help requests or hints used
        self.grade = None  # Final grade/result of the quiz

        # LED data
        self.led_data = led_data

        # Accepted string inputs for 3V and 5V supply values (Without V symbol)
        self.vs3_list = ['3', '3.0']  # Accepted inputs for 3V supply
        self.vs5_list = ['5', '5.0']  # Accepted inputs for 5V supply

        # Terminal color codes for colored outputs
        self.green = "\033[32m"
        self.yellow = "\033[33m"
        self.red = "\033[31m"
        self.reset = "\033[0m"

    def clear(self):
        """Function to clear the terminal screen
        (changes depending on the os).
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    # Provides a delay between outputs (quick)
    # def pause_quick(self):
    # time.sleep(2)

    # Provides a delay between outputs (medium)
    # def pause_medium(self):
    # time.sleep(4)

    # Provides a delay between outputs (slow)
    # def pause_slow(self):
    # time.sleep(6)

    def intro(self):
        """Introduction to the program, Welcome message,
        Brief explanation, and an input for guidelines."""
        print("\n" + "=" * 50)
        print("  🔥 Welcome to Manav's Resistor Quiz Program! 🔥")
        print("=" * 50)

        # Purpose of the quiz
        print("\n📢 This program will test your ability to calculate")
        print("the recommended resistor for various LEDs in a series circuit.\n")  # noqa

        # Introduces the equation to the user.
        print("💡 Resistor Formula: R = (V_supply - V_forward) / I_forward")
        print("   - V_supply = Voltage from the power source")
        print("   - V_forward = Voltage drop across the LED")
        print("   - I_forward = Desired current for the LED\n")

        # Ask if the user wants guidelines.
        text = input(
            "📝 Would you like some guidelines before starting? (Yes/No): "
        ).strip().lower()

        # Calls the guidelines function.
        if text == "yes":
            print("\n📖 Great choice! Let's go over the guidelines first...\n")
            self.guidelines()

        # Doesn't call the guidelines function.
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
        """Provide guidelines to the user on how the quiz works."""
        index = 0
        self.clear()
        self.select_led(index)

        # Uses lowest possible supply voltage value.
        self.voltage_supply = 3
        if self.voltage_forward >= self.voltage_supply:
            self.voltage_supply = 5

        # Finds the resistance based of the data.
        self.calculate_resistance()

        # Prints nicely formatted title.
        print("\n" + "=" * 50)
        print(" 📖 GUIDELINES: Understanding the Resistor Quiz ")
        print("=" * 50)

        # Prints the LED data.
        print("\n🔧 The key values for this calculation are:")
        print(f"    ⚡ Supply Voltage: {self.voltage_supply}V")
        print(f"   💡 Forward Voltage: {self.voltage_forward}V")
        print(f"   🔌 Forward Current: {self.current}mA\n")

        # self.pause_medium()
        # Reason for the quiz.
        print(
            "📌 These values are used to find the recommended resistor in a series circuit (e.g., for a JackBord).")  # noqa
        print("💡 The formula required is Ohm’s Law, allowing us to calculate resistance.")  # noqa

        # self.pause_quick()

        # Provides user with a tip on converting amps to milliamps.
        print("\n✨ Quick Tip:")
        print("   🔹 Current (I) is measured in Amps (A), but the data given for forward current is in "  # noqa
              "milliamps (mA).")
        print("   🔹 To convert mA to A, divide by 1000.")

        # self.pause_medium()

        print("\n📐 Formula Required to Find Resistance:")
        print("   Resistance = (Vs - Vf) ÷ (If ÷ 1000)")

        # self.pause_medium()

        # Shows how to calculate the resistance
        print("\n📊 Step-by-Step Calculation:")
        print(f"   1️⃣ Convert current: {self.current}mA ÷ 1000 = {self.current_amps}A")  # noqa
        print("   2️⃣ Substitute values into the formula:")
        print(f"      Resistance = ({self.voltage_supply} - {self.voltage_forward}) ÷ {self.current_amps}")  # noqa
        print(f"      Resistance = {self.resistance_calculate} Ω")

        # self.pause_slow()

        # Final value
        print(f"\n📌 Final Resistance Value: {self.resistance_calculate} Ω")

        # self.pause_slow()

        # Waits for the input then clears the screen and proceeding.
        input("\n🎯 Press Enter to continue...")
        self.clear()

        # Removes the LED that's used in the guidelines
        del self.led_data[index]
        self.loop()

    def help_function(self):
        """Provide the user help for each question."""
        self.clear()

        print("\n" + "=" * 50)
        print(" 🆘 HELP: Step-by-Step Resistance Calculation ")
        print("=" * 50)

        # Identifying the main variables.
        print("\n📌 Step 1: Identify the Key Variables")
        print(f"   Supply Voltage (Vs): {self.voltage_supply}V")
        print(f"   Forward Voltage (Vf): {self.voltage_forward}V")
        print(f"   Forward Current (If): {self.current}mA")

        # self.pause_slow()

        # Shows how to convert from milliamps to amps.
        print("\n📌 Step 2: Convert Forward Current to Amps")
        print("   Since current is given in milliamps, we convert it to amps by dividing by 1000.")  # noqa
        print(f"   {self.current}mA ÷ 1000 = {self.current_amps}A")

        # self.pause_medium()

        # Utilizes the equation for calculating resistance
        print("\n📌 Step 3: Apply the Formula")
        print("   Resistance = (Vs - Vf) ÷ If")
        print(f"   ({self.voltage_supply} - {self.voltage_forward}) ÷ {self.current_amps} = "  # noqa
              f"{self.resistance_calculate} Ω")

        # self.pause_medium()

        # Provides the Final answer.
        print("\n🎯 Final Answer:")
        print(f"   The calculated resistance is {self.resistance_calculate} Ω")

        # self.pause_slow()

        # Waits for the input then clears the screen and proceeding.
        input("\n🔄 Press Enter to continue...")
        self.clear()
        return

    def select_led(self, index):
        """Function sets the LED."""
        # Retrieves the LED data from the list using the index.
        led = self.led_data[index]
        self.voltage_forward = led["Vf"]
        self.current = led["If"]

    def voltage_input(self):
        """Function that gathers Supply voltage."""

        # Displaying the LED specifications.
        print("\n" + "=" * 50)
        print("💡 LED Specifications 💡")
        print("=" * 50)

        print(f"🔋 Forward Voltage: {self.voltage_forward}V"
              f"\n ⚡ Forward Current: {self.current}mA")
        print("=" * 50 + "\n")
        print(f'Resistance Calculated: {self.resistance_calculate} Ω')

        # Loops until a valid Vs is entered.
        while True:
            try:
                guess = input(
                    f"🔌 Select a supply voltage for question {self.question} (3V or 5V): "  # noqa
                ).strip()

                # Allow different valid inputs ("3", "3.0", "3V", "3.0V")
                valid_3 = self.vs3_list + [x + 'V' for x in self.vs3_list]
                valid_5 = self.vs5_list + [x + 'V' for x in self.vs5_list]

                if guess in valid_3:
                    self.voltage_supply = 3
                    # Check if the LED's forward voltage is too high for 3V.
                    if self.voltage_forward > self.voltage_supply:
                        print(
                            f"\n❌{self.yellow}  Oops! {self.voltage_forward}V is greater than {self.voltage_supply}V."  # noqa
                            f"\n🔄 Try again with a 5V supply instead.{self.reset}\n"
                        )

                    elif self.voltage_forward == self.voltage_supply:
                        print(
                            f"\n❌ {self.yellow} Oops! {self.voltage_forward}V is equal to {self.voltage_supply}V."  # noqa
                            f"\n🔄 Try again with a 5V supply instead.{self.reset}\n"
                        )
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
                    print(
                        f"\n⚠️ {self.yellow}Invalid choice! Please enter either 3V or 5V.{self.reset}\n"  # noqa
                    )
                    # self.pause_quick()

            except ValueError:
                print(
                    f"\n⚠️{self.yellow} Invalid input. Please enter a valid number (3 or 5).{self.reset}\n"  # noqa
                )
                # self.pause_quick()
        self.clear()

    def resistance(self):
        """Asks for resistance input, and checks it."""

        # Outputs core information.
        print("\n" + "=" * 50)
        print("📏 Resistance Calculation 📏")
        print("=" * 50)
        print(f"🔋 Supply Voltage: {self.voltage_supply}V"
              f"\n ⚡ Forward Voltage: {self.voltage_forward}V"
              f"\n🔌 Forward Current: {self.current}mA")
        print("=" * 50 + "\n")
        # self.pause_quick()

        # Loops until a valid resistance guess is entered.
        while True:
            try:
                # Asking user for their resistance guess
                self.resistance_guess = int(input("📝 Enter the resistance: "))
                # Ensuring the number is rounded correctly
                if self.resistance_guess > 0:
                    break

                else:
                    print(
                        f"⚠️ {self.yellow}Invalid input. Please enter a valid number for a resistor.{self.reset}"
                        # noqa
                    )

            except ValueError:
                print(
                    f"\n⚠️{self.yellow} That doesn't seem like a valid number!{self.reset}\n"  # noqa
                )
                # self.pause_quick()

    def calculate_resistance(self):
        """Calculates the resistance of the given question."""

        self.current_amps = self.current / 1000  # Current in amps
        # rounds resistance to 0 decimal places
        self.resistance_calculate = round(
            (self.voltage_supply - self.voltage_forward) / self.current_amps
        )
        print(f'Resistance Calculated: {self.resistance_calculate} Ω')

    def output(self):
        """Provides feedback based on the user's answer."""

        # Title with formatting
        print("\n" + "=" * 50)
        print("📊 QUIZ PROGRESS 📊")
        print("=" * 50)

        # Output if guess is correct.
        if self.resistance_guess == self.resistance_calculate:
            self.score += 1
            print(
                f"✅ {self.green}Correct! The resistance for question {self.question} is {self.resistance_calculate}"  # noqa
                f" Ω.{self.reset}"
            )
        # Output if guess is incorrect.
        else:
            print(
                f"❌ {self.red}Incorrect! The correct resistance for question {self.question} is "  # noqa
                f"{self.resistance_calculate} Ω.{self.reset}"
            )

        # Displays the number of correct answers out of the total questions.
        print(f"\n📈 You have answered {self.score} out of {self.question} questions correctly so far.")  # noqa
        print("=" * 50 + "\n")

        # self.pause_medium()

        # Prompts the user for help, regardless of their answer.
        self.help = input(
            "💡 Need a worked answer? Type 'help' or press Enter to continue: "
        ).strip().lower()
        self.clear()

        if self.help == "help":
            self.help_function()

    def grade_boundaries(self):
        """Function determines the final grade based on the users score."""

        if self.score < (self.question / 2):
            self.grade = f"{self.red} Not Achieved {self.reset}"
        else:
            if (self.question / 2) <= self.score < (self.question / 1.5):
                self.grade = f"{self.yellow} Achieved {self.reset}"

            else:
                if (self.question / 1.5) <= self.score < (self.question / 1.1):
                    self.grade = f"{self.green} Merit {self.reset}"

                else:
                    if (self.question / 1.1) <= self.score == self.question:
                        self.grade = f"{self.green} Excellence {self.reset}"

    def end(self):
        """Provides the final output."""
        print("\n" + "=" * 50)
        print(f"🏆 QUIZ COMPLETE! 🏆")
        print("=" * 50)
        print(f"📊 You answered {self.score} out of {self.question} correctly.")
        print(f"🎓 Your final grade: {self.grade}")
        print("\nThank you for using the Resistor Quiz Program! 🎉")
        print("🚀 Hopefully, you now have the skills to ace your test! 🏆")

    def start(self):
        """Start function."""

        # Initiates the intro function.
        self.intro()

    def loop(self):
        """Function for looping program."""

        # Iterates through each LED quiz process.
        for index in range(len(self.led_data)):
            self.select_led(index)  # Sets the current LED parameters.
            self.question += 1  # Increments the question count.
            self.voltage_input()  # Displays LED specs and request supply voltage.
            self.calculate_resistance()  # Calculates the correct resistance.
            self.resistance()  # Gathers user resistance input.
            self.output()  # Provides feedback to user, updates score.
        self.grade_boundaries()  # Outputs the final grade.
        self.end()  # Displays the final results/outputs.


# Main program

# Loads LED Data, from the "data.txt" file, via LED class
led_data = LED("data.txt").led_list

# Creates the Quiz object, via the LED data and starts the quiz
quiz = Quiz(led_data)
quiz.start()
