class TemperatureControlUnit:
    def __init__(self):
        self.state = "OFF"
    
    def get_state(self):
        return self.state

    def select_coffee_brewing_option(self):
        if self.state == "OFF":
            self.state = "HEATING"
    
    def start_heating(self):
        if self.state == "HEATING":
            # Simulate the heating process
            # In a real embedded system, this might involve interacting with hardware
            self.state = "HEATING"
    
    def reach_desired_temperature(self):
        if self.state == "HEATING":
            # Simulate reaching the desired temperature
            # In a real embedded system, this might involve temperature sensors
            self.state = "READY"
