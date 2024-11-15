import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from typing import List, Union, Sequence, Optional
from matplotlib.figure import Figure
from matplotlib.axes import Axes

def hist_box(dataset: pd.DataFrame, column: str) -> tuple[plt, Figure, Axes]:
    """
    Function, which plots the histogram and boxplot
    for the column of the given dataset.
    Create two subplots, one above another. At the higher plot
    there is a boxplot, plot histogram.
    Parameters:
        - dataset(DataFrame): table with the data to plot
        - column(str): column name for which do the plotting
    Retiurn:
        - tuple[plt, Figure, Axes]: the figure, pyplot and axes where 
    we performed the plotting
    """
    fig, ax = plt.subplots(2, 1,
                           sharex=True,
                           gridspec_kw={'height_ratios': [1, 3]})

    # set the distance between subplots to 0
    plt.subplots_adjust(hspace=0)

    # plot box plot horizontally
    sns.boxplot(x=dataset[column],
                ax=ax[0],
                color="blue")

    # plot histogram
    sns.histplot(x=dataset[column],
                 ax=ax[1], color="blue")
    return plt, fig, ax

def customize_bar(position: str, *ax_args: Sequence[Axes], values_font=12) -> None:
    """
    Function, which customizes bar chart
    Takes arbitrary number of Axes objects and:
        - gets rid of spines
        - modifies ticks
        - adds value above each bar
    Parameters:
        - *ax_args(Sequence[Axes]): list of Axes to modify
        - position(str): modify the bar depending on how the
        bars are positioned: vertically or horizontally
    Return: None
    """
    for ax in ax_args:
        # get rid of spines
        for spine in ax.spines.values():
            spine.set_visible(False)
        # modify ticklabels
        if position == "v":
            ax.set_yticks([])
            for tick in ax.get_xticklabels():
                tick.set_rotation(0)
        if position == "h":
            ax.set_xticks([])
            for tick in ax.get_yticklabels():
                tick.set_rotation(0)
        # add height value above each bar
        for bar in ax.patches:
            if position == "v":
                text_location = (bar.get_x() + bar.get_width()/2,
                                 bar.get_height() + 1/100*bar.get_height())
                value = bar.get_height()
                location = "center"
            elif position == "h":
                text_location = (bar.get_width(),
                                 bar.get_y() + bar.get_height() / 2)
                value = bar.get_width()
                location = "left"
            if int(value) == value:
                value = int(value)
            else:
                value = round(value, 2)
            ax.text(text_location[0],
                    text_location[1],
                    str(value),
                    fontsize=values_font,
                    ha=location)