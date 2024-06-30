import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(size=1000)
data = pd.DataFrame(data, columns=['dist_norm'])
st.write(data)

fig, plt = plt.subplots()
plt.hist(data)
st.pyplot(fig)