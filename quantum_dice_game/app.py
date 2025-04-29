import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random

st.set_page_config(page_title="Quantum-Inspired Dice Game", layout="centered")
st.title("🎲 Quantum-Inspired Dice Game")
st.write("Simulate dice rolls using classical vs quantum-inspired randomness and observe how probability distributions evolve.")

# Number of rolls
num_rolls = st.slider("Number of Rolls", min_value=10, max_value=1000, value=100, step=10)

# Quantum-inspired randomness (pseudo for now)
def quantum_dice_roll():
    # Introduce a small, intentional bias or anomaly for quantum-like effect
    probabilities = [0.15, 0.15, 0.15, 0.15, 0.20, 0.20]  # slightly favoring 5 and 6
    return np.random.choice([1, 2, 3, 4, 5, 6], p=probabilities)

# Classical randomness
def classical_dice_roll():
    return random.randint(1, 6)

# Roll both dice
quantum_results = [quantum_dice_roll() for _ in range(num_rolls)]
classical_results = [classical_dice_roll() for _ in range(num_rolls)]

# Count frequencies
quantum_counts = [quantum_results.count(i) for i in range(1, 7)]
classical_counts = [classical_results.count(i) for i in range(1, 7)]

# Plot
fig, ax = plt.subplots(figsize=(8, 5))
x = np.arange(1, 7)
width = 0.35
ax.bar(x - width/2, classical_counts, width, label='Classical Dice', color='skyblue')
ax.bar(x + width/2, quantum_counts, width, label='Quantum-Inspired Dice', color='salmon')
ax.set_xticks(x)
ax.set_xlabel("Dice Face")
ax.set_ylabel("Frequency")
ax.set_title(f"Outcome Distribution over {num_rolls} Rolls")
ax.legend()
st.pyplot(fig)
