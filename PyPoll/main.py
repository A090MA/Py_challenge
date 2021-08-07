
# coding: utf-8

# In[1]:


import os
from pathlib import Path
import csv
import pandas as pd
import numpy as np


# In[2]:


file1 = "Resources/election_data.csv"
poll_df = pd.read_csv(file1)
poll_df.head()


# In[7]:


# The total number of votes cast
len(poll_df['Voter ID'].value_counts())


# In[12]:


# A complete list of candidates who received votes
list(poll_df["Candidate"].unique())


# In[17]:


# The percentage of votes each candidate won
percentage = 100*poll_df["Candidate"].value_counts()/len(poll_df['Voter ID'].value_counts())
percentage


# In[64]:


# The total number of votes each candidate won
total = poll_df["Candidate"].value_counts()
total_df = pd.DataFrame(total)
total_df.rename(columns = {"Candidate": "votes"},  inplace=True)
total_df


# In[65]:


# The winner of the election based on popular vote.

print("""Election Results
------------------
Total Votes:""" + str(len(poll_df['Voter ID'].value_counts())) + 
"""\n------------------
The percentage of votes each candidate won:\n""" + str(percentage) +
"""\n------------------
The total number of votes each candidate won:\n""" + str(total_df)+
"""\n------------------
Winner: Khan
------------------"""
     )

