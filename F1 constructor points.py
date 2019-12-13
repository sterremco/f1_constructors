#!/usr/bin/env python
# coding: utf-8

# F1 top 3 constructors 2010 - 2017

# My goal was to analyse the progrese the Mercedes team made during the years to win the 6th championship in 2019. 
# I found three datasets, merged them and filtered it starting from 2010 since the FIA changed the point count from then.
# After that I selected just the 2nd (Ferrari) and 3rd (Red Bull) team to get a good view. 
# 
# This learned me that they came from far since 2010. 
# In 2014 they seem to switch sites with Red Bull who lost a lot since then. 
# In general you can say that Ferrari is the most consitant but it has been a long time ago since they won the constructors tittle. 

# In[239]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'notebook')

df_results = pd.read_csv('constructorResults.csv')
df_races = pd.read_csv('races.csv')
df_constr = pd.read_csv('constructors.csv')

df1 = pd.merge(df_results, df_races, on='raceId')
df = pd.merge(df1, df_constr, on='constructorId')

df_f2010 = df[(df['year'] > 2009)]
#df_f2010

df_index = df_f2010.set_index('year')
#df_index

df_new = df_index.groupby(['year', 'name_y'])['points'].sum().reset_index()

list = ['Ferrari', 'Mercedes', 'Red Bull']
df_top3 = df_new[df_new['name_y'].isin(list)]
#df_top3

ax = sns.lineplot(x='year', y='points', hue='name_y', data=df_top3, legend=False);
ax.set_title('Top 3 constructors annual points F1 2010-2017')
ax.set_ylabel('Annual points')
plt.legend(title='Constructor', loc='lower right', labels=['Ferrari','Mercedes','Red Bull']);


# In[ ]:




