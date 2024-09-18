import pandas as pd
import random
from collections import defaultdict

# Load the CSV file (replace 'file_name.csv' with your file's path)
file_path = '/champions-league-2024-UTC.csv'

df = pd.read_csv(file_path)

# Extract the matches
matches = df[['Home Team', 'Away Team', 'Result']]

# Filter the matches to simulate (those without results)
matches_to_simulate = matches[matches['Result'].isnull()]
points_for_entering_top8_avg = 0

for i in range(100):
    def simulate_result():
        home_goals = random.randint(0, 4)  # Home team goals (between 0 and 4)
        away_goals = random.randint(0, 4)  # Away team goals (between 0 and 4)
        return f"{home_goals} - {away_goals}"

    # Apply the function to generate random results and combine
    matches_to_simulate['Result'] = matches_to_simulate.apply(lambda row: simulate_result(), axis=1)
    complete_matches = pd.concat([matches[matches['Result'].notnull()], matches_to_simulate])

    # Empty standings for each team
    standings = defaultdict(lambda: {'Points': 0, 'Played': 0, 'Won': 0, 'Drawn': 0, 'Lost': 0, 'Goals Scored': 0, 'Goals Conceded': 0, 'Goal Difference': 0})

    # Function to update the standings based on match result
    def update_standings(home_team, away_team, result):
        home_goals, away_goals = map(int, result.split(' - '))
        
        # Update stats for home team
        standings[home_team]['Played'] += 1
        standings[home_team]['Goals Scored'] += home_goals
        standings[home_team]['Goals Conceded'] += away_goals
        standings[home_team]['Goal Difference'] = standings[home_team]['Goals Scored'] - standings[home_team]['Goals Conceded']
        
        # Update stats for away team
        standings[away_team]['Played'] += 1
        standings[away_team]['Goals Scored'] += away_goals
        standings[away_team]['Goals Conceded'] += home_goals
        standings[away_team]['Goal Difference'] = standings[away_team]['Goals Scored'] - standings[away_team]['Goals Conceded']
        
        # Assign points
        if home_goals > away_goals:
            standings[home_team]['Points'] += 3
            standings[home_team]['Won'] += 1
            standings[away_team]['Lost'] += 1
        elif home_goals < away_goals:
            standings[away_team]['Points'] += 3
            standings[away_team]['Won'] += 1
            standings[home_team]['Lost'] += 1
        else:
            standings[home_team]['Points'] += 1
            standings[away_team]['Points'] += 1
            standings[home_team]['Drawn'] += 1
            standings[away_team]['Drawn'] += 1

    # Apply the function to update standings for all matches
    for index, row in complete_matches.iterrows():
        update_standings(row['Home Team'], row['Away Team'], row['Result'])

    # Sort the standings by Points, Goal Difference, and Goals Scored
    sorted_standings = sorted(standings.items(), key=lambda x: (x[1]['Points'], x[1]['Goal Difference'], x[1]['Goals Scored']), reverse=True)

    print("Final Standings:")
    for position, (team, stats) in enumerate(sorted_standings, 1):
        print(f"{position}. {team}: {stats['Points']} points, {stats['Played']} played, {stats['Won']} won, {stats['Drawn']} drawn, {stats['Lost']} lost, {stats['Goals Scored']} GS, {stats['Goals Conceded']} GC, {stats['Goal Difference']} GD")
        if position == 8:
            points_for_entering_top8_avg += stats['Points']

# Calculate the average points to be in top8
print(points_for_entering_top8_avg / 100)
