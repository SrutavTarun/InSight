import joblib
import numpy as np
from PIL import Image

# Load the trained SVM model
clf = joblib.load('svm_model.pkl')

# Preprocess the MRI Image
def preprocess_mri(image_path):
    img = Image.open(image_path).convert('L')  # Convert to grayscale
    img = img.resize((256, 256))
    img_array = np.array(img).reshape(1, -1)  # Flatten the image to a 1D array
    return img_array


# Path to the MRI image you want to classify
new_mri_path = '../images/alzheimers.png'  # Replace 'path_to_new_mri_image.jpg' with the actual path to your MRI image
# Preprocess the new MRI image
new_mri_array = preprocess_mri(new_mri_path)
print(new_mri_array.shape)

# Predict the class label using the trained SVM model
predicted_class = clf.predict(new_mri_array)

# Map the predicted class label to the corresponding diagnosis
diagnosis_mapping = {0: 'Non-Demented', 1: 'Very Mild Demented', 2: 'Mild Demented', 3: 'Moderate Demented'}
predicted_diagnosis = diagnosis_mapping[predicted_class[0]]

print('Predicted Diagnosis:', predicted_diagnosis)
