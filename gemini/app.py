import tumour
import gemini_tumour as geminiTumour
import gemini_dementia as geminiDementia
import gemini_pneumo as geminiPneumo
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


dementia_text = str(geminiDementia.run('../images/alzheimer_1.jpeg'))

tumour_text = str(geminiTumour.run('../images/ytumour.jpg'))

pneumo_text = str(geminiPneumo.run('../images/xray_pic2.jpg'))

def generate_pdf(text, filename):
    # Create a canvas
    c = canvas.Canvas(filename, pagesize=letter)
    
    # Set font and size
    c.setFont("Helvetica", 12)
    
    # Write text to the canvas
    text_lines = text.split("\n")
    y_coordinate = 750  # Starting y-coordinate
    for line in text_lines:
        c.drawString(50, y_coordinate, line)
        y_coordinate -= 20  # Decrease y-coordinate for next line
    
    # Save the canvas to a PDF file
    c.save()

generate_pdf(dementia_text,"dementia_report.pdf")
generate_pdf(tumour_text,"tumour_report.pdf")
generate_pdf(pneumo_text,"pneumo_report.pdf")
