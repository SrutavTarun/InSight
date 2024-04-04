import torch
import torchvision.transforms as transforms
from PIL import Image
from torchxrayvision import models

# Load a pre-trained DenseNet model for X-ray analysis
model = models.DenseNet(weights='all')

def run(image_path):
# Define image preprocessing transformations
    transform = transforms.Compose([
        transforms.Resize((224, 224)),  # Resize input image to match model's input size
        transforms.ToTensor(),           # Convert image to PyTorch tensor
        transforms.Normalize(mean=[0.485], std=[0.229])  # Normalize pixel values for single channel
    ])

    # Define the path to your X-ray image
    # image_path = "xray_pic2grey.jpg"

    # Load the X-ray image
    image = Image.open(image_path)

    # Preprocess the image
    input_tensor = transform(image).unsqueeze(0)  # Add batch dimension

    # Set the model to evaluation mode
    model.eval()

    # Make predictions
    with torch.no_grad():
        output = model(input_tensor)

    # Get class probabilities and labels
    class_probs = torch.sigmoid(output[0])
    labels = ['Cardiomegaly', 'Emphysema', 'Effusion', 'Hernia', 'Infiltration', 'Mass',
            'Nodule', 'Atelectasis', 'Pneumothorax', 'Pleural_Thickening', 'Pneumonia',
            'Fibrosis', 'Edema', 'Consolidation']

    # Print predicted labels and probabilities
    results = {}
    for i, label in enumerate(labels):
        results[label] = class_probs[i].item()

    # Sort results by probability in descending order
    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    # Print top predicted classes and their probabilities
    # for label, prob in sorted_results:
    #     print(f"{label}: {prob:.4f}")
    # if(label=='Pneumonia'):
    #   if(prob>=0.64):
    #     print("is pnuemonic")
    #   else:
    #     print("not pnuemonic")
    return sorted_results