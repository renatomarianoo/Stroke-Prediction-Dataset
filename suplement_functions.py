import pandas as pd
import seaborn as sns

def create_countplot_vertical(df, ax, col, colors, plot_xlabel="", plot_ylabel="", percent=0):
    '''
    Creates an vertical countplot with the provided percentages on the top.
    '''
    sns.countplot(
        x=df[col],
        alpha=0.8,
        ax=ax,
        palette=colors,
    )

    ax.set(xlabel=plot_xlabel, ylabel=plot_ylabel)
    ax.tick_params(axis="both", which="both", length=0)
    sns.despine()

    if percent != 0:
        total_height = len(df)
        for p in ax.patches:
            height = p.get_height()
            ax.annotate(f'{height/total_height:.1%}', (p.get_x() + p.get_width() / 2., height),
                        ha='center', va='center', fontsize=10, color='black', xytext=(0, 5),
                        textcoords='offset points')

def create_catplot(df, ax, col, hue_col, colors, plot_xlabel="", plot_ylabel=""):
    '''
    Creates an vertical catplot and calculate the percentages to set on bars.
    '''
    sns.countplot(
        x=df[col],
        hue=df[hue_col],
        palette=colors,
        alpha=0.8,
        ax=ax,
        order = df[col].value_counts(ascending=False).index,
    )
    
    ax.set(xlabel=plot_xlabel, ylabel=plot_ylabel)
    ax.tick_params(axis='both', which='both', length=0)
    sns.despine()

def find_percentages_with_hue(ax, col, Number_of_categories=2, hue_categories=2):
    '''
    Calculate the percentages for countplots with a subcategory (hue) and plot them on the top of the bars
    '''
    a = [p.get_height() for p in ax.patches]
    patch = [p for p in ax.patches]

    for i in range(Number_of_categories):
        total = col.value_counts(ascending=False).values[i]
        for j in range(hue_categories):
            percentage = '{:.1f}%'.format(100 * a[(j*Number_of_categories + i)]/total)
            x = patch[(j*Number_of_categories + i)].get_x() + patch[(j*Number_of_categories + i)].get_width() / 2 - 0.1
            y = patch[(j*Number_of_categories + i)].get_y() + patch[(j*Number_of_categories + i)].get_height() + 50
            ax.annotate(percentage, (x, y), size=10)