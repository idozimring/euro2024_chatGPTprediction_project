import numpy as np
import pandas as pd

# Data load from Excels - forecast
forecast_file = r'C:\Users\Ido Zimring\Desktop\pythonProjects_euro\euro\euro_forecast_chat.xlsx'
df_forecast_group_a = pd.read_excel(forecast_file, sheet_name='Group A')
df_forecast_group_b = pd.read_excel(forecast_file, sheet_name='Group B')
df_forecast_group_c = pd.read_excel(forecast_file, sheet_name='Group C')
df_forecast_group_d = pd.read_excel(forecast_file, sheet_name='Group D')
df_forecast_group_e = pd.read_excel(forecast_file, sheet_name='Group E')
df_forecast_group_f = pd.read_excel(forecast_file, sheet_name='Group F')

# Data load from Excels - real results
actual_file = r'C:\Users\Ido Zimring\Desktop\pythonProjects_euro\euro\euro_real_chat.xlsx'
df_actual_group_a = pd.read_excel(actual_file, sheet_name='Group A')
df_actual_group_b = pd.read_excel(actual_file, sheet_name='Group B')
df_actual_group_c = pd.read_excel(actual_file, sheet_name='Group C')
df_actual_group_d = pd.read_excel(actual_file, sheet_name='Group D')
df_actual_group_e = pd.read_excel(actual_file, sheet_name='Group E')
df_actual_group_f = pd.read_excel(actual_file, sheet_name='Group F')

# Combine data from all groups into unified data frames
df_forecast = pd.concat([df_forecast_group_a, df_forecast_group_b, df_forecast_group_c,
                         df_forecast_group_d, df_forecast_group_e, df_forecast_group_f])

df_actual = pd.concat([df_actual_group_a, df_actual_group_b, df_actual_group_c,
                       df_actual_group_d, df_actual_group_e, df_actual_group_f])

#-------------------------------------------------------------------
# View sample of the  data

print("Forecast DataFrame Head:")
print(df_forecast.head(10))

print("\nActual DataFrame Head:")
print(df_actual.head(10))

#-------------------------------------------------------------------
#EXACT PREDICTION
# Calculate the absolute errors for goals (the diff between the forecast goals to the real ones)
errors = np.abs(df_forecast[['Goals for Team A', 'Goals for Team B']] - df_actual[['Goals for Team A', 'Goals for Team B']])

# Calculate the mean squared error for each game
mse = ((df_forecast[['Goals for Team A', 'Goals for Team B']] - df_actual[['Goals for Team A', 'Goals for Team B']]) ** 2).mean(axis=1)

# Calculate the root mean squared error for each game
rmse = np.sqrt(mse)
#print("Root Mean Squared Error for each game:\n", rmse)

# Calculate the mean standard error
mean_rmse = rmse.mean()
print("Mean Root Mean Squared Error for all the games was:", mean_rmse)

#Calculate Exact Prediction
exact_prediction = (df_forecast == df_actual).all(axis=1).mean() * 100
print("Exact Prediction Accuracy (%):", exact_prediction)

correct_result = (df_forecast['Winning Team'] == df_actual['Winning Team']).mean() * 100
print("Correct Result Accuracy (%):", correct_result)

#-------------------------------------------------------------------
#Calculate precentage of predicting the number of goals for each team in a game
correct_goals_team_a = (df_forecast['Goals for Team A'] == df_actual['Goals for Team A']).mean() * 50
correct_goals_team_b = (df_forecast['Goals for Team B'] == df_actual['Goals for Team B']).mean() * 50
correct_goals = correct_goals_team_a + correct_goals_team_b
print("Correct Goals for a team Accuracy (%):", correct_goals)

#-------------------------------------------------------------------
# checking the goal difference accuracy

forecast_goal_diff = df_forecast['Goals for Team A'] - df_forecast['Goals for Team B']
actual_goal_diff = df_actual['Goals for Team A'] - df_actual['Goals for Team B']
correct_goal_diff = (forecast_goal_diff == actual_goal_diff).mean() * 100
print("Correct Goal Difference Accuracy (%):", correct_goal_diff)

#-------------------------------------------------------------------
#Overall accuracy for each National team
teams = pd.concat([df_forecast['Team A'], df_forecast['Team B']]).unique()
team_accuracy = {}

for team in teams:
    forecast_games = df_forecast[(df_forecast['Team A'] == team) | (df_forecast['Team B'] == team)]
    actual_games = df_actual[(df_actual['Team A'] == team) | (df_actual['Team B'] == team)]
    correct_games = (forecast_games.reset_index(drop=True) == actual_games.reset_index(drop=True)).all(axis=1).mean() * 100
    team_accuracy[team] = correct_games

df_team_accuracy = pd.DataFrame(list(team_accuracy.items()), columns=['Team', 'Accuracy'])

# Sort DataFrame by 'Accuracy' in descending order
df_team_accuracy = df_team_accuracy.sort_values(by='Accuracy', ascending=False).reset_index(drop=True)

# Display the DataFrame
print(df_team_accuracy.head(1))

#-------------------------------------------------------------------
#CHECK THE CLOSEST AND THE FURTHEST FROM PREDICTION

# Calculate the absolute difference for goals
df_forecast['Absolute Error Team A'] = np.abs(df_forecast['Goals for Team A'] - df_actual['Goals for Team A'])
df_forecast['Absolute Error Team B'] = np.abs(df_forecast['Goals for Team B'] - df_actual['Goals for Team B'])

# Combine the forecast and actual DataFrames
df_combined = pd.concat([df_forecast, df_actual[['Goals for Team A', 'Goals for Team B']].rename(columns={'Goals for Team A': 'Actual Goals for Team A', 'Goals for Team B': 'Actual Goals for Team B'})], axis=1)

# Calculate the mean absolute error for each team
teams = pd.concat([df_forecast['Team A'], df_forecast['Team B']]).unique()
team_mae = {}

for team in teams:
    errors_team_a = df_combined[df_combined['Team A'] == team]['Absolute Error Team A'].mean()
    errors_team_b = df_combined[df_combined['Team B'] == team]['Absolute Error Team B'].mean()
    team_mae[team] = np.mean([errors_team_a, errors_team_b])

# Convert to DataFrame
df_team_mae = pd.DataFrame(list(team_mae.items()), columns=['Team', 'Mean Absolute Error'])

# Find the team closest and furthest from their forecast goals
closest_team =  df_team_mae[df_team_mae['Mean Absolute Error'] == 0.00]

furthest_team = df_team_mae.loc[df_team_mae['Mean Absolute Error'].idxmax()]

print("Team closest to their forecast goals:")
print(closest_team)
print("\nTeam furthest from their forecast goals:")
print(furthest_team)

