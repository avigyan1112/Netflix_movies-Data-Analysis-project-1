#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[11]:


df_imdb_rating = pd.read_csv('imdb.title.ratings.csv.gz')
df_imdb_rating


# In[14]:


df_movieinfo = pd.read_csv('imdb.title.basics.csv.gz')
df_movieinfo


# In[13]:


df_merge_movieinfo_imdb_rating = pd.merge(df_movieinfo, df_imdb_rating, on = 'tconst')
df_merge_movieinfo_imdb_rating


# In[18]:


df_drama_ratings = df_merge_movieinfo_imdb_rating.loc[df_merge_movieinfo_imdb_rating['genres'] == 'Drama']
df_drama_ratings


# In[19]:


max_drama = df_drama_ratings['averagerating'].max()

print(max_drama)


# In[22]:


df_comedy_ratings = df_merge_movieinfo_imdb_rating.loc[df_merge_movieinfo_imdb_rating['genres'] == 'Comedy']
df_comedy_ratings


# In[23]:


max_comedy = df_comedy_ratings['averagerating'].max()

print(max_comedy)


# In[24]:


df_Biography_ratings = df_merge_movieinfo_imdb_rating.loc[df_merge_movieinfo_imdb_rating['genres'] == 'Biography']
df_Biography_ratings


# In[25]:


max_Biography = df_Biography_ratings['averagerating'].max()

print(max_Biography)


# In[26]:


df_adven_ratings = df_merge_movieinfo_imdb_rating.loc[df_merge_movieinfo_imdb_rating['genres'] == 'Adventure']
df_adven_ratings


# In[27]:


max_adven= df_adven_ratings['averagerating'].max()

print(max_adven)


# In[21]:


max_action = df_merge_movieinfo_imdb_rating['averagerating'].max()

print(max_action)


# In[31]:


import numpy as py
import matplotlib.pyplot as plt 
  
x = [1,2,3,4] 
y = [max_adven, max_drama, max_comedy, max_action] 
labels = ['adven','drama', 'comedy','action']
plt.plot(x, y)
plt.title('imbd_ratings VS Gernes')
plt.xlabel('genres')
plt.ylabel('imbd_ratings')
plt.xticks(x, labels, rotation ='vertical') 
 

plt.show()


# In[30]:


data = [['adven',max_adven], ['drama',max_drama], ['comedy',max_comedy], ['action',max_action]]
df_finalimdb=pd.DataFrame(data, columns=['genres','imbd_ratings'])
df_finalimdb


# In[ ]:




