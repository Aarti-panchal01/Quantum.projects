A collection of beginner-friendly quantum experiments and games built with Python, Qiskit, and Streamlit.

✨ Overview
A bunch of small quantum projects I’ve been working on—just for fun and learning. Most of these are beginner-friendly and use Python, Qiskit, and Streamlit. They’re designed to make quantum concepts more approachable through interactive simulations, games, and visual tools.

🧩 What's Inside
🔐 QDotCrypt_Encryptor
A basic encryptor inspired by quantum principles. It’s more classical than quantum, but introduces the idea of secure encoding in a fun way.

🎯 QDot_Visualizer_ML
An interactive visualizer that shows how qubits behave, with a touch of ML to classify and analyze different states and gates.

🎲 Quantum_Dice_Game
A simple dice game that uses quantum randomness from a real QRNG API instead of pseudo-random numbers—great for exploring the unpredictability of quantum outcomes.

🤝 Quantum_Prisoners_Dilemma
A quantum twist on the classic game theory dilemma. Simulates different player strategies with quantum randomness and visual payoffs.

📈 Quantum_Stock_Simulator
Simulates stock market behavior using quantum-inspired randomness. It’s not for real trading—just a creative way to explore quantum noise and volatility.

💻 How to Run

# Clone the repository
git clone https://github.com/Aarti-panchal01/Quantum.projects.git
cd Quantum.projects

# Create a virtual environment
python -m venv quantum_env

# Activate the environment
# On Windows
.\quantum_env\Scripts\activate
# On Mac/Linux
source quantum_env/bin/activate



Each sub-project has its own requirements.txt. For example:
cd quantum_dice_game
pip install -r requirements.txt
streamlit run app.py


📝 Note
These are educational and experimental tools built for learning. Some projects use Qiskit simulators due to limited access to quantum hardware. Streamlit makes the UI easy to work with—perfect for non-coders too!

Made with ❤️ by @Aarti Panchal
Powered by Python, Qiskit, and Streamlit.
