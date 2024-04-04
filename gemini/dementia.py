import joblib
import numpy as np
from PIL import Image

# Load the trained SVM model
clf = joblib.load('svm_model.pkl')

# Preprocess the MRI Image
def run(image_path):
    img = Image.open(image_path).convert('L')  # Convert to grayscale
    img = img.resize((256, 256))
    img_array = np.array(img).reshape(1, -1)  # Flatten the image to a 1D array


    # Path to the MRI image you want to classify  # Replace 'path_to_new_mri_image.jpg' with the actual path to your MRI image
    # Preprocess the new MRI image
    new_mri_array = img_array
    # print(new_mri_array.shape)

    # Predict the class label using the trained SVM model
    predicted_class = clf.predict(new_mri_array)

    # Map the predicted class label to the corresponding diagnosis
    diagnosis_mapping = {0: 'Non-Dementia', 1: 'Very Mild Dementia', 2: 'Mild Dementia', 3: 'Moderate Dementia'}
    predicted_diagnosis = diagnosis_mapping[predicted_class[0]]
    # print(predicted_diagnosis)
    return predicted_diagnosis

