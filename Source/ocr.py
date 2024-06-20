from paddleocr import PaddleOCR
from pydantic import BaseModel
from typing import List

# Optical Character Recognition of .pdf or .png email contents.
class OCR(BaseModel):
    filename: str
    extraction_list: List[str] = []
    
    def mail_extraction(self,ocr: PaddleOCR = PaddleOCR(use_angle_cls=True, lang='en', use_gpu=False)) -> str:
        
        extraction = ocr.ocr(self.filename)
        self.extraction_list.append([i[1][0] for i in [x for x in extraction[0]]])
        email = ' '.join(self.extraction_list[0])
        return email
        
