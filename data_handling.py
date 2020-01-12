"""
This script will contain a series of functions used to gather the necessary parts of the data we want.
"""

# imports for handling the data
import pandas as pd
import numpy as np


# here we are going to create global variables (usually denoted in ALL CAPS) to use throughout the various functions
# PLAYER_DATA = pd.read_excel()

# SECTION 1: GATHERING THE ACTUAL DATASETS
def get_player_game_data():
	# read in the csv with all the player box scores
	player_game_data = pd.read_csv('./nba-enhanced-stats/2012-18_playerBoxScore.csv')

	# feature engineering (get the number of fantasy points in each game)
	
	# this line is calling a function found in section 2 of this script to create a new column for the fantasy points
	# this is a little complicated but I am a "vectorize" function which allows the function (formula for points)
	# to be used on all the rows of the player data simulataneously making it way faster than line by line
	player_game_data['fantasy_points'] = np.vectorize(calculate_game_fantasy_points)(
		player_game_data['playPTS'], player_game_data['playTRB'], player_game_data['playSTL'], player_game_data['playAST'],
		player_game_data['playBLK'], player_game_data['playTO'])

	# return the player game data
	return player_game_data


def get_team_game_data():
	# read in the csv with all the team box scores
	team_game_data = pd.read_csv('./nba-enhanced-stats/2012-18_officialBoxScore.csv')
	# team_game_data = pd.DataFrame(columns=team_game_data_raw.columns)

	# go through each game and add it if it is a unique data point
	# team_game_data.loc[0] = team_game_data_raw.loc[0]
	# for i in range(len(team_game_data_raw) - 1):
	# 	if (team_game_data_raw.loc[i]['gmDate'] != team_game_data.loc[len(team_game_data)-1]['gmDate']) \
	# 			or (team_game_data_raw.loc[i]['teamAbbr'] != team_game_data.loc[len(team_game_data)-1]['teamAbbr']):
	# 		team_game_data.loc[len(team_game_data)] = team_game_data_raw.loc[i+1]

	# this dataset has 3 lines for every game (one for each official)
	# only keep every 3rd line (we don't care about the officals)
	# print(team_game_data.loc[0])
	team_game_data = team_game_data[team_game_data.index % 3 == 0].reset_index(drop=True)

	# make a variable for the game number
	team_game_data['Game Number'] = np.floor(team_game_data.index / 2)

	# get meta data for this dataset
	dates = np.array(team_game_data['gmDate'].apply(parse_date))
	print(np.shape(dates))
	dates = np.array(dates).reshape(3, int(len(dates) / 3))

	team_game_data['year'] = dates[:0]
	team_game_data['month'] = dates[:1]
	team_game_data['day'] = dates[:2]

	return team_game_data


# SECTION 2: CALCULATING VARIABLES FROM THE DATASETS
def calculate_game_fantasy_points(points, rebounds, steals, assists, blocks, turnovers):
	"""
	The equation I am using (which could totally be changed depending on league) is the following: 
	Points = 1
	Rebounds = 1.2
	Steals = 3
	Assists = 1.5
	Blocks = 3
	Turnovers = -1
	
	I found this on ESPN, but I may be way wrong
	"""
	fantasy_points = points + 1.2 * rebounds + 3.0 * steals + 1.5 * assists + 3.0 * blocks - turnovers
	return fantasy_points


def parse_date(date_string):
	year = int(date_string[:4])
	month = int(date_string[5:7])
	day = int(date_string[8:])

	return [year, month, day]



