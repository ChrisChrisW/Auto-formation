import pandas as pd
import re

## my files link
path = "data/"
output_path = "output/"

## get csv file
pokedex = pd.read_csv(path + 'pokemon_data.csv')
# print(pokedex.head(3))
# print(pokedex.tail(3))

## get xslx/excel file
pokedex_xlsx = pd.read_excel(path + 'pokemon_data.xlsx')
# print(pokedex_xlsx.head(3))

## get txt file
pokedex_txt = pd.read_csv(path + 'pokemon_data.txt', delimiter="\t") # change delimiter if you have something else
# print(pokedex_txt.head(5))

# ---------------------------------------------
## read header
# print(pokedex.columns)

## read each column
# print(pokedex['Name'])
# print(pokedex['Name'][0:5])
# print(pokedex.Name)
# print(pokedex[['Name', 'Type 1', 'HP']])

## read each row
# print(pokedex.head(2))
# print(pokedex.iloc[2])
# print(pokedex.iloc[0:4])
# for index, row in pokedex.iterrows():
#     print(index, row['Name'])
# print(pokedex.loc[pokedex['Type 1'] == "Fire"])

## read a specific location
# print(pokedex.iloc[2,1])

# ---------------------------------------------

## describe data
# print(pokedex.describe())

## sort data
# print(pokedex.sort_values('Name'))
# print(pokedex.sort_values(['Name', 'HP'], ascending=[False, True]))

# ---------------------------------------------

## making changes to the data
# pokedex['Total'] = pokedex['HP'] + pokedex['Attack'] + pokedex['Defense'] + pokedex['Sp. Atk'] + pokedex['Sp. Def'] + pokedex['Speed']
# print(pokedex.head(2))
# pokedex = pokedex.drop(columns=['Total'])
# print(pokedex.head(2))
# pokedex['Total'] = pokedex.iloc[:, 4:10].sum(axis=1) # axis=1 -> horizontal
# print(pokedex.head(2))

# ---------------------------------------------

## saving data
# pokedex.to_csv(output_path + "modified.csv", index=False)
# pokedex.to_excel(output_path + "modified.xlsx", index=False)
# pokedex.to_csv(output_path + "modified.txt", index=False, sep='\t')

# ---------------------------------------------

## filtering Data 
# new_df = pokedex.loc[(pokedex['Type 1'] == 'Grass') & (pokedex['Type 2'] == 'Poison') & (pokedex['HP'] > 70)]
# new_df.reset_index(drop=True, inplace=True)
# print(new_df)
# print(pokedex.loc[(pokedex['Type 1'] == 'Grass') | (pokedex['Type 2'] == 'Poison')])

# print(pokedex.loc[pokedex['Name'].str.contains("Mega")])
# print(pokedex.loc[~pokedex['Name'].str.contains("Mega")]) # Inverse

# print(pokedex.loc[pokedex["Type 1"].str.contains('Fire|Grass', regex=True)])
# print(pokedex.loc[pokedex["Type 1"].str.contains('fire|grass', flags=re.I, regex=True)])
# print(pokedex.loc[pokedex["Type 1"].str.contains('fire|grass', flags=re.I, regex=True)])
# print(pokedex.loc[pokedex["Name"].str.contains('^pi[a-z]*', flags=re.I, regex=True)])

# ---------------------------------------------

## conditional changes
# pokedex.loc[pokedex['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'
# pokedex.loc[pokedex['Type 1'] == 'Flamer', 'Legendary'] = True
# pokedex.loc[pokedex['Type 1'] == 'Fire', ['Type 1', 'Legendary']] = ['Flamer',True]
# print(pokedex)

# ---------------------------------------------

## aggreate statisics (groupby)
# df = pd.read_csv(output_path + "modified.csv")
# print(df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False)) # TODO : don't working
# print(df.groupby(['Type 1']).sum())
# df['count'] = 1
# print(df.groupby(['Type 1']).count()['count'])


# ---------------------------------------------

## working with large amounts of data
# df = pd.read_csv(output_path + "modified.csv")
# new_df = pd.DataFrame(columns=df.columns)

# for df in pd.read_csv(output_path + "modified.csv", chunksize=5):
#     result = df.groupby(["Type 1"]).count()

#     new_df = pd.concat([new_df, result])

# print(new_df)