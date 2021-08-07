
# coding: utf-8

# In[35]:


import os
from pathlib import Path
import csv
import pandas as pd
import numpy as np


# In[36]:


file = "Resources/budget_data.csv"
bank_df = pd.read_csv(file)
bank_df.head()


# In[37]:


# The total number of months included in the dataset
month = len(bank_df["Date"].unique())
month


# In[38]:


# The net total amount of "Profit/Losses" over the entire period
total = bank_df["Profit/Losses"].sum()
print("$",format(total,","))


# In[39]:


# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
bank_df['change'] = bank_df['Profit/Losses'].shift(-1) - bank_df['Profit/Losses']
ave = format(bank_df["change"].mean(),",.2f")
ave


# In[40]:


# The greatest increase in profits (date and amount) over the entire period
bank_max = bank_df[bank_df["change"] == bank_df["change"].max()]
bank_max


# In[41]:


# The greatest decrease in profits (date and amount) over the entire period
bank_min = bank_df[bank_df["change"] == bank_df["change"].min()]
bank_min


# In[63]:


# print
print("Financial Analysis\n-----------------------------\nTotal Months:" + str(month) +"\nTotal: $ "+ str(total)+"\nAverage Change: $" + str(ave) + "\nGreatest Increase in Porfits:\n" + str(bank_max) + "\nGreatest Decrease in Porfits:\n" + str(bank_min))

