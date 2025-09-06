# 🍎🍌 Fruit Classification with Deep Learning

This project is a **deep learning pipeline** for classifying fruit images using a custom CNN model built with **TensorFlow/Keras**.  
It also includes a **Streamlit web app** that lets you upload a fruit image and get predictions instantly.

---

## 🚀 Features
- Train a CNN model on the [Fruits Classification Dataset](https://www.kaggle.com/datasets/utkarshsaxenadn/fruits-classification/data)  
- Supports **train / valid / test** splits  
- Save and load trained models (`.h5` format)  
- Streamlit app to classify uploaded fruit images  
- Optional bounding box detection (OpenCV workaround)  

---

## 📂 Project Structure

fruit-classification/
│── app.py # Streamlit app for predictions
│── train.py # Train model script
│── predict.py # Prediction utilities
│── data_loader.py # Data loading pipeline
│── model.py # Model architecture
│── requirements.txt # Project dependencies
│── README.md # Project documentation
│── models/ # Saved trained models
│── data/ # Dataset (train / valid / test)



---

## ⚙️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/fruit-classification.git
   cd fruit-classification
Install dependencies:

  bash

pip install -r requirements.txt
▶️ Training the Model
Place the dataset inside the data/ folder:

bash
Sao chép mã
data/
├── train/
├── valid/
└── test/
Run the training script:

bash
Sao chép mã
python train.py
The trained model will be saved at:

bash
Sao chép mã
models/fruit_model.h5
▶️ Running the App
Start the Streamlit app:

bash
Sao chép mã
streamlit run app.py
Upload a fruit image (.jpg, .jpeg, .png).

Get classification results instantly.


Confidence: 92.5%
✨ Future Improvements
Add YOLOv8 object detection for bounding boxes

Improve accuracy with transfer learning (ResNet, EfficientNet, etc.)

Deploy app on Streamlit Cloud / Hugging Face Spaces





---

👉 Do you want me to also generate a **ready-to-use `requirements.txt`** with **TensorFlow, Streamlit, OpenCV,
