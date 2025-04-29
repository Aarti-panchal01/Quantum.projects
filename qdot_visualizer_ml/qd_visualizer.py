import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# Simulate data: QD size (nm) vs emitted wavelength (nm)
# Smaller dots emit higher energy (shorter wavelength)
np.random.seed(0)
sizes = np.linspace(2, 10, 30).reshape(-1, 1)  # QD sizes from 2nm to 10nm
wavelengths = 1240 / (1.5 + 10 / sizes.flatten()) + np.random.normal(0, 5, size=sizes.shape[0])  # dummy bandgap-wavelength relation

# Train polynomial regression model (degree 3)
model = make_pipeline(PolynomialFeatures(degree=3), LinearRegression())
model.fit(sizes, wavelengths)

# Predict for plotting
sizes_test = np.linspace(2, 10, 100).reshape(-1, 1)
predicted_wavelengths = model.predict(sizes_test)

# Plotting
plt.figure(figsize=(8, 5))
plt.scatter(sizes, wavelengths, color='blue', label='Simulated Data')
plt.plot(sizes_test, predicted_wavelengths, color='red', label='ML Model Prediction')
plt.title("Quantum Dot Size vs Emitted Wavelength")
plt.xlabel("QD Size (nm)")
plt.ylabel("Emitted Wavelength (nm)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("QD_size_vs_wavelength.png")
plt.show()
