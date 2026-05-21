class SmartDevice:
    def __init__(self, name, device_type):
        """Initializes the device with a name and type."""
        self.name = name
        self.device_type = device_type
        self.is_on = False
        print(f"Device '{self.name}' ({self.device_type}) is ready.")

    def toggle_power(self):
        """Switches the device on or off."""
        self.is_on = not self.is_on
        status = "ON" if self.is_on else "OFF"
        print(f"{self.name} is now {status}.")

    def get_status(self):
        """Returns a string describing the current state."""
        status = "running" if self.is_on else "idle"
        return f"Status: {self.name} is currently {status}."

    def reset(self):
        """Resets the device to its default state."""
        self.is_on = False
        print(f"{self.name} has been reset.")

# --- Using the class ---
if __name__ == "__main__":
    # Create an instance
    my_light = SmartDevice("Living Room Light", "Bulb")

    # Call different methods
    my_light.toggle_power()  # Turn it on
    print(my_light.get_status())
    my_light.reset()         # Turn it off via reset
