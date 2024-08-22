import random

class SpaceMissionScenarioGenerator:
    def __init__(self):
        self.scenarios = ["Spacewalk Emergency", "Spacecraft Malfunction", "Unexpected Meteor Shower", "Communication Blackout"]

    def generate_scenario(self):
        scenario = random.choice(self.scenarios)
        events = self.generate_events(scenario)
        return {"scenario": scenario, "events": events}

    def generate_events(self, scenario):
        events = []
        if scenario == "Spacewalk Emergency":
            events = [
                {"time": 0, "description": "Astronaut reports suit malfunction during spacewalk."},
                {"time": 5, "description": "Oxygen levels in suit dropping rapidly."},
                {"time": 10, "description": "Astronaut loses communication with spacecraft."}
            ]
        # Add more scenarios here
        return events

if __name__ == "__main__":
    generator = SpaceMissionScenarioGenerator()
    scenario = generator.generate_scenario()
    print("Generated Scenario:", scenario)
