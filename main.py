from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware  
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)


model = tf.keras.models.load_model('model_solo_final.keras')
class_names = ['Anorganik', 'B3', 'Organik'] 

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert('RGB').resize((224, 224))
    
    img_array = tf.keras.utils.img_to_array(image)
    img_array = np.expand_dims(img_array, axis=0)
    
    predictions = model.predict(img_array)
    idx = np.argmax(predictions[0])
    label = class_names[idx]
    confidence = float(np.max(predictions[0]))

    descriptions = {
        "Organik": "Sampah sisa makanan/tumbuhan yang mudah terurai alami.",
        "Anorganik": "Sampah plastik, kertas, atau logam yang bisa didaur ulang.",
        "B3": "Sampah beracun (baterai, lampu, kabel) yang butuh penanganan khusus."
    }

    return {
        "prediction": label.upper(),
        "confidence": round(confidence, 2),
        "description": descriptions.get(label, "-")
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
