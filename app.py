import sys
from PIL import Image
import numpy as np
import tensorflow as tf
import traceback

# Suppress TensorFlow logs
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Load your trained model
model = tf.keras.models.load_model("vgg19_best (1).keras")
classes = ['Cataract', 'Diabetic_retinopathy', 'Glaucoma', 'Normal']

def preprocess_image(path):
    img = Image.open(path).resize((224, 224))
    arr = np.array(img) / 255.0
    return np.expand_dims(arr, axis=0)

if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            print("No image path provided.")
            sys.exit(1)

        img_path = sys.argv[1]
        img = preprocess_image(img_path)

        # Get the prediction array: shape (4,)
        preds = model.predict(img, verbose=0)[0]

        # Prepare output for the webpage
        output = ""
        for cls, p in zip(classes, preds):
            output += f"{cls}: {p * 100:.2f}%<br>\n"

        # Compute predicted class and confidence
	#output+="<br>\n"
        idx = int(np.argmax(preds))
        best_cls = classes[idx]
        conf = preds[idx] * 100
        output +=f"<b>PREDICTED DISEASE: </b>{best_cls} <br>\n"
        output += f"<b>CONFIDENCE: </b>{conf:.2f}%<br>\n"

        # Add disease status
        if best_cls == 'Normal':
            output += "<b>STATUS: no,</b> disease detected (Normal retina)<br>\n"
        else:
            output += f"<b>STATUS: yes,</b> Disease detected ({best_cls})<br>\n"

        # Print the output so that PHP can capture and display it
        print(output)
    except Exception as e:
        # Catch any exceptions and print them to the console
        print(f"An error occurred: {e}")
        print(traceback.format_exc())


















