import pandas as pd

# This is the given Sample data
data = {
    'Size': [
        'Small', 'Medium', 'Large', 'Medium', 'Small', 
        'ExtraLarge', 'Large', 'Medium', 'Small'
    ]
}
df = pd.DataFrame(data)

# Manual mapping done to make string into number
size_mapping = {'Small': 1, 'Medium': 2, 'Large': 3}

# Apply mapping
#here map funct is used to map or compare each element of size in df with size_mapping
#It will replace all the string into number as given in size_mapping 
#and if any element is not in the mapping it will but nan there
#a new colummn will be made in df with name Size encoded
df['Size_Encoded'] = df['Size'].map(size_mapping)

print("Original DataFrame With Ordinal Encoding:")
print(df) 