from fastapi import FastAPI, File, UploadFile
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import json
import io

# Load model and class labels once when the server starts
model = load_model("kukusmart_model.h5")

with open("class_labels.json", "r") as f:
    class_labels = json.load(f)

# Create the API
app = FastAPI()

# Home route — confirms API is running
@app.get("/")
def home():
    return {"message": "KukuSmart API is running!"}

# Prediction route — receives an image and returns a prediction
@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    contents = await file.read()
    img = Image.open(io.BytesIO(contents)).convert("RGB")
    img = img.resize((224, 224))  # Change 224 if your model uses a different size

    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    predicted_index = str(np.argmax(predictions))
    predicted_label = class_labels[predicted_index]
    confidence = round(float(np.max(predictions)) * 100, 2)

    return {
        "disease": predicted_label,
        "confidence": f"{confidence}%"
    }