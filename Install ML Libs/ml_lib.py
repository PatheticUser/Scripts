import os

# Update pip
os.system("python -m pip install --upgrade pip")

# List of essential ML/AI libraries
libraries = [
    "numpy",
    "pandas",
    "matplotlib",
    "seaborn",
    "scikit-learn",
    "tensorflow",
    "jupyter"
]

# Install each library
for lib in libraries:
    os.system(f"pip install {lib}")

print("\n✅ ML/AI libraries installed successfully!")
