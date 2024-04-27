import json
import pandas as pd
import os

def load_data(folder):
    # Load goals data
    with open(os.path.join(folder,  "goals.json"), 'r') as f:
        goals_data = json.load(f)

    # Load return speculation data
    with open(os.path.join(folder,  'return_speculation.json'), 'r') as f:
        return_speculation_data = json.load(f)


    # Load investments data from CSV
    with open(os.path.join(folder,  'return_speculation.json'), 'r') as f:
        investments_data = pd.read_csv(os.path.join(folder,  'output_investments_by_year.csv'))

    with open(os.path.join(folder,  'investment_pattern.json'), 'r') as f:
        investments_pattern = json.load(f)
        
    return goals_data, return_speculation_data, investments_data, investments_pattern

# Other data processing functions...
