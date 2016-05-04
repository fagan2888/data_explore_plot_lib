# -*- coding: utf-8 -*-
"""
Created on Mon May  2 08:51:56 2016
Author: Lee MacKenzie Fischer

Custom plotting functions for data exploration.

"""
import matplotlib.pyplot as plt
import brewer2mpl as bm
from matplotlib.widgets import  RectangleSelector, Button
import numpy as np

def ten_perc_of_range(data):
    data_range = data.max() - data.min()
    return data_range*0.1

def scatter_single(x_data, y_data, x_title="x-axis", y_title="y-axis", plot_title="chart title", labels=[None]):
    """
    Script for plotting multiple parameters on the same set of x- and y- 
    axes ("single" refers to a single set of axes, as opposed to scatter_matrix).
    x_data, y_data, and labels are all lists.  List must be at least length==1.
    
    Input: x_data, Type: list
    Contents - Elements of list can be either series, array, or list. Must 
    be equal length to y_data.
    
    Input: y_data, Type: list
    Contents - Elements of list can be either series, array, or list. Must 
    be equal length to x_data.
    
    Input: x_title, Type: string
    Contents - x-axis title
    
    Input: y_title, Type: string
    Contents - y-axis title
    
    Input: plot_title, Type: string
    Contents - Title of the entire plot
    
    Input: labels, Type: list (of strings)
    Contents - Strings correspond to the labels to be associated with data
    
    """
    
    i_len = len(x_data)  # get length of input matrix
    
    fig, ax = plt.subplots(1)  # define plot
    
    # define colors to be used
    almost_black = '#262626'
    light_gray = '#DADADA'
    very_light_gray = '#FAFAFA'
    set2 = bm.get_map('Set2', 'qualitative', 8).mpl_colors  # color set from brewer2mpl
    
    # initialization of maximum and minimum values before loop
    val_ymax = max(y_data[0])
    val_ymin = min(y_data[0])
    val_xmin = max(x_data[0])
    val_xmax = min(x_data[0])

    # set up scatter plots in same axis
    for i in range(i_len):
        # checking if labels are going to be used
        if labels[0] == None:
            ax.scatter(x_data[i], y_data[i], facecolor=set2[i], s=80, 
                    alpha=0.6, linewidths=0.15, edgecolor=almost_black, linewidth=0.15)
        else:
            ax.scatter(x_data[i], y_data[i], facecolor=set2[i], label=labels[i], s=80, 
                    alpha=0.6, linewidths=0.15, edgecolor=almost_black, linewidth=0.15)
        
        # get overall maximum and minimum values for plot edges
        if max( y_data[i] ) > val_ymax:
            val_ymax = max( y_data[i] )
        if min( y_data[i] ) < val_ymin:
            val_ymin = min( y_data[i] )
        if max( x_data[i] ) > val_xmax:
            val_xmax = max( x_data[i] )
        if min( x_data[i] ) < val_xmin:
            val_xmin = min( x_data[i] )
            
    # setup axis limits, 10% greater than actual limits each way for starters
    y_max_init = val_ymax + ten_perc_of_range(np.array([val_ymin, val_ymax]))
    y_min_init = val_ymin - ten_perc_of_range(np.array([val_ymin, val_ymax]))
    x_max_init = val_xmax + ten_perc_of_range(np.array([val_xmin, val_xmax]))
    x_min_init = val_xmin - ten_perc_of_range(np.array([val_xmin, val_xmax]))
    x_min, x_max, y_min, y_max = x_min_init, x_max_init, y_min_init, y_max_init
    ax.axis([x_min, x_max, y_min, y_max])
    
    # set chart border (spine) parameters    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(True)
    ax.spines['bottom'].set_linewidth(1.0)
    ax.spines['bottom'].set_color(almost_black)
    ax.spines['left'].set_visible(True)
    ax.spines['left'].set_linewidth(1.0)
    ax.spines['left'].set_color(almost_black)

    # set plot background properties, with minimal grid
    ax.set_axis_bgcolor('w')
    ax.yaxis.grid(True)
    ax.xaxis.grid(True)
    ax.grid(b=True, which='major', color=light_gray, linestyle='-', linewidth=0.4)    

    # format axis labels
    plt.xlabel(x_title, fontsize=14, color=almost_black)
    plt.ylabel(y_title, fontsize=14, color=almost_black)
    plt.title(plot_title, fontsize=16)

    # format legend, if used
    if labels[0] != None:
        legend = ax.legend(frameon=True, scatterpoints=1, fontsize=12, loc='best')
        rect = legend.get_frame()
        rect.set_facecolor(very_light_gray)
        rect.set_alpha(0.5)
        rect.set_linewidth(0.0)
    
    # setup interactive axis properties using widgets
    # rectangle zoom selector built from RectangleSelector example:
    # http://matplotlib.org/examples/widgets/rectangle_selector.html
    # reset button built from Slider example:
    # http://matplotlib.org/examples/widgets/slider_demo.html
    def onselect(eclick, erelease):
        x_min, x_max = min(eclick.xdata, erelease.xdata), max(eclick.xdata, erelease.xdata)
        y_min, y_max = min(eclick.ydata, erelease.ydata), max(eclick.ydata, erelease.ydata)
        ax.axis([x_min, x_max, y_min, y_max])
    
    def reset(event):
        ax.axis([x_min_init, x_max_init, y_min_init, y_max_init])
    
    resetax = plt.axes([0.01, 0.025, 0.08, 0.04])  # button location and size
    reset.button = Button(resetax, 'RESET', color=light_gray, hovercolor=very_light_gray)
    reset.button.on_clicked(reset)
    onselect.RS = RectangleSelector(ax, onselect, drawtype='box')
    
    plt.show()

    return None

