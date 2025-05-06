import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from noise import pnoise2, snoise2

# set the page configuration
st.set_page_config(
    page_title="Interactive Noise Pattern Generator",
    layout="wide",
    initial_sidebar_state="expanded",
)

# sidebar for user inputs
st.sidebar.title("Noise Pattern Controls")

# noise type selection
noise_type = st.sidebar.selectbox(
    "Select Noise Type",
    ["Perlin Noise", "Simplex Noise", "Gaussian Noise"]
)

# pattern complexity
complexity = st.sidebar.slider(
    "Pattern Complexity (Frequency)",
    min_value=1,
    max_value=10,
    value=5
)

# color mapping
color_map = st.sidebar.color_picker(
    "Pick a Color",
    "#00f900"
)

# random seed
seed = st.sidebar.number_input(
    "Random Seed",
    value=42,
    step=1
)

# generate noise pattern based on user inputs
def generate_noise(noise_type, complexity, seed):
    np.random.seed(seed)
    width, height = 512, 512
    scale = complexity * 0.1
    noise = np.zeros((width, height))

    if noise_type == "Perlin Noise":
        for i in range(width):
            for j in range(height):
                noise[i][j] = pnoise2(i * scale, j * scale, octaves=6)
    elif noise_type == "Simplex Noise":
        for i in range(width):
            for j in range(height):
                noise[i][j] = snoise2(i * scale, j * scale, octaves=6)
    elif noise_type == "Gaussian Noise":
        noise = np.random.normal(0, 1, (width, height))

    # normalize to 0-1
    noise = (noise - noise.min()) / (noise.max() - noise.min())
    return noise

# generate and display the noise pattern
noise_pattern = generate_noise(noise_type, complexity, seed)

fig, ax = plt.subplots(figsize=(6, 6))
ax.imshow(noise_pattern, cmap='gray')
ax.axis('off')
st.pyplot(fig)
