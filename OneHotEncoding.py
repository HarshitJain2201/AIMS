import pandas as pd
import numpy as np

# Let this is the given Sample data
data = {
    'Color': ['Red', 'Blue', 'Green', 'Blue','Yellow']
}
df = pd.DataFrame(data)

# we get unique categories using unique() function
unique_values = df['Color'].unique()

# Create empty DataFrame for encoded columns
for val in unique_values:
    encoded_col = []  # Empty list for this column
    
    # Loop through each row in the 'Color' column
    for color in df['Color']:
        if color == val:
            encoded_col.append(1)
        else:
            encoded_col.append(0)
    
    # Assign the list as a new column
    df[val] = encoded_col


print("One-Hot Encoded DataFrame:")
print(df)