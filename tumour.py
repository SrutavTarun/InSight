import torch
from PIL import ImageFile,Image
import requests
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import warnings
# Suppress deprecation warnings
warnings.filterwarnings("ignore")

# Load model directly
from transformers import AutoImageProcessor, AutoModelForObjectDetection
def predict_tumour(img_path):
    flag=0
    # img_path="ytumour.jpg"
    image_processor = AutoImageProcessor.from_pretrained("DunnBC22/yolos-tiny-Brain_Tumor_Detection")
    model = AutoModelForObjectDetection.from_pretrained("DunnBC22/yolos-tiny-Brain_Tumor_Detection")
    image_gray = Image.open(img_path)
    image = image_gray.convert("RGB")
    image = image.resize((224, 224))



    inputs = image_processor(images=image, return_tensors="pt")
    outputs = model(**inputs)

    # convert outputs (bounding boxes and class logits) to Pascal VOC format (xmin, ymin, xmax, ymax)
    target_sizes = torch.tensor([image.size[::-1]])
    results = image_processor.post_process_object_detection(outputs, threshold=0.9, target_sizes=target_sizes)[0]

    for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
        box = [round(i, 2) for i in box.tolist()]
        if(len(box)!=0):
            return 1
            # print(f"Detected {model.config.id2label[label.item()]} with confidence "f"{round(score.item(), 3)} at location {box}")
    return 0
    
def run(val):
    num = predict_tumour(val)
    return num


