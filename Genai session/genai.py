
# Gen ai session 


import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Set page config for a better layout
st.set_page_config(page_title="Beautiful Sine Wave Generator", layout="wide")

# Sidebar inputs
st.sidebar.header("Sine Wave Parameters")
frequency = st.sidebar.slider("Frequency", 1, 10, 5)
amplitude = st.sidebar.slider("Amplitude", 0.1, 5.0, 1.0)
phase_shift = st.sidebar.slider("Phase Shift", 0.0, 2 * np.pi, 0.0)
x_limit = st.sidebar.slider("X-axis limit", 0, 10, 5)

# Main title and description
st.title("Beautiful Sine Wave Generator")
st.markdown(
    """
    This app generates a sine wave based on user-defined parameters.
    Use the sliders in the sidebar to adjust the frequency, amplitude, and phase shift of the sine wave.
    """
)

# Generate sine wave data
x = np.linspace(0, x_limit, 1000)
y = amplitude * np.sin(frequency * x + phase_shift)

# Plotting
fig, ax = plt.subplots()
ax.plot(x, y, color='magenta', linewidth=2)
ax.set_title('Sine Wave', fontsize=20)
ax.set_xlabel('X', fontsize=15)
ax.set_ylabel('Y', fontsize=15)
ax.grid(True)

# Display the plot
st.pyplot(fig)

# Additional Information
st.markdown(
    """
    ### How it works
    - **Frequency:** Controls the number of oscillations per unit of x.
    - **Amplitude:** Controls the height of the oscillations.
    - **Phase Shift:** Controls the horizontal shift of the sine wave.
    - **X-axis limit:** Adjusts the range of x values shown.
    """
)

# Footer
st.markdown(
    """
    ---
    **Streamlit App by Your Name** | [GitHub](https://github.com/yourusername)
    """
)
