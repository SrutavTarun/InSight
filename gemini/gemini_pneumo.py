import google.generativeai as genai
import PIL.Image
import pneumonia_conversion as pneumo

# img = PIL.Image.open('ytumour.jpg')
genai.configure(api_key='AIzaSyAQVTwJz8HE2A8br7T9FlNnh1YtntR1F-g')

val = 'xray_pic2.jpg'

def run(val):
    img = PIL.Image.open(val)
    x = pneumo.run(val)
    prompt = ''
    for label, prob in x:
        prompt += label + ' ' + str(prob) + ' '
    model=genai.GenerativeModel('gemini-pro-vision')


    response = model.generate_content([f"You are an advanced chest X-RAY radiologist assistant, experienced in observing and analysing a given x-ray scan image.The image contained is diagnosed with {val} where the numbers indicate the probabilty of the disease. Choose an apt threshold for diagnosis and return a short report of the image analysis and how did you detect them (possible signs of disease present). Provide few checkpoints so that radiologists can cross check using them if they ever want to.Dont show any unecessary texts and cautions. ",img ])
    # print(response.text)
    return response.text

