import pytesseract
import pdf2image
import pdfplumber
from fastapi import HTTPException

def run(message: str, params: dict):
    """
    Extracts text from a scanned PDF file, first attempting text extraction with pdfplumber,
    then using OCR (Tesseract) if the text extraction fails.

    Args:
        message (str): A message, not used for this function, but included for standardization.
        params (dict): Parameters containing the 'file_path' of the scanned PDF.

    Returns:
        dict: Status and the extracted text or an error message.
    """
    file_path = params.get("file_path", "")
    
    if not file_path:
        return {"status": "error", "message": "file_path is required"}

    try:
        # Try to extract text using pdfplumber first
        with pdfplumber.open(file_path) as pdf:
            text = ''
            for page in pdf.pages:
                text += page.extract_text()

        # If pdfplumber returns no text (i.e., the PDF is scanned), use OCR
        if not text.strip():
            # Convert PDF pages to images
            images = pdf2image.convert_from_path(file_path)
            text = ""
            for image in images:
                text += pytesseract.image_to_string(image)
        
        return {"status": "success", "text": text.strip()}

    except Exception as e:
        return {"status": "error", "message": f"Error extracting text from scanned PDF: {str(e)}"}
