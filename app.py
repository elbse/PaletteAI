Text cell <view-in-github>
# %% [markdown]
<a href="https://colab.research.google.com/github/elbse/PaletteAI/blob/main/PaletteAI.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

Code cell <J8nyD9yqKwgA>
# %% [code]
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
    # Read the uploaded image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Resize for faster processing
    resized = cv2.resize(image, (300, 300))
    pixels = resized.reshape(-1, 3)

    # Run KMeans clustering
    kmeans = KMeans(n_clusters=num_colors, random_state=42, n_init=10)
    kmeans.fit(pixels)
    colors = np.array(kmeans.cluster_centers_, dtype='uint8')

    # Display uploaded image
    st.image(image, caption="📸 Uploaded Image", use_column_width=True)

    # Plot color palette
    st.subheader("🎨 Extracted Color Palette")
    fig, ax = plt.subplots(figsize=(8, 2))
    for i, color in enumerate(colors):
        plt.fill_between([i, i+1], 0, 1, color=color/255)
    plt.xlim(0, num_colors)
    plt.axis("off")
    st.pyplot(fig)

    # Display RGB + HEX values
    st.subheader("🧾 Color Details")
    hex_colors = ['#%02x%02x%02x' % tuple(c) for c in colors]
    for i, color in enumerate(colors):
        rgb_str = f"RGB: {tuple(color)}"
        hex_str = f"HEX: {hex_colors[i]}"
        st.markdown(
            f"<div style='display:flex;align-items:center;'>"
            f"<div style='width:25px;height:25px;background-color:{hex_colors[i]};border-radius:4px;margin-right:10px;'></div>"
            f"<span>{rgb_str} | {hex_str}</span></div>",
            unsafe_allow_html=True,
        )

    # Prepare text file for download
    color_data = "\n".join([f"{i+1}. RGB: {tuple(c)} | HEX: {h}" for i, (c, h) in enumerate(zip(colors, hex_colors))])
    download = io.BytesIO(color_data.encode())
    st.download_button("💾 Download Palette as TXT", data=download, file_name="color_palette.txt", mime="text/plain")

else:
    st.info("⬆️ Upload an image to get started.")



Execution output
2KB
	Stream
		Requirement already satisfied: opencv-python in /usr/local/lib/python3.12/dist-packages (4.12.0.88)
		Requirement already satisfied: scikit-learn in /usr/local/lib/python3.12/dist-packages (1.6.1)
		Requirement already satisfied: matplotlib in /usr/local/lib/python3.12/dist-packages (3.10.0)
		Requirement already satisfied: numpy<2.3.0,>=2 in /usr/local/lib/python3.12/dist-packages (from opencv-python) (2.0.2)
		Requirement already satisfied: scipy>=1.6.0 in /usr/local/lib/python3.12/dist-packages (from scikit-learn) (1.16.2)
		Requirement already satisfied: joblib>=1.2.0 in /usr/local/lib/python3.12/dist-packages (from scikit-learn) (1.5.2)
		Requirement already satisfied: threadpoolctl>=3.1.0 in /usr/local/lib/python3.12/dist-packages (from scikit-learn) (3.6.0)
		Requirement already satisfied: contourpy>=1.0.1 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (1.3.3)
		Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (0.12.1)
		Requirement already satisfied: fonttools>=4.22.0 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (4.60.1)
		Requirement already satisfied: kiwisolver>=1.3.1 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (1.4.9)
		Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (25.0)
		Requirement already satisfied: pillow>=8 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (11.3.0)
		Requirement already satisfied: pyparsing>=2.3.1 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (3.2.5)
		Requirement already satisfied: python-dateutil>=2.7 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (2.9.0.post0)
		Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.12/dist-packages (from python-dateutil>=2.7->matplotlib) (1.17.0)

Code cell <2VRNaYzpMBjJ>
# %% [code]
!git clone https://github.com/elbse/PalleteAI.git
%cd PalleteAI
Execution output
0KB
	Stream
		Cloning into 'PalleteAI'...
		warning: You appear to have cloned an empty repository.
		/content/PalleteAI

Code cell <4kbPLV5SNMRP>
# %% [code]
!ls


Execution output
0KB
	Stream
		sample_data

Code cell <PoIQP8ssN0Cs>
# %% [code]
from google.colab import drive
drive.mount('/content/drive')


Execution output
0KB
	Stream
		Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount("/content/drive", force_remount=True).

Code cell <vlrZ0ijjcTyO>
# %% [code]
!ls /content/drive/MyDrive/Colab\ Notebooks/

Execution output
0KB
	Stream
		'bitcoin_sentiment_analysis (1).ipynb'	 PaletteAI.ipynb
		 bitcoin_sentiment_analysis.ipynb	 PalleteAI.txt
		'Copy of PaletteAI.ipynb'		'Rock vs Mine Prediction.ipynb'
		'Movie Recommendation System.ipynb'

Code cell <koVjfvrxQhC4>
# %% [code]
!jupyter nbconvert --to script "/content/drive/MyDrive/Colab Notebooks/PaletteAI.ipynb"



Execution output
0KB
	Stream
		[NbConvertApp] Converting notebook /content/drive/MyDrive/Colab Notebooks/PaletteAI.ipynb to script
		[NbConvertApp] Writing 2845 bytes to /content/drive/MyDrive/Colab Notebooks/PaletteAI.txt

Code cell <MHE7RDYhQmjj>
# %% [code]
!mv "/content/drive/MyDrive/Colab Notebooks/PaletteAI.ipynb" app.py


Code cell <5jcWgZNUdqlq>
# %% [code]



