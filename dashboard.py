import os
os.system('pip install matplotlib')
os.system('pip install seaborn')
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib.colors import ListedColormap

df = pd.read_csv("dataset_2.csv")

bot_rock_win_count = df.apply(lambda row: row["Bot Pick"] == "ROCK" and row["Bot Result"] == "Win", axis=1).sum()
bot_paper_win_count = df.apply(lambda row: row["Bot Pick"] == "PAPER" and row["Bot Result"] == "Win", axis=1).sum()
bot_scissors_win_count = df.apply(lambda row: row["Bot Pick"] == "SCISSORS" and row["Bot Result"] == "Win", axis=1).sum()
computer_rock_win_count = df.apply(lambda row: row["Computer Pick"] == "ROCK" and row["Computer Result"] == "Win", axis=1).sum()
computer_paper_win_count = df.apply(lambda row: row["Computer Pick"] == "PAPER" and row["Computer Result"] == "Win", axis=1).sum()
computer_scissors_win_count = df.apply(lambda row: row["Computer Pick"] == "SCISSORS" and row["Computer Result"] == "Win", axis=1).sum()
computer_rock_loss_count = df.apply(lambda row: row["Computer Pick"] == "ROCK" and row["Computer Result"] == "Loss", axis=1).sum()
computer_paper_loss_count = df.apply(lambda row: row["Computer Pick"] == "PAPER" and row["Computer Result"] == "Loss", axis=1).sum()
computer_scissors_loss_count = df.apply(lambda row: row["Computer Pick"] == "SCISSORS" and row["Computer Result"] == "Loss", axis=1).sum()
bot_rock_loss_count = df.apply(lambda row: row["Bot Pick"] == "ROCK" and row["Bot Result"] == "Loss", axis=1).sum()
bot_paper_loss_count = df.apply(lambda row: row["Bot Pick"] == "PAPER" and row["Bot Result"] == "Loss", axis=1).sum()
bot_scissors_loss_count = df.apply(lambda row: row["Bot Pick"] == "SCISSORS" and row["Bot Result"] == "Loss", axis=1).sum()
bot_total_win_count = bot_paper_win_count + bot_rock_win_count + bot_scissors_win_count
computer_total_win_count = computer_paper_win_count + computer_rock_win_count + computer_scissors_win_count
bot_total_loss_count = bot_paper_loss_count + bot_rock_loss_count + bot_scissors_loss_count
computer_total_loss_count = computer_paper_loss_count + computer_rock_loss_count + computer_scissors_loss_count
bot_total_tie_count = 1000 - (bot_total_win_count + bot_total_loss_count)
computer_total_tie_count = 1000 - (computer_total_loss_count + computer_total_win_count)


st.title("Data Analysis Dashboard")

# Add a description
st.write("""
This dashboard provides a visual representation of the differences between the approach of Javascript's random function and that of Python using a fun game.
""")

data = {
    "Player": ["Bot (Python)", "Computer (JavaScript)"],
    "Wins": [bot_total_win_count, computer_total_win_count],
    "Losses": [bot_total_loss_count, computer_total_loss_count],
    "Draws": [bot_total_tie_count, computer_total_tie_count]
}

winning_sequence = {
    "1st Time": df["Bot Pick"].iloc[131:136].tolist(),  # Convert to list
    "2nd Time": df["Bot Pick"].iloc[593:598].tolist()   # Convert to list
}

comp_winning_sequence = {
    "1st Time": df["Computer Pick"].iloc[117:121].tolist(),  # Convert to list
    "2nd Time": df["Computer Pick"].iloc[197:201].tolist(),   # Convert to list
    "3rd Time": df["Computer Pick"].iloc[299:303].tolist(),  # Convert to list
    "4th Time": df["Computer Pick"].iloc[306:310].tolist()   # Convert to list
}

table = pd.DataFrame(data)
bot_winning_sequence = pd.DataFrame(winning_sequence)
computer_winning_sequence = pd.DataFrame(comp_winning_sequence)

st.header("Game Results Table")
st.table(table)

col1, col2 = st.columns([1, 2])  # Creates a flex-like layout
col3, col4 = st.columns([2, 2])  # Creates a flex-like layout
col5, col6 = st.columns([2, 2])  # Creates a flex-like layout

