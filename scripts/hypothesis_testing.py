# src/eda/hypothesis_testing.py

import pandas as pd
import numpy as np
from scipy import stats


class HypothesisTester:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        self.df['ClaimOccurred'] = (self.df['TotalClaims'] > 0).astype(int)
        self.df['ProfitMargin'] = self.df['TotalPremium'] - self.df['TotalClaims']

    def t_test(self, group_col: str, metric_col: str, group1_val, group2_val):
        """
        Perform an independent t-test between two groups on a numerical metric.
        """
        group1_data = self.df[self.df[group_col] == group1_val][metric_col]
        group2_data = self.df[self.df[group_col] == group2_val][metric_col]

        t_stat, p_val = stats.ttest_ind(group1_data, group2_data, equal_var=False, nan_policy='omit')

        return {
            'Test': 'T-test',
            'Metric': metric_col,
            'Group 1': group1_val,
            'Group 2': group2_val,
            'Group 1 Mean': group1_data.mean(),
            'Group 2 Mean': group2_data.mean(),
            'T-statistic': t_stat,
            'P-value': p_val,
            'Significant': p_val < 0.05
        }

    def chi_square_test(self, group_col: str, target_col='ClaimOccurred'):
        """
        Perform a chi-square test of independence for ClaimOccurred across categories.
        """
        contingency_table = pd.crosstab(self.df[group_col], self.df[target_col])
        chi2, p_val, dof, expected = stats.chi2_contingency(contingency_table)

        return {
            'Test': 'Chi-square',
            'Group': group_col,
            'Chi²': chi2,
            'P-value': p_val,
            'Degrees of Freedom': dof,
            'Significant': p_val < 0.05,
            'Contingency Table': contingency_table
        }
