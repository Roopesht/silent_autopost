# POC

1. We'll have a JSON file with data about goals like date, goal, amount, and risk profile. Also, it'll include general risk profile, current salary, minimum expenditure, current investments, current loans, lump sum investment, monthly investment, inflation rate, and start date.

2. The tool will have market return data for each year for things like gold, mutual funds, stocks, and bonds.

3. We'll use the inflation rate to figure out how much the goals will cost in the future. 

4. Using this info, the tool will guess how investments will perform each year and see if the goals are reached, likewise it'll suggest how to invest to reach the goals.

5. Investment Pattern: How investments are made: The system will invest in different instruments and time frames based on the speculated returns percentage, risk profile, and other factors.

6. If goals aren't met, the tool will tell you how much more money is needed and how to invest to reach the goals.

7. The tool will shuffle the investments based on the market speculation data and time cycles. 

8. What you get: A spreadsheet with multiple sheets. 
The sheet 1 will list the goals along with dates and amount (at the current value) and amount after applying the inflation rate. Below it will list the other parameters such as current salary, minimum expenditure, inflation rate, Lumpsum investment, monthly investment, and start date.
Below that, it will show the current investments, current loans
Sheet 2 will list the year in each row, and columns will show investment types and their value changes. It'll also sum up total investment value and its change each year.


## Glossary
1. *Risk*: How important is the returns for the client. If the client is willing to take more risk that means he is looking for more returns. If the client is not willing to take more risk, that means he is favoring the safety of the returns over the returns.

## Test data for POC
goals.json



json
{
"goals": [
{
"date": "2029-01-01",
"goal": "House",
"amount": 10000000,
"risk_profile": "50"
},
{
"date": "2025-01-01",
"goal": "Car",
"amount": 5000000,
"risk_profile": "50"
}
],
"General_risk_profile": "High",
"current_salary": 200000,
"minimum_expenditure": 100000,
"current_investments": 5000000,
"current_loans": 2000000,
"lumpsum_investment": 1000000,
"monthly_investment": 10000,
"inflation_rate": 7,
"start_date": "2024-06-01"
}


return_speculation.json
json
{
"returns": [
{
"year": 2024,
"gold": 10,
"mutual_funds": 15,
"stocks": 20,
"bonds": 5
},
{
"year": 2025,
"gold": 12,
"mutual_funds": 17,
"stocks": 22,
"bonds": 7
}
]
}


output_investments_by_year.csv
```csv
Year, Investment, Gold, Gold_change, Mutual_funds, Mutual_funds_change, Stocks, Stocks_change, Bonds, Bonds_change, Total_investment
2024, 5000000, 5500000, 500000, 5750000, 750000, 6000000, 1000000, 5250000, 250000, 22500000