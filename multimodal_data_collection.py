import pandas as pd

class MultimodalDataCollection:
    def __init__(self):
        self.physiological_data = []
        self.decision_logs = []
        self.communication_logs = []

    def collect_physiological_data(self, data):
        self.physiological_data.append(data)

    def log_decision(self, time, decision):
        self.decision_logs.append({"time": time, "decision": decision})

    def log_communication(self, time, message):
        self.communication_logs.append({"time": time, "message": message})

    def save_data(self, filename="mission_data.csv"):
        df = pd.DataFrame({
            "Physiological Data": self.physiological_data,
            "Decision Logs": self.decision_logs,
            "Communication Logs": self.communication_logs
        })
        df.to_csv(filename, index=False)

if __name__ == "__main__":
    data_collection = MultimodalDataCollection()
    data_collection.collect_physiological_data({"heart_rate": 90, "stress_level": 0.5})
    data_collection.log_decision(5, "Attempt suit reboot")
    data_collection.log_communication(6, "Astronaut to Mission Control: Losing oxygen")
    data_collection.save_data()
    print("Data Collected and Saved.")
