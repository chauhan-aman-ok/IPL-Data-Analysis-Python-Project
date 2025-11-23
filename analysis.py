import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data=pd.read_csv(r"data\IPL.csv")
# print(data.info())

# printing count of rows and columns of dataset
# print(f"Rows : {data.shape[0]}, Columns : {data.shape[1]}")

# printing null values in each column
# print(data.isnull().sum())


# which team won the most matches 
match_wins=data["match_winner"].value_counts()
# sns.barplot(y=match_wins.index, x=match_wins.values)
# plt.title("Number of matches won by each team")
# plt.show()

# counting toss decicion trends
# sns.countplot(x=data["toss_decision"],palette="Set2")
# plt.title("Toss Decision Trends")
# plt.show()

# chance of winning if a team wins the toss
count=data[data["toss_winner"]==data["match_winner"]]["match_id"].count()
percentage=(count*100)/data.shape[0]
print(round(percentage,2))

# how do team wins (by runs or by wickets)
# sns.countplot(x=data["won_by"],palette="Set2")
# plt.show()

# top 10 most player of the match
# pomCount=data["player_of_the_match"].value_counts().head(10)
# sns.barplot(x=pomCount.values,y=pomCount.index)
# plt.title("Top 10 most player of the match")
# plt.show()

# top 2 scorer 
top=data.groupby("top_scorer")["highscore"].sum().sort_values(ascending=False).head(2)
# print(top)
# sns.barplot(x=top.index,y=top.values)
# plt.show()

# top 10 best bowling figures
data["mostWickets"]=data["best_bowling_figure"].apply(lambda x : x.split("--")[0])
data["mostWickets"]=data["mostWickets"].astype(int)
topBowlers=data.groupby("best_bowling")["mostWickets"].sum().sort_values(ascending=False).head(10)
# topBowlers.plot(kind="bar")
# plt.show()

# most matches played by venue
venue=data["venue"].value_counts()
# sns.barplot(x=venue.values,y=venue.index)
# plt.show()

# who won the highest margin by runs
highestMargin=data[data["won_by"]=="Runs"].sort_values(by='margin',ascending=False)[["match_winner","margin"]].head(1)
# print(highestMargin)

# which player has the highest individual score
highScore=data[data["highscore"]==data["highscore"].max()][["top_scorer","highscore"]]
# print(highScore)

# which bowler had the best bowling figure
bestBowling=data[data["mostWickets"]==data["mostWickets"].max()][["best_bowling","best_bowling_figure"]]
print(bestBowling)
