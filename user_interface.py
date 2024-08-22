import streamlit as st
from space_mission_scenario_generator import SpaceMissionScenarioGenerator
from multimodal_data_collection import MultimodalDataCollection
from temporal_learning_analysis import TemporalLearningAnalysis
from explainable_ai_feedback import ExplainableAIFeedback

st.title("AI-Driven Space Mission Training Platform")

generator = SpaceMissionScenarioGenerator()
data_collection = MultimodalDataCollection()
analyzer = TemporalLearningAnalysis()
ai_feedback = ExplainableAIFeedback()

if st.button("Generate Mission Scenario"):
    scenario = generator.generate_scenario()
    st.write("Scenario:", scenario)

    # Placeholder for user interaction and data collection
    data_collection.log_decision(5, "Attempt suit reboot")
    data_collection.log_communication(6, "Astronaut to Mission Control: Losing oxygen")

    st.write("Data Collected")

if st.button("Analyze Decisions"):
    decision_timeline = analyzer.analyze_decisions_over_time(data_collection.decision_logs)
    st.write("Decision Timeline:", decision_timeline)

if st.button("Generate AI Explanation"):
    outcomes = [1, 0]  # Placeholder outcomes
    model = ai_feedback.train_model(data_collection.decision_logs, outcomes)
    explanation = ai_feedback.generate_explanation(model)
    st.write("AI Explanation:", explanation)
