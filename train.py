import os
from data_loader import load_data
from model import build_model

BASE_DIR = os.path.join(os.getcwd(), "data")

train_dir = os.path.join(BASE_DIR, "train")
val_dir   = os.path.join(BASE_DIR, "valid")
test_dir  = os.path.join(BASE_DIR, "test")

train_data, val_data, test_data = load_data(train_dir, val_dir, test_dir)

model = build_model(num_classes=train_data.num_classes)

history = model.fit(
    train_data,
    validation_data=val_data,
    epochs=10
)

model.save("fruit_model.h5")
