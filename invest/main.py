import data_processing
import investment_analysis
import investment_strategy
import reporting
import os
import pandas as pd
import json
from investment_analysis import predict_investment_performance

def write_to_excel(investment_performance, goals_data, filename):
    # Extract column names from the first row of data
    columns = investment_performance[0]

    # Create a DataFrame from the remaining investment performance data
    investment_df = pd.DataFrame(investment_performance[1:], columns=columns)

    # Write investment performance DataFrame to "Investment Performance" sheet
    with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
        investment_df.to_excel(writer, sheet_name='Investment Performance', index=False)

        # Select only the "Goals" column from goals_data
        goals_df = pd.DataFrame(goals_data["goals"], columns=["Goals"])
        goals_df.to_excel(writer, sheet_name='Main', index=False)


def main():
    # Get the directory of the current script
    current_dir = os.path.dirname(__file__)

    # Load and process data
    goals_data, return_speculation_data, investments_data, investment_pattern = data_processing.load_data(current_dir)
    inflation_rate = 8

    # Perform financial analysis
    adjusted_goals = investment_analysis.adjust_goals_for_inflation(goals_data, inflation_rate)
    investment_performance = predict_investment_performance(return_speculation_data, investment_pattern)
    #goal_achievement = investment_analysis.assess_goal_achievement(adjusted_goals, investment_performance)
    write_to_excel(investment_performance, goals_data, "investment_performance.xlsx")



    # Generate investment strategy
    strategy=investment_strategy.generate_strategy(goal_achievement)

    # Generate Excel report
    reporting.generate_excel_report(adjusted_goals, investment_performance, strategy, return_speculation_data)

    return goals_data, return_speculation_data, investments_data




if __name__ == "__main__":
    main()
