"""Resistor quiz program, using the formula (Vs-Vf)/If, program made for year 10/11 students """

class led_data:
    """Stored data about each single LED"""

    def __init__(self, voltage, current, voltage_supply):
        self.voltage = voltage # Forward voltage
        self.current = current # Forward Current
        self.voltage = voltage_supply # Supply voltage

