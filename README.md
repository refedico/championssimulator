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
9. Paris: 16 points, 8 played, 5 won, 1 drawn, 2 lost, 31 GS, 28 GC, 3 GD
10. Sturm Graz: 15 points, 8 played, 5 won, 0 drawn, 3 lost, 18 GS, 16 GC, 2 GD
11. Club Brugge: 14 points, 8 played, 4 won, 2 drawn, 2 lost, 27 GS, 22 GC, 5 GD
12. Monaco: 14 points, 8 played, 4 won, 2 drawn, 2 lost, 27 GS, 22 GC, 5 GD
13. Milan: 14 points, 8 played, 4 won, 2 drawn, 2 lost, 26 GS, 22 GC, 4 GD
14. B. Dortmund: 13 points, 8 played, 3 won, 4 drawn, 1 lost, 29 GS, 25 GC, 4 GD
15. Leverkusen: 13 points, 8 played, 4 won, 1 drawn, 3 lost, 26 GS, 22 GC, 4 GD
16. Celtic: 13 points, 8 played, 4 won, 1 drawn, 3 lost, 22 GS, 19 GC, 3 GD
17. Benfica: 13 points, 8 played, 4 won, 1 drawn, 3 lost, 29 GS, 27 GC, 2 GD
18. Juventus: 13 points, 8 played, 4 won, 1 drawn, 3 lost, 29 GS, 29 GC, 0 GD
19. PSV: 13 points, 8 played, 4 won, 1 drawn, 3 lost, 21 GS, 23 GC, -2 GD
20. Aston Villa: 11 points, 8 played, 3 won, 2 drawn, 3 lost, 22 GS, 22 GC, 0 GD
21. Salzburg: 10 points, 8 played, 3 won, 1 drawn, 4 lost, 22 GS, 22 GC, 0 GD
22. Sporting CP: 10 points, 8 played, 3 won, 1 drawn, 4 lost, 21 GS, 21 GC, 0 GD
23. Barcelona: 9 points, 8 played, 3 won, 0 drawn, 5 lost, 28 GS, 29 GC, -1 GD
24. Feyenoord: 8 points, 8 played, 2 won, 2 drawn, 4 lost, 16 GS, 22 GC, -6 GD
25. GNK Dinamo: 8 points, 8 played, 2 won, 2 drawn, 4 lost, 14 GS, 28 GC, -14 GD
26. Leipzig: 7 points, 8 played, 1 won, 4 drawn, 3 lost, 25 GS, 29 GC, -4 GD
27. Young Boys: 7 points, 8 played, 2 won, 1 drawn, 5 lost, 16 GS, 22 GC, -6 GD
28. Lille: 7 points, 8 played, 2 won, 1 drawn, 5 lost, 16 GS, 23 GC, -7 GD
29. Atalanta: 7 points, 8 played, 2 won, 1 drawn, 5 lost, 16 GS, 25 GC, -9 GD
30. Stuttgart: 6 points, 8 played, 2 won, 0 drawn, 6 lost, 20 GS, 23 GC, -3 GD
31. S. Bratislava: 5 points, 8 played, 1 won, 2 drawn, 5 lost, 16 GS, 23 GC, -7 GD
32. Sparta Praha: 5 points, 8 played, 1 won, 2 drawn, 5 lost, 19 GS, 28 GC, -9 GD
33. Bologna: 5 points, 8 played, 1 won, 2 drawn, 5 lost, 14 GS, 23 GC, -9 GD
34. Crvena Zvezda: 5 points, 8 played, 1 won, 2 drawn, 5 lost, 16 GS, 29 GC, -13 GD
35. Girona: 4 points, 8 played, 1 won, 1 drawn, 6 lost, 16 GS, 27 GC, -11 GD
36. Brest: 1 points, 8 played, 0 won, 1 drawn, 7 lost, 15 GS, 29 GC, -14 GD
```

## Some Interesting Results
| Top | Average | Best | Worst
|----------|-----------|-----------|-----------|
| Top8   | 17  | 15  |19  |
| Top24   | 8  | 7  |10  |


