\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{listings}
\usepackage{fontawesome5}
\usepackage{hyperref}
\usepackage{geometry}
\geometry{margin=1in}

\title{\Huge \textbf{\faApple\ \faBanana\ Fruit Classification}}
\author{Nguyễn Vương Trung Hiếu}
\date{}

\begin{document}

\maketitle

\section*{Project Overview}
This project is a complete pipeline for \textbf{Fruit Classification} using deep learning. It includes:

\begin{itemize}
    \item \textbf{Custom CNN model with Keras}
    \item \textbf{Training pipeline (train/valid/test split)}
    \item \textbf{Prediction from single images}
    \item \textbf{Streamlit web app for deployment}
    \item \textbf{(Optional) Bounding box detection with OpenCV}
\end{itemize}

\section*{Project Structure}
\begin{verbatim}
fruit-classification/
│
├── data/                 # Dataset (train/valid/test folders)
│
├── models/
│   └── fruit_model.h5    # Saved trained model
│
├── data_loader.py        # Data loading & preprocessing
├── model.py              # Model architecture
├── train.py              # Train model
├── predict.py            # Predict from image
├── app.py                # Streamlit web app
│
├── requirements.txt
└── README.md
\end{verbatim}

\section*{Installation}
\begin{lstlisting}[language=bash]
# Clone project
git clone https://github.com/Hieu29052005/fruit-classification.git
cd fruit-classification

# Install dependencies
pip install -r requirements.txt
\end{lstlisting}

\section*{Dataset Setup}
Organize dataset in this format:
\begin{verbatim}
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
\end{verbatim}

\section*{Training}
Train the CNN model:
\begin{lstlisting}[language=bash]
python train.py
\end{lstlisting}

The trained model will be saved as:
\begin{verbatim}
models/fruit_model.h5
\end{verbatim}

\section*{Prediction}
Predict from a single image:
\begin{lstlisting}[language=bash]
python predict.py --image path/to/fruit.jpg
\end{lstlisting}

\section*{Web App (Streamlit)}
Run the app:
\begin{lstlisting}[language=bash]
streamlit run app.py
\end{lstlisting}

Upload a fruit image $\rightarrow$ see predicted class and confidence score

(Optional) Bounding boxes drawn using OpenCV

\section*{Requirements}
\begin{itemize}
    \item Python 3.8+
    \item TensorFlow 2.x
    \item Keras
    \item OpenCV
    \item Streamlit
    \item Pillow
    \item NumPy
\end{itemize}

Install all with:
\begin{lstlisting}[language=bash]
pip install -r requirements.txt
\end{lstlisting}

\section*{Deployment}
You can deploy on:
\begin{itemize}
    \item Streamlit Cloud
    \item Hugging Face Spaces
    \item Render
    \item Docker
\end{itemize}

\section*{Author}
Nguyễn Vương Trung Hiếu

\end{document}
