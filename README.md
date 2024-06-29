# euro2024_chatGPTprediction_project
data analysis project that compare the reality and chatGPT prediction for the results of the Euro 2024 group stage matches

-----------------------------------------------------------

Can ChatGPT predict the results of Euro 2024 matches?

Ahead of the Euro, I decided to challenge the chat (and my betting abilities) to see if it could find the best statistical model in its view and predict the results of the Euro 2024 group stage matches.

Highlights
•	 The chat managed to accurately predict 22.2% of the matches (1 in 5 matches) - the score, the type of result and the identity of the winner.
•	In 50% of the matches, the chat successfully predicted the type of result and the identity of the winner but not the score.
•	In 45.83% of the matches, the chat successfully predicted the exact number of goals a specific team would score in a particular match.
•	In 25% of the matches, the chat predicted the goal difference in that match.
•	 The chat best predicted the achievements of the Czech Republic team during the group stage (accurately predicting results related to them in 66.6% of the matches).
•	The teams for which the chat accurately predicted the number of goals they would score were Slovenia, Poland, and the Czech Republic.
•	The team furthest from the chat's prediction in terms of expected goals is (not surprisingly...) - England, with an average deviation of 2.0 goals per match, followed by France of course, with an average deviation of 1.75 goals per match.

Proposed prediction model
Based on 4 parameters:
•	 FIFA ranking
•	 The team's achievements in the Euro qualifiers tournament
•	 The team's historical achievements
•	 Betting odds per match and team in the 20 leading betting sites in the world today.

In the model, a weighted average is performed for each parameter, normalization and calculation of the number of goals for a team in a match and the ratio between them.

I'm attaching here on GitHub the full statistical model with example, the Python code for data analysis and an organized and detailed documentation.
Wishing us all a successful and interesting continuation of the Euro!Wishing us all a successful and interesting continuation of the Euro!

Annexes

Prediction Model:
•	Goals for Germany = (Qualification performance + FIFA ranking + Achievements + Betting odds) / 4
•	Goals for Scotland = (Qualification performance + FIFA ranking + Achievements + Betting odds) / 4
Example - Step-by-Step Prediction Process for Germany vs. Scotland
1.	Collect Relevant Data:
o	Qualification Performance:
	Germany: 8 wins, 1 draw, 1 loss (9/10)
	Scotland: 6 wins, 2 draws, 2 losses (7/10)
o	FIFA Rankings (as of May 2024):
	Germany: 4th (9.6/10)
	Scotland: 22nd (8.8/10)
o	Previous Achievements:
	Germany: 3-time European champions (9/10)
	Scotland: Best finish - Group Stage (4/10)
o	Betting Odds (average from top 20 sites):
	Germany win: 1.40 (7.14/10)
	Draw: 4.50
	Scotland win: 7.50 (1.33/10)
2.	Assign Numerical Values:
o	Germany:
	Qualification Performance: 9
	FIFA Ranking: 9.6
	Previous Achievements: 9
	Betting Odds: 7.14
o	Scotland:
	Qualification Performance: 7
	FIFA Ranking: 8.8
	Previous Achievements: 4
	Betting Odds: 1.33
3.	Combine the Data for Each Team:
o	Goals for Germany: 9+9.6+9+7.144=34.744=8.685\frac{9 + 9.6 + 9 + 7.14}{4} = \frac{34.74}{4} = 8.68549+9.6+9+7.14=434.74=8.685 Normalize to a realistic scoring range: Normalized Goals for Germany=3\text{Normalized Goals for Germany} = 3Normalized Goals for Germany=3
o	Goals for Scotland: 7+8.8+4+1.334=21.134=5.2825\frac{7 + 8.8 + 4 + 1.33}{4} = \frac{21.13}{4} = 5.282547+8.8+4+1.33=421.13=5.2825 Normalize to a realistic scoring range: Normalized Goals for Scotland=0\text{Normalized Goals for Scotland} = 0Normalized Goals for Scotland=0
4.	Final Prediction:
o	Goals for Germany: 3
o	Goals for Scotland: 0
o	Winning Team: Germany
------------------------------
Top 20 Betting Sites for Forecast
1.	Bet365
2.	William Hill
3.	Betway
4.	888sport
5.	Unibet
6.	Bwin
7.	Ladbrokes
8.	Paddy Power
9.	Betfair
10.	Coral
11.	Sky Bet
12.	Sportingbet
13.	Marathonbet
14.	BetVictor
15.	BoyleSports
16.	Betfred
17.	10Bet
18.	MansionBet
19.	Parimatch
20.	STS

