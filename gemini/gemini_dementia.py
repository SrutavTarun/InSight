import google.generativeai as genai
import PIL.Image
import gemini.dementia as dementia

img = PIL.Image.open('ytumour.jpg')
genai.configure(api_key='AIzaSyAQVTwJz8HE2A8br7T9FlNnh1YtntR1F-g')
img_path = 'alzheimer_1.jpeg'


def run(img_path):
    img = PIL.Image.open(img_path)
    val = dementia.run(img_path)
    model=genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([f"You are an advanced brain MRI radiologist assistant, experienced in observing and analysing a given MRI or CT scan image.The image contained is diagnosed with {val}. Return a short desciription of the image and how did you detect them (possible signs of disease present). Provide few checkpoints so that radiologists can cross check using them if they ever want to.Dont show any unecessary texts and cautions. ",img ])

    # print(response.text)
    return response.text

run(img_path)