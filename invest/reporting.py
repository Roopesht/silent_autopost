import pandas as pd

def generate_excel_report(goals_data, investment_performance, investment_strategy):
    # Convert scalar values to lists if necessary
    if not isinstance(goals_data, list):
        goals_data = [goals_data]
    if not isinstance(investment_performance, list):
        investment_performance = [investment_performance]
    if not isinstance(investment_strategy, list):
        investment_strategy = [investment_strategy]

    # Create DataFrame for Excel report
    report_data = {
        'Goals': goals_data,
        'Investment Performance': investment_performance,
        'Investment Strategy': investment_strategy
    }
    report_df = pd.DataFrame(report_data)

    # Generate Excel file
    report_df.to_excel('financial_report.xlsx', index=False)

# Define scalar values
goal = 'House'
investment_performance = 15.5
investment_strategy = 'Aggressive'

# Convert scalar values to lists
goal_list = [goal]
investment_performance_list = [investment_performance]
investment_strategy_list = [investment_strategy]

# Call the function with the lists
generate_excel_report(goal_list, investment_performance_list, investment_strategy_list)



