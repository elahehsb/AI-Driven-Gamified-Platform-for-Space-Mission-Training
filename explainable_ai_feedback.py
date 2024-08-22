from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

class ExplainableAIFeedback:
    def train_model(self, decision_logs, outcomes):
        X = [log['time'] for log in decision_logs]
        y = outcomes
        model = DecisionTreeClassifier()
        model.fit(X, y)
        return model

    def generate_explanation(self, model):
        return tree.export_text(model)

if __name__ == "__main__":
    ai_feedback = ExplainableAIFeedback()
    decision_logs = [{"time": 5, "decision": "Attempt suit reboot"}, {"time": 10, "decision": "Initiate emergency return"}]
    outcomes = [1, 0]  # Placeholder outcomes
    model = ai_feedback.train_model(decision_logs, outcomes)
    explanation = ai_feedback.generate_explanation(model)
    print("Decision Tree Explanation:\n", explanation)
