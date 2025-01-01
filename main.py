import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

st.markdown("""

# title
# subtitle
-bullet 1
-bullet 2
-bullet 3

> Amazing quote

""")

st.radio("which desert are best ?", ["cake", "icecream", "pie"])
df = sns.load_dataset('penguins')

fig, ax = plt.subplots()  # create new figure, get the axes objects

sns.scatterplot(data=df, x="flipper_length_mm", y="bill_length_mm",
                hue="species")  # use the axes objects to plot on fig

st.pyplot(fig)  # show fig in streamlit
