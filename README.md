# Champions League 2024 Group Stage Simulation

This repository contains a Python script that simulates the group stage of the 2024 Champions League. The competition format involves 36 teams, each playing 8 matches against different opponents.

### Key Features:
- Each team is assigned a strength coefficient based on their real-world performance, which influences the outcome of simulated matches.
- The simulation generates random results for each match, taking into account the relative strength of the teams.
- The final standings are calculated based on points, goal difference, and other statistics, just like in the real Champions League.
- After 10,000 simulations, the average number of points required to finish in the top 8 is 17 points.

Feel free to modify the code to extract additional insights or explore different scenarios. This project offers a fun way to simulate the tournament and analyze potential outcomes!

## How to Run

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/refedico/championssimulator.git
   cd championssimulator
2. Run the simulation script:
   ```bash
   python main.py

## Example Output

After running the simulation, you might see output like the following: 
```yalm
Final Standings:
1. Bayern München: 21 points, 8 played, 7 won, 0 drawn, 1 lost, 40 GS, 21 GC, 19 GD
2. Man City: 20 points, 8 played, 6 won, 2 drawn, 0 lost, 35 GS, 23 GC, 12 GD
3. Liverpool: 17 points, 8 played, 5 won, 2 drawn, 1 lost, 31 GS, 17 GC, 14 GD
4. Real Madrid: 17 points, 8 played, 5 won, 2 drawn, 1 lost, 34 GS, 25 GC, 9 GD
5. Arsenal: 17 points, 8 played, 5 won, 2 drawn, 1 lost, 30 GS, 22 GC, 8 GD
6. Inter: 16 points, 8 played, 5 won, 1 drawn, 2 lost, 34 GS, 24 GC, 10 GD
7. Shakhtar: 16 points, 8 played, 5 won, 1 drawn, 2 lost, 28 GS, 22 GC, 6 GD
8. Atleti: 16 points, 8 played, 5 won, 1 drawn, 2 lost, 28 GS, 23 GC, 5 GD
...
33. Bologna: 5 points, 8 played, 1 won, 2 drawn, 5 lost, 14 GS, 23 GC, -9 GD
34. Crvena Zvezda: 5 points, 8 played, 1 won, 2 drawn, 5 lost, 16 GS, 29 GC, -13 GD
35. Girona: 4 points, 8 played, 1 won, 1 drawn, 6 lost, 16 GS, 27 GC, -11 GD
36. Brest: 1 points, 8 played, 0 won, 1 drawn, 7 lost, 15 GS, 29 GC, -14 GD
```

## Some Interesting Results
After running simulations with 1000 repetitions, we obtained the following results: the best-case scenario refers to the simulation where the fewest points were required to reach the top 8 and top 24, respectively; the worst-case scenario refers to the simulation where the highest number of points was required in that case.
| Top | Average | Best | Worst
|----------|-----------|-----------|-----------|
| Top8   | 16.213  | 14  |19  |
| Top24   | 8.434  | 6  | 11  |

Now, let's look at a table for the same thing, but this time with goal difference instead of points:

| Top | Average | Best | Worst
|----------|-----------|-----------|-----------|
| Top8   | 7.163  | -1  |19  |
| Top24   | -4.065 | -17  | 2  |

Obviously, if the simulation is run on 10,000 or 100,000 cases, the results will be more accurate. However, the implementation does not take advantage of parallelization.


