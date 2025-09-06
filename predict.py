import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

# Define class labels (must match your dataset order)
class_labels = ["Apple", "Banana", "Grapes", "Mango", "Strawberry"]

def predict_image(img_path, model_path="fruit_model.h5", img_size=(128,128)):
    model = load_model(model_path)
    img = image.load_img(img_path, target_size=img_size)
    x = image.img_to_array(img) / 255.0
    x = np.expand_dims(x, axis=0)

    preds = model.predict(x)
    class_idx = np.argmax(preds, axis=1)[0]
    confidence = np.max(preds)
    class_name = class_labels[class_idx]
    return class_name, confidence

