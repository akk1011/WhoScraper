#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from selenium import webdriver
import whoscrape


# In[2]:


league_urls = whoscrape.getLeagueUrls()
league_urls


# In[27]:


match_urls = whoscrape.getMatchUrls(comp_urls=league_urls, competition='Premier League', season='2021/2022')


# In[28]:


team_urls =whoscrape.getTeamUrls(team='Manchester City', match_urls=match_urls)
matches_data = whoscrape.getMatchesData(match_urls=team_urls)


# In[29]:


df= matches_data


# In[30]:


events_ls = [whoscrape.createEventsDF(match) for match in matches_data]
# Add EPV column
events_list = [whoscrape.addEpvToDataFrame(match) for match in events_ls]
events_dfs = pd.concat(events_list)
events_dfs.head()


# In[31]:


#Converting to CSV
events_dfs.to_csv('Mancity2122.csv')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




