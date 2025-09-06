import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image

# Load model
model = load_model("fruit_model.h5")
class_labels = ["Apple", "Banana", "Grapes", "Mango", "Strawberry"]

def detect_fruit(image_file, img_size=(128,128)):
    # Read file with PIL and convert to OpenCV format
    img = Image.open(image_file).convert("RGB")
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    output = img.copy()

    # Convert to HSV for color segmentation
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (0, 40, 40), (179, 255, 255))

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if w*h < 500:  # skip very small detections
            continue

        # Crop ROI
        roi = img[y:y+h, x:x+w]
        roi_resized = cv2.resize(roi, img_size) / 255.0
        roi_array = np.expand_dims(img_to_array(roi_resized), axis=0)

        preds = model.predict(roi_array)
        class_idx = np.argmax(preds, axis=1)[0]
        label = class_labels[class_idx]
        confidence = np.max(preds)

        # Draw bounding box + label
        cv2.rectangle(output, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(output, f"{label} {confidence:.2f}", (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Convert back to RGB for Streamlit
    output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
    return output
