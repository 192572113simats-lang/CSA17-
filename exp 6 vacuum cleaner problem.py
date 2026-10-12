import random

class VacuumCleanerEnvironment:
    def __init__(self):
        # Randomly set the status of rooms: 'Dirty' or 'Clean'
        self.rooms = {
            'A': random.choice(['Dirty', 'Clean']),
            'B': random.choice(['Dirty', 'Clean'])
        }
        # Vacuum starts at a random location
        self.location = random.choice(['A', 'B'])

    def display_state(self, step):
        print(f"\nStep {step}:")
        print(f"Vacuum is at Room {self.location}")
        print(f"Room A is {self.rooms['A']}")
        print(f"Room B is {self.rooms['B']}")


class VacuumCleanerAgent:
    def __init__(self, environment):
        self.env = environment
        self.performance_score = 0

    def clean(self):
        current_location = self.env.location

        if self.env.rooms[current_location] == 'Dirty':
            print(f"Room {current_location} is Dirty. Cleaning now...")
            self.env.rooms[current_location] = 'Clean'
            self.performance_score += 10
        else:
            print(f"Room {current_location} is already Clean.")

    def move(self):
        if self.env.location == 'A':
            self.env.location = 'B'
        else:
            self.env.location = 'A'
        self.performance_score -= 1  # Cost for movement
        print(f"Moving to Room {self.env.location}")

    def run(self, steps=4):
        for step in range(1, steps + 1):
            self.env.display_state(step)
            self.clean()
            if self.env.rooms['A'] == 'Clean' and self.env.rooms['B'] == 'Clean':
                print("\nBoth rooms are clean. Task Completed!")
                break
            self.move()

        print(f"\nFinal Performance Score: {self.performance_score}")


# Main Program
if __name__ == "__main__":
    env = VacuumCleanerEnvironment()
    agent = VacuumCleanerAgent(env)
    agent.run()
