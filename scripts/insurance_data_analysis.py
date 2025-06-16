import pandas as pd;

class InsuranceDataAnalysis:
    def __init__(self, df:pd.DataFrame):
        self.df = df
        
    def display_head(self):
        return self.df.head()

    def display_columns(self):
        return self.df.columns

    def display_shape(self):
        return self.df.shape

    def display_description(self):
        return self.df.describe()
    
    def describe_selected_numericals(self, columns: list):
      """
      Display descriptive statistics (mean, std, min, max) for selected numerical columns.
      """
      numerical_cols = [col for col in columns if col in self.df]
      print(f"\n Descriptive statistics for selected columns: {numerical_cols}")
      stats = self.df[numerical_cols].describe().T.sort_values(by='std', ascending=False)
      print(stats)


    def check_data_structure(self):
      """
        Print data types, detect mismatches, and recommend fixes.
      """
      print("\nColumn Data Types Overview:")
      print(self.df.dtypes.value_counts())
     
      print("\nFull Data Type Listing:")
      for col in self.df.columns:
         print(f"{col}: {self.df[col].dtype}")


      print("\nChecking date format for 'TransactionMonth':")
      if 'TransactionMonth' in self.df.columns:
        if not pd.api.types.is_datetime64_any_dtype(self.df['TransactionMonth']):
            print("'TransactionMonth' is NOT in datetime format.")
         
        else:
            print("TransactionMonth' is already in datetime format.")

      print("\Top Categorical-Like Columns (object or category):")
      cat_cols = self.df.select_dtypes(include=['object', 'category']).columns
      for col in cat_cols[:10]: 
          print(f" - {col} ({self.df[col].nunique()} unique values)")


    def summarize_missing_values(self, top_n: int = 20):
        """
           Displays the top columns with the most missing values in absolute count and percent.
        """
        print("\ Missing Values Summary:")

        total_missing = self.df.isnull().sum()
        percent_missing = (total_missing / len(self.df)) * 100

        missing_df = pd.DataFrame({
           'Missing Count': total_missing,
           'Missing Percent': percent_missing
       })

        # Filter columns that have at least one missing value
        missing_df = missing_df[missing_df['Missing Count'] > 0]
        missing_df = missing_df.sort_values(by='Missing Count', ascending=False)

        if missing_df.empty:
          print("No missing values found.")
        else:
          print(missing_df.head(top_n))
          print(f"\n{missing_df.shape[0]} columns have missing values.")
     
     # src/eda/data_cleaning.py


    def clean_and_save_data(self, output_path: str) -> pd.DataFrame:
        """
        Cleans the insurance data based on missing value strategy and saves to a new CSV file.

        Parameters:
         output_path (str): Path to save the cleaned CSV

        Returns:
          pd.DataFrame: Cleaned dataframe
        """

        print("Starting data cleaning...")

       # Drop columns with too many missing values
        columns_to_drop = [
          'NumberOfVehiclesInFleet', 'CrossBorder',
          'WrittenOff', 'Converted', 'Rebuilt'
         ]
        self.df.drop(columns=columns_to_drop, inplace=True, errors='ignore')
        print(f"✅ Dropped columns: {columns_to_drop}")

         # Fill moderate-missing columns
        if 'CustomValueEstimate' in self.df.columns:
           median_value = self.df['CustomValueEstimate'].median()
           self.df['CustomValueEstimate'].fillna(median_value, inplace=True)
           print(f"✅ Filled 'CustomValueEstimate' with median: {median_value}")

        if 'NewVehicle' in self.df.columns:
          self.df['NewVehicle'].fillna('No', inplace=True)
          print("✅ Filled 'NewVehicle' with 'No'")

        if 'Bank' in self.df.columns:
          self.df['Bank'].fillna('Unknown', inplace=True)
          print("✅ Filled 'Bank' with 'Unknown'")

        if 'AccountType' in self.df.columns:
          mode_val = self.df['AccountType'].mode()[0]
          self.df['AccountType'].fillna(mode_val, inplace=True)
          print(f"✅ Filled 'AccountType' with mode: {mode_val}")

         # Drop rows with low-percentage missing values
        low_missing_columns = [
        'Gender', 'MaritalStatus', 'make', 'Model', 'mmcode',
        'VehicleType', 'bodytype', 'VehicleIntroDate', 'CapitalOutstanding'
       ]
        
        self.df.dropna(subset=low_missing_columns, inplace=True)
        print(f"✅ Dropped rows with missing values in: {low_missing_columns}")

       # Save cleaned data
        self.df.to_csv(output_path, index=False)
        print(f"📁 Cleaned data saved to: {output_path}")

        return self.df
