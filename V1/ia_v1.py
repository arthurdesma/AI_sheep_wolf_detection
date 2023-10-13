import numpy as np
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import cv2
import os

#Load the pre-trained VGG16 model
model = VGG16(weights='imagenet')

# Function to classify the image the real
def classify_image(image_path):
    # Load and preprocess the image
    img = image.load_img(image_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    # Use VGG16 model to classify the image
    preds = model.predict(x)

    # Decode the predictions
    decoded_preds = decode_predictions(preds, top=3)[0]

    # Check if any of the predicted labels match the desired animals
    for _, animal, probability in decoded_preds:
        if animal in ['coyote', 'timber_wolf', 'white_wolf', 'red_wolf','Irish_wolfhound']:
            return True, probability

    return False, None

# Path to the folder containing the images
folder_path = 'V1\image'

# Looking all files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is an image
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        # Complete path of the image
        image_path = os.path.join(folder_path, filename)

        # Classify the image
        result, probability = classify_image(image_path)
        print(f"{filename}: {result}, Probability: {probability}")
        # Effacer l'image après l'avoir analysée
        #os.remove(image_path)