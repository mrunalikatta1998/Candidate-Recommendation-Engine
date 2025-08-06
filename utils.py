from PyPDF2 import PdfReader  # For reading text from PDF files
from docx import Document     # For reading text from Word files (DOCX)

# Function to extract text from a PDF file
def extract_text_from_pdf(file):
    reader = PdfReader(file)  # Load the PDF
    text = ""
    for page in reader.pages:  # Go through each page
        if page.extract_text():  # Check if text exists on the page
            text += page.extract_text()  # Add the text to our result
    return text  # Return all combined text

# Function to extract text from a DOCX (Word) file
def extract_text_from_docx(file):
    doc = Document(file)  # Load the DOCX
    # Get all paragraphs and combine them with line breaks
    return "\n".join([para.text for para in doc.paragraphs])
