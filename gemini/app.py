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
    
    # Calculate the available width for the text
    text_width = letter[0] - 100  # Assuming left and right margin of 50 units
    
    # Write text to the canvas
    lines = []
    for line in text.split("\n"):
        if c.stringWidth(line) <= text_width:
            lines.append(line)
        else:
            # Split long lines into multiple lines to fit within the page width
            words = line.split()
            new_line = ''
            for word in words:
                if c.stringWidth(new_line + ' ' + word) <= text_width:
                    new_line += ' ' + word if new_line else word
                else:
                    lines.append(new_line.strip())
                    new_line = word
            if new_line:
                lines.append(new_line.strip())
    
    y_coordinate = 750  # Starting y-coordinate
    for line in lines:
        c.drawString(50, y_coordinate, line)
        y_coordinate -= 20  # Decrease y-coordinate for next line
    
    # Save the canvas to a PDF file
    c.save()

generate_pdf(dementia_text,"dementia_report.pdf")
generate_pdf(tumour_text,"tumour_report.pdf")
generate_pdf(pneumo_text,"pneumo_report.pdf")
