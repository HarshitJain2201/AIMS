import pandas as pd
import numpy as np

def WithForLoop():
    # Sample data
    data = {
    'Age': [25, np.nan, 30, np.nan, 40, 100],
    'Gender': ['M', 'F', np.nan, 'F', 'M', np.nan]
    }
    df = pd.DataFrame(data)

    # ---- Mean Imputation for Numerical ----
    mean_val = np.nanmean(df['Age'])

    imputed = []
    for x in df['Age']:
        if not np.isnan(x):
            imputed.append(x)  # keep existing value
        else:
            imputed.append(mean_val)  # replace missing

    df['Age_Mean_Imputed'] = imputed

    # ---- Median Imputation for Numerical ----
    median_val = np.nanmedian(df['Age'])
    imputed = []
    for x in df['Age']:
        if not np.isnan(x):
            imputed.append(x)  # keep existing value
        else:
            imputed.append(median_val)  # replace missing 
    df['Age_Median_Imputed'] = imputed

    # ---- Mode Imputation for Categorical ----
    mode_val = df['Gender'].mode()[0]  # using pandas only to find mode
    imputed = []
    for x in df['Gender']:
        if pd.notna(x):
            imputed.append(x)  # keep existing value
        else:
            imputed.append( mode_val)  # replace missing 

    df['Gender_Mode_Imputed'] = imputed


    print("Data After Imputation:")
    print(df)
    return df


def WithListComprehension():
    # Sample data
    data = {
    'Age': [25, np.nan, 30, np.nan, 40, 100],
    'Gender': ['M', 'F', np.nan, 'F', 'M', np.nan]
    }
    df = pd.DataFrame(data)

    # ---- Mean Imputation for Numerical ----
    mean_val = df['Age'].mean()
    df['Age_Mean_Imputed']=[x if not np.isnan(x) else mean_val for x in df['Age']]

    # ---- Median Imputation for Numerical ----
    median_val = df['Age'].median()
    df['Age_Median_Imputed'] = [x if not np.isnan(x) else median_val for x in df['Age']]

    # ---- Mode Imputation for Categorical ----
    mode_val = df['Gender'].mode()[0]  # using pandas only to find mode
    df['Gender_Mode_Imputed'] = [x if pd.notna(x) else mode_val for x in df['Gender']]
    print(df)
    return df



if WithListComprehension().equals(WithForLoop()):
    print("Both Methods are correct")
else:
    print("Something is different")
