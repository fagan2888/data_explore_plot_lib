# data_explore_plot_lib
A collection of Python scripts I use for plotting and exploring data. I've recently starting using Python for data analysis, and found myself missing the ability to zoom into clusters of data points directly on the plot (a la SAS JMP). Basically incorporates a bunch of scatter plot modifications in a single script to be run automatically, including more pleasant coloring (via brewer2mpl), rectangular-selection zooming (via Widgets) and a faster way (for me, at least) to plot data on the same set of axes.

Tested on Python 3.4.3 and later.
Uses the following packages:
- numpy
- matplotlib.pyplot 
- matplotlib.widgets 
- brewer2mpl

## Description of functions
### scatter_single
#####scatter_single(x_data, y_data, x_title="x-axis", y_title="y-axis", plot_title="chart title", labels=[None])
Script for plotting multiple parameters on the same set of x- and y- 
axes ("single" refers to a single set of axes, as opposed to scatter_matrix).
x_data, y_data, and labels are all lists.  List must be at least length==1.

Input: x_data, Type: list
Contents - Elements of list can be either series, array, or list. Must be equal length to y_data.

Input: y_data, Type: list
Contents - Elements of list can be either series, array, or list. Must be equal length to x_data.

Input: x_title, Type: string
Contents - x-axis title

Input: y_title, Type: string
Contents - y-axis title

Input: plot_title, Type: string
Contents - Title of the entire plot

Input: labels, Type: list (of strings)
Contents - Strings correspond to the labels to be associated with data
