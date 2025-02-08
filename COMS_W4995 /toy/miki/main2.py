# %% 
import pandas as pd

df = pd.read_csv('data/API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_11.csv')

# Read the country names from the text file
with open('paste.txt', 'r') as f:
    countries = [line.strip() for line in f.readlines()]

# Check if countries are in the index or in a specific column
# Assuming there might be a column named 'Country' or similar
country_columns = [col for col in df.columns if 'country' in col.lower()]

if country_columns:
    # If there's a country column, filter rows based on it
    country_col = country_columns[0]
    filtered_df = df[df[country_col].isin(countries)]
else:
    # If countries are in the index
    filtered_df = df.loc[countries]

# Save the filtered dataset
filtered_df.to_csv('filtered_dataset.csv')

# Print shape of filtered dataset
print(f"Filtered dataset shape: {filtered_df.shape}")

# %%
columns_to_remove = ['Unnamed: 68','Country Name', 'Indicator Name', 'Indicator Code', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2023', '2022', '2021', '2020']
filtered_df = filtered_df.drop(columns=columns_to_remove)

#%%
filtered_df.to_csv('filtered_dataset.csv')
