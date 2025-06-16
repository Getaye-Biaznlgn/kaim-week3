# src/eda/univariate_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style="whitegrid")

class UnivariateAnalysis:
    def __init__(self, df: pd.DataFrame):
        """
        Initializes the UnivariateAnalysis class with a DataFrame.

        Parameters:
        df (pd.DataFrame): The DataFrame to analyze.
        """
        self.df = df  
        
    def plot_numeric_distributions(self, df, columns=None, save_dir=None):
        if columns is None:
            columns = df.select_dtypes(include=['int64', 'float64']).columns

        for col in columns:
            plt.figure(figsize=(8, 4))
            sns.histplot(df[col].dropna(), kde=True, bins=30)
            plt.title(f"Distribution of {col}")
            plt.xlabel(col)
            plt.tight_layout()
            if save_dir:
                plt.savefig(f"{save_dir}/{col}_distribution.png")
            plt.show()


    def plot_categorical_distributions(self, df: pd.DataFrame, columns: list = None, save_dir: str = None, top_n: int = 10):
        """
          Plots bar charts for specified or top categorical columns based on cardinality.
        """
        if columns is None:
            columns = df.select_dtypes(include=['object', 'category']).columns.tolist()

        for col in columns[:top_n]:
          plt.figure(figsize=(8, 4))
          df[col].value_counts(normalize=True).plot(kind='bar')
          plt.title(f"Distribution of {col}")
          plt.ylabel("Proportion")
          plt.xlabel(col)
          plt.tight_layout()

        if save_dir:
            os.makedirs(save_dir, exist_ok=True)
            plt.savefig(f"{save_dir}/{col}_distribution.png")
        plt.show()
