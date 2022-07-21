import pytesseract
from PIL import Image
import re

def get_text(image):
    """ 
    Recebe uma imagem e retorna o texto presente na mesma (string)
    """
    im = Image.open(image)
    txt = pytesseract.image_to_string(im)
    txt = re.sub(' +', ' ', txt)
    txt = txt.replace('\n',' ')
    txt = txt.lower()
    return txt

