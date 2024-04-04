import cv2
import pneumonia

def run(image_path):
# image_path = 'xray_pic2.jpg'
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("xray_picgrey.jpg",image)
    sorted_results = pneumonia.run("xray_picgrey.jpg")
    return sorted_results
