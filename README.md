# 🎨 AI Color Palette Generator

An intelligent color palette extraction tool powered by KMeans clustering and built with Streamlit. Upload any image and instantly extract its dominant colors with RGB and HEX values.

## 🚀 Live Demo

**[Try it now!](https://paletteai-ng9dsyb46wzm5hhkwazhks.streamlit.app/)**

## ✨ Features

- 🖼️ Upload images in JPG, JPEG, or PNG format
- 🎯 Extract 3-10 dominant colors using KMeans clustering
- 🎨 Visual color palette display
- 📊 RGB and HEX color codes for each extracted color
- 💾 Download color palette as a text file
- ⚡ Fast processing with optimized image resizing
- 📱 Responsive design that works on all devices

## 🛠️ Technologies Used

- **Streamlit** - Web application framework
- **OpenCV** - Image processing
- **scikit-learn** - KMeans clustering algorithm
- **NumPy** - Numerical computations
- **Matplotlib** - Color palette visualization

## 📦 Installation

### Local Setup

1. Clone the repository:
```bash
git clone https://github.com/elbse/PaletteAI.git
cd PaletteAI
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the app:
```bash
streamlit run app.py
```

5. Open your browser and navigate to `http://localhost:8501`

## 📋 Requirements

```
streamlit>=1.28.0
numpy>=1.24.0
opencv-python-headless>=4.8.0
scikit-learn>=1.3.0
matplotlib>=3.7.0
```

## 🎯 How to Use

1. **Upload an Image**: Click on the upload button and select an image file (JPG, JPEG, or PNG)
2. **Adjust Colors**: Use the sidebar slider to choose how many dominant colors you want to extract (3-10)
3. **View Results**: See the extracted color palette with RGB and HEX values
4. **Download**: Click the download button to save your color palette as a text file

## 🧠 How It Works

The app uses KMeans clustering algorithm to analyze the pixels in your image:

1. The uploaded image is resized to 300x300 pixels for faster processing
2. All pixels are converted into a feature space of RGB values
3. KMeans clustering groups similar colors together
4. The cluster centers represent the dominant colors
5. Results are displayed with visual swatches and color codes

## 🎨 Use Cases

- **Web Design**: Extract color schemes from inspiration images
- **Brand Identity**: Analyze competitor or reference brand colors
- **Art & Design**: Get color palettes from photographs and artwork
- **UI/UX Design**: Generate consistent color schemes for applications
- **Digital Marketing**: Extract colors from images for campaign consistency

## 📸 Screenshots

### Main Interface
<img width="1919" height="909" alt="Image" src="https://github.com/user-attachments/assets/3116c617-0305-47f2-8a97-500002c6c0fb" />

### Color Palette Display
<img width="824" height="585" alt="Image" src="https://github.com/user-attachments/assets/783813d5-11cd-4622-8cf6-0911b71cb3f2" />

### Download Feature
<img width="234" height="53" alt="Image" src="https://github.com/user-attachments/assets/c7c427d9-47ae-446d-a5da-ab0e9d7e6371" />

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## 🐛 Issues

Found a bug or have a feature request? Please open an issue on the [GitHub repository](https://github.com/elbse/PalleteAI/issues).

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**elbse**

- GitHub: [@elbse](https://github.com/elbse)

## 🌟 Show Your Support

Give a ⭐️ if this project helped you!

## 📝 Changelog

### Version 1.0.0
- Initial release
- KMeans color clustering
- RGB and HEX color extraction
- Download functionality
- Responsive UI

---

**Made with ❤️ using Streamlit**
