# %%
import pandas as pd
import numpy as np
from pathlib import Path

# %%
file_path = 'data/nhl_18_19_player_stats_small.csv'
df = pd.read_csv(file_path)
# %% 1. shows you a gist of the data
df.head()

# %% 2. Some statistical information about your data
df.describe()

#  %% 3. List of columns headers
df.columns.values

# %%
columns_to_be_selected = ['Player', 'Team', 'Goals']
df[columns_to_be_selected]


# %%
df.iloc[0:3, :]
row_index_to_select = [0, 1, 4, 5]
df.loc[row_index_to_select]

# %% 1. Total points > 100
df[df["Points"] > 100]

# %% 2. Total points > 100 and in Western Conference

df[(df["Points"] > 100) & (df["Conference"] == "Western")]

# %%
df["Points"].sum()
# %%
df[["Points", "Games"]].mean()
# %%
df[["Points", "Games"]].min()
# %%
df[["Points", "Games"]].max()
# %%
df[["Points", "Games"]].median()
# %%
df[["Points", "Games"]].mode()


# %% 1. Conference wise stats
df.groupby("Conference").sum()

# %% 2. goals over each conference & division
df.groupby(["Conference", "Division", "Team"]).sum()

# %% 3. More than one aggregation
df.groupby(["Conference", "Division", "Team"]).agg({
    'Goals': ['sum', 'max'],
    'Points': 'mean'
})

# %%
file_path = 'data/nhl_18_19_player_stats.csv'
df_full = pd.read_csv(file_path)
# %%
df_full.pivot_table(
    index=["Team"],
    columns=["Position"],
    values=["Goals"],
    aggfunc=np.sum,
)
# %%
df_full['Positive Goal Balance'] = df_full['+/-'] >= 0
pivot = df_full.pivot_table(
    index=["Team"],
    columns=["Position", "Positive Goal Balance"],
    values=["Goals"],
    aggfunc=[np.sum],
    margins=True,
    margins_name="Total Goals",
)

pivot.sort_values(by=('sum', 'Goals', 'Total Goals', ''), ascending=False)


# %%
pivot = df_full.pivot_table(
    index=["Team"],
    columns=["Position"],
    values=["Goals"],
    aggfunc=[np.sum],
)
# %%
pivot.to_csv('nhl_stats_18_19.csv')
pivot.to_excel('nhl_stats_18_19.xlsx')

# %%
pivot.loc[
    ['BOS', 'CAR', 'STL', 'SJS']
].plot(
    kind='bar'
).legend(
    bbox_to_anchor=(1.6, 1)
)

# %%
