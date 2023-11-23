from IPython.display import display, Markdown
import pandas as pd
import matplotlib.pyplot as plt
from typing import Optional


def pprint(content):
    """
    Display content in Markdown format.

    Parameters:
        content (str): The Markdown content to be displayed.
    """
    display(Markdown(content)) 


def plot_missing_values(df: pd.DataFrame,
                        as_percentage: Optional[bool] = False,
                        figsize=(10,6)) -> None:
    """
    Plot a horizontal stacked bar chart showing the number of missing values per column.

    Parameters:
    - df (pd.DataFrame): The input DataFrame.
    - as_percentage (bool, optional): If True, display values as percentages. Default is False.

    Returns:
    None
    """
    # Count missing values per column
    missing_values = df.isnull().sum()

    # Calculate non-missing values per column
    total_values = df.shape[0]
    non_missing_values = total_values - missing_values

    # Convert values to percentages if requested
    if as_percentage:
        missing_values_percentage = (missing_values / total_values) * 100
        non_missing_values_percentage = (non_missing_values / total_values) * 100
    else:
        missing_values_percentage = missing_values
        non_missing_values_percentage = non_missing_values

    fig, ax = plt.subplots(figsize=figsize)
    
    # Plot non-missing values in black on the left
    ax.barh(missing_values.index, non_missing_values_percentage, color='black', label='Non-Missing')

    # Plot missing values in white on the right
    ax.barh(missing_values.index, missing_values_percentage, left=non_missing_values_percentage, color='white', edgecolor='black', label='Missing')

    ax.set_xlabel('Number of Values' if not as_percentage else 'Percentage of Values')
    ax.set_ylabel('Columns')
    ax.set_title('Missing Values per Column')
    ax.legend()

    # Show the plot
    plt.tight_layout()
    plt.show()
    
    
    
def plot_value_counts(value_counts, k=20, plot_title=""):
    fig, ax = plt.subplots()
    ax.set_title(plot_title)

    # Take the top k value counts
    total = value_counts.sum()
    
    value_counts = value_counts.head(k)

    # Calculate percentages
    percentages = (value_counts / total) * 100
    
    # Plot horizontal bar chart without bounding box
    bars = value_counts[::-1].plot.barh()

    # Annotate each bar with the percentage
    for bar, percentage in zip(bars.patches, percentages[::-1]):
        ax.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f'{percentage:.2f}%', 
                va='center', ha='left', color='black')

    # Remove the bounding box
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    plt.show()

    
def generate_sample_history(main, query=None):
    """
    Generate a sample transactional history of ONE random importer
    Optional: provide a query to narrow down sampling pool
    """
    if query is None:
        sample_importer = list(main['importer_deduped_name'].drop_duplicates().sample(1))[0]
    else:
        sample_importer = list(main.query(query)['importer_deduped_name'].drop_duplicates().sample(1))[0]
    print(sample_importer)
    sample_history = main[main["id"]==sample_importer]
    return (
        sample_history[['file_month', 'hs_codes', 'calculated_teu',
                        'country_of_origin', 'port_of_unlading', 
                        'importer_deduped_name', 'importer_rank', 'id']].sort_values(
        ['file_month', 'hs_codes']
        )
        )
