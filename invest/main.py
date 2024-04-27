import data_processing
import investment_analysis
import investment_strategy
import reporting
import os
import pandas as pd
import json

def main():
    # Get the directory of the current script
    current_dir = os.path.dirname(__file__)

    # Load and process data
    goals_data, return_speculation_data, investments_data = data_processing.load_data(current_dir)
    inflation_rate = 8

    # Perform financial analysis
    adjusted_goals = investment_analysis.adjust_goals_for_inflation(goals_data, inflation_rate)
    investment_performance = investment_analysis.predict_investment_performance(return_speculation_data, investments_data)
    goal_achievement = investment_analysis.assess_goal_achievement(adjusted_goals, investment_performance)

    # Generate investment strategy
    strategy=investment_strategy.generate_strategy(goal_achievement)

    # Generate Excel report
    reporting.generate_excel_report(adjusted_goals, investment_performance, strategy, return_speculation_data)

    return goals_data, return_speculation_data, investments_data




if __name__ == "__main__":
    main()
