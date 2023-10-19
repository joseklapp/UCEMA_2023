import pandas as pd
def validate_columns(df):
    # Initialize an empty DataFrame to store validation results
    validation_df = pd.DataFrame(columns=['Column', 'Unique_Values', 'Num_Unique_Values', 'Num_Null_Values',  'Sample_Unique_Values'])

    # Loop through each column in the input DataFrame
    for col in df.columns:
        # Calculate the number of unique values
        num_unique_values = df[col].nunique()

        # Calculate the number of null values
        num_null_values = df[col].isnull().sum()

        # Calculate the percentage of null values
        percent_null_values = (num_null_values / len(df)) * 100

        # Get sample unique values
        sample_unique_values = df[col].dropna().sample(min(num_unique_values, 5)).tolist()

        # Append the validation results to the DataFrame
        validation_df = validation_df.append({
            'Column': col,
            'Unique_Values': df[col].unique(),
            'Num_Unique_Values': num_unique_values,
            'Num_Null_Values': num_null_values,
            '%_Null_Values': percent_null_values,
            'Sample_Unique_Values': sample_unique_values
        }, ignore_index=True)

    return validation_df




Latex text in markdown
$$ \text{Total_Students_Surveyed} = \sum_{i=1}^{n} \text{Number_of_Students_Surveyed}_i $$



