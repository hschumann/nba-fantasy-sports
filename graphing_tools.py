"""
This script will contain functions for plotting exploratory analysis things, and
maybe some final findings (who knows?).
"""


import matplotlib.pyplot as plt  # this is a graphing tool in python (like matlab, but less clunky)
import seaborn as sns  # this is a graphing tools that makes prettier graphs (also has more options for cooler ones)


def histogram(data, label):
	# make a density plot of the data
	sns.distplot(data, hist=True, bins=30, kde=True, color='darkblue', kde_kws={'linewidth': 4})

	# label the axes and graph
	plt.title('Histogram of ' + label)
	plt.xlabel(label)
	plt.ylabel('Frequency')
	plt.show()

