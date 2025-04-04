import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow import keras
# Load the trained model
model = keras.models.load_model("final_fake_image_checker_model.h5")

# ✅ Load and preprocess a test image
img_path = "real_image3.jpg"

img = image.load_img(img_path, target_size=(224, 224))
img = image.load_img(img_path, target_size=(224, 224))  # Resize to match model input
img_array = image.img_to_array(img)  
img_array = np.expand_dims(img_array, axis=0)  # Expand dimensions for batch format
img_array = img_array / 255.0  # Normalize like training data

# ✅ Make Prediction
prediction = model.predict(img_array)[0][0]

# ✅ Interpret the result
if prediction > 0.5:
    print("🟢 This is a FAKE image.")
else:
    print("🔵 This is a REAL image.")