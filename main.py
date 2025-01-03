import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

secret = st.secrets["MY_SECRET"] # access my secret
st.text(f"my secret is {secret},dont tell anyone")
# Load dataset
df = sns.load_dataset('penguins').dropna()
df = df.dropna()
# Title and description
st.title("Interactive Penguins Visualization")
st.markdown("""
Use the radio button below to switch between Seaborn and Plotly plots for visualizing penguin data.
""")

# Radio button for selecting plot type
plot_type = st.radio("Select plot type:", ["Seaborn", "Plotly"])

if plot_type == "Seaborn":
    # Create a Seaborn plot
    fig, ax = plt.subplots()  # Add parentheses to call the function
    sns.scatterplot(data=df, x="flipper_length_mm", y="bill_length_mm", hue="species", ax=ax)
    ax.set_title("Seaborn Scatter Plot")
    ax.set_xlabel("Flipper Length (mm)")
    ax.set_ylabel("Bill Length (mm)")

    # Display the Seaborn plot
    st.pyplot(fig)

elif plot_type == "Plotly":
    # Create a Plotly plot
    fig = px.scatter(df, x="flipper_length_mm", y="bill_length_mm", color="species",
                     title="Plotly Scatter Plot", labels={
            "flipper_length_mm": "Flipper Length (mm)",
            "bill_length_mm": "Bill Length (mm)"
        })

    # Display the Plotly plot
    st.plotly_chart(fig)
   
