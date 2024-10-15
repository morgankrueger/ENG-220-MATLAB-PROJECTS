# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OqfwDSIm_atJPTMFuTlce86X8Ajfnqfi
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the page title
st.set_page_config(page_title='ENG 220 Class Assignment 5')

# Set the title of the app
st.title('Class Assignment 5')


# Text input for name and degree
name = st.text_input('Enter your name:', 'Your Name')
degree = st.text_input('Enter your degree:', 'Your Degree')

# Display a welcome message after the user inputs their name
if name != 'Your Name':  # Check if the user has entered their name
    st.write(f'Hello {name}, welcome to the class!')

# Display the user's name and degree
st.write(f'**Name:** {name}')
st.write(f'**Degree:** {degree}')

# Create some sample data for the graph
data = pd.DataFrame({
    'x': np.linspace(0, 10, 100),
    'y': np.sin(np.linspace(0, 10, 100))
})

# Display the graph
st.line_chart(data.set_index('x'))