import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from pydantic import BaseModel
#%%
st.title('My first app')
#%%
name = st.text_input("Enter your name", '')
st.write(f"Hello {name}!")
x = st.slider("Select an integer x", 0, 10, 1)
y = st.slider("Select an integer y", 0, 10, 1)
df = pd.DataFrame({"x": [x], "y": [y] , "x + y": [x + y]}, index = ["addition row"])
st.write(df)#%%

#%%
