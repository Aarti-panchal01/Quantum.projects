import streamlit as st
import numpy as np
import requests
import matplotlib.pyplot as plt

st.set_page_config(page_title="Quantum Prisoner's Dilemma Online", layout="centered")
st.title("🌐 Quantum Prisoner's Dilemma: Multiplayer + QRNG")

st.markdown("""
This version supports:
- Simultaneous strategy input for Player A and B
- Real **Quantum Random Numbers** (QRNG API)
- Superposition outcomes using quantum randomness

### Choose Strategy:
- **Cooperate (C)**
- **Defect (D)**
- **Quantum (Q)** — outcome depends on true QRNG
""")

st.sidebar.header("Player Inputs")
player_A = st.sidebar.selectbox("Player A", ["Cooperate", "Defect", "Quantum"])
player_B = st.sidebar.selectbox("Player B", ["Cooperate", "Defect", "Quantum"])

# Classic payoff matrix
payoffs = {
    ("C", "C"): (3, 3),
    ("C", "D"): (0, 5),
    ("D", "C"): (5, 0),
    ("D", "D"): (1, 1)
}

# Get a quantum random number (0 or 1) using ANU QRNG API
def get_qrng_bit():
    try:
        r = requests.get("https://qrng.anu.edu.au/API/jsonI.php?length=1&type=uint8")
        bit = int(r.json()["data"][0]) % 2
        return bit
    except:
        # fallback to pseudo-random
        return np.random.randint(0, 2)

# Determine strategy based on QRNG for "Quantum"
def resolve_strategy(choice):
    if choice == "Quantum":
        return "C" if get_qrng_bit() == 0 else "D"
    return choice[0]  # Cooperate or Defect

resolved_A = resolve_strategy(player_A)
resolved_B = resolve_strategy(player_B)

payoff_result = payoffs[(resolved_A, resolved_B)]

st.subheader("🧠 Strategy Resolution")
st.write(f"**Player A Actual Strategy:** `{resolved_A}`")
st.write(f"**Player B Actual Strategy:** `{resolved_B}`")
st.success(f"Payoffs → Player A: `{payoff_result[0]}`, Player B: `{payoff_result[1]}`")

if st.checkbox("Show Strategy Matrix (Classical Only)"):
    strategies = ["C", "D"]
    matrix = np.zeros((2, 2, 2))
    for i, sa in enumerate(strategies):
        for j, sb in enumerate(strategies):
            matrix[i, j, :] = payoffs[(sa, sb)]
    fig, ax = plt.subplots(figsize=(5, 4))
    cax = ax.matshow(matrix[:, :, 0], cmap="Blues")
    ax.set_xticks(range(2))
    ax.set_yticks(range(2))
    ax.set_xticklabels(strategies)
    ax.set_yticklabels(strategies)
    for i in range(2):
        for j in range(2):
            ax.text(j, i, f"{matrix[i,j,0]:.1f}/{matrix[i,j,1]:.1f}", va='center', ha='center')
    st.pyplot(fig)

st.caption("QRNG API from Australian National University (ANU) used for quantum randomness.")
