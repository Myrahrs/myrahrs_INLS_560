import time
import random  # Used to simulate race times randomly

class Bike:
    """
    Represents a general bike without an engine (e.g., pedal bike).

    Attributes:
        brand (str): Brand name of the bike.
        model (str): Model name of the bike.
    """
    def __init__(self, brand, model):
        """
        Initialize a Bike object.

        Args:
            brand (str): The brand of the bike.
            model (str): The model of the bike.
        """
        self.brand = brand
        self.model = model

    def __str__(self):
        """Return string representation of the bike."""
        return f"{self.brand} {self.model}"

class MotorBike(Bike):
    """
    Represents a motorbike, inheriting from Bike, with engine size.

    Attributes:
        engine_cc (int): Engine size in cubic centimeters.
    """
    def __init__(self, brand, model, engine_cc):
        """
        Initialize a MotorBike object.

        Args:
            brand (str): The brand of the motorbike.
            model (str): The model of the motorbike.
            engine_cc (int): The engine size in cc.
        """
        super().__init__(brand, model)
        self.engine_cc = engine_cc

    def __str__(self):
        """Return string including engine size."""
        return f"{self.brand} {self.model} ({self.engine_cc}cc engine)"

class Participant:
    """
    Base class for race participants.

    Attributes:
        name (str): Participant's name.
        age (int): Participant's age.
        bike (Bike or MotorBike): The bike assigned to the participant.
        race_time (float): Simulated time to finish the race in seconds.
    """
    def __init__(self, name, age, bike):
        """
        Initialize a Participant object.

        Args:
            name (str): Participant's name.
            age (int): Participant's age.
            bike (Bike or MotorBike): Participant's bike.
        """
        self.name = name
        self.age = age
        self.bike = bike
        self.race_time = None  # Will hold race completion time

    def start_race(self):
        """
        Simulate race start with countdown and assign a race time.
        """
        print(f"{self.name} on {self.bike} is ready to race!")
        for i in range(3, 0, -1):
            print(f"{i}...")
            time.sleep(1)  # Countdown delay for realism
        print("Go!\n")
        
        # Generate race time and store it
        self.race_time = self.simulate_race_time()
        print(f"{self.name} finished the race in {self.race_time:.2f} seconds.\n")

    def simulate_race_time(self):
        """
        Generate a random race time.
        Base method returns None; subclasses should override.
        """
        return None

    def __str__(self):
        """Return string with participant details."""
        return f"{self.name}, Age: {self.age}, Riding: {self.bike}"

class PedalBikeParticipant(Participant):
    """
    Participant riding a pedal bike (usually kids).
    Race times between 20 and 60 seconds.
    """
    def simulate_race_time(self):
        return random.uniform(20, 60)

class MotorBikeParticipant(Participant):
    """
    Participant riding a motorbike (usually adults).
    Race times between 15 and 45 seconds.
    """
    def simulate_race_time(self):
        return random.uniform(15, 45)

# ---------- Helper Functions for Input Validation ----------

def input_positive_int(prompt):
    """
    Prompt the user to enter a positive integer.
    Repeat until valid input is given.

    Args:
        prompt (str): The message shown to the user.

    Returns:
        int: A positive integer entered by the user.
    """
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def input_non_empty_string(prompt):
    """
    Prompt the user to enter a non-empty string.

    Args:
        prompt (str): The message shown to the user.

    Returns:
        str: A non-empty string entered by the user.
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("Input cannot be empty.")

def create_pedal_bike_participant():
    """
    Prompt for pedal bike participant data, validate, and return object.

    Returns:
        PedalBikeParticipant: The created participant object.
    """
    print("\n-- Enter Pedal Bike Participant Details --")
    name = input_non_empty_string("Participant's name: ")
    age = input_positive_int("Participant's age: ")
    brand = input_non_empty_string("Pedal bike brand: ")
    model = input_non_empty_string("Pedal bike model: ")
    bike = Bike(brand, model)
    return PedalBikeParticipant(name, age, bike)

def create_motorbike_participant():
    """
    Prompt for motorbike participant data, validate, and return object.

    Returns:
        MotorBikeParticipant: The created participant object.
    """
    print("\n-- Enter Motorbike Participant Details --")
    name = input_non_empty_string("Participant's name: ")
    age = input_positive_int("Participant's age: ")
    brand = input_non_empty_string("Motorbike brand: ")
    model = input_non_empty_string("Motorbike model: ")
    engine_cc = input_positive_int("Engine size (cc): ")
    bike = MotorBike(brand, model, engine_cc)
    return MotorBikeParticipant(name, age, bike)

def main():
    """
    Main program loop: collect participants, simulate races,
    and determine winners by fastest race time.
    """
    print("Welcome to the Motor-Cross Rally Participant Entry System")
    participants = []

    while True:
        # Ask user for race type or quit
        race_type = input("\nEnter race type ('pedal', 'motor') or 'q' to quit: ").strip().lower()

        if race_type == 'q':
            break
        elif race_type == 'pedal':
            participant = create_pedal_bike_participant()
            participants.append(participant)
            print(f"Added pedal bike participant: {participant.name}")
        elif race_type == 'motor':
            participant = create_motorbike_participant()
            participants.append(participant)
            print(f"Added motorbike participant: {participant.name}")
        else:
            print("Invalid input. Please enter 'pedal', 'motor', or 'q'.")

    # After all participants entered, print all and simulate races
    print("\n--- All Participants and Race Simulation ---")
    for participant in participants:
        print(participant)
        participant.start_race()

    # Determine winners per race type
    pedal_racers = [p for p in participants if isinstance(p, PedalBikeParticipant)]
    motor_racers = [p for p in participants if isinstance(p, MotorBikeParticipant)]

    if pedal_racers:
        winner = min(pedal_racers, key=lambda p: p.race_time)
        print(f"Pedal Bike Race Winner: {winner.name} with time {winner.race_time:.2f} seconds!")
    else:
        print("No pedal bike participants to determine a winner.")

    if motor_racers:
        winner = min(motor_racers, key=lambda p: p.race_time)
        print(f"Motorbike Race Winner: {winner.name} with time {winner.race_time:.2f} seconds!")
    else:
        print("No motorbike participants to determine a winner.")

if __name__ == "__main__":
    main()