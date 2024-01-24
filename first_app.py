import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from pydantic import BaseModel
#%%
st.title('My first app')
#creating and showing histogram in streamlit using seaborn
#create subplots

df = pd.read_csv('train.csv')
y = df['income_>50K']
X = df.drop('income_>50K', axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
df_for_sns = pd.concat([X_train,pd.DataFrame(y_train)], axis=1)
fig, ax = plt.subplots(figsize=(20, 14))

sns.violinplot(
    ax=ax,
    data=df_for_sns, hue="income_>50K", x="workclass", split=True,
    scale="count", inner="quartile"
)
plt.legend(fontsize='x-large')
ax.tick_params(axis='both', which='major', labelsize='x-large')
st.pyplot(fig)





#%%
