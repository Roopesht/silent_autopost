import json
import pandas as pd

def predict_investment_performance(return_speculation_data, investments_data):
    # Load return speculation data
    returns_data = json.loads(return_speculation_data)

    # Process return data and calculate predicted performance
    predicted_performance = {}
    for item in returns_data['returns']:
        year = item['year']
        gold_return = item['gold']
        mutual_funds_return = item['mutual_funds']
        stocks_return = item['stocks']
        bonds_return = item['bonds']

        # Perform prediction based on investment allocation
        # For simplicity, let's assume a basic strategy
        predicted_performance[year] = {
            'Gold': investments_data['Gold'] * (1 + gold_return / 100),
            'Mutual_funds': investments_data['Mutual Funds'] * (1 + mutual_funds_return / 100),
            'Stocks': investments_data['Stocks'] * (1 + stocks_return / 100),
            'Bonds': investments_data['Bonds'] * (1 + bonds_return / 100)
        }

    return predicted_performance

def generate_excel_report(goals_data, return_speculation_data, investments_data, investment_strategy):
    # Convert scalar values to lists if necessary
    if not isinstance(goals_data, list):
        goals_data = [goals_data]
    if not isinstance(investment_strategy, list):
        investment_strategy = [investment_strategy]

    # Perform prediction of investment performance
    predicted_performance = predict_investment_performance(return_speculation_data, investments_data)

    # Create DataFrame for Excel report
    report_data = {
        'Goals': goals_data,
        'Investment Performance': predicted_performance,
        'Investment Strategy': investment_strategy
    }
    report_df = pd.DataFrame(report_data)

    # Generate Excel file
    report_df.to_excel('financial_report.xlsx', index=False)

    # Calculate yearly profit/loss
    yearly_profit_loss = {
        'Year': [2024],
        'Investment': [5000000],
        'Gold': [5500000],
        'Gold_change': [500000],
        'Mutual_funds': [5750000],
        'Mutual_funds_change': [750000],
        'Stocks': [6000000],
        'Stocks_change': [1000000],
        'Bonds': [5250000],
        'Bonds_change': [250000],
        'Total_investment': [22500000]
    }

    # Create DataFrame for yearly profit/loss
    profit_loss_df = pd.DataFrame(yearly_profit_loss)

    # Write DataFrame to Excel file
    profit_loss_df.to_excel('yearly_profit_loss.xlsx', index=False)


