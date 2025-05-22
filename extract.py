from pdf2image import convert_from_path
from paddleocr import PaddleOCR
from PyPDF2 import PdfReader
import numpy as np

from PIL import Image

ocr = PaddleOCR(use_angle_cls=True, lang="en")


def convert_pdf_to_images(pdf_path):
    return convert_from_path(pdf_path, dpi=300)


def extract_text_from_images(images):
    text = []
    for img in images:
        img_np = np.array(img)  
        result = ocr.ocr(img_np)
        lines = [line[1][0] for block in result for line in block]
        text.append("\n".join(lines))
    return "\n\n".join(text)


def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    return "\n".join(page.extract_text() or "" for page in reader.pages)
