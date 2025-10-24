import streamlit as st
import numpy as np
import cv2
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import io

# Streamlit app settings
st.set_page_config(page_title="🎨 AI Color Palette Generator", page_icon="🎨", layout="centered")

st.title("🎨 AI Color Palette Generator")
st.write("Upload an image and extract its dominant colors using KMeans clustering.")

# Sidebar controls
st.sidebar.header("Settings")
num_colors = st.sidebar.slider("Number of colors", min_value=3, max_value=10, value=5)
st.sidebar.info("Move the slider to choose how many dominant colors you want.")

# File uploader
uploaded_file = st.file_uploader("📤 Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        # Read the uploaded image
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Resize for faster processing
        resized = cv2.resize(image, (300, 300))
        pixels = resized.reshape(-1, 3)

        # Run KMeans clustering
        with st.spinner('Extracting colors...'):
            kmeans = KMeans(n_clusters=num_colors, random_state=42, n_init=10)
            kmeans.fit(pixels)
            colors = np.array(kmeans.cluster_centers_, dtype='uint8')

        # Display uploaded image
        st.image(image, caption="📸 Uploaded Image", use_container_width=True)

        # Plot color palette
        st.subheader("🎨 Extracted Color Palette")
        fig, ax = plt.subplots(figsize=(8, 2))
        for i, color in enumerate(colors):
            plt.fill_between([i, i+1], 0, 1, color=color/255)
        plt.xlim(0, num_colors)
        plt.axis("off")
        st.pyplot(fig)
        plt.close(fig)  # Close figure to free memory

        # Display RGB + HEX values
        st.subheader("🧾 Color Details")
        hex_colors = ['#%02x%02x%02x' % tuple(c) for c in colors]
        for i, color in enumerate(colors):
            rgb_str = f"RGB: {tuple(color)}"
            hex_str = f"HEX: {hex_colors[i]}"
            st.markdown(
                f"<div style='display:flex;align-items:center;margin-bottom:8px;'>"
                f"<div style='width:30px;height:30px;background-color:{hex_colors[i]};border-radius:4px;margin-right:12px;border:1px solid #ddd;'></div>"
                f"<span>{rgb_str} | {hex_str}</span></div>",
                unsafe_allow_html=True,
            )

        # Prepare text file for download
        color_data = "\n".join([f"{i+1}. RGB: {tuple(c)} | HEX: {h}" for i, (c, h) in enumerate(zip(colors, hex_colors))])
        download = io.BytesIO(color_data.encode())
        st.download_button(
            "💾 Download Palette as TXT", 
            data=download, 
            file_name="color_palette.txt", 
            mime="text/plain"
        )

    except Exception as e:
        st.error(f"Error processing image: {str(e)}")
        st.info("Please try uploading a different image.")

else:
    st.info("⬆️ Upload an image to get started.")
    
    # Show example/instructions
    st.markdown("""
    ### How to use:
    1. Upload a JPG, JPEG, or PNG image using the uploader above
    2. Adjust the number of colors using the slider in the sidebar
    3. View the extracted color palette and download the results
    
    ### What this app does:
    - Uses KMeans clustering to find dominant colors in your image
    - Extracts RGB and HEX color codes
    - Allows you to download the color palette as a text file
    """)