with col1:
    st.write("Bot 5 moves winning sequence")
    st.table(bot_winning_sequence)

with col2:
    st.write("Computer 4 moves winning sequence")
    st.table(computer_winning_sequence)

# Bot Weapons Grouped Bar Chart
# Data
categories = ["Rock", "Paper", "Scissors"]
weapon_win = [bot_rock_win_count, bot_paper_win_count, bot_scissors_win_count]
weapon_loss = [bot_rock_loss_count, bot_paper_loss_count, bot_scissors_loss_count]

x = np.arange(len(categories))  # X-axis positions for bars
width = 0.4  # Width of bars

with col3:
    st.subheader("Grouped Bar Chart - Bot Weapons")
    # Create the figure before plotting
    fig, ax = plt.subplots(figsize=(8, 5))  

    # Create grouped bars
    ax.bar(x - width/2, weapon_win, width=width, label="Bot Weapon Win", color="#FF4B4B")
    ax.bar(x + width/2, weapon_loss, width=width, label="Bot Weapon Loss", color="#31333F")

    # Labels and title
    ax.set_xlabel("Move")
    ax.set_ylabel("Result Count")
    ax.set_title("Bot Weapon Comparison: Win vs Loss")
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.set_yticks(np.arange(0, max(weapon_win + weapon_loss) + 5, 5))  # Adjusted spacing
    ax.legend()

    # Display the plot in Streamlit
    st.pyplot(fig)


# Computer Weapons Grouped Bar Chart
# Data
categories = ["Rock", "Paper", "Scissors"]
weapon_win = [computer_rock_win_count, computer_paper_win_count, computer_scissors_win_count]
weapon_loss = [computer_rock_loss_count, computer_paper_loss_count, computer_scissors_loss_count]

x = np.arange(len(categories))  # X-axis positions for bars
width = 0.4  # Width of bars

with col4: 
    st.subheader("Grouped Bar Chart - Computer Weapons")

    # Create figure and axis before plotting
    fig, ax = plt.subplots(figsize=(8, 5))

    # Create grouped bars
    ax.bar(x - width/2, weapon_win, width=width, label="Computer Weapon Win", color="#FF4B4B")
    ax.bar(x + width/2, weapon_loss, width=width, label="Computer Weapon Loss", color="#31333F")

    # Labels and title
    ax.set_xlabel("Move")
    ax.set_ylabel("Result Count")
    ax.set_title("Computer Weapon Comparison: Win vs Loss")
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.set_yticks(np.arange(0, max(weapon_win + weapon_loss) + 5, 5))  # Adjusted spacing
    ax.legend()

    # Display the plot in Streamlit
    st.pyplot(fig)

# Heatmap
# Pivot table
df_pivot = df.pivot_table(index="Bot Pick", columns="Computer Pick", aggfunc="size", fill_value=0)

# Create heatmap figure
fig, ax = plt.subplots(figsize=(6, 5))

# Define custom colors transitioning between red and dark gray
custom_colors = ["#FF4B4B", "#D43F3F", "#A83232", "#7D2626", "#532020", "#31333F"]

# Convert to colormap
custom_cmap = ListedColormap(custom_colors)

sns.heatmap(df_pivot, annot=True, cmap=custom_cmap, linewidths=0.5, fmt=",.0f", ax=ax)  # Use 'ax' to avoid extra figures

# Labels and title
ax.set_title("Opponent Response Heatmap")
ax.set_xlabel("Computer Pick")
ax.set_ylabel("Bot Pick")

# Display in Streamlit
st.pyplot(fig)

wins = [bot_paper_win_count, bot_rock_win_count, bot_scissors_win_count, computer_paper_win_count, computer_rock_win_count, computer_scissors_win_count]
losses = [bot_paper_loss_count, bot_scissors_loss_count, bot_rock_loss_count, computer_paper_loss_count, computer_rock_loss_count, computer_scissors_loss_count]

with col5:
    st.write("Most Wins - Bot (Paper): ", str(max(wins)))
with col6:
    st.write("Most Losses - Computer (Rock): ", str(max(losses)))
with col5:
    st.write("Least Wins - Computer (Scissors): ", str(min(wins)))
with col6:
    st.write("Least Losses - Bot (paper): ", str(min(losses)))
