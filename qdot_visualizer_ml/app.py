import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

st.set_page_config(page_title="Quantum Dot Visualizer", layout="centered")
st.title("🔬 Quantum Dot Behavior Visualizer")
st.write("Explore how quantum dot size affects emitted wavelength using the quantum confinement effect.")

# Sidebar controls
st.sidebar.header("Simulation Controls")
min_size = st.sidebar.slider("Minimum QD Size (nm)", 1.0, 5.0, 2.0, 0.1)
max_size = st.sidebar.slider("Maximum QD Size (nm)", 6.0, 15.0, 10.0, 0.1)
degree = st.sidebar.slider("Polynomial Degree", 1, 5, 3)

if min_size >= max_size:
    st.error("Minimum size must be less than maximum size.")
else:
    # Simulate data
    np.random.seed(0)
    sizes = np.linspace(min_size, max_size, 30).reshape(-1, 1)
    wavelengths = 1240 / (1.5 + 10 / sizes.flatten()) + np.random.normal(0, 5, size=sizes.shape[0])

    # Train model
    model = make_pipeline(PolynomialFeatures(degree=degree), LinearRegression())
    model.fit(sizes, wavelengths)
    sizes_test = np.linspace(min_size, max_size, 200).reshape(-1, 1)
    predicted_wavelengths = model.predict(sizes_test)

    # Plot
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(sizes, wavelengths, color='blue', label='Simulated Data')
    ax.plot(sizes_test, predicted_wavelengths, color='red', label=f'Degree {degree} Prediction')
    ax.set_title("Quantum Dot Size vs Emitted Wavelength")
    ax.set_xlabel("QD Size (nm)")
    ax.set_ylabel("Emitted Wavelength (nm)")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)
