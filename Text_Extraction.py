import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def Text_Extractor(image_path) -> str:
    img = cv2.imread(image_path)
    text = pytesseract.image_to_string(img)
    return text

