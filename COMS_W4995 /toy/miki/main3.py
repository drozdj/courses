# %% 

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('filtered_dataset.csv')
df_melted = df.melt(id_vars=['Unnamed: 0', 'Country Code'], 
                    var_name='Year', 
                    value_name='GDP Growth')
df_melted['Year'] = pd.to_numeric(df_melted['Year'])

# Create a 4x2 subplot grid (8 subplots)
fig, axes = plt.subplots(4, 2, figsize=(15, 20))
fig.suptitle('GDP Growth by Region', fontsize=16, y=0.95)

# Define country groups
countries_groups = {
    'Group 1': ['FRA', 'DEU', 'ITA', 'ESP'],
    'Group 2': ['POL', 'HUN', 'CZE', 'SVK'],
    'Group 3': ['NOR', 'SWE', 'DNK', 'FIN'],
    'Group 4': ['GRC', 'PRT', 'IRL', 'NLD'],
    'Group 5': ['AND', 'AUT', 'BEL', 'BGR', 'BIH', 'BLR', 'CHE', 'CYP', 'CZE', 'NOR'],
    'Group 6': ['DNK', 'ESP', 'EST', 'FIN', 'GBR', 'GRC', 'HRV', 'HUN', 'IRL', 'ISL'],
    'Group 7': ['LIE', 'LTU', 'LUX', 'LVA', 'MCO', 'MDA', 'MKD', 'MLT', 'MNE', 'NLD'],
    'Group 8': ['PRT', 'ROU', 'RUS', 'SMR', 'SRB', 'SVK', 'SVN', 'SWE', 'TUR', 'UKR']
}

# Flatten axes for easier iteration
axes_flat = axes.flatten()

# Plot each group in a different subplot
for idx, (group_name, countries) in enumerate(countries_groups.items()):
    ax = axes_flat[idx]
    for country in countries:
        country_data = df_melted[df_melted['Country Code'] == country]
        if not country_data.empty:  # Only plot if data exists
            ax.plot(country_data['Year'], country_data['GDP Growth'], label=country, linewidth=1.5)
    
    ax.set_title(f'{group_name}', pad=10)
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.set_xlabel('Year')
    ax.set_ylabel('GDP Growth (%)')

plt.tight_layout()
plt.show()


# %% 