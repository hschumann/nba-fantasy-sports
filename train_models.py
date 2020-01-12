"""
Just like the # symbol, you can also commment using the the triple quotations. 

I usually have the triple quotes at the top of each of the python scripts in a poject just to give an overview
of the contents that you'll find in it. It helps to keep things in order and know what is going on when things
grow and you have to come back to fix old issues.

Some people list the functions up here too. That's a big of a pain in the a** so I usually don't, but
it's still good practice if you were into that.

Anyways... see below for the start of this file.
"""

"""
This is a script to train (and test) the statistical models for predicting the amount of fantasy points a given
player will earn on a given day. 
"""

# import the necessary tools
import numpy as np  # will be used for doing most of the math efficiently
import pandas as pd  # will be used for handling dataframes

# import helper scripts that we have made
import data_handling
import graphing_tools


def main(plot_histograms=False):
	"""
	by default, the plot_histograms argument will be set to False, if it is made True, then the histograms will plot
	"""

	# first let's start by reading in the data we want
	player_game_data = data_handling.get_player_game_data()
	team_game_data = data_handling.get_team_game_data()

	print(team_game_data[['year', 'month', 'day']].head())

	if plot_histograms:
		# make a histogram of the fantasy points on a game level for players
		graphing_tools.histogram(data=player_game_data['fantasy_points'], label='Fantasy Points')

		# make a histogram of the true points on a game level for players (to demonstrate how this graph can plot many things)
		graphing_tools.histogram(data=player_game_data['playPTS'], label='Game Points')

	# FUN LITTLE PROBLEMS TO WORK ON FOR LEARNING DATA HANDLING AND SOME PYTHON
	# 0) Find out how to show those histograms in the lines above.

	# 1) Find out the highest number of fantasy points that James Harden had.
	#    How many fantasy points did he have per minute? 
	# Hint: you can subset to all James Harden games and then take the max


	# 2) Find the average number of points for Al Horford.


	# 3) Explore if there correlation between total team fantasy points and winning.
	#    Is there correlation between average fantasy points per game and season wins? 
	#    What about game to game data? Does a large gap between best player and average rest of team hinder a team?
	#    These are all probably useful findings to real NBA teams (aka Houston)
	# These ones are really tricky and I'll probably work on them myself too


	# 4) Anything else you want to explore. (If #3 is too hard, I'm already having some trouble with it)


	"""
	Hans' Developments are below. 
	"""




# this line allows you to use a bunch of functions and then just run them sequentially starting here
if __name__ == "__main__":
	# call the main function (specifying what we want to do in the function arguments as well) 
	main(plot_histograms=False)

