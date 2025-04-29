# Quantum.projects

A bunch of small quantum projects I’ve been working on—just for fun and learning. Most are beginner-friendly and use Python, Qiskit, and Streamlit. Nothing too fancy, just cool experiments to explore quantum concepts in an easy way.

# 🧩 What's Inside

🔐 QDotCrypt_Encryptor
A basic encryptor inspired by quantum ideas. More classical than quantum, but a nice starting point.

🎯 QDot_Visualizer_ML
Visual tool that shows how qubits behave. It mixes in some machine learning to make the visuals smarter.

🎲 Quantum_Dice_Game
A dice game that uses quantum randomness (real QRNG!) instead of regular randomness. Surprisingly fun.

🤝 Quantum_Prisoners_Dilemma
Classic game theory—now with a quantum twist. You can simulate how two players might behave with random (or quantum) strategies.

📈 Quantum_Stock_Simulator
Stock prices, but with a bit of quantum chaos. Not real predictions, just for experimenting.


# 💻 How to Run
1. Clone it
git clone https://github.com/Aarti-panchal01/Quantum.projects.git
cd Quantum.projects

2. Create a virtual environment
python -m venv quantum_env
# On Windows
.\quantum_env\Scripts\activate
# On Mac/Linux
source quantum_env/bin/activate

3. Install project dependencies
Each folder has its own requirements.txt. Example:
cd quantum_dice_game
pip install -r requirements.txt

4. Run the project
streamlit run app.py



# 📝 Note
These are all experimental projects, I thought these woild be great for learning and trying out ideas.
These work best with Qiskit 1.0+, but some fall back to simulations as i was not on a quantum backend.
Streamlit makes it easy to use, even without coding much.

Made with ❤️ by @Aarti Panchal  — powered by Python, Qiskit, and Streamlit
