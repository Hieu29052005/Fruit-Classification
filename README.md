# Fruit Classification

This project is a complete pipeline for **Fruit Classification** using deep learning. It includes:

- **Custom CNN model with Keras**
- **Training pipeline (train/valid/test split)**
- **Prediction from single images**
- **Streamlit web app for deployment**
- **(Optional) Bounding box detection with OpenCV**

---

## Project Structure
```
fruit-classification/
│
├── data/ # Dataset (train/valid/test folders)
│
├── fruit_model.h5 # Saved trained model
│
├── data_loader.py # Data loading & preprocessing
├── model.py # Model architecture
├── train.py # Train model
├── predict.py # Predict from image
├── app.py # Streamlit web app
│
├── requirements.txt
└── README.md
```


---

## Installation

```bash
# Clone project
git clone https://github.com/Hieu29052005/fruit-classification.git
cd fruit-classification

# Install dependencies
pip install -r requirements.txt
```
* Dataset Setup
  
Organize dataset in this format:

```
data/
├── train/
│   ├── apple/
│   ├── banana/
│   ├── orange/
│   └── ...
├── valid/
│   ├── apple/
│   ├── banana/
│   ├── orange/
│   └── ...
├── test/
    ├── apple/
    ├── banana/
    ├── orange/
    └── ...
```
Training
```bash
python train.py
```
The trained model will be saved as:

```
models/fruit_model.h5
```
Prediction
```bash
python predict.py --image path/to/fruit.jpg
```
Web App (Streamlit)
```bash
streamlit run app.py
```
Upload a fruit image → see predicted class and confidence score
(Optional) Bounding boxes drawn using OpenCV

Requirements
* Python 3.8+

* TensorFlow 2.x

* Keras

* OpenCV

* Streamlit

* Pillow

* NumPy

Install all with:

```bash
pip install -r requirements.txt
```
# Deployment
You can deploy on:

* Streamlit Cloud

* Hugging Face Spaces

* Render

* Docker

# Author

Nguyen Vuong Trung Hieu